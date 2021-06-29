import re
from dataclasses import field, is_dataclass as is_dc
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from pydantic.dataclasses import dataclass
from pydantic import validator, PydanticValueError
from vitya.validators import validate_inn, validate_oktmo, ValidationError
from lxml import etree
from camel_converter import to_upper_camel

__NAMESPACE__ = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"
__PREFIX__ = 'smz'


class PydanticValidationError(PydanticValueError):
    msg_template = 'invalid {name}: {reason}'


@dataclass
class FnsValidators:
    @validator('longitude', check_fields=False)
    def validator_longitude(cls, longitude):
        if abs(longitude) <= 180:
            return longitude
        else:
            raise PydanticValidationError(name='longitude', reason='wrong value, greater than 180 modulo')

    @validator('latitude', check_fields=False)
    def validator_latitude(cls, latitude):
        if abs(latitude) <= 90:
            return latitude
        else:
            raise PydanticValidationError(name='latitude', reason='wrong value, greater than 90 modulo')

    @validator('inn', check_fields=False)
    def validator_inn(cls, inn):
        try:
            validate_inn(inn)
            return inn
        except ValidationError as e:
            raise PydanticValidationError(name='inn', reason=str(e))

    @validator('inn_list', check_fields=False)
    def validator_inn_list(cls, inn_list):
        try:
            for inn in inn_list:
                validate_inn(inn)
            return inn_list
        except ValidationError as e:
            raise PydanticValidationError(name='inn_list', reason=str(e))

    @validator('oktmo', check_fields=False)
    @validator('region', check_fields=False)
    def validator_oktmo(cls, oktmo):
        try:
            validate_oktmo(oktmo)
            return oktmo
        except ValidationError as e:
            raise PydanticValidationError(name='inn', reason=str(e))

    @validator('phone', check_fields=False)
    def validator_phone(cls, phone):
        if re.match(r'7[0-9]{10}', phone):
            return phone
        else:
            raise PydanticValidationError(name='phone', reason='invalid format: not 7xxxxxxxxxx')

    @validator('email', check_fields=False)
    def validator_email(cls, email):
        #  ToDo: validator_email
        return email

    def __generate(self):
        root = etree.Element(f"{{{__NAMESPACE__}}}{self.__class__.__name__}", nsmap={__PREFIX__: __NAMESPACE__})
        for el in self.__dataclass_fields__:
            el_type = self.__annotations__[el]
            is_typing = '__origin__' in el_type.__dict__
            if is_typing and el_type.__origin__ is list:
                for sub_el in self.__dict__[el]:
                    if is_dc(el_type.__args__[0]):
                        root.insert(-1, sub_el.__generate())
                    else:
                        sub_el_instance = etree.SubElement(root, f"{{{__NAMESPACE__}}}{to_upper_camel(el)}")
                        sub_el_instance.text = str(sub_el)
            elif is_dc(el_type):
                root.insert(-1, self.__dict__[el].__generate())
            else:
                el_instance = etree.SubElement(root, f"{{{__NAMESPACE__}}}{to_upper_camel(el)}")
                el_instance.text = str(self.__dict__[el])
        return root

    def export(self) -> bytes:
        message = self.__generate()
        return etree.tostring(message, pretty_print=True)


@dataclass
class AttachedFile(FnsValidators):
    """
    Присоединенный файл.

    :var mimetype: MIME тип файла
    :var filename: Имя файла
    :var content: Содержимое файла
    """
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    content: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class ChangePermissoinsInfo(FnsValidators):
    """
    Информация о смене прав.

    :var inn: ИНН пользователя
    :var request_id: Id запроса на смену прав
    :var request_partner_id: Id партнера запросившего смену прав
    :var partner_name: Название партнера запросившего смену прав
    :var permissions_list: Список новых запрашиваемых разрешений
    :var request_time: Дата последней постановки на учёт
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    request_partner_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestPartnerId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    partner_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    permissions_list: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PermissionsList",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "min_occurs": 1,
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class GeoInfo(FnsValidators):
    """
    Информация о местоположении пользователя во время выполнения запроса.

    :var latitude: Широта
    :var longitude: Долгота
    """
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class GetAccrualsAndDebtsRequest(FnsValidators):
    """
    Получение информации о незакрытых налоговых начислениях.

    :var inn_list: Список ИНН
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn_list: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InnList",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetActivitiesListRequest(FnsValidators):
    """
    Получение актуального списка видов деятельности.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetActivitiesListRequestV2:
    """
    Получение актуального двухуровневого списка видов деятельности.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetActivitiesListResponse(FnsValidators):
    """
    Ответ на GetActivitiesListRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Activities(FnsValidators):
        """
        :var id: ID вида деятельности
        :var name: Название вида деятельности
        """
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            }
        )

    activities: List[Activities] = field(
        default_factory=list,
        metadata={
            "name": "Activities",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetActivitiesListResponseV2:
    """
    Ответ на GetActivitiesListRequestV2.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Activities(FnsValidators):
        """
        :var id: ID вида деятельности
        :var parent_id: ID родительского вида деятельности
        :var name: Название вида деятельности
        :var is_active: Признак активности вида деятельности в системе
        """
        id: Optional[int] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Element",
                "required": True,
            }
        )
        parent_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "ParentId",
                "type": "Element",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            }
        )
        is_active: Optional[bool] = field(
            default=None,
            metadata={
                "name": "IsActive",
                "type": "Element",
                "required": True,
            }
        )

    activities: List[Activities] = field(
        default_factory=list,
        metadata={
            "name": "Activities",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetBindPartnerStatusRequest(FnsValidators):
    """
    Получение статуса заявки на привязку НП НПД к партнеру.

    :var id: Id заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetBindPartnerStatusResponse(FnsValidators):
    """
    Ответ на GetBindPartnerStatusRequest.

    :var result: Результат запроса
    :var inn: ИНН
    :var permissions: Список согласованных разрешений
    :var processing_time: Дата рассмотрения заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    result: Optional[str] = field(
        default=None,
        metadata={
            "name": "Result",
            "type": "Element",
            "required": True,
        }
    )
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
        }
    )
    permissions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Permissions",
            "type": "Element",
        }
    )
    processing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProcessingTime",
            "type": "Element",
        }
    )


