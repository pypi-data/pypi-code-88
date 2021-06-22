from datetime import datetime
from functools import cached_property, lru_cache
from typing import Any, Dict, List, Optional, Set, Tuple, Type, cast

from tortoise import Tortoise, fields
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from tortoise.contrib.pydantic.creator import PydanticMeta
from tortoise.fields.relational import Field
from tortoise.models import Model

from .patch import patch_pydantic


class BaseModel(Model):
    id: int = fields.IntField(pk=True)
    created_at: datetime = fields.DatetimeField(null=False, auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(null=False, auto_now=True)

    class Meta:
        abstract = True

    # class PydanticMeta:
    #     list_exclude: Tuple[str, ...] = ()  # 列表排除
    #     detail_include: Tuple[str, ...] = ()  # 详情叠加

    @cached_property
    def computed_cache(self) -> Dict[str, Any]:
        return {}

    async def dict(
        self, prefetch: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        if prefetch:
            await self.fetch_related(*prefetch)
        return self.detail().from_orm(self).dict()

    @classmethod
    @lru_cache
    def list(cls) -> Type[PydanticModel]:
        meta: Optional[PydanticMeta] = getattr(cls, "PydanticMeta", None)
        list_exclude: Tuple[str, ...] = (
            meta and getattr(meta, "list_exclude", ()) or ()
        )
        return patch_pydantic(
            pydantic_model_creator(
                cls, name=cls.pydantic_name() + ".list", exclude=list_exclude
            )
        )

    @classmethod
    @lru_cache
    def detail(cls) -> Type[PydanticModel]:
        meta: Optional[PydanticMeta] = getattr(cls, "PydanticMeta", None)
        detail_include: Tuple[str, ...] = (
            meta and getattr(meta, "detail_include", ()) or ()
        )
        return patch_pydantic(
            pydantic_model_creator(
                cls,
                name=cls.pydantic_name() + ".detail",
                include=detail_include,
            )
        )

    @classmethod
    def pydantic_name(cls) -> str:
        return f"{cls.__module__}.{cls.__qualname__}"

    def update(self, input: Any):
        dic: Dict[str, Any] = (
            input
            if isinstance(input, dict)
            else input.dict(exclude_unset=True)
        )
        self.update_from_dict(dic)  # type: ignore

    def get_computed(self, field: str, default: Any = None) -> Any:
        return self.computed_cache.get(field, default)

    async def fetch_related(
        self, *args: Any, using_db: Optional[BaseDBAsyncClient] = None
    ) -> None:
        meta: Optional[PydanticMeta] = getattr(
            self.__class__, "PydanticMeta", None
        )
        cached_args: Set[str] = set()
        if meta and hasattr(meta, "computed"):
            for field in args:
                if field in meta.computed:
                    f = getattr(self, f"compute_{field}", None)
                    if not f:
                        continue
                    self.computed_cache[field] = await f()
                    cached_args.add(field)
        normlized_args = [
            field.replace(".", "__") if isinstance(field, str) else field
            for field in args
            if field not in cached_args
        ]
        return await super().fetch_related(*normlized_args, using_db=using_db)

    @classmethod
    @lru_cache
    def get_model(cls, model_name: str) -> Type[Model]:
        parts: List[str] = model_name.split(".")
        return cast(Type[BaseModel], Tortoise.apps[parts[0]][parts[1]])

    @classmethod
    @lru_cache
    def get_field_model(cls, field: str) -> Type[Model]:
        meta = getattr(cls, "_meta")
        fields_map: Dict[str, Field] = getattr(meta, "fields_map")
        fk_field = fields_map[field]
        model_name = getattr(fk_field, "model_name")
        return cls.get_model(model_name)

    async def save_related(self, raw: Any):
        meta = getattr(self.__class__, "_meta")

        # 保存 ForeignKeyField
        fk_fields: Set[str] = getattr(meta, "fk_fields")
        for fk_field_name in fk_fields:
            v: Optional[Any] = raw.get(fk_field_name)
            if not v:
                continue

            field_model: Type[BaseModel] = cast(
                Type[BaseModel], self.get_field_model(fk_field_name)
            )

            v_id = v.pop("id", None)
            if v_id:
                field_value: Optional[BaseModel] = await field_model.filter(
                    id=v_id
                ).first()
                assert field_value
                field_value.update(v)
            else:
                field_value = field_model(**v)
                setattr(self, fk_field_name, field_value)
            await field_value.save()

        # 保存 ManyToMany
        m2m_fields: Set[str] = getattr(meta, "m2m_fields")
        for m2m_field_name in m2m_fields:
            v: Optional[Any] = raw.get(m2m_field_name)
            if not v:
                continue
            assert isinstance(v, List)
            vs: List[Any] = v

            field_model: Type[BaseModel] = cast(
                Type[BaseModel], self.get_field_model(m2m_field_name)
            )

            field_values: List[Any] = []
            for v in vs:
                assert v
                v_id = v.pop("id", None)
                if v_id:
                    field_value: Optional[
                        BaseModel
                    ] = await field_model.filter(id=v_id).first()
                    assert field_value
                    field_value.update(v)
                else:
                    field_value = field_model(**v)
                    field_values.append(field_value)
                await field_value.save()

            if not self.id:
                setattr(self, m2m_field_name, field_values)
