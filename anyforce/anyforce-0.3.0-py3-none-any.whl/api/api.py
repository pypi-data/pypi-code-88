from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    Generic,
    List,
    Type,
    TypeVar,
    Union,
)

from fastapi import APIRouter, Body, Depends, Query, status
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel as PydanticBaseModel
from pydantic import create_model
from tortoise.queryset import QuerySet
from tortoise.transactions import atomic

from .. import json
from ..model import BaseModel
from .exceptions import HTTPNotFoundError

UserModel = TypeVar("UserModel")
Model = TypeVar("Model", bound=BaseModel)
CreateForm = TypeVar("CreateForm", bound=PydanticBaseModel)
UpdateForm = TypeVar("UpdateForm", bound=PydanticBaseModel)


class API(Generic[UserModel, Model, CreateForm, UpdateForm]):
    def __init__(
        self,
        model: Type[Model],
        create_form: Type[CreateForm],
        update_form: Type[UpdateForm],
        get_current_user: Callable[
            ..., Union[Coroutine[Any, Any, UserModel], UserModel]
        ],
        enable_create: bool = True,
        enable_update: bool = True,
        enable_delete: bool = True,
        enable_get: bool = True,
    ) -> None:
        super().__init__()
        self.model = model
        self.create_form = create_form
        self.update_form = update_form
        self.get_current_user = get_current_user
        self.enable_create = enable_create
        self.enable_update = enable_update
        self.enable_delete = enable_delete
        self.enable_get = enable_get

    def translate_id(self, user: UserModel, id: str) -> str:
        return id

    def q(self, user: UserModel, q: QuerySet[Model]) -> QuerySet[Model]:
        return q

    async def before_create(
        self, user: UserModel, obj: Model, input: CreateForm
    ) -> Model:
        return obj

    async def after_create(
        self, user: UserModel, obj: Model, input: CreateForm
    ) -> Model:
        return obj

    async def before_update(
        self, user: UserModel, obj: Model, input: UpdateForm
    ) -> Model:
        return obj

    async def after_update(
        self, user: UserModel, obj: Model, input: UpdateForm
    ) -> Model:
        return obj

    async def before_delete(self, user: UserModel, obj: Model) -> Model:
        return obj

    def bind(self, router: APIRouter):
        ListPydanticModel = self.model.list()
        DetailPydanticModel = self.model.detail()
        CreateForm = self.create_form
        UpdateForm = self.update_form

        DetailPydanticModels = Union[
            DetailPydanticModel, List[DetailPydanticModel]  # type: ignore
        ]
        Response = create_model(
            f"{self.model.__name__}.Response",
            __base__=PydanticBaseModel,
            total=0,
            data=(List[ListPydanticModel], ...),  # type: ignore
        )

        async def find(id: str, current_user: UserModel) -> Model:
            obj = await self.q(current_user, self.model.filter(id=id)).first()
            if not obj:
                raise HTTPNotFoundError
            return obj

        def get_form_type(t: Any) -> Any:
            f = getattr(t, "form_type", None)
            return f and f() or Body(...)

        methods: Dict[str, Callable[..., Any]] = {}

        if self.enable_create:

            @router.post(
                "/",
                response_model=DetailPydanticModel,
                response_class=ORJSONResponse,
                status_code=status.HTTP_201_CREATED,
            )
            @atomic()
            async def create(
                input: CreateForm = get_form_type(CreateForm),
                prefetch: List[str] = Query([]),
                current_user: UserModel = Depends(self.get_current_user),
            ) -> Any:
                raw = input.dict(exclude_unset=True)
                raw, m2m_raw = await self.model.save_related(raw)
                obj = self.model(**raw)

                obj_rtn = await self.before_create(current_user, obj, input)
                if obj_rtn is not obj:
                    obj = obj_rtn

                await obj.save()
                prefetch = list(set([*prefetch, *m2m_raw.keys()]))
                for k, v in m2m_raw.items():
                    await getattr(obj, k).add(*v)
                if prefetch:
                    await obj.fetch_related(*prefetch)

                obj_rtn = await self.after_create(current_user, obj, input)
                if obj_rtn is not obj:
                    obj = obj_rtn

                return DetailPydanticModel.from_orm(obj)

            methods["create"] = create

        if self.enable_get:

            @router.get(
                "/", response_model=Response, response_class=ORJSONResponse
            )
            async def index(
                offset: int = 0,
                limit: int = 20,
                condition: List[str] = Query([]),
                order_by: List[str] = Query([]),
                prefetch: List[str] = Query([]),
                current_user: UserModel = Depends(self.get_current_user),
            ) -> Any:
                q = self.model.all()
                q = self.q(current_user, q)

                # 通用过滤方案
                # https://tortoise-orm.readthedocs.io/en/latest/query.html
                if condition:
                    for raw in condition:
                        kv = json.loads(raw)
                        q = q.filter(
                            **{
                                k: safe_condition_value(v)
                                for k, v in kv.items()
                            }
                        )

                # 排序
                if order_by:
                    for item in order_by:
                        q = q.order_by(item)

                # 分页
                total = await q.count()
                objs = await q.offset(offset).limit(limit)

                if prefetch:
                    for obj in objs:
                        await obj.fetch_related(*prefetch)

                return Response(
                    total=total,
                    data=[ListPydanticModel.from_orm(obj) for obj in objs],
                )

            @router.get(
                "/{id}",
                response_model=DetailPydanticModel,
                response_class=ORJSONResponse,
            )
            @atomic()
            async def get(
                id: str,
                prefetch: List[str] = Query([]),
                current_user: UserModel = Depends(self.get_current_user),
            ) -> Any:
                id = self.translate_id(current_user, id)
                q = self.q(current_user, self.model.all().filter(id=id))
                obj = await q.first()
                if not obj:
                    raise HTTPNotFoundError
                if prefetch:
                    await obj.fetch_related(*prefetch)
                return DetailPydanticModel.from_orm(obj)

            methods["index"] = index
            methods["get"] = get

        if self.enable_update:

            @router.put(
                "/{ids}",
                response_model=DetailPydanticModels,
                response_class=ORJSONResponse,
            )
            @atomic()
            async def update(
                ids: str,
                input: UpdateForm = get_form_type(UpdateForm),
                prefetch: List[str] = Query([]),
                current_user: UserModel = Depends(self.get_current_user),
            ) -> Any:
                rtns: List[Any] = []
                raw = input.dict(exclude_unset=True)
                for id in ids.split(","):
                    id = self.translate_id(current_user, id)
                    obj = await find(id, current_user)
                    raw, m2m_raw = await self.model.save_related(raw)
                    obj.update(raw)

                    obj_rtn = await self.before_update(
                        current_user, obj, input
                    )
                    if obj_rtn is not obj:
                        obj = obj_rtn

                    await obj.save()
                    obj_prefetch = list(set([*prefetch, *m2m_raw.keys()]))
                    for k, v in m2m_raw.items():
                        await getattr(obj, k).add(*v)
                    if obj_prefetch:
                        await obj.fetch_related(*obj_prefetch)

                    obj_rtn = await self.after_update(current_user, obj, input)
                    if obj_rtn is not obj:
                        obj = obj_rtn

                    rtns.append(DetailPydanticModel.from_orm(obj))
                return len(rtns) > 1 and rtns or rtns[0]

            methods["update"] = update

        if self.enable_delete:

            @router.delete(
                "/{ids}",
                response_model=DetailPydanticModels,
                response_class=ORJSONResponse,
            )
            @atomic()
            async def delete(
                ids: str,
                current_user: UserModel = Depends(self.get_current_user),
            ) -> Any:
                rtns: List[Any] = []
                for id in ids.split(","):
                    id = self.translate_id(current_user, id)
                    obj = await find(id, current_user)
                    obj_rtn = await self.before_delete(current_user, obj)
                    if obj_rtn is not obj:
                        obj = obj_rtn

                    await obj.delete()
                    rtns.append(DetailPydanticModel.from_orm(obj))
                return len(rtns) > 1 and rtns or rtns[0]

            methods["delete"] = delete

        return methods


def safe_condition_value(
    v: Union[List[Any], Any]
) -> Union[str, float, List[Union[str, float]]]:
    if isinstance(v, List):
        rs: List[Union[str, float]] = []
        for e in v:
            r = safe_condition_value(e)
            assert not isinstance(r, list)
            rs.append(r)
        return rs
    return v if isinstance(v, float) else str(v)


def get_anonymous_user() -> Dict[str, str]:
    return {}


class PublicAPI(API[object, Model, CreateForm, UpdateForm]):
    def __init__(
        self,
        model: Type[Model],
        create_form: Type[CreateForm],
        update_form: Type[UpdateForm],
        enable_create: bool = True,
        enable_update: bool = True,
        enable_delete: bool = True,
        enable_get: bool = True,
    ) -> None:
        super().__init__(
            model,
            create_form=create_form,
            update_form=update_form,
            get_current_user=get_anonymous_user,
            enable_create=enable_create,
            enable_update=enable_update,
            enable_delete=enable_delete,
            enable_get=enable_get,
        )