@dataclass
class GetCancelIncomeReasonsListRequest(FnsValidators):
    """
    Получение справочника причин аннулирования.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetCancelIncomeReasonsListResponse(FnsValidators):
    """
    Ответ на GetCancelIncomeReasonsListRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Codes(FnsValidators):
        """
        :var code: Код причины аннулирования чека
        :var description: Описание причины аннулирования чека
        """
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Element",
                "required": True,
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            }
        )

    codes: List[Codes] = field(
        default_factory=list,
        metadata={
            "name": "Codes",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetChangeInnHistoryRequest(FnsValidators):
    """
    Получение информации о смене ИНН.

    :var offset: Глобальное смещение в журнале смены ИНН начиная с
        которого будут отдаваться записи
    :var limit: Максимальное число записей в ответе
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "required": True,
        }
    )
    limit: int = field(
        default=100,
        metadata={
            "name": "Limit",
            "type": "Element",
        }
    )


@dataclass
class GetChangeInnHistoryResponse(FnsValidators):
    """
    Ответ на GetChangeInnHistoryRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Items(FnsValidators):
        """
        :var offset: Глобальное смещение в журнале смены ИНН. Записи
            отсортированы по возрастанию. Могуть быть пробелы между
            записями
        :var previous_inn: Предыдущий ИНН у налогоплательщика
        :var inn: ИНН
        :var from_value: Дата, начиная с которой, применен ИНН
        :var to: Дата, до которой, применен ИНН
        """
        offset: Optional[int] = field(
            default=None,
            metadata={
                "name": "Offset",
                "type": "Element",
                "required": True,
            }
        )
        previous_inn: Optional[str] = field(
            default=None,
            metadata={
                "name": "PreviousInn",
                "type": "Element",
                "required": True,
            }
        )
        inn: Optional[str] = field(
            default=None,
            metadata={
                "name": "Inn",
                "type": "Element",
                "required": True,
            }
        )
        from_value: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "From",
                "type": "Element",
                "required": True,
            }
        )
        to: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "To",
                "type": "Element",
            }
        )

    items: List[Items] = field(
        default_factory=list,
        metadata={
            "name": "Items",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetGrantedPermissionsRequest(FnsValidators):
    """
    Получение списка разрешений, предоставленных партнеру.

    :var inn: ИНН пользователя
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"
        target_namespace = 'smz'

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetGrantedPermissionsResponse(FnsValidators):
    """
    Ответ на GetGrantedPermissionsRequest.

    :var granted_permissions_list: Список выданных разрешений
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    granted_permissions_list: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GrantedPermissionsList",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetGrantedPermissionsStatusRequest(FnsValidators):
    """
    Получение статуса заявки на изменение прав НП НПД.

    :var id: Id заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetGrantedPermissionsStatusResponse(FnsValidators):
    """
    Ответ на GetGrantedPermissionsStatusRequest.

    :var inn: ИНН
    :var result: Результат запроса
    :var processing_time: Дата рассмотрения заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
        }
    )
    result: Optional[str] = field(
        default=None,
        metadata={
            "name": "Result",
            "type": "Element",
            "required": True,
        }
    )
    processing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProcessingTime",
            "type": "Element",
        }
    )


@dataclass
class GetIncomeForPeriodRequest(FnsValidators):
    """
    Получение информации по доходу НП НПД за период.

    :var inn: ИНН пользователя
    :var tax_period_id: ID налогового периода (YYYYMM)
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    tax_period_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPeriodId",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetIncomeForPeriodResponse(FnsValidators):
    """
    Ответ на GetIncomeForPeriodRequest.

    :var total_amount: Сумма зарегистрированного дохода за период
    :var canceled_total_amount: Сумма сторнированного дохода за период
    :var tax: Рассчитанный налог за период
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "required": True,
        }
    )
    canceled_total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CanceledTotalAmount",
            "type": "Element",
            "required": True,
        }
    )
    tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetIncomeReferenceRequestV2:
    """
    Получение справки о доходах НП НПД в новом формате.

    :var inn: ИНН пользователя
    :var request_time: Дата запроса
    :var request_year: Год, за который запрашивается справка
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "required": True,
        }
    )
    request_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestYear",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetIncomeRequest(FnsValidators):
    """
    Получение информации по зарегистрированным доходам.

    :var inn: ИНН пользователя
    :var from_value: Дата, начиная с которой отображать
        зарегистрированные доходы
    :var to: Дата, до которой отображать зарегистрированные доходы.
    :var limit: Максимальное количество зарегистрированных доходов в
        ответе
    :var offset: Отступ от начала списка
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    from_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "required": True,
        }
    )
    to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "required": True,
        }
    )
    limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Limit",
            "type": "Element",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
        }
    )


@dataclass
class GetIncomeRequestV2:
    """
    Получение информации по зарегистрированным доходам с поддержкой нескольких
    услуг в чеках.

    :var inn: ИНН пользователя
    :var from_value: Дата, начиная с которой отображать
        зарегистрированные доходы
    :var to: Дата, до которой отображать зарегистрированные доходы.
    :var limit: Максимальное количество зарегистрированных доходов в
        ответе
    :var offset: Отступ от начала списка
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    from_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "required": True,
        }
    )
    to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "required": True,
        }
    )
    limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Limit",
            "type": "Element",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
        }
    )


@dataclass
class GetInnByPersonalInfoRequest(FnsValidators):
    """
    Получение ИНН по персональным данным.

    Инициатор вызова: банки-партнёры, платформы-партнёры.

    :var first_name: Имя пользователя
    :var second_name: Фамилия пользователя
    :var patronymic: Отчество пользователя
    :var birthday: Дата рождения
    :var passport_series: Серия паспорта
    :var passport_number: Номер паспорта
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    first_name: str = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "required": True,
        }
    )
    second_name: str = field(
        default=None,
        metadata={
            "name": "SecondName",
            "type": "Element",
            "required": True,
        }
    )
    patronymic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Patronymic",
            "type": "Element",
        }
    )
    birthday: XmlDate = field(
        default=None,
        metadata={
            "name": "Birthday",
            "type": "Element",
            "required": True,
        }
    )
    passport_series: str = field(
        default=None,
        metadata={
            "name": "PassportSeries",
            "type": "Element",
            "required": True,
        }
    )
    passport_number: str = field(
        default=None,
        metadata={
            "name": "PassportNumber",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetInnByPersonalInfoResponse(FnsValidators):
    """
    Ответ на GetInnByPersonalInfoRequest.

    :var inn: ИНН пользрвателя
    :var status: Статус ответа
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Inn",
            "type": "Element",
        }
    )
    status: str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
        }
    )


@dataclass
class GetKeysRequest(FnsValidators):
    """
    Получение партнером ключей для работы в режиме Offline.

    :var inn: ИНН пользователя
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Inn",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetLegalEntityInfoRequest(FnsValidators):
    """
    Получение информации о юридическом лице по ИНН.

    :var inn: ИНН ЮЛ (не обязательно если в запросе есть Наименование и
        ОКТМО )
    :var ogrn: ОГРН ЮЛ
    :var name: Наименование ЮЛ
    :var oktmo: ОКТМО региона места нахождения ЮЛ
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
        }
    )
    ogrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ogrn",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        }
    )
    oktmo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Oktmo",
            "type": "Element",
        }
    )


@dataclass
class GetLegalEntityInfoResponse(FnsValidators):
    """
    Ответ на GetLegalEntityInfoRequest.

    :var inn: ИНН ЮЛ
    :var ogrn: ОГРН ЮЛ
    :var name: Название ЮЛ
    :var address: Адрес регистрации ЮЛ
    :var termination_date: Дата прекращения деятельности
    :var invalidation_date: Дата признания регистрации недействительной
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    ogrn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ogrn",
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "required": True,
        }
    )
    termination_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TerminationDate",
            "type": "Element",
            "required": True,
        }
    )
    invalidation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InvalidationDate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetNewPermissionsChangeRequest(FnsValidators):
    """
    Получение списка запросов на подтверждение прав.

    :var inn: Список НП по которым необходимо получить оповещения
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class GetNewlyUnboundTaxpayersRequest(FnsValidators):
    """
    Получение списка вновь отвязанных от партнера НП НПД.

    :var from_value: Дата, начиная с которой отображать вновь
        отвязанных НП НПД
    :var to: Дата, до которой отображать вновь отвязанных НП НПД
    :var limit: Максимальное количество НП НПД на странице
    :var offset: Отступ от начала списка
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    from_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
        }
    )
    to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
        }
    )
    limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "Limit",
            "type": "Element",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
        }
    )


