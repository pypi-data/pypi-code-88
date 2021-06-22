from typing import Any, List, Union

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from pydantic import (
    EmailError,
    IntegerError,
    MissingError,
    UrlError,
    ValidationError,
)
from pydantic.error_wrappers import ErrorWrapper

HTTPForbiddenError = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail={"errors": "禁止访问"}
)
HTTPNotFoundError = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail={"errors": "不存在"}
)
HTTPUnAuthorizedError = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail={"errors": "未认证"}
)


ValidateError = Union[RequestValidationError, ErrorWrapper, ValidationError]


def translate_validation_error(e: ValidationError) -> List[str]:
    msgs: List[str] = []
    model: Any = getattr(e, "model")
    raw_errors: List[Any] = getattr(e, "raw_errors")
    for raw_error in raw_errors:
        if isinstance(raw_error, ErrorWrapper):
            inner_exc = getattr(raw_error, "exc")

            if isinstance(inner_exc, ValidationError):
                msgs = msgs + translate_validation_error(inner_exc)
                continue

            translated_msg = ""
            if isinstance(inner_exc, MissingError):
                translated_msg = "必填项"
            elif isinstance(inner_exc, IntegerError):
                translated_msg = "无效的整数"
            elif isinstance(inner_exc, EmailError):
                translated_msg = "无效的邮箱地址"
            elif isinstance(inner_exc, UrlError):
                translated_msg = "无效的链接"
            # TODO: tranlstate more if needed

            if translated_msg:
                for loc in raw_error.loc_tuple():
                    property = (
                        model.schema().get("properties", {}).get(loc, {})
                    )
                    title: str = property.get("title", loc)
                    msgs.append(f"{title} 是{translated_msg}")
                continue
        msgs.append(str(raw_error))
    return msgs


def translate_validate_error(e: Any) -> List[str]:
    msgs: List[str] = []
    errors: List[Any] = e if isinstance(e, List) else [e]
    for error in errors:
        if isinstance(error, ValidationError):
            msgs += translate_validation_error(error)
        else:
            msgs + translate_validate_error(error)
    return msgs


# TODO: 翻译数据库的异常, 比如 unique, 长度超过等等


def register(app: FastAPI):
    @app.exception_handler(RequestValidationError)  # type: ignore
    async def requestValidationErrorHandle(
        request: Request, exc: RequestValidationError
    ) -> ORJSONResponse:
        return ORJSONResponse(
            {"detail": {"errors": translate_validate_error(exc)}},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return requestValidationErrorHandle
