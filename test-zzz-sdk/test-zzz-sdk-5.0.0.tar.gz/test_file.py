import zcrmsdk.src.com.zoho.crm.api.dc as DC
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api import UserSignature
import zcrmsdk.src.com.zoho.api.authenticator.oauth_token as OAuthToken
import zcrmsdk.src.com.zoho.crm.api.initializer as Init
import zcrmsdk.src.com.zoho.crm.api.record as Record
from zcrmsdk.src.com.zoho.crm.api.util import StreamWrapper, ModuleFieldsHandler
import zcrmsdk.src.com.zoho.crm.api.attachments as Attachments
import zcrmsdk.src.com.zoho.crm.api.users as Users
import zcrmsdk.src.com.zoho.crm.api.layouts as Layout
import zcrmsdk.src.com.zoho.crm.api.currencies as Currency
from zcrmsdk.src.com.zoho.crm.api.bulk_write import *
from zcrmsdk.src.com.zoho.crm.api import HeaderMap
import zcrmsdk.src.com.zoho.crm.api.related_records as RelatedRecord
import zcrmsdk.src.com.zoho.api.authenticator.store.db_store as DBStore
import zcrmsdk.src.com.zoho.api.authenticator.store.file_store as FileStore
import zcrmsdk.src.com.zoho.crm.api.contact_roles as CR
import zcrmsdk.src.com.zoho.crm.api.attachments as Att
import zcrmsdk.src.com.zoho.crm.api.file as File
from zcrmsdk.src.com.zoho.crm.api.util.constants import Constants
from zcrmsdk.src.com.zoho.crm.api.util import Choice
from zcrmsdk.src.com.zoho.crm.api.request_proxy import RequestProxy
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
import importlib
from datetime import date, datetime