@dataclass
class GetNotificationsCountRequest(FnsValidators):
    """
    Получение количеств не прочитанных оповещений.

    :var inn: Список НП по которым необходимо получить оповещения
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class GetPartnersPermissionsRequest(FnsValidators):
    """
    Получение списка привязанных партнеров и предоставленных им прав.

    :var inn: ИНН НП
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetPaymentDocumentsRequest(FnsValidators):
    """
    Получение платежных документов на оплату налоговых начислений,
    задолженностей и пеней.

    :var inn_list: Список ИНН
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn_list: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InnList",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetRegionsListRequest(FnsValidators):
    """
    Получение актуального списка регионов, где осуществляется режим НПД.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetRegionsListResponse(FnsValidators):
    """
    Ответ на GetRegionsListRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Regions(FnsValidators):
        """
        :var oktmo: ОКТМО региона ведения деятельности
        :var name: Название региона ведения деятельности
        """
        oktmo: Optional[str] = field(
            default=None,
            metadata={
                "name": "Oktmo",
                "type": "Element",
                "required": True,
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "name": "Name",
                "type": "Element",
                "required": True,
            }
        )

    regions: List[Regions] = field(
        default_factory=list,
        metadata={
            "name": "Regions",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetRegistrationReferenceRequestV2:
    """
    Получение справки о постановке на учет в качестве НП НПД в новом формате.

    :var inn: ИНН пользователя
    :var request_time: Дата запроса
    :var request_year: Год, за который запрашивается справка
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "required": True,
        }
    )
    request_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestYear",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetRegistrationStatusRequest(FnsValidators):
    """
    Запрос статуса заявки на постановку на учет.

    :var id: Id заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetRegistrationStatusResponse(FnsValidators):
    """
    Ответ на GetRegistrationStatusRequest.

    :var request_result: Результат запроса `ORDER_REGISTERED`, `IN_PROGRESS`, `COMPLETED`, `FAILED`
    :var rejection_reason: Код причины отказа
    :var registration_time: Дата текущей постановки на учет
    :var last_registration_time: Дата последней постановки на учет
    :var update_time: Дата последнего обновления данных
    :var unregistration_time: Дата снятия с учёта
    :var bind_request_id: ID запроса на согласование разрешений для
        партнера от НП НПД
    :var registration_certificate_number: Номер свидетельства о
        постановке на учет
    :var inn: ИНН налогоплательщика
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_result: str = field(
        default=None,
        metadata={
            "name": "RequestResult",
            "type": "Element",
            "required": True,
        }
    )
    rejection_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "RejectionReason",
            "type": "Element",
        }
    )
    registration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RegistrationTime",
            "type": "Element",
        }
    )
    last_registration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastRegistrationTime",
            "type": "Element",
        }
    )
    update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UpdateTime",
            "type": "Element",
        }
    )
    unregistration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UnregistrationTime",
            "type": "Element",
        }
    )
    bind_request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BindRequestId",
            "type": "Element",
        }
    )
    registration_certificate_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationCertificateNumber",
            "type": "Element",
        }
    )
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
        }
    )


@dataclass
class GetRejectionReasonsListRequest(FnsValidators):
    """
    Получение справочника причин отказа в постановке на учет.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetRejectionReasonsListResponse(FnsValidators):
    """
    Ответ на GetRejectionReasonsListRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Codes(FnsValidators):
        """
        :var code: Код причины отказа
        :var description: Описание причины отказа
        """
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Element",
                "required": True,
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            }
        )

    codes: List[Codes] = field(
        default_factory=list,
        metadata={
            "name": "Codes",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetRestrictionsStatusRequest(FnsValidators):
    """
    Получение статуса заявки на наложение ограничений на действия конкретного
    НП НПД в ПП НПД.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetRestrictionsStatusResponse(FnsValidators):
    """
    Ответ на GetRestrictionsStatusRequest.

    :var request_result: Результат рассмотрения
    :var message: Примечание
    :var processing_time: Дата рассмотрения заявки Налоговым Органом
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestResult",
            "type": "Element",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "required": True,
        }
    )
    processing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProcessingTime",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerAccountStatusInfo(FnsValidators):
    """
    Информация о состояния Лицевого счета НП НПД.

    :var id: Идентификатор налогового начисления в КРСБ
    :var payment_time: Дата совершения оплаты НП НПД
    :var payment_received_time: Дата поступления денег в КРСБ
    :var rejection_reason: Причина отказа фиксирования оплаты в КРСБ
    :var amount: Сумма начислений
    :var tax_payment_time: Целевая дата оплаты по начислению
    :var penalty_amount: Сумма пени
    :var tax_bonus: Налоговый бонус
    :var surplus: Сальдо счета
    :var report_time: Дата формирования отчета
    """
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    payment_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PaymentTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    payment_received_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PaymentReceivedTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    rejection_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "RejectionReason",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_payment_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TaxPaymentTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    penalty_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PenaltyAmount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_bonus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxBonus",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    surplus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Surplus",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    report_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ReportTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerAccountStatusRequest(FnsValidators):
    """
    Получение состояния лицевого счета НП НПД.

    :var inn: ИНН пользователя
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerAccountStatusResponse(FnsValidators):
    """
    Ответ на GetTaxpayerAccountStatusRequest.

    :var bonus_amount: Сумма бонусного счета
    :var unpaid_amount: Общая сумма неоплаченных платежей
    :var debt_amount: Сумма задолжности (включена в общая сумму
        неоплаченных платежей)
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    bonus_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BonusAmount",
            "type": "Element",
            "required": True,
        }
    )
    unpaid_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UnpaidAmount",
            "type": "Element",
            "required": True,
        }
    )
    debt_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DebtAmount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerRatingRequest(FnsValidators):
    """
    Получение рейтинга НП НПД.

    Инициатор вызова: банки-партнёры, платформы-партнёры.

    :var inn: ИНН пользователя
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerRatingResponse(FnsValidators):
    """
    Ответ на GetTaxpayerRatingRequest.

    :var rating: Рейтинг
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    rating: str = field(
        default=None,
        metadata={
            "name": "Rating",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerRestrictionsRequest(FnsValidators):
    """
    Проверка наличия ограничений для постановки на учет.

    Инициаторы вызова: банки-партнёры

    Постановка невозможна, если:
    > Уже поставлен на учёт
    > Уже был на учёте и превысил  лимит дохода в налоговом периоде
    > Пользователю запрещено вставать на учёт

    Важно: отсутствие ограничений не гарантирует возможность
    постановки.

    :var inn: ИНН
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


class GetTaxpayerRestrictionsResponseRequestResult(Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"


@dataclass
class GetTaxpayerStatusRequest(FnsValidators):
    """
    Получение детального статуса НП НПД. Только для стоящих на учёте НПД

    Инициатор вызова: банки-партнёры, платформы-партнёры

    :var inn: ИНН пользователя
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerStatusResponse(FnsValidators):
    """
    Ответ на GetTaxpayerStatusRequest.

    :var first_name: Имя пользователя
    :var second_name: Фамилия пользователя
    :var patronymic: Отчество пользователя
    :var registration_time: Дата последней постановки на учёт
    :var unregistration_time: Дата снятия с учёта
    :var unregistration_reason: Причина снятия с учёта
    :var activities: Виды деятельности
    :var region: ОКТМО региона преимущественного ведения деятельности
        на текущий отчетный                             период
    :var phone: Номер телефона
    :var email: E-mail
    :var account_number: Номер счета для уплаты налога
    :var update_time: Дата последнего обновления данных
    :var registration_certificate_number: Номер свидетельства о
        постановке на учет
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    first_name: str = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "required": True,
        }
    )
    second_name: str = field(
        default=None,
        metadata={
            "name": "SecondName",
            "type": "Element",
            "required": True,
        }
    )
    patronymic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Patronymic",
            "type": "Element",
        }
    )
    registration_time: XmlDateTime = field(
        default=None,
        metadata={
            "name": "RegistrationTime",
            "type": "Element",
            "required": True,
        }
    )
    unregistration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UnregistrationTime",
            "type": "Element",
        }
    )
    unregistration_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnregistrationReason",
            "type": "Element",
        }
    )
    activities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Activities",
            "type": "Element",
        }
    )
    region: str = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "required": True,
        }
    )
    phone: str = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Element",
        }
    )
    update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UpdateTime",
            "type": "Element",
        }
    )
    registration_certificate_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationCertificateNumber",
            "type": "Element",
        }
    )


@dataclass
class GetTaxpayerUnregistrationReasonsListRequest(FnsValidators):
    """
    Получение справочника причин по которым НП может подать заявку на снятие с
    учета.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetTaxpayerUnregistrationReasonsListResponse(FnsValidators):
    """
    Ответ на GetTaxpayerUnregistrationReasonsListRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Codes(FnsValidators):
        """
        :var code: Код причины снятия с учёта
        :var description: Описание причины снятия с учёта
        """
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Element",
                "required": True,
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            }
        )

    codes: List[Codes] = field(
        default_factory=list,
        metadata={
            "name": "Codes",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetUnregistrationReasonsListRequest(FnsValidators):
    """
    Получение справочника причин снятия с учета.

    :var request_time: Время запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
        }
    )


