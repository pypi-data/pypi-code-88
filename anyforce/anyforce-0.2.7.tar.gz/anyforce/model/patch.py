from typing import Any, Dict, Optional, Type

from pydantic import validate_model
from tortoise import fields
from tortoise.contrib.pydantic import PydanticModel
from tortoise.exceptions import NoValuesFetched
from tortoise.queryset import AwaitableQuery


def patch_pydantic(model: Type[PydanticModel]) -> Type[PydanticModel]:
    # 解决数据动态加载的问题
    for field in model.__fields__.values():
        if not field.required:
            continue
        field.required = not issubclass(field.type_, PydanticModel)
        field.allow_none = True
        config = getattr(field.type_, "__config__", None)
        if config:
            orig_model: Optional[Any] = getattr(config, "orig_model", None)
            if orig_model:
                field.type_ = orig_model.detail()

    def from_orm(obj: Any) -> PydanticModel:
        obj = model._decompose_class(obj)  # type: ignore
        new_obj: Dict[str, Any] = {}
        for k, v in obj.items():
            if k not in model.__fields__:
                continue

            if isinstance(v, AwaitableQuery):
                v = None
            if isinstance(v, fields.ReverseRelation) or isinstance(
                v, fields.ManyToManyRelation
            ):
                try:
                    v.__len__()
                except NoValuesFetched:
                    v = None
            new_obj[k] = v

        m = model.__new__(model)
        values, fields_set, validation_error = validate_model(model, new_obj)
        if validation_error:
            raise validation_error
        object.__setattr__(m, "__dict__", values)
        object.__setattr__(m, "__fields_set__", fields_set)
        m._init_private_attributes()
        return m

    def dict(self: model, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        if kwargs and kwargs.get("exclude_none") is not None:
            kwargs["exclude_none"] = True
        return super(model, self).dict(*args, **kwargs)

    model.from_orm = from_orm
    model.dict = dict

    return model