class Call(object):
    @staticmethod
    def test():
        my_logger = Logger.get_instance(Logger.Levels.INFO, '/Users/aswin-7455/Documents/SDK-workspace/latest-git-csez/python/latest/zohocrm-python-sdk/' + str(datetime.now().date()) + '.log')
        environment = DC.USDataCenter.PRODUCTION()
        user = UserSignature(email='aswinkumar.m@zohocorp.com')
        # store = DBStore.DBStore(password="root@123")

        store = FileStore.FileStore("/Users/aswin-7455/Documents/SDK-workspace/latest-git-csez/python/latest/zohocrm-python-sdk/tokens_path.txt")

        # store = FileStore.FileStore("/Users/aswin-7455/Documents/SDK-workspace/latest-git-csez/python/latest/zohocrm-python-sdk/tokens_path.txt")
        # all_tokens = store.get_tokens()

        # store.delete_tokens()

        token = OAuthToken.OAuthToken("1000.FHTTK269B45O83233AA8D3G2YZ9FDH",
                                      "f264324b0f40259a5d7e27ca923e38bb7026cbda7f",
                                      "1000.2e149cb5c8c0c53c2e2b406a05abf594.3a65e27fc6a0bd6854022429963170a8",
                                      OAuthToken.TokenType.REFRESH)
        config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        resource_path = '/Users/aswin-7455/Documents/SDK-workspace/latest-git-csez/python/latest/zohocrm-python-sdk/zcrmsdk'

        sdk_logger = Logger.get_instance(level=Logger.Levels.INFO, file_path="/Users/user_name/Documents/python_sdk_log.log")

        Init.Initializer.initialize(user, environment, token, store, config, resource_path, my_logger)

        # file1 = StreamWrapper(file_path="/Users/aswin-7455/Documents/SDK-workspace/Sample-package/nodejs/zohocrm-nodejs-sdk-sample-application/downloads/Test.jpg")
        #
        # file2 = StreamWrapper(file_path="/Users/aswin-7455/Documents/SDK-workspace/Sample-package/nodejs/zohocrm-nodejs-sdk-sample-application/downloads/wod.png")

        # files_body_1 = File.FileBodyWrapper()
        #
        # files_body_1.set_file(file1)
        #
        # files_body_2 = File.FileBodyWrapper()
        #
        # files_body_2.set_file(file2)
        #
        # files_request = File.BodyWrapper()
        #
        # files_request.set_file([file1, file2])
        #
        # response =File.FileOperations().upload_file(files_request, None)
        #

        response = Record.RecordOperations().get_records("leads_x_contacts")

        print(response)

        # ModuleFieldsHandler.refresh_all_modules()

        # Init.Initializer.switch_user(user, environment, token, False)

        # CR.ContactRolesOperations().get_contact_roles()

        # response = Record.RecordOperations().get_photo("Contacts", 3409643000002034003)

        # file_path = "/Users/aswin-7455/Documents/Bulk-Write/test.zip"
        #
        # org_id = '673899828'
        #
        # # Get instance of HeaderMap Class
        # header_instance = HeaderMap()
        #
        # # Possible parameters for upload_file operation
        # header_instance.add(UploadFileHeader.feature, "bulk-write")
        #
        # header_instance.add(UploadFileHeader.x_crm_org, org_id)
        #
        # st = StreamWrapper(file_path=file_path)
        #
        # fbw = FileBodyWrapper()
        #
        # fbw.set_file(st)

        # response  = BulkWriteOperations().upload_file(fbw, header_instance)

        # response = RelatedRecord.RelatedRecordsOperations('Leads', '3409643000002267003', 'Attachments').get_related_record(None, '3409643000002653001')

        # response = Attachments.AttachmentsOperations('3409643000002267003', 'Leads').download_attachment('3409643000002654001')

        # record_instance = Record.Record()
        #
        # record_instance.add_field_value(Record.Field.Events.event_title(), "124")
        # record_instance.add_field_value(Record.Field.Events.start_datetime(), "124")
        # record_instance.add_key_value("Currency", Choice("INR"))

        # record_instance.add_field_value(Record.Field.Events.who_id(), Record.Record())

        # record_instance.add_field_value(Record.Field.Events.what_id(), "!23")

        # record_body = Record.BodyWrapper()
        #
        # record_body.set_data([record_instance])

        # response = Record.RecordOperations().get_records(None, None, 'events')

        # response = Record.RecordOperations().create_records(record_body, 'events')

        # response = Layout.LayoutsOperations('Leads').get_layout()

        #
        # req = Record.Record()
        #
        # req.add_field_value(Record.Field.Deals.closing_date(), date(2020,10,1))
        #
        # req.set_created_time(datetime.fromisoformat('2020-01-01T12:12:12+05:30'))
        #
        # records_list = []
        #
        # records_list.append(req)
        #
        # reqs.set_data(records_list)
        #
        # response = Record.RecordOperations().create_records(reqs, 'Deals')

        # print(response)

        # wrapper = response.get_object().get_file()
        #
        # import os
        #
        # with open(os.path.join('/Users/aswin-7455/Desktop', wrapper.get_name()), 'wb') as f:
        #     for chunk in wrapper.get_stream():
        #         f.write(chunk)
        #
        # f.close()

        # response = RelatedRecord.RelatedRecordsOperations('Accounts', '3409643000002282001', 'Test').get_related_records(None, None)

        # resp = Att.AttachmentsOperations('3477061000004996185', 'Leads').get_attachments()
        #
        # if isinstance(resp.get_object(), Att.ResponseWrapper):
        #     print(resp.get_object())
        # else:
        #     print('Exception')

        # data = []
        #
        # rec = Record.Record()
        #
        # rec.add_key_value('Last_Name', "Date test")
        #
        # parti = Record.Participants()
        #
        # parti.set_id('1234')
        #
        # parti.set_invited(True)
        #
        # rec.add_field_value(Record.Field.Events.participants(), [parti])
        #
        # contact = Record.Record()
        #
        # x = "123"
        #
        # isinstance(x, str)
        #
        # Record.Field.Leads.email()
        #
        # contact.add_key_value("id", "3477061000005800004")
        #
        # rec.add_key_value("Who_Id", contact)
        #
        # data.append(rec)
        #
        # body = Record.BodyWrapper()
        #
        # body.set_data(data)
        #
        # response = Record.RecordOperations().create_records(body, 'Events')
        #
        # #
        # # # response = Record.RecordOperations().get_record(None, 'Leads', '3477061000004996185')
        # #
        # if isinstance(response.get_object(), Record.ActionWrapper):
        #     print(response.get_object())
        # else:
        #     print('Exception')

        # l = []
        #
        # for i in range(0,5):
        #     five_instance = Five('val' + str(i))
        #     l.append(five_instance)
        #
        # print(map(lambda x: x.get_actual_value(), l))
        #
        # test = map(lambda x: Call.populate_values(x, 'string'), l)
        #
        # print(Call.me)

    @staticmethod
    def build_name(member_name):
        name_split = str(member_name).split('_')
        sdk_name = name_split[0].lower()

        if len(name_split) > 1:
            for i in range(1, len(name_split)):
                if len(name_split[i]) > 0:
                    sdk_name += '_' + name_split[i].lower()

        return sdk_name


Call.test()