@dataclass
class GetUnregistrationReasonsListResponse(FnsValidators):
    """
    Ответ на GetUnregistrationReasonsListRequest.
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Codes(FnsValidators):
        """
        :var code: Код причины отказа постановки на учет
        :var description: Описание причины снятия с учёта
        """
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Element",
                "required": True,
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "required": True,
            }
        )

    codes: List[Codes] = field(
        default_factory=list,
        metadata={
            "name": "Codes",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetUnregistrationStatusRequest(FnsValidators):
    """
    Запрос статуса заявки на снятие с учета.

    :var id: Id заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetUnregistrationStatusResponse(FnsValidators):
    """
    Ответ на GetUnregistrationStatusRequest.

    :var request_result: Результат запроса. `COMPLETED`, `FAILED` or `N_PROGRESS`
    :var rejection_reason: Код причины отказа
    :var unregistration_time: Дата снятия с учёта
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_result: str = field(
        default=None,
        metadata={
            "name": "RequestResult",
            "type": "Element",
            "required": True,
        }
    )
    rejection_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "RejectionReason",
            "type": "Element",
        }
    )
    unregistration_time: XmlDateTime = field(
        default=None,
        metadata={
            "name": "UnregistrationTime",
            "type": "Element",
        }
    )


@dataclass
class IncomeService(FnsValidators):
    """
    Информация по оказанной услуге.

    :var amount: Цена
    :var name: Наименование
    :var quantity: Количество
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class InnByPersonalInfo(FnsValidators):
    """
    ИНН найденный поперсональным данным НП.

    :var inn: ИНН пользрвателя
    :var status: Статус ответа
    """
    inn: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class KeyInfo(FnsValidators):
    """
    Информация о ключе для совершения продаж offline.

    :var inn: ИНН пользователя
    :var key_record:
    """

    @dataclass
    class KeyRecord(FnsValidators):
        """
        :var sequence_number: Инкрементная часть чека
        :var expire_time: Срок валидности
        :var base64_key: Ключ для формирования чека
        """
        sequence_number: Optional[int] = field(
            default=None,
            metadata={
                "name": "SequenceNumber",
                "type": "Element",
                "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
                "required": True,
            }
        )
        expire_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "ExpireTime",
                "type": "Element",
                "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
                "required": True,
            }
        )
        base64_key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Base64Key",
                "type": "Element",
                "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
                "required": True,
            }
        )

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    key_record: List[KeyRecord] = field(
        default_factory=list,
        metadata={
            "name": "KeyRecord",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class Krsb(FnsValidators):
    """
    Карточка расчета с бюджетом (КРСБ) по данным АИС Налог 3.

    :var debt: Сумма задолженности по карточке
    :var penalty: Сумма пени по карточке
    :var overpayment: Сумма переплаты по карточке
    :var oktmo: ОКТМО региона ведения деятельности, связанного с КРСБ
    :var kbk: Код бюджетной классификации, связанный с КРСБ
    :var tax_organ_code: Код налогового органа, связанного с КРСБ
    :var update_time: Дата/Время обновления информации по карточке в ПП
        НПД
    :var id: Внутренний идентификатор карточки в ПП НПД
    """
    debt: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Debt",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    penalty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    overpayment: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Overpayment",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    oktmo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Oktmo",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    kbk: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kbk",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_organ_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxOrganCode",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UpdateTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class NewlyUnboundTaxpayersInfo(FnsValidators):
    """
    Информация о НП НПД.

    :var inn: ИНН пользователя
    :var first_name: Имя пользователя
    :var second_name: Фамилия пользователя
    :var patronymic: Отчество пользователя
    :var unbound_time: Дата отвязки
    :var registration_time: Дата постановки на учёт
    :var phone: Номер телефона
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    second_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    patronymic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Patronymic",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    unbound_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UnboundTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    registration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RegistrationTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class Notifications(FnsValidators):
    """
    Структура для запроса уведомлений НП.

    :var id: Идентификатор уведомления
    :var title: Заголовок уведомления
    :var message: Уведомление
    :var status: Статус уведомления
    :var created_at: Дата создания
    :var updated_at: Дата последнего обновления
    :var partner_id: идентификатор партнера, внесшего последние
        изменения
    :var application_id: идентификатор приложения, внесшего последние
        изменения
    """
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    created_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "createdAt",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    updated_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "updatedAt",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    partner_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "partnerId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    application_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class NotificationsActionRequest(FnsValidators):
    """
    Структура для отметки списка оповещений прочитанными или заархивированными.

    :var inn: ИНН НП
    :var message_id: Список идентификаторов сообщений
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    message_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "messageId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class NotificationsCount(FnsValidators):
    """
    Структура для получния кол-ване прочитанных сообщений.

    :var inn: ИНН НП
    :var count: Кол-во не прочитанных сообщений
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class NotificationsRequest(FnsValidators):
    """
    Структура для запроса уведомлений НП.

    :var inn: ИНН НП
    :var get_acknowleged: Показывать прочитанные
    :var get_archived: Показывать заархивированные
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    get_acknowleged: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GetAcknowleged",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    get_archived: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GetArchived",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class PartnersAndPermissions(FnsValidators):
    """
    Информация о правах выданных партнеру.

    :var partner_id: Id партнера запросившего смену прав
    :var partner_name: Название партнера запросившего смену прав
    :var partner_bind_status: Статус привязки партнера к НП
    :var bind_time: Дата привязки партнера к НП
    :var permissions_change_time: Дата последнего изменения прав
    :var permissions_list: Список текущих разрешений
    """
    partner_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    partner_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    partner_bind_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerBindStatus",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    bind_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "BindTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    permissions_change_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "PermissionsChangeTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    permissions_list: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PermissionsList",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentDocument(FnsValidators):
    """
    Платежный документ.

    :var type: Тип платежного документа
    :var document_index: Индекс документа (УИН)
    :var full_name: ФИО налогоплательщика
    :var address: Адрес места жительства
    :var inn: ИНН налогоплательщика
    :var amount: Сумма к оплате
    :var recipient_bank_name: Банк получателя
    :var recipient_bank_bik: БИК банка получателя
    :var recipient_bank_account_number: Номер счёта банка получателя
    :var recipient: Получатель
    :var recipient_account_number: Номер счёта получателя
    :var recipient_inn: ИНН получателя
    :var recipient_kpp: КПП получателя
    :var kbk: КБК
    :var oktmo: ОКТМО
    :var code101: Код для поля 101
    :var code106: Код для поля 106
    :var code107: Код для поля 107
    :var code110: Код для поля 110
    :var due_date: Оплатить до
    :var create_time: Дата/Время создания документа
    :var source_id: Внутренний идентификатор источника документа в ПП
        НПД
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    document_index: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentIndex",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    recipient_bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecipientBankName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    recipient_bank_bik: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecipientBankBik",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    recipient_bank_account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecipientBankAccountNumber",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    recipient: Optional[str] = field(
        default=None,
        metadata={
            "name": "Recipient",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    recipient_account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecipientAccountNumber",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    recipient_inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecipientInn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    recipient_kpp: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecipientKpp",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    kbk: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kbk",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    oktmo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Oktmo",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    code101: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code101",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    code106: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code106",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    code107: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code107",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    code110: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code110",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    create_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    source_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "SourceId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class PersonalInfo(FnsValidators):
    """
    Персональные данные НП.

    :var first_name: Имя пользователя
    :var second_name: Фамилия пользователя
    :var patronymic: Отчество пользователя
    :var birthday: Дата рождения
    :var passport_series: Серия паспорта
    :var passport_number: Номер паспорта
    """
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    second_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    patronymic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Patronymic",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    birthday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Birthday",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    passport_series: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassportSeries",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    passport_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassportNumber",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class PersonalInfoV3:
    """
    Персональные данные НП V3.

    :var first_name: Имя пользователя
    :var second_name: Фамилия пользователя
    :var patronymic: Отчество пользователя
    :var birthday: Дата рождения
    :var document_spdul: СПДУЛ код документа
    :var document_series: Серия паспорта
    :var document_number: Номер паспорта
    """
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    second_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondName",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    patronymic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Patronymic",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    birthday: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Birthday",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    document_spdul: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentSpdul",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    document_series: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentSeries",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    document_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentNumber",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class PostBindPartnerWithInnRequest(FnsValidators):
    """
    Запрос на привязку НП НПД к партнеру по ИНН.

    :var inn: ИНН пользователя
    :var permissions: Список разрешений на подключение
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    permissions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Permissions",
            "type": "Element",
        }
    )


