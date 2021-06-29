_smz_schema = """<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:smz="urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="urn://x-artefacts-gnivc-ru/ais3/SMZ/SmzPartnersIntegrationService/types/1.0"
           elementFormDefault="qualified" version="0.28">

    <xs:complexType name="IncomeService">
        <xs:annotation>
            <xs:documentation>Информация по оказанной услуге</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Amount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Цена</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Наименование</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Quantity" type="xs:long" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Количество</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="Receipt">
        <xs:annotation>
            <xs:documentation>Информация о выписанном чеке</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Link" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Ссылка на чек</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TotalAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма чека</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="ReceiptId" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ID чека</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата формирования</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="OperationTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата расчёта</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PartnerCode" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ID банка/платформы-партнера</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="CancelationTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата сторнирования</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Services" type="smz:IncomeService" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Список услуг</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ReceiptV2">
        <xs:annotation>
            <xs:documentation>Информация о выписанном чеке с несколькими услугами</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Link" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Ссылка на чек</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TotalAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма чека</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="ReceiptId" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ID чека</xs:documentation>
                </xs:annotation>
            </xs:element>
			<xs:element name="IncomeType" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Источник/Тип дохода:
                            1) FROM_INDIVIDUAL (Доход от Физического Лица)
                            2) FROM_LEGAL_ENTITY (Доход от Юридического Лица)
                            3) FROM_FOREIGN_AGENCY (Доход от Иностранной Организации)
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата формирования</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="OperationTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата расчёта</xs:documentation>
                </xs:annotation>
            </xs:element>
			<xs:element name="TaxPeriodId" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Налоговый период, в котором при расчете налога будет/был учтен чек (формат, yyyyMM)</xs:documentation>
                </xs:annotation>
            </xs:element>
			<xs:element name="TaxToPay" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Налог к уплате с данного чека (начисленный налог - использованный бонус)</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PartnerCode" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ID банка/платформы-партнера</xs:documentation>
                </xs:annotation>
            </xs:element>
			<xs:element name="SupplierInn" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН поставщика данных(площадки третьего звена)</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="CancelationTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата сторнирования</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Services" type="smz:IncomeService" minOccurs="1" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список услуг</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="GeoInfo">
        <xs:annotation>
            <xs:documentation>Информация о местоположении пользователя во время выполнения запроса</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Latitude" type="xs:double" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Широта</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Longitude" type="xs:double" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Долгота</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="NewlyUnboundTaxpayersInfo">
        <xs:annotation>
            <xs:documentation>Информация о НП НПД</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="FirstName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Имя пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="SecondName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Фамилия пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Patronymic" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Отчество пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="UnboundTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата отвязки</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RegistrationTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата постановки на учёт</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Phone" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Номер телефона</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="KeyInfo">
        <xs:annotation>
            <xs:documentation>Информация о ключе для совершения продаж offline</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Inn" type="xs:string">
                <xs:annotation>
                    <xs:documentation>ИНН пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="KeyRecord" minOccurs="0" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="SequenceNumber" type="xs:int">
                            <xs:annotation>
                                <xs:documentation>Инкрементная часть чека</xs:documentation>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="ExpireTime" type="xs:dateTime">
                            <xs:annotation>
                                <xs:documentation>Срок валидности</xs:documentation>
                            </xs:annotation>
                        </xs:element>
                        <xs:element name="Base64Key" type="xs:string">
                            <xs:annotation>
                                <xs:documentation>Ключ для формирования чека</xs:documentation>
                            </xs:annotation>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="GetTaxpayerAccountStatusInfo">
        <xs:annotation>
            <xs:documentation>Информация о состояния Лицевого счета НП НПД</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Идентификатор налогового начисления в КРСБ</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PaymentTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата совершения оплаты НП НПД</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PaymentReceivedTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата поступления денег в КРСБ</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RejectionReason" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Причина отказа фиксирования оплаты в КРСБ</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Amount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма начислений</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TaxPaymentTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Целевая дата оплаты по начислению</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PenaltyAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма пени</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TaxBonus" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Налоговый бонус</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Surplus" type="xs:decimal">
                <xs:annotation>
                    <xs:documentation>Сальдо счета</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="ReportTime" type="xs:dateTime">
                <xs:annotation>
                    <xs:documentation>Дата формирования отчета</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="AttachedFile">
        <xs:annotation>
            <xs:documentation>Присоединенный файл</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element minOccurs="0" name="mimetype" type="xs:string">
                <xs:annotation>
                    <xs:documentation>MIME тип файла</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element minOccurs="0" name="filename" type="xs:string">
                <xs:annotation>
                    <xs:documentation>Имя файла</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="content" type="xs:base64Binary">
                <xs:annotation>
                    <xs:documentation>Содержимое файла</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PersonalInfo">
        <xs:annotation>
            <xs:documentation>Персональные данные НП</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="FirstName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Имя пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="SecondName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Фамилия пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Patronymic" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Отчество пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Birthday" type="xs:date" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата рождения</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PassportSeries" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Серия паспорта</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PassportNumber" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Номер паспорта</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="PersonalInfoV3">
        <xs:annotation>
            <xs:documentation>Персональные данные НП V3</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="FirstName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Имя пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="SecondName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Фамилия пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Patronymic" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Отчество пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Birthday" type="xs:date" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата рождения</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DocumentSpdul" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>СПДУЛ код документа</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DocumentSeries" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Серия паспорта</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DocumentNumber" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Номер паспорта</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="InnByPersonalInfo">
        <xs:annotation>
            <xs:documentation>ИНН найденный поперсональным данным НП</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Inn" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>ИНН пользрвателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Status" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Статус ответа</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="NotificationsRequest">
        <xs:annotation>
            <xs:documentation>Структура для запроса уведомлений НП</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН НП</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="GetAcknowleged" type="xs:boolean" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Показывать прочитанные</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="GetArchived" type="xs:boolean" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Показывать заархивированные</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="NotificationsResponse">
        <xs:annotation>
            <xs:documentation>Структура получения уведомлений из ПП НПД</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН НП</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="notif" type="smz:Notifications" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Лист уведомлений</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="Notifications">
        <xs:annotation>
            <xs:documentation>Структура для запроса уведомлений НП</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="id" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Идентификатор уведомления</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="title" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Заголовок уведомления</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="message" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Уведомление</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Статус уведомления</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="createdAt" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата создания</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="updatedAt" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата последнего обновления</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="partnerId" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>идентификатор партнера, внесшего последние изменения</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="applicationId" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>идентификатор приложения, внесшего последние изменения</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="NotificationsActionRequest">
        <xs:annotation>
            <xs:documentation>Структура для отметки списка оповещений прочитанными или заархивированными</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН НП</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="messageId" type="xs:string" minOccurs="1" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список идентификаторов сообщений</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="NotificationsCount">
        <xs:annotation>
            <xs:documentation>Структура для получния кол-ване прочитанных сообщений</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН НП</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="count" type="xs:int" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Кол-во не прочитанных сообщений</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PartnersAndPermissions">
        <xs:annotation>
            <xs:documentation>Информация о правах выданных партнеру</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="PartnerId" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Id партнера запросившего смену прав</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PartnerName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Название партнера запросившего смену прав</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PartnerBindStatus" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Статус привязки партнера к НП</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="BindTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата привязки партнера к НП</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PermissionsChangeTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата последнего изменения прав</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PermissionsList" type="xs:string" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список текущих разрешений</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="ChangePermissoinsInfo">
        <xs:annotation>
            <xs:documentation>Информация о смене прав</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="requestId" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Id запроса на смену прав</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="requestPartnerId" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Id партнера запросившего смену прав</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PartnerName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Название партнера запросившего смену прав</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PermissionsList" type="xs:string" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список новых запрашиваемых разрешений</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата последней постановки на учёт</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="TaxCharge">
        <xs:annotation>
            <xs:documentation>Налоговое начисление</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Amount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма начисления</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DueDate" type="xs:date" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Срок оплаты</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TaxPeriodId" type="xs:int" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Идентификатор налогового периода (YYYYMM)</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Oktmo" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ОКТМО региона ведения деятельности</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Kbk" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Код бюджетной классификации</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="PaidAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма поступивших оплат в АИС Налог 3 по данному начислению</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="CreateTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата/Время создания налогового начисления</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Id" type="xs:long" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Внутренний идентификатор налогового начисления в ПП НПД</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="Krsb">
        <xs:annotation>
            <xs:documentation>Карточка расчета с бюджетом (КРСБ) по данным АИС Налог 3</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Debt" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма задолженности по карточке</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Penalty" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма пени по карточке</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Overpayment" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма переплаты по карточке</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Oktmo" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ОКТМО региона ведения деятельности, связанного с КРСБ</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Kbk" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Код бюджетной классификации, связанный с КРСБ</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TaxOrganCode" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Код налогового органа, связанного с КРСБ</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="UpdateTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата/Время обновления информации по карточке в ПП НПД</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Id" type="xs:long" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Внутренний идентификатор карточки в ПП НПД</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="AccrualsAndDebts">
        <xs:annotation>
            <xs:documentation>Налоговые начисления и задолженности по НП</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="TaxChargeList" type="smz:TaxCharge" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список налоговых начислений</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="KrsbList" type="smz:Krsb" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список карточек расчета с бюджетом</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:complexType name="PaymentDocument">
        <xs:annotation>
            <xs:documentation>Платежный документ</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Type" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Тип платежного документа</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DocumentIndex" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Индекс документа (УИН)</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="FullName" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ФИО налогоплательщика</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Address" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Адрес места жительства</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН налогоплательщика</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Amount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Сумма к оплате</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RecipientBankName" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Банк получателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RecipientBankBik" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>БИК банка получателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RecipientBankAccountNumber" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Номер счёта банка получателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Recipient" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Получатель</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RecipientAccountNumber" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Номер счёта получателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RecipientInn" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН получателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="RecipientKpp" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>КПП получателя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Kbk" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>КБК</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Oktmo" type="xs:string" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ОКТМО</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Code101" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Код для поля 101</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Code106" type="xs:string">
                <xs:annotation>
                    <xs:documentation>Код для поля 106</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Code107" type="xs:string">
                <xs:annotation>
                    <xs:documentation>Код для поля 107</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="Code110" type="xs:string">
                <xs:annotation>
                    <xs:documentation>Код для поля 110</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DueDate" type="xs:date" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Оплатить до</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="CreateTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Дата/Время создания документа</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="SourceId" type="xs:long" minOccurs="0" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>Внутренний идентификатор источника документа в ПП НПД</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="PaymentDocumentList">
        <xs:annotation>
            <xs:documentation>Список платежных документов для НП</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                <xs:annotation>
                    <xs:documentation>ИНН пользователя</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="DocumentList" type="smz:PaymentDocument" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Список платежных документов</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
    </xs:complexType>

    <xs:element name="SmzPlatformError">
        <xs:annotation>
            <xs:documentation>Бизнес ошибка в платформе СМЗ</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Code" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Код ошибки</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Message" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Сообщение конечному пользователю в виде шаблона с {attrKey} атрибутами
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Args" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Аргументы для сообщения пользователю</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Key" type="xs:string" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>Ключ</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Value" type="xs:string" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>Значение</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerRestrictionsRequest">
        <xs:annotation>
            <xs:documentation>Проверка наличия ограничений для постановки на учет</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerRestrictionsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetTaxpayerRestrictionsRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestResult">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="ALLOW"/>
                            <xs:enumeration value="DENY"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="RejectionCode" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Код причины отказа</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerStatusRequest">
        <xs:annotation>
            <xs:documentation>Получение детального статуса НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetTaxpayerStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="FirstName" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Имя пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="SecondName" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Фамилия пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Patronymic" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Отчество пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RegistrationTime" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата последней постановки на учёт</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UnregistrationTime" type="xs:dateTime" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Дата снятия с учёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UnregistrationReason" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Причина снятия с учёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Activities" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Виды деятельности</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Region" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ОКТМО региона преимущественного ведения деятельности на текущий отчетный
                            период
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Phone" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Номер телефона</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Email" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>E-mail</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="AccountNumber" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Номер счета для уплаты налога</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UpdateTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата последнего обновления данных</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RegistrationCertificateNumber" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Номер свидетельства о постановке на учет</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostRegistrationRequest">
        <xs:annotation>
            <xs:documentation>Постановка на учет</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя (обязательное поле если не указана серия и номер паспорта)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="FirstName" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Имя пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="SecondName" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Фамилия пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Patronymic" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Отчество пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Birthday" type="xs:date" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата рождения</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PassportSeries" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Серия паспорта (обязательное поле если не указан ИНН)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PassportNumber" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер паспорта (обязательное поле если не указан ИНН)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Activities" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Вид деятельности</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Phone" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер телефона</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Email" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>E-mail</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="BankcardNumber" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер банковской карты</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="BankcardAccountNumber" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер счета банкоской карты</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата и время формирования запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Oktmo" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ОКТМО региона преимущественного ведения деятельности на текущий отчетный
                            период
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostRegistrationResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostRegistrationRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Id заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRegistrationStatusRequest">
        <xs:annotation>
            <xs:documentation>Запрос статуса заявки на постановку на учет</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRegistrationStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetRegistrationStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestResult" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RejectionReason" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Код причины отказа</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RegistrationTime" type="xs:dateTime" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Дата текущей постановки на учет</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="LastRegistrationTime" type="xs:dateTime" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Дата последней постановки на учет</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UpdateTime" type="xs:dateTime" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Дата последнего обновления данных</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UnregistrationTime" type="xs:dateTime" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Дата снятия с учёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="BindRequestId" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>ID запроса на согласование разрешений для партнера от НП НПД
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RegistrationCertificateNumber" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Номер свидетельства о постановке на учет</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Inn" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>ИНН налогоплательщика</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostUnregistrationRequest">
        <xs:annotation>
            <xs:documentation>Снятие с учета</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Code" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Код причины снятия с учёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostUnregistrationResponse">
        <xs:annotation>
            <xs:documentation>Ответ на UnregistrationRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostUnregistrationRequestV2">
        <xs:annotation>
            <xs:documentation>Снятие с учета V2</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReasonCode" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Код причины снятия с учёта:
                            1) REFUSE (Отказываюсь от применения специального налогового режима)
                            2) RIGHTS_LOST (Утратил право на применение специального налогового режима)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostUnregistrationResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на UnregistrationRequestV2.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetUnregistrationStatusRequest">
        <xs:annotation>
            <xs:documentation>Запрос статуса заявки на снятие с учета</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetUnregistrationStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetUnregistrationProcessStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestResult" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RejectionReason" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Код причины отказа</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UnregistrationTime" type="xs:dateTime" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>Дата снятия с учёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PutTaxpayerDataRequest">
        <xs:annotation>
            <xs:documentation>Обновление настроечных данных НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Phone" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер телефона</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Email" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>E-mail</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Activities" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Вид деятельности</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Region" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>ОКТМО региона преимущественного ведения деятельности на текущий отчетный
                            период
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PutTaxpayerDataResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PutTaxpayerDataRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="UpdateTime" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата последнего обновления данных</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerAccountStatusRequest">
        <xs:annotation>
            <xs:documentation>Получение состояния лицевого счета НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerAccountStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetTaxpayerAccountStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="BonusAmount" type="xs:decimal">
                    <xs:annotation>
                        <xs:documentation>Сумма бонусного счета</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="UnpaidAmount" type="xs:decimal">
                    <xs:annotation>
                        <xs:documentation>Общая сумма неоплаченных платежей</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="DebtAmount" type="xs:decimal">
                    <xs:annotation>
                        <xs:documentation>Сумма задолжности (включена в общая сумму неоплаченных платежей)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostBindPartnerWithInnRequest">
        <xs:annotation>
            <xs:documentation>Запрос на привязку НП НПД к партнеру по ИНН.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Permissions" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список разрешений на подключение</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostBindPartnerWithInnResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostBindPartnerByInnRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostBindPartnerWithPhoneRequest">
        <xs:annotation>
            <xs:documentation>Запрос на привязку НП НПД к партнеру по номеру телефона.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Phone" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Номер телефона НП НПД, указанный при регистрации в ПП Самозанятые
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Permissions" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список разрешений на подключение</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostBindPartnerWithPhoneResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostBindPartnerWithPhoneRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetBindPartnerStatusRequest">
        <xs:annotation>
            <xs:documentation>Получение статуса заявки на привязку НП НПД к партнеру</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetBindPartnerStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetBindPartnerStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Result" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Inn" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Permissions" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список согласованных разрешений</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ProcessingTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата рассмотрения заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostGrantedPermissionsRequest">
        <xs:annotation>
            <xs:documentation>Запрос на изменение набора прав, выданных НП НПД партнеру</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Permissions" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список разрешений на подключение</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostGrantedPermissionsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostGrantedPermissionsRequest</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostUnbindPartnerRequest">
        <xs:annotation>
            <xs:documentation>Запрос на отвязку НП НПД от партнера по ИНН</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostUnbindPartnerResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostUnbindPartnerRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="UnregistrationTime" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата снятия с учёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetGrantedPermissionsRequest">
        <xs:annotation>
            <xs:documentation>Получение списка разрешений, предоставленных партнеру</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetGrantedPermissionsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetGrantedPermissionsRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="GrantedPermissionsList" type="xs:string" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список выданных разрешений</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostIncomeRequest">
        <xs:annotation>
            <xs:documentation>Регистрация дохода партнером</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReceiptId" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id чека (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата формирования</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="OperationTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата расчёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="IncomeType" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Источник/Тип дохода:
                            1) FROM_INDIVIDUAL (Доход от Физического Лица)
                            2) FROM_LEGAL_ENTITY (Доход от Юридического Лица)
                            3) FROM_FOREIGN_AGENCY (Доход от Иностранной Организации)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="CustomerInn" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН покупателя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="CustomerOrganization" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Организация покупателя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Services" type="smz:IncomeService" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Список услуг</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="TotalAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Общая стоимость оказанных услуг</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="IncomeHashCode" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ФП чека (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Link" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Ссылка (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="GeoInfo" type="smz:GeoInfo" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Координаты продажи</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="OperationUniqueId" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Уникальный идентификатор операции</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostIncomeResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostIncomeRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="ReceiptId" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Id чека</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Link" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Ссылка на чек</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostIncomeRequestV2">
        <xs:annotation>
            <xs:documentation>Регистрация дохода партнером с возможностью указания нескольких услуг</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReceiptId" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id чека (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата формирования</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="OperationTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата расчёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="IncomeType" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Источник/Тип дохода:
                            1) FROM_INDIVIDUAL (Доход от Физического Лица)
                            2) FROM_LEGAL_ENTITY (Доход от Юридического Лица)
                            3) FROM_FOREIGN_AGENCY (Доход от Иностранной Организации)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="CustomerInn" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН покупателя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="CustomerOrganization" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Организация покупателя</xs:documentation>
                    </xs:annotation>
                </xs:element>
				<xs:element name="SupplierInn" type="xs:string" minOccurs="0" maxOccurs="1">
				    <xs:annotation>
					    <xs:documentation>ИНН поставщика данных(площадки третьего звена)</xs:documentation>
				    </xs:annotation>
				</xs:element>
                <xs:element name="Services" type="smz:IncomeService" minOccurs="1" maxOccurs="6">
                    <xs:annotation>
                        <xs:documentation>Список услуг</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="TotalAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Общая стоимость оказанных услуг</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="IncomeHashCode" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ФП чека (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Link" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Ссылка (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="GeoInfo" type="smz:GeoInfo" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Координаты продажи</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="OperationUniqueId" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Уникальный идентификатор операции</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostIncomeResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на PostIncomeRequestV2.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="ReceiptId" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Id чека</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Link" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Ссылка на чек</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostIncomeFromIndividualRequest">
        <xs:annotation>
            <xs:documentation>Регистрация дохода от Физического лица партнером</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReceiptId" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id чека (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата формирования</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="OperationTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата расчёта</xs:documentation>
                    </xs:annotation>
                </xs:element>
				<xs:element name="SupplierInn" type="xs:string" minOccurs="0" maxOccurs="1">
					<xs:annotation>
						<xs:documentation>ИНН поставщика данных(площадки третьего звена)</xs:documentation>
					</xs:annotation>
				</xs:element>
                <xs:element name="Services" type="smz:IncomeService" minOccurs="1" maxOccurs="6">
                    <xs:annotation>
                        <xs:documentation>Список услуг</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="TotalAmount" type="xs:decimal" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Общая стоимость оказанных услуг</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="IncomeHashCode" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ФП чека (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Link" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Ссылка (offline режим)</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="GeoInfo" type="smz:GeoInfo" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Координаты продажи</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="OperationUniqueId" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Уникальный идентификатор операции</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostIncomeFromIndividualResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostIncomeFromIndividualRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="ReceiptId" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Id чека</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Link" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Ссылка на чек</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostCancelReceiptRequest">
        <xs:annotation>
            <xs:documentation>Сторнирование чека</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReceiptId" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id чека</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Message" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Причина отзыва чека</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostCancelReceiptResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostCancelReceiptRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestResult" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostCancelReceiptRequestV2">
        <xs:annotation>
            <xs:documentation>Сторнирование чека V2</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReceiptId" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id чека</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ReasonCode" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Код причины аннулирования чека:
                            1) REFUND (Возврат средств)
                            2) REGISTRATION_MISTAKE (Чек сформирован ошибочно)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostCancelReceiptResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на PostCancelReceiptRequestV2.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestResult" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeRequest">
        <xs:annotation>
            <xs:documentation>Получение информации по зарегистрированным доходам</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="From" type="xs:dateTime" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата, начиная с которой отображать зарегистрированные доходы
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="To" type="xs:dateTime" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата, до которой отображать зарегистрированные доходы.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Limit" type="xs:int" default="100" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Максимальное количество зарегистрированных доходов в ответе</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Offset" type="xs:int" default="0" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Отступ от начала списка</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetIncomeRequest</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="HasMore" type="xs:boolean">
                    <xs:annotation>
                        <xs:documentation>Есть ли ещё чеки в списке</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Receipts" type="smz:Receipt" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список полученных чеков</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeRequestV2">
        <xs:annotation>
            <xs:documentation>Получение информации по зарегистрированным доходам с поддержкой нескольких услуг в чеках</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="From" type="xs:dateTime" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата, начиная с которой отображать зарегистрированные доходы
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="To" type="xs:dateTime" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата, до которой отображать зарегистрированные доходы.</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Limit" type="xs:int" default="100" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Максимальное количество зарегистрированных доходов в ответе</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Offset" type="xs:int" default="0" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Отступ от начала списка</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на GetIncomeRequestV2</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="HasMore" type="xs:boolean">
                    <xs:annotation>
                        <xs:documentation>Есть ли ещё чеки в списке</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Receipts" type="smz:ReceiptV2" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список полученных чеков</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeForPeriodRequest">
        <xs:annotation>
            <xs:documentation>Получение информации по доходу НП НПД за период</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="TaxPeriodId" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ID налогового периода (YYYYMM)</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeForPeriodResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetIncomeForPeriodRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="TotalAmount" type="xs:decimal">
                    <xs:annotation>
                        <xs:documentation>Сумма зарегистрированного дохода за период</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="CanceledTotalAmount" type="xs:decimal">
                    <xs:annotation>
                        <xs:documentation>Сумма сторнированного дохода за период</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Tax" type="xs:decimal">
                    <xs:annotation>
                        <xs:documentation>Рассчитанный налог за период</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetTaxpayerRatingRequest">
        <xs:annotation>
            <xs:documentation>Получение рейтинга НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerRatingResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetTaxpayerRatingRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Rating" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Рейтинг</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostRestrictionsRequest">
        <xs:annotation>
            <xs:documentation>Запрос на наложение ограничений на НП НПД при работе в ПП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Type" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Тип ограничений</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Message" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Причина введения</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostRestrictionsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostRestrictionsRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRestrictionsStatusRequest">
        <xs:annotation>
            <xs:documentation>Получение статуса заявки на наложение ограничений на действия конкретного НП НПД в ПП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ID заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRestrictionsStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetRestrictionsStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestResult" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат рассмотрения</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Message" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Примечание</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ProcessingTime" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата рассмотрения заявки Налоговым Органом</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetKeysRequest">
        <xs:annotation>
            <xs:documentation>Получение партнером ключей для работы в режиме Offline</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetKeysResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetKeysRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Keys" type="smz:KeyInfo" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Ключи для работы оффлайн</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetLegalEntityInfoRequest">
        <xs:annotation>
            <xs:documentation>Получение информации о юридическом лице по ИНН</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН ЮЛ (не обязательно если в запросе есть Наименование и ОКТМО )
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Ogrn" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ОГРН ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Наименование ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Oktmo" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ОКТМО региона места нахождения ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetLegalEntityInfoResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetLegalEntityInfoRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ИНН ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Ogrn" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ОГРН ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Name" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Название ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Address" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Адрес регистрации ЮЛ</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="TerminationDate" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата прекращения деятельности</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="InvalidationDate" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата признания регистрации недействительной</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetNewlyUnboundTaxpayersRequest">
        <xs:annotation>
            <xs:documentation>Получение списка вновь отвязанных от партнера НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="From" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата, начиная с которой отображать вновь отвязанных НП НПД</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="To" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата, до которой отображать вновь отвязанных НП НПД</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Limit" type="xs:int" default="100" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Максимальное количество НП НПД на странице</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Offset" type="xs:int" default="0" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Отступ от начала списка</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetNewlyUnboundTaxpayersResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetNewlyUnboundTaxpayersRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Taxpayers" type="smz:NewlyUnboundTaxpayersInfo" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Информация о НП НПД</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="HasMore" type="xs:boolean">
                    <xs:annotation>
                        <xs:documentation>Есть ли ещё НП НПД на следующих страницах</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRegionsListRequest">
        <xs:annotation>
            <xs:documentation>Получение актуального списка регионов, где осуществляется режим НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRegionsListResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetRegionsListRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Regions" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Oktmo" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>ОКТМО региона ведения деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Name" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Название региона ведения деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetActivitiesListRequest">
        <xs:annotation>
            <xs:documentation>Получение актуального списка видов деятельности</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetActivitiesListResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetActivitiesListRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Activities" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Id" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>ID вида деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Name" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Название вида деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetActivitiesListRequestV2">
        <xs:annotation>
            <xs:documentation>Получение актуального двухуровневого списка видов деятельности</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetActivitiesListResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на GetActivitiesListRequestV2.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Activities" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Id" type="xs:int" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>ID вида деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="ParentId" type="xs:int" minOccurs="0" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>ID родительского вида деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>Название вида деятельности</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="IsActive" type="xs:boolean" minOccurs="1" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>Признак активности вида деятельности в системе</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNewActivityRequest">
        <xs:annotation>
            <xs:documentation>Запрос на добавление нового вида деятельности</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Activity" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Вид деятельности</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNewActivityResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostNewActivityRequest</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID вида деятельности</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRejectionReasonsListRequest">
        <xs:annotation>
            <xs:documentation>Получение справочника причин отказа в постановке на учет</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRejectionReasonsListResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetRejectionReasonsListRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Codes" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Code" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Код причины отказа</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Description" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Описание причины отказа</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetUnregistrationReasonsListRequest">
        <xs:annotation>
            <xs:documentation>Получение справочника причин снятия с учета</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetUnregistrationReasonsListResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetUnregistrationReasonsListRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Codes" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Code" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Код причины отказа постановки на учет</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Description" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Описание причины снятия с учёта</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetInnByPersonalInfoRequest">
        <xs:annotation>
            <xs:documentation>Получение ИНН по персональным данным</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="FirstName" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Имя пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="SecondName" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Фамилия пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Patronymic" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Отчество пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Birthday" type="xs:date" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата рождения</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PassportSeries" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Серия паспорта</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PassportNumber" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер паспорта</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetInnByPersonalInfoResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetInnByPersonalInfoRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>ИНН пользрвателя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Status" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Статус ответа</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetInnByPersonalInfoRequestV2">
        <xs:annotation>
            <xs:documentation>Получение ИНН по листу персональных данных</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="PersonalInfoList" type="smz:PersonalInfo" minOccurs="1" maxOccurs="100">
                    <xs:annotation>
                        <xs:documentation>Список персональных данных на получение ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetInnByPersonalInfoResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на GetInnByPersonalInfoRequestV2.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="InnList" type="smz:InnByPersonalInfo" minOccurs="1" maxOccurs="100">
                    <xs:annotation>
                        <xs:documentation>Список ИНН по запрашиваемым персональным данным</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetInnByPersonalInfoRequestV3">
        <xs:annotation>
            <xs:documentation>Получение ИНН по листу персональных данных V3</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="PersonalInfoList" type="smz:PersonalInfoV3" minOccurs="1" maxOccurs="100">
                    <xs:annotation>
                        <xs:documentation>Список персональных данных на получение ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetInnByPersonalInfoResponseV3">
        <xs:annotation>
            <xs:documentation>Ответ на GetInnByPersonalInfoRequestV3.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="InnList" type="smz:InnByPersonalInfo" minOccurs="1" maxOccurs="100">
                    <xs:annotation>
                        <xs:documentation>Список ИНН по запрашиваемым персональным данным</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostPlatformRegistrationRequest">
        <xs:annotation>
            <xs:documentation>Регистрация приложения партнера</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="PartnerName" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Название партнера</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PartnerType" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Тип партнера</xs:documentation>
                    </xs:annotation>
                    <xs:simpleType>
                        <xs:restriction base="xs:string">
                            <xs:enumeration value="BANK"/>
                            <xs:enumeration value="PARTNER"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:element>
                <xs:element name="PartnerDescription" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Описание партнера</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PartnerConnectable" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Может ли НП подключаться сам</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PartnerAvailableForBind" type="xs:boolean" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Доступен ди партнер для запросов на подключение со стороны ПП НПД</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="TransitionLink" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Diplink или ссылка на ресур партнера для перехода и начала привязки</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PartnersText" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Текст партенра для отображения в ЛК НПД и МП МойНалог</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="PartnerImage" type="xs:base64Binary" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Ссылка на картинку с логотипом</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН партнера</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Phone" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Номер телефона для связи</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostPlatformRegistrationResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostPlatformRegistrationRequest</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="PartnerID" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>ID партнера</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RegistrationDate" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>Дата регистрации в ПП Самозанятые</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetRegistrationReferenceRequestV2">
        <xs:annotation>
            <xs:documentation>Получение справки о постановке на учет в качестве НП НПД в новом формате</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestYear" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Год, за который запрашивается справка</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetRegistrationReferenceResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на GetRegistrationReferenceRequestV2</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RegistrationReferencePdf" type="smz:AttachedFile">
                    <xs:annotation>
                        <xs:documentation>PDF файл справки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetIncomeReferenceRequestV2">
        <xs:annotation>
            <xs:documentation>Получение справки о доходах НП НПД в новом формате</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН пользователя</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="RequestYear" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Год, за который запрашивается справка</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetIncomeReferenceResponseV2">
        <xs:annotation>
            <xs:documentation>Ответ на GetIncomeReferenceRequestV2</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="IncomeReferencePdf" type="smz:AttachedFile">
                    <xs:annotation>
                        <xs:documentation>PDF файл справки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetChangeInnHistoryRequest">
        <xs:annotation>
            <xs:documentation>Получение информации о смене ИНН</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Offset" type="xs:long" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Глобальное смещение в журнале смены ИНН начиная с которого будут отдаваться записи</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Limit" type="xs:int" default="100" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Максимальное число записей в ответе</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetChangeInnHistoryResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetChangeInnHistoryRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Items" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Offset" type="xs:long">
                                <xs:annotation>
                                    <xs:documentation>Глобальное смещение в журнале смены ИНН. Записи отсортированы по возрастанию. Могуть быть пробелы между записями</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="PreviousInn" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Предыдущий ИНН у налогоплательщика</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Inn" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>ИНН</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="From" type="xs:dateTime">
                                <xs:annotation>
                                    <xs:documentation>Дата, начиная с которой, применен ИНН</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="To" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                                <xs:annotation>
                                    <xs:documentation>Дата, до которой, применен ИНН</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetGrantedPermissionsStatusRequest">
        <xs:annotation>
            <xs:documentation>Получение статуса заявки на изменение прав НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Id" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetGrantedPermissionsStatusResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetGrantedPermissionsStatusRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="Result" type="xs:string">
                    <xs:annotation>
                        <xs:documentation>Результат запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="ProcessingTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Дата рассмотрения заявки</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetNotificationsRequest">
        <xs:annotation>
            <xs:documentation>Получение списка оповещений для НП НПД</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="notificationsRequest" type="smz:NotificationsRequest" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП по которым запрашиваются оповещения</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetNotificationsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос GetNotificationsRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="notificationsResponse" type="smz:NotificationsResponse" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список оповещений по НП</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsAckRequest">
        <xs:annotation>
            <xs:documentation>Отметка оповещения как прочитанного</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="notificationList" type="smz:NotificationsActionRequest" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП и оповещений, которые были прочитаны</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsAckResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос PostNotificationsAckRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>статус отметки оповещений прочитанными</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsArchRequest">
        <xs:annotation>
            <xs:documentation>Отметка оповещения как архивного</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="notificationList" type="smz:NotificationsActionRequest" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП и оповещений, которые были заархивированны</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsArchResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос PostNotificationsArchRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>статус отметки оповещений архивными</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsAckAllRequest">
        <xs:annotation>
            <xs:documentation>Отметка всех оповещений как прочитанных</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП которые пометили все сообщения как прочитанные</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsAckAllResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос PostNotificationsAckAllRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>статус отметки оповещений прочитанными</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsArchAllRequest">
        <xs:annotation>
            <xs:documentation>Отметка всех оповещений как архивных</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП которые пометили все сообщения как заархивированные</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsArchAllResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос PostNotificationsArchRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>статус отметки оповещений архивными</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetNotificationsCountRequest">
        <xs:annotation>
            <xs:documentation>Получение количеств не прочитанных оповещений</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП по которым необходимо получить оповещения</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetNotificationsCountResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос GetNotificationsCountRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="smz:NotificationsCount" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Кол-во не прочитанных оповещений по НП</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsDeliveredRequest">
        <xs:annotation>
            <xs:documentation>Отметка оповещения как доставленного клиенту</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="notificationList" type="smz:NotificationsActionRequest" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП и оповещений, которые были доставлены</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostNotificationsDeliveredResponse">
        <xs:annotation>
            <xs:documentation>Ответ на запрос PostNotificationsDeliveredRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>статус отметки оповещений доставленных</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetNewPermissionsChangeRequest">
        <xs:annotation>
            <xs:documentation>Получение списка запросов на подтверждение прав</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1000">
                    <xs:annotation>
                        <xs:documentation>Список НП по которым необходимо получить оповещения</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetNewPermissionsChangeResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetNewPermissionsChangeRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Taxpayers" type="smz:ChangePermissoinsInfo" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Информация о запрашиваемых сменах прав</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostDecisionPermissionsChangeRequest">
        <xs:annotation>
            <xs:documentation>Подтверждение/отказ изменения прав</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="requestId" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Id запроса на изменение прав</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН НП по которому происходит смена прав</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Решение по изменению прав</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="PostDecisionPermissionsChangeResponse">
        <xs:annotation>
            <xs:documentation>Ответ на PostDecisionPermissionsChangeRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="status" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>статус</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetPartnersPermissionsRequest">
        <xs:annotation>
            <xs:documentation>Получение списка привязанных партнеров и предоставленных им прав</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Inn" type="xs:string" minOccurs="1" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>ИНН НП</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetPartnersPermissionsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetPartnersPermissionsRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="PartnersPermissionsList" type="smz:PartnersAndPermissions" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список выданных разрешений партнерам</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetAccrualsAndDebtsRequest">
        <xs:annotation>
            <xs:documentation>Получение информации о незакрытых налоговых начислениях</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="InnList" type="xs:string" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetAccrualsAndDebtsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetAccrualsAndDebtsRequest</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="AccrualsAndDebtsList" type="smz:AccrualsAndDebts" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список начислений для каждого НП</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name="GetPaymentDocumentsRequest">
        <xs:annotation>
            <xs:documentation>Получение платежных документов на оплату налоговых начислений, задолженностей и пеней</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="InnList" type="xs:string" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список ИНН</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetPaymentDocumentsResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetPaymentDocumentsRequest</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="PaymentDocumentsList" type="smz:PaymentDocumentList" minOccurs="1" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>Список платежных документов для каждого НП</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetCancelIncomeReasonsListRequest">
        <xs:annotation>
            <xs:documentation>Получение справочника причин аннулирования</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetCancelIncomeReasonsListResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetCancelIncomeReasonsListRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Codes" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Code" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Код причины аннулирования чека</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Description" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Описание причины аннулирования чека</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerUnregistrationReasonsListRequest">
        <xs:annotation>
            <xs:documentation>Получение справочника причин по которым НП может подать заявку на снятие с учета</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="RequestTime" type="xs:dateTime" minOccurs="0" maxOccurs="1">
                    <xs:annotation>
                        <xs:documentation>Время запроса</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="GetTaxpayerUnregistrationReasonsListResponse">
        <xs:annotation>
            <xs:documentation>Ответ на GetTaxpayerUnregistrationReasonsListRequest.</xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="Codes" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="Code" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Код причины снятия с учёта</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="Description" type="xs:string">
                                <xs:annotation>
                                    <xs:documentation>Описание причины снятия с учёта</xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
"""