@dataclass
class PostBindPartnerWithInnResponse(FnsValidators):
    """
    Ответ на PostBindPartnerByInnRequest.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostBindPartnerWithPhoneRequest(FnsValidators):
    """
    Запрос на привязку НП НПД к партнеру по номеру телефона.

    :var phone: Номер телефона НП НПД, указанный при регистрации в ПП
        Самозанятые
    :var permissions: Список разрешений на подключение
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "required": True,
        }
    )
    permissions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Permissions",
            "type": "Element",
        }
    )


@dataclass
class PostBindPartnerWithPhoneResponse(FnsValidators):
    """
    Ответ на PostBindPartnerWithPhoneRequest.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostCancelReceiptRequest(FnsValidators):
    """
    Сторнирование чека.

    :var inn: ИНН пользователя
    :var receipt_id: Id чека
    :var message: Причина отзыва чека
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostCancelReceiptRequestV2:
    """
    Сторнирование чека V2.

    :var inn: ИНН пользователя
    :var receipt_id: Id чека
    :var reason_code: Код причины аннулирования чека:
        1) REFUND (Возврат средств)                             2)
        REGISTRATION_MISTAKE (Чек сформирован ошибочно)
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostCancelReceiptResponse(FnsValidators):
    """
    Ответ на PostCancelReceiptRequest.

    :var request_result: Результат запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostCancelReceiptResponseV2:
    """
    Ответ на PostCancelReceiptRequestV2.

    :var request_result: Результат запроса
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_result: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestResult",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostDecisionPermissionsChangeRequest(FnsValidators):
    """
    Подтверждение/отказ изменения прав.

    :var request_id: Id запроса на изменение прав
    :var inn: ИНН НП по которому происходит смена прав
    :var status: Решение по изменению прав
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requestId",
            "type": "Element",
            "required": True,
        }
    )
    inn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostDecisionPermissionsChangeResponse(FnsValidators):
    """
    Ответ на PostDecisionPermissionsChangeRequest.

    :var status: статус
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostGrantedPermissionsRequest(FnsValidators):
    """
    Запрос на изменение набора прав, выданных НП НПД партнеру.

    :var inn: ИНН пользователя
    :var permissions: Список разрешений на подключение
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    permissions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Permissions",
            "type": "Element",
        }
    )


@dataclass
class PostGrantedPermissionsResponse(FnsValidators):
    """
    Ответ на PostGrantedPermissionsRequest.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostIncomeFromIndividualResponse(FnsValidators):
    """
    Ответ на PostIncomeFromIndividualRequest.

    :var receipt_id: Id чека
    :var link: Ссылка на чек
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "required": True,
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostIncomeResponse(FnsValidators):
    """
    Ответ на PostIncomeRequest.

    :var receipt_id: Id чека
    :var link: Ссылка на чек
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "required": True,
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostIncomeResponseV2:
    """
    Ответ на PostIncomeRequestV2.

    :var receipt_id: Id чека
    :var link: Ссылка на чек
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "required": True,
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNewActivityRequest(FnsValidators):
    """
    Запрос на добавление нового вида деятельности.

    :var activity: Вид деятельности
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    activity: Optional[str] = field(
        default=None,
        metadata={
            "name": "Activity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNewActivityResponse(FnsValidators):
    """
    Ответ на PostNewActivityRequest.

    :var id: ID вида деятельности
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNotificationsAckAllRequest(FnsValidators):
    """
    Отметка всех оповещений как прочитанных.

    :var inn: Список НП которые пометили все сообщения как прочитанные
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class PostNotificationsAckAllResponse(FnsValidators):
    """
    Ответ на запрос PostNotificationsAckAllRequest.

    :var status: статус отметки оповещений прочитанными
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNotificationsAckResponse(FnsValidators):
    """
    Ответ на запрос PostNotificationsAckRequest.

    :var status: статус отметки оповещений прочитанными
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNotificationsArchAllRequest(FnsValidators):
    """
    Отметка всех оповещений как архивных.

    :var inn: Список НП которые пометили все сообщения как
        заархивированные
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class PostNotificationsArchAllResponse(FnsValidators):
    """
    Ответ на запрос PostNotificationsArchRequest.

    :var status: статус отметки оповещений архивными
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNotificationsArchResponse(FnsValidators):
    """
    Ответ на запрос PostNotificationsArchRequest.

    :var status: статус отметки оповещений архивными
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostNotificationsDeliveredResponse(FnsValidators):
    """
    Ответ на запрос PostNotificationsDeliveredRequest.

    :var status: статус отметки оповещений доставленных
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class PostPlatformRegistrationRequestPartnerType(Enum):
    BANK = "BANK"
    PARTNER = "PARTNER"


@dataclass
class PostPlatformRegistrationResponse(FnsValidators):
    """
    Ответ на PostPlatformRegistrationRequest.

    :var partner_id: ID партнера
    :var registration_date: Дата регистрации в ПП Самозанятые
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    partner_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerID",
            "type": "Element",
            "required": True,
        }
    )
    registration_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RegistrationDate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostRegistrationRequest(FnsValidators):
    """
    Постановка на учет. Может осуществляться банками-партнёрами

    Инициаторы вызова: банки-партнёры

    Важно: запрос должен быть подписан УКЭП кредитной организации

    :var inn: ИНН пользователя (обязательное поле если не указана серия
        и номер паспорта)
    :var first_name: Имя пользователя
    :var second_name: Фамилия пользователя
    :var patronymic: Отчество пользователя
    :var birthday: Дата рождения
    :var passport_series: Серия паспорта (обязательное поле если не
        указан ИНН)
    :var passport_number: Номер паспорта (обязательное поле если не
        указан ИНН)
    :var activities: Вид деятельности
    :var phone: Номер телефона
    :var email: E-mail
    :var bankcard_number: Номер банковской карты
    :var bankcard_account_number: Номер счета банкоской карты
    :var request_time: Дата и время формирования запроса
    :var oktmo: ОКТМО региона преимущественного ведения деятельности на
        текущий отчетный период
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
        }
    )
    first_name: str = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "required": True,
        }
    )
    second_name: str = field(
        default=None,
        metadata={
            "name": "SecondName",
            "type": "Element",
            "required": True,
        }
    )
    patronymic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Patronymic",
            "type": "Element",
        }
    )
    birthday: XmlDate = field(
        default=None,
        metadata={
            "name": "Birthday",
            "type": "Element",
            "required": True,
        }
    )
    passport_series: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassportSeries",
            "type": "Element",
        }
    )
    passport_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassportNumber",
            "type": "Element",
        }
    )
    activities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Activities",
            "type": "Element",
        }
    )
    phone: str = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        }
    )
    bankcard_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankcardNumber",
            "type": "Element",
        }
    )
    bankcard_account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankcardAccountNumber",
            "type": "Element",
        }
    )
    request_time: XmlDateTime = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "required": True,
        }
    )
    oktmo: str = field(
        default=None,
        metadata={
            "name": "Oktmo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostRegistrationResponse(FnsValidators):
    """
    Ответ на PostRegistrationRequest.

    :var id: Id заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostRestrictionsRequest(FnsValidators):
    """
    Запрос на наложение ограничений на НП НПД при работе в ПП НПД.

    :var inn: ИНН
    :var type: Тип ограничений
    :var message: Причина введения
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostRestrictionsResponse(FnsValidators):
    """
    Ответ на PostRestrictionsRequest.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostUnbindPartnerRequest(FnsValidators):
    """
    Запрос на отвязку НП НПД от партнера по ИНН.

    :var inn: ИНН пользователя
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostUnbindPartnerResponse(FnsValidators):
    """
    Ответ на PostUnbindPartnerRequest.

    :var unregistration_time: Дата снятия с учёта
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    unregistration_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "UnregistrationTime",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostUnregistrationRequest(FnsValidators):
    """
    Снятие с учета.

    Инициаторы вызовы: банки-партнёры

    :var inn: ИНН пользователя
    :var code: Код причины снятия с учёта
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    code: str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
        }
    )


@dataclass
class PostUnregistrationRequestV2:
    """
    Снятие с учета V2.

    Инициатор вызова: банки-партнёры

    :var inn: ИНН пользователя
    :var reason_code: Код причины снятия с учёта:
        1) REFUSE (Отказываюсь от применения специального
        налогового режима)
        2) RIGHTS_LOST (Утратил право на применение
        специального налогового режима)
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    reason_code: str = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostUnregistrationResponse(FnsValidators):
    """
    Ответ на UnregistrationRequest.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PostUnregistrationResponseV2:
    """
    Ответ на UnregistrationRequestV2.

    :var id: ID заявки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    id: str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PutTaxpayerDataRequest(FnsValidators):
    """
    Обновление настроечных данных НП НПД.

    Инициатор вызова: банки-партнёры

    Процедура выполняется Партнером только в случае
    наличия разрешения со стороны НП НПД на выполнение
    таких действие от его имени.

    :var inn: ИНН пользователя
    :var phone: Номер телефона
    :var email: E-mail
    :var activities: Вид деятельности
    :var region: ОКТМО региона преимущественного ведения деятельности
        на текущий отчетный                             период
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        }
    )
    activities: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Activities",
            "type": "Element",
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        }
    )


@dataclass
class PutTaxpayerDataResponse(FnsValidators):
    """
    Ответ на PutTaxpayerDataRequest.

    :var update_time: Дата последнего обновления данных
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    update_time: XmlDateTime = field(
        default=None,
        metadata={
            "name": "UpdateTime",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SmzPlatformError(FnsValidators):
    """
    Бизнес ошибка в платформе СМЗ.

    :var code: Код ошибки
    :var message: Сообщение конечному пользователю в виде шаблона с
        {attrKey} атрибутами
    :var args: Аргументы для сообщения пользователю
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    @dataclass
    class Args(FnsValidators):
        """
        :var key: Ключ
        :var value: Значение
        """
        key: Optional[str] = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Element",
                "required": True,
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Element",
                "required": True,
            }
        )

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
            "required": True,
        }
    )
    args: List[Args] = field(
        default_factory=list,
        metadata={
            "name": "Args",
            "type": "Element",
        }
    )


@dataclass
class TaxCharge(FnsValidators):
    """
    Налоговое начисление.

    :var amount: Сумма начисления
    :var due_date: Срок оплаты
    :var tax_period_id: Идентификатор налогового периода (YYYYMM)
    :var oktmo: ОКТМО региона ведения деятельности
    :var kbk: Код бюджетной классификации
    :var paid_amount: Сумма поступивших оплат в АИС Налог 3 по данному
        начислению
    :var create_time: Дата/Время создания налогового начисления
    :var id: Внутренний идентификатор налогового начисления в ПП НПД
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDate",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_period_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "TaxPeriodId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    oktmo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Oktmo",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    kbk: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kbk",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    paid_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PaidAmount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    create_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreateTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class AccrualsAndDebts(FnsValidators):
    """
    Налоговые начисления и задолженности по НП.

    :var inn: ИНН пользователя
    :var tax_charge_list: Список налоговых начислений
    :var krsb_list: Список карточек расчета с бюджетом
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_charge_list: List[TaxCharge] = field(
        default_factory=list,
        metadata={
            "name": "TaxChargeList",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    krsb_list: List[Krsb] = field(
        default_factory=list,
        metadata={
            "name": "KrsbList",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class GetIncomeReferenceResponseV2:
    """
    Ответ на GetIncomeReferenceRequestV2.

    :var income_reference_pdf: PDF файл справки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    income_reference_pdf: Optional[AttachedFile] = field(
        default=None,
        metadata={
            "name": "IncomeReferencePdf",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetInnByPersonalInfoRequestV2:
    """
    Получение ИНН по листу персональных данных.

    :var personal_info_list: Список персональных данных на получение
        ИНН
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    personal_info_list: List[PersonalInfo] = field(
        default_factory=list,
        metadata={
            "name": "PersonalInfoList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )


@dataclass
class GetInnByPersonalInfoRequestV3:
    """
    Получение ИНН по листу персональных данных V3.

    :var personal_info_list: Список персональных данных на получение
        ИНН
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    personal_info_list: List[PersonalInfoV3] = field(
        default_factory=list,
        metadata={
            "name": "PersonalInfoList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )


@dataclass
class GetInnByPersonalInfoResponseV2:
    """
    Ответ на GetInnByPersonalInfoRequestV2.

    :var inn_list: Список ИНН по запрашиваемым персональным данным
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn_list: List[InnByPersonalInfo] = field(
        default_factory=list,
        metadata={
            "name": "InnList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )


@dataclass
class GetInnByPersonalInfoResponseV3:
    """
    Ответ на GetInnByPersonalInfoRequestV3.

    :var inn_list: Список ИНН по запрашиваемым персональным данным
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn_list: List[InnByPersonalInfo] = field(
        default_factory=list,
        metadata={
            "name": "InnList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
        }
    )


@dataclass
class GetKeysResponse(FnsValidators):
    """
    Ответ на GetKeysRequest.

    :var keys: Ключи для работы оффлайн
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    keys: List[KeyInfo] = field(
        default_factory=list,
        metadata={
            "name": "Keys",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetNewPermissionsChangeResponse(FnsValidators):
    """
    Ответ на GetNewPermissionsChangeRequest.

    :var taxpayers: Информация о запрашиваемых сменах прав
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    taxpayers: List[ChangePermissoinsInfo] = field(
        default_factory=list,
        metadata={
            "name": "Taxpayers",
            "type": "Element",
        }
    )


@dataclass
class GetNewlyUnboundTaxpayersResponse(FnsValidators):
    """
    Ответ на GetNewlyUnboundTaxpayersRequest.

    :var taxpayers: Информация о НП НПД
    :var has_more: Есть ли ещё НП НПД на следующих страницах
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    taxpayers: List[NewlyUnboundTaxpayersInfo] = field(
        default_factory=list,
        metadata={
            "name": "Taxpayers",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    has_more: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMore",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetNotificationsCountResponse(FnsValidators):
    """
    Ответ на запрос GetNotificationsCountRequest.

    :var status: Кол-во не прочитанных оповещений по НП
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    status: List[NotificationsCount] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class GetNotificationsRequest(FnsValidators):
    """
    Получение списка оповещений для НП НПД.

    :var notifications_request: Список НП по которым запрашиваются
        оповещения
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    notifications_request: List[NotificationsRequest] = field(
        default_factory=list,
        metadata={
            "name": "notificationsRequest",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class GetPartnersPermissionsResponse(FnsValidators):
    """
    Ответ на GetPartnersPermissionsRequest.

    :var partners_permissions_list: Список выданных разрешений
        партнерам
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    partners_permissions_list: List[PartnersAndPermissions] = field(
        default_factory=list,
        metadata={
            "name": "PartnersPermissionsList",
            "type": "Element",
        }
    )


@dataclass
class GetRegistrationReferenceResponseV2:
    """
    Ответ на GetRegistrationReferenceRequestV2.

    :var registration_reference_pdf: PDF файл справки
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    registration_reference_pdf: Optional[AttachedFile] = field(
        default=None,
        metadata={
            "name": "RegistrationReferencePdf",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetTaxpayerRestrictionsResponse(FnsValidators):
    """
    Ответ на GetTaxpayerRestrictionsRequest.

    :var request_result: Результат запроса
    :var rejection_code: Код причины отказа
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    request_result: GetTaxpayerRestrictionsResponseRequestResult = field(
        default=None,
        metadata={
            "name": "RequestResult",
            "type": "Element",
            "required": True,
        }
    )
    rejection_code: str = field(
        default=None,
        metadata={
            "name": "RejectionCode",
            "type": "Element",
        }
    )


@dataclass
class NotificationsResponse(FnsValidators):
    """
    Структура получения уведомлений из ПП НПД.

    :var inn: ИНН НП
    :var notif: Лист уведомлений
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    notif: List[Notifications] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class PaymentDocumentList(FnsValidators):
    """
    Список платежных документов для НП.

    :var inn: ИНН пользователя
    :var document_list: Список платежных документов
    """
    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    document_list: List[PaymentDocument] = field(
        default_factory=list,
        metadata={
            "name": "DocumentList",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )


@dataclass
class PostIncomeFromIndividualRequest(FnsValidators):
    """
    Регистрация дохода от Физического лица партнером.

    :var inn: ИНН пользователя
    :var receipt_id: Id чека (offline режим)
    :var request_time: Дата формирования
    :var operation_time: Дата расчёта
    :var supplier_inn: ИНН поставщика данных(площадки третьего звена)
    :var services: Список услуг
    :var total_amount: Общая стоимость оказанных услуг
    :var income_hash_code: ФП чека (offline режим)
    :var link: Ссылка (offline режим)
    :var geo_info: Координаты продажи
    :var operation_unique_id: Уникальный идентификатор операции
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "required": True,
        }
    )
    operation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "required": True,
        }
    )
    supplier_inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierInn",
            "type": "Element",
        }
    )
    services: List[IncomeService] = field(
        default_factory=list,
        metadata={
            "name": "Services",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 6,
        }
    )
    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "required": True,
        }
    )
    income_hash_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncomeHashCode",
            "type": "Element",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
        }
    )
    geo_info: Optional[GeoInfo] = field(
        default=None,
        metadata={
            "name": "GeoInfo",
            "type": "Element",
        }
    )
    operation_unique_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationUniqueId",
            "type": "Element",
        }
    )


@dataclass
class PostIncomeRequest(FnsValidators):
    """
    Регистрация дохода партнером.

    :var inn: ИНН пользователя
    :var receipt_id: Id чека (offline режим)
    :var request_time: Дата формирования
    :var operation_time: Дата расчёта
    :var income_type: Источник/Тип дохода:
        1) FROM_INDIVIDUAL (Доход от Физического Лица)
        2) FROM_LEGAL_ENTITY (Доход от Юридического Лица)
        3) FROM_FOREIGN_AGENCY (Доход от Иностранной Организации)
    :var customer_inn: ИНН покупателя
    :var customer_organization: Организация покупателя
    :var services: Список услуг
    :var total_amount: Общая стоимость оказанных услуг
    :var income_hash_code: ФП чека (offline режим)
    :var link: Ссылка (offline режим)
    :var geo_info: Координаты продажи
    :var operation_unique_id: Уникальный идентификатор операции
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "required": True,
        }
    )
    operation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "required": True,
        }
    )
    income_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncomeType",
            "type": "Element",
        }
    )
    customer_inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerInn",
            "type": "Element",
        }
    )
    customer_organization: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerOrganization",
            "type": "Element",
        }
    )
    services: Optional[IncomeService] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Element",
            "required": True,
        }
    )
    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "required": True,
        }
    )
    income_hash_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncomeHashCode",
            "type": "Element",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
        }
    )
    geo_info: Optional[GeoInfo] = field(
        default=None,
        metadata={
            "name": "GeoInfo",
            "type": "Element",
        }
    )
    operation_unique_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationUniqueId",
            "type": "Element",
        }
    )


@dataclass
class PostIncomeRequestV2:
    """
    Регистрация дохода партнером с возможностью указания нескольких услуг.

    :var inn: ИНН пользователя
    :var receipt_id: Id чека (offline режим)
    :var request_time: Дата формирования
    :var operation_time: Дата расчёта
    :var income_type: Источник/Тип дохода:
        1) FROM_INDIVIDUAL (Доход от Физического Лица)
        2) FROM_LEGAL_ENTITY (Доход от Юридического Лица)
        3) FROM_FOREIGN_AGENCY (Доход от Иностранной Организации)
    :var customer_inn: ИНН покупателя
    :var customer_organization: Организация покупателя
    :var supplier_inn: ИНН поставщика данных(площадки третьего звена)
    :var services: Список услуг
    :var total_amount: Общая стоимость оказанных услуг
    :var income_hash_code: ФП чека (offline режим)
    :var link: Ссылка (offline режим)
    :var geo_info: Координаты продажи
    :var operation_unique_id: Уникальный идентификатор операции
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "required": True,
        }
    )
    operation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "required": True,
        }
    )
    income_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncomeType",
            "type": "Element",
            "required": True,
        }
    )
    customer_inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerInn",
            "type": "Element",
        }
    )
    customer_organization: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomerOrganization",
            "type": "Element",
        }
    )
    supplier_inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierInn",
            "type": "Element",
        }
    )
    services: List[IncomeService] = field(
        default_factory=list,
        metadata={
            "name": "Services",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 6,
        }
    )
    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "required": True,
        }
    )
    income_hash_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncomeHashCode",
            "type": "Element",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
        }
    )
    geo_info: Optional[GeoInfo] = field(
        default=None,
        metadata={
            "name": "GeoInfo",
            "type": "Element",
        }
    )
    operation_unique_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationUniqueId",
            "type": "Element",
        }
    )


@dataclass
class PostNotificationsAckRequest(FnsValidators):
    """
    Отметка оповещения как прочитанного.

    :var notification_list: Список НП и оповещений, которые были
        прочитаны
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    notification_list: List[NotificationsActionRequest] = field(
        default_factory=list,
        metadata={
            "name": "notificationList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class PostNotificationsArchRequest(FnsValidators):
    """
    Отметка оповещения как архивного.

    :var notification_list: Список НП и оповещений, которые были
        заархивированны
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    notification_list: List[NotificationsActionRequest] = field(
        default_factory=list,
        metadata={
            "name": "notificationList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class PostNotificationsDeliveredRequest(FnsValidators):
    """
    Отметка оповещения как доставленного клиенту.

    :var notification_list: Список НП и оповещений, которые были
        доставлены
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    notification_list: List[NotificationsActionRequest] = field(
        default_factory=list,
        metadata={
            "name": "notificationList",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class PostPlatformRegistrationRequest(FnsValidators):
    """
    Регистрация приложения партнера.

    Инициатор вызова: банки-партнеры, платформы-партнеры.

    Процедура должна вызываться партнерами в самом
    начале взаимодействия с ПП НПД. Партнер передает
    сведения о себе в ПП НПД.

    :var partner_name: Название партнера
    :var partner_type: Тип партнера (BANK или PARTNER)
    :var partner_description: Описание партнера
    :var partner_connectable: Доступность для подключения из ЛК НПД
    :var partner_available_for_bind: Доступен ли партнер для запросов
        на подключение со стороны ПП НПД
    :var transition_link: Diplink или ссылка на ресурс партнера для
        перехода и начала привязки
    :var partners_text: Текст партнера для отображения в ЛК НПД и МП
        МойНалог
    :var partner_image: Ссылка на картинку с логотипом
    :var inn: ИНН партнера
    :var phone: Номер телефона для связи
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    partner_name: str = field(
        default=None,
        metadata={
            "name": "PartnerName",
            "type": "Element",
            "required": True,
        }
    )
    partner_type: PostPlatformRegistrationRequestPartnerType = field(
        default=None,
        metadata={
            "name": "PartnerType",
            "type": "Element",
            "required": True,
        }
    )
    partner_description: str = field(
        default=None,
        metadata={
            "name": "PartnerDescription",
            "type": "Element",
        }
    )
    partner_connectable: str = field(
        default=None,
        metadata={
            "name": "PartnerConnectable",
            "type": "Element",
            "required": True,
        }
    )
    partner_available_for_bind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PartnerAvailableForBind",
            "type": "Element",
        }
    )
    transition_link: str = field(
        default=None,
        metadata={
            "name": "TransitionLink",
            "type": "Element",
        }
    )
    partners_text: str = field(
        default=None,
        metadata={
            "name": "PartnersText",
            "type": "Element",
        }
    )
    partner_image: bytes = field(
        default=None,
        metadata={
            "name": "PartnerImage",
            "type": "Element",
            "format": "base64",
        }
    )
    inn: str = field(
        default=None,
        metadata={
            "name": "Inn",
            "type": "Element",
            "required": True,
        }
    )
    phone: str = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Receipt(FnsValidators):
    """
    Информация о выписанном чеке.

    :var link: Ссылка на чек
    :var total_amount: Сумма чека
    :var receipt_id: ID чека
    :var request_time: Дата формирования
    :var operation_time: Дата расчёта
    :var partner_code: ID банка/платформы-партнера
    :var cancelation_time: Дата сторнирования
    :var services: Список услуг
    """
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    operation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    partner_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerCode",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    cancelation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CancelationTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    services: Optional[IncomeService] = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )


@dataclass
class ReceiptV2:
    """
    Информация о выписанном чеке с несколькими услугами.

    :var link: Ссылка на чек
    :var total_amount: Сумма чека
    :var receipt_id: ID чека
    :var income_type: Источник/Тип дохода:
        1) FROM_INDIVIDUAL (Доход от Физического Лица)
        2) FROM_LEGAL_ENTITY (Доход от Юридического Лица)
        3) FROM_FOREIGN_AGENCY (Доход от Иностранной Организации)
    :var request_time: Дата формирования
    :var operation_time: Дата расчёта
    :var tax_period_id: Налоговый период, в котором при расчете налога
        будет/был учтен чек (формат, yyyyMM)
    :var tax_to_pay: Налог к уплате с данного чека (начисленный налог -
        использованный бонус)
    :var partner_code: ID банка/платформы-партнера
    :var supplier_inn: ИНН поставщика данных(площадки третьего звена)
    :var cancelation_time: Дата сторнирования
    :var services: Список услуг
    """
    link: Optional[str] = field(
        default=None,
        metadata={
            "name": "Link",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    receipt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    income_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IncomeType",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    request_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    operation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_period_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPeriodId",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    tax_to_pay: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TaxToPay",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "required": True,
        }
    )
    partner_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartnerCode",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    supplier_inn: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierInn",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    cancelation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CancelationTime",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
        }
    )
    services: List[IncomeService] = field(
        default_factory=list,
        metadata={
            "name": "Services",
            "type": "Element",
            "namespace": "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class GetAccrualsAndDebtsResponse(FnsValidators):
    """
    Ответ на GetAccrualsAndDebtsRequest.

    :var accruals_and_debts_list: Список начислений для каждого НП
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    accruals_and_debts_list: List[AccrualsAndDebts] = field(
        default_factory=list,
        metadata={
            "name": "AccrualsAndDebtsList",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class GetIncomeResponse(FnsValidators):
    """
    Ответ на GetIncomeRequest.

    :var has_more: Есть ли ещё чеки в списке
    :var receipts: Список полученных чеков
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    has_more: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMore",
            "type": "Element",
            "required": True,
        }
    )
    receipts: List[Receipt] = field(
        default_factory=list,
        metadata={
            "name": "Receipts",
            "type": "Element",
        }
    )


@dataclass
class GetIncomeResponseV2:
    """
    Ответ на GetIncomeRequestV2.

    :var has_more: Есть ли ещё чеки в списке
    :var receipts: Список полученных чеков
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    has_more: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasMore",
            "type": "Element",
            "required": True,
        }
    )
    receipts: List[ReceiptV2] = field(
        default_factory=list,
        metadata={
            "name": "Receipts",
            "type": "Element",
        }
    )


@dataclass
class GetNotificationsResponse(FnsValidators):
    """
    Ответ на запрос GetNotificationsRequest.

    :var notifications_response: Список оповещений по НП
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    notifications_response: List[NotificationsResponse] = field(
        default_factory=list,
        metadata={
            "name": "notificationsResponse",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class GetPaymentDocumentsResponse(FnsValidators):
    """
    Ответ на GetPaymentDocumentsRequest.

    :var payment_documents_list: Список платежных документов для
        каждого НП
    """
    class Meta:
        namespace = "urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"

    payment_documents_list: List[PaymentDocumentList] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDocumentsList",
            "type": "Element",
            "min_occurs": 1,
        }
    )
