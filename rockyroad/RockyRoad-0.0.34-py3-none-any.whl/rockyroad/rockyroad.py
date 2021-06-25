from uplink import (
    Consumer,
    get,
    post,
    patch,
    delete,
    returns,
    headers,
    Body,
    json,
    Query,
)
import os

try:
    key = os.environ["OCP_APIM_SUBSCRIPTION_KEY"]
except KeyError as e:
    print(
        f"""ERROR: Define the environment variable {e} with your subscription key.  For example:

    export OCP_APIM_SUBSCRIPTION_KEY="INSERT_YOUR_SUBSCRIPTION_KEY"

    """
    )
    key = None


def build(serviceName, version, base_url, **kw):
    """Returns a resource to interface with the RockyRoad API.

    Usage Examples - Data Services:

        from rockyroad.rockyroad import build

        dataservice = build(serviceName="data-services", version="v1", base_url='INSERT_URL_FOR_API')

        api_response = dataservice.helloWorld().list()

        dataservice.docs().swagger().content
        dataservice.docs().redocs().content
        dataservice.docs().openapi()

        api_response = dataservice.alerts().requests().list()
        api_response = dataservice.alerts().requests().list(creator_email='user@acme.com')
        api_response = dataservice.alerts().requests().insert(new_alert_request_json)
        api_response = dataservice.alerts().requests().delete(brand=brand, alert_request_id=alert_request_id)

        api_response = dataservice.alerts().reports().list()
        api_response = dataservice.alerts().reports().list(creator_email='user@acme.com')

        api_response = dataservice.machines().utilData().list(brand=brand, time_period='today')
        api_response = dataservice.machines().utilData().stats().list()

        api_response = dataservice.dealers().list()
        api_response = dataservice.customers().list(dealer_name=dealer_name)

        api_response = dataservice.accounts().list()
        api_response = dataservice.accounts().list(account="c123")
        api_response = dataservice.accounts().insert(new_account=new_account)
        api_response = dataservice.accounts().update(account=update_account)
        api_response = dataservice.accounts().delete(account="d123")

        api_response = dataservice.accounts().set_is_dealer(account="d123", is_dealer=True)
        api_response = dataservice.accounts().assign_dealer(customer_account="c123", dealer_account="d123", is_default_dealer=True, dealer_internal_account="abc")
        api_response = dataservice.accounts().assign_dealer(customer_account="c123", dealer_account="d123")
        api_response = dataservice.accounts().unassign_dealer(customer_account="c123", dealer_account="d123")

        api_response = dataservice.accounts().contacts().list(account=account)
        api_response = dataservice.accounts().contacts().list(account=account, include_dealer_contacts=True)
        api_response = dataservice.accounts().contacts().list(account_uid=account_uid)
        api_response = dataservice.accounts().contacts().list(account_contact_uid=account_contact_uid)
        api_response = dataservice.accounts().contacts().insert(new_account_contact=new_account_contact)
        api_response = dataservice.accounts().contacts().update(account_contact=account_contact)
        api_response = dataservice.accounts().contacts().delete(account_contact_uid="123e4567-e89b-12d3-a456-426614174000")

        api_response = dataservice.accounts().customers().list()
        api_response = dataservice.accounts().customers().list(dealer_account="D123")
        api_response = dataservice.accounts().customers().list(account_association_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.accounts().customers().dealer_provided_information().list(dealer_account=dealer_account, customer_account=customer_account)
        api_response = dataservice.accounts().customers().dealer_provided_information().update(dealer_provided_information=dealer_provided_information)

        api_response = dataservice.accounts().dealers().list()
        api_response = dataservice.accounts().dealers().list(customer_account="A123")

        api_response = dataservice.apbs().list()
        api_response = dataservice.apbs().list(apb_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.apbs().list(brand="brand", model="model", serial="1234")
        api_response = dataservice.apbs().insert(new_apb=new_apb)
        api_response = dataservice.apbs().delete(apb_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.apbs().update(apb=updated_apb)

        api_response = dataservice.apbs().status().list(apb_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.apbs().status().insert(new_apb_status=new_apb_status)
        api_response = dataservice.apbs().status().delete(apb_status_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.apbs().status().update(apb_status=updated_apb_status)

        api_response = dataservice.apbs().requests().list(uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.apbs().requests().insert(new_apb_request=new_apb_request)
        api_response = dataservice.apbs().requests().delete(uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.apbs().requests().update(apb_request=updated_apb_request)

        api_response = dataservice.machines().catalog().list()
        api_response = dataservice.machines().catalog().list(machine_catalog_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.machines().catalog().insert(new_machine_catalog=new_machine_catalog)
        api_response = dataservice.machines().catalog().delete(machine_catalog_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.machines().catalog().update(machine_catalog=machine_catalog)

        api_response = dataservice.machines().list()
        api_response = dataservice.machines().list(account="a123")
        api_response = dataservice.machines().list(account_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.machines().list(account="a123", dealer_account="d123")
        api_response = dataservice.machines().list(account_uid="123e4567-e89b-12d3-a456-426614174000", dealer_account_uid="07cc67f4-45d6-494b-adac-09b5cbc7e2b5")
        api_response = dataservice.machines().list(brand="brand", model="model", serial="1234")
        api_response = dataservice.machines().insert(new_machine=new_machine)
        api_response = dataservice.machines().delete(machine_uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.machines().update(machine=updated_machine)
        api_response = dataservice.machines().assign_machines_to_default_dealer(customer_account="c123", ignore_machines_with_dealer=True)

        api_response = dataservice.parts().list()
        api_response = dataservice.parts().list(uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.parts().list(partName="abc")
        api_response = dataservice.parts().list(partNumber="acme-01")
        api_response = dataservice.parts().list(isKit=True)
        api_response = dataservice.parts().list(isKitPart=True)
        api_response = dataservice.parts().list(isKit=True, isKitPart=False)
        api_response = dataservice.parts().insert(part=part)
        api_response = dataservice.parts().update(part=part)
        api_response = dataservice.parts().delete(uid="123e4567-e89b-12d3-a456-426614174000")

        api_response = dataservice.parts().kits().list(uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.parts().kits().list(uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.parts().kits().list(kitPartNumber="acme-01")
        api_response = dataservice.parts().kits().list(partNumber="acme-01")
        api_response = dataservice.parts().kits().insert(kit=kit)
        api_response = dataservice.parts().kits().update(kit=kit)
        api_response = dataservice.parts().kits().delete(uid="123e4567-e89b-12d3-a456-426614174000")

        api_response = dataservice.services().maintenanceIntervals().list()
        api_response = dataservice.services().maintenanceIntervals().list(uid="123e4567-e89b-12d3-a456-426614174000")
        api_response = dataservice.services().maintenanceIntervals().list(hours=250, brand=brand, model=model)
        api_response = dataservice.services().maintenanceIntervals().insert(maintenanceInterval=maintenanceInterval)
        api_response = dataservice.services().maintenanceIntervals().update(maintenanceInterval=maintenanceInterval)
        api_response = dataservice.services().maintenanceIntervals().delete(uid="123e4567-e89b-12d3-a456-426614174000")


    Usage Examples - Email Services:

        from rockyroad.rockyroad import build

        emailservice = build(serviceName="email-services", version="v1", base_url='INSERT_URL_FOR_API')

        email_message = {
            "recipient": "someone@acme.com",
            "subject": "Sending Email Message via API",
            "html_message": "This email send via the API!",
            "text_message": "This email send via the API!",
            }

        api_response = emailservice.emails().send(email_message_json)


    """
    try:
        service = {
            "data-services": DataServicesResource,
            "email-services": EmailServicesResource,
        }[serviceName]
        return service(
            serviceName=serviceName,
            version=version,
            base_url=base_url,
            test=kw.get("test", False),
        )
    except KeyError:
        print(
            f"ERROR:  The service name '{serviceName}' was not found or is not supported."
        )


class DataServicesResource(object):
    """Inteface to Data Services resources for the RockyRoad API."""

    def __init__(self, *args, **kw):
        base_url = kw["base_url"]
        serviceName = kw["serviceName"]
        version = kw["version"]
        test = kw["test"]
        if test:
            api_base_url = base_url + "/"
        else:
            api_base_url = base_url + "/" + serviceName + "/" + version + "/"
        self._base_url = api_base_url

    def helloWorld(self):
        return self.__HelloWorld(self)

    def docs(self):
        return self.__Docs(self)

    def alerts(self):
        return self.__Alerts(self)

    def machines(self):
        return self.__Machines(self)

    def dealers(self):
        return self.__Dealers(self)

    def customers(self):
        return self.__Customers(self)

    def accounts(self):
        return self.__Accounts(self)

    def apbs(self):
        return self.__Apbs(self)

    def parts(self):
        return self.__Parts(self)

    def services(self):
        return self.__Services(self)

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __HelloWorld(Consumer):
        def __init__(self, Resource, *args, **kw):
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @returns.json
        @get("")
        def list(self):
            """This call will return Hello World."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Docs(Consumer):
        def __init__(self, Resource, *args, **kw):
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @get("docs/swagger")
        def swagger(self):
            """This call will return swagger ui."""

        @get("docs/redocs")
        def redocs(self):
            """This call will return redoc ui."""

        @returns.json
        @get("docs/openapi.json")
        def openapi(self):
            """This call will return OpenAPI json."""

    class __Alerts(object):
        """Inteface to alerts resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url

        def requests(self):
            return self.__Requests(self)

        def reports(self):
            return self.__Reports(self)

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Requests(Consumer):
            """Inteface to alert requests resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("alerts/requests")
            def list(self, creator_email: Query = None):
                """This call will return detailed alert request information for the creator's email specified or all alert requests if no email is specified."""

            @returns.json
            @json
            @post("alerts/requests")
            def insert(self, new_alert_request: Body):
                """This call will create an alert request with the specified parameters."""

            @returns.json
            @delete("alerts/requests")
            def delete(self, brand: Query(type=str), alert_request_id: Query(type=int)):
                """This call will delete the alert request for the specified brand and alert request id."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Reports(Consumer):
            """Inteface to alert reports resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("alerts/reports")
            def list(self, creator_email: Query = None):
                """This call will return detailed alert report information for the creator's email specified or all alert reports if no email is specified."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Machines(Consumer):
        """Inteface to machines resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def utilData(self):
            return self.__UtilData(self)

        def catalog(self):
            return self.__Catalog(self)

        @returns.json
        @get("machines")
        def list(
            self,
            machine_uid: Query(type=str) = None,
            brand: Query(type=str) = None,
            model: Query(type=str) = None,
            serial: Query(type=str) = None,
            account: Query(type=str) = None,
            account_uid: Query(type=str) = None,
            dealer_account: Query(type=str) = None,
            dealer_account_uid: Query(type=str) = None,
        ):
            """This call will return machine information for the machine or account specified or all machines if nothing is specified."""

        @returns.json
        @json
        @post("machines")
        def insert(self, new_machine: Body):
            """This call will create a machine with the specified parameters."""

        @returns.json
        @delete("machines")
        def delete(self, machine_uid: Query(type=str)):
            """This call will delete the machine for the specified id."""

        @returns.json
        @json
        @patch("machines")
        def update(self, machine: Body):
            """This call will update the machine with the specified parameters."""

        @returns.json
        @json
        @post("machines/assign-to-default-dealer")
        def assign_machines_to_default_dealer(
            self,
            customer_account: Query(type=str),
            ignore_machines_with_dealer: Query(type=bool) = None,
        ):
            """This call will set the supporting dealer for machines owned by the customer to the default dealer for the customer."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Catalog(Consumer):
            """Inteface to Machine Catalog resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("machines/catalog")
            def list(self, machine_catalog_uid: Query(type=str) = None):
                """This call will return detailed machine catalog information for the id specified or all machine catalog information if uid is specified."""

            @returns.json
            @json
            @post("machines/catalog")
            def insert(self, new_machine_catalog: Body):
                """This call will create a Machine Catalog entry with the specified parameters."""

            @returns.json
            @delete("machines/catalog")
            def delete(self, machine_catalog_uid: Query(type=str)):
                """This call will delete the Machine Catalog entry for the specified Machine Catalog uid."""

            @returns.json
            @json
            @patch("machines/catalog")
            def update(self, machine_catalog: Body):
                """This call will update the Machine Catalog with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __UtilData(Consumer):
            """Inteface to machine utildata resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)
                self._base_url = Resource._base_url

            def stats(self):
                return self.__Stats(self)

            @returns.json
            @get("machines/util-data")
            def list(self, brand: Query(type=str), time_period: Query(type=str)):
                """This call will return utilization data for the time period specified in the query parameter."""

            @headers({"Ocp-Apim-Subscription-Key": key})
            class __Stats(Consumer):
                """Inteface to utildata stats resource for the RockyRoad API."""

                def __init__(self, Resource, *args, **kw):
                    super().__init__(base_url=Resource._base_url, *args, **kw)

                @returns.json
                @get("machines/util-data/stats")
                def list(self):
                    """This call will return stats for the utildatastatus table."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Dealers(Consumer):
        def __init__(self, Resource, *args, **kw):
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @returns.json
        @get("dealers")
        def list(self):
            """This call will return a list of dealers."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Customers(Consumer):
        def __init__(self, Resource, *args, **kw):
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @returns.json
        @get("customers")
        def list(self, dealer_name: Query(type=str)):
            """This call will return a list of customers and machines supported by the specified dealer."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Accounts(Consumer):
        """Inteface to accounts resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def dealers(self):
            return self.__Dealers(self)

        def customers(self):
            return self.__Customers(self)

        def contacts(self):
            return self.__Contacts(self)

        @returns.json
        @get("accounts")
        def list(self, account: Query = None, account_uid: Query = None):
            """This call will return detailed account information for account specified or all accounts if none is specified."""

        @returns.json
        @delete("accounts")
        def delete(self, account: Query = None, account_uid: Query = None):
            """This call will delete the account for the specified brand and alert request id."""

        @returns.json
        @json
        @post("accounts")
        def insert(self, new_account: Body):
            """This call will create an account with the specified parameters."""

        @returns.json
        @json
        @patch("accounts")
        def update(self, account: Body):
            """This call will update an account with the specified parameters."""

        @returns.json
        @json
        @post("accounts/assign-dealer")
        def assign_dealer(
            self,
            customer_account: Query(type=str),
            dealer_account: Query(type=str),
            is_default_dealer: Query(type=bool) = None,
            dealer_internal_account: Query(type=str) = None,
        ):
            """This call will assign the dealer for the customer with the specified parameters."""

        @returns.json
        @json
        @post("accounts/unassign-dealer")
        def unassign_dealer(
            self, customer_account: Query(type=str), dealer_account: Query(type=str)
        ):
            """This call will unassign the dealer for the customer."""

        @returns.json
        @json
        @post("accounts/set-is-dealer")
        def set_is_dealer(self, account: Query(type=str), is_dealer: Query(type=bool)):
            """This call will set the account as a dealer account."""

        @returns.json
        @json
        @post("accounts/set-default-dealer")
        def set_default_dealer(
            self, customer_account: Query(type=str), dealer_account: Query(type=str)
        ):
            """This call will set the account as a dealer account."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Contacts(Consumer):
            """Inteface to account contacts resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                self._base_url = Resource._base_url
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("accounts/contacts")
            def list(
                self,
                account: Query = None,
                account_uid: Query = None,
                account_contact_uid: Query = None,
                include_dealer_contacts: Query = False,
            ):
                """This call will return detailed contact information for the account specified."""

            @returns.json
            @delete("accounts/contacts")
            def delete(self, account_contact_uid: Query = None):
                """This call will delete the specified account contact."""

            @returns.json
            @json
            @post("accounts/contacts")
            def insert(self, new_account_contact: Body):
                """This call will create an account contact with the specified parameters."""

            @returns.json
            @json
            @patch("accounts/contacts")
            def update(self, account_contact: Body):
                """This call will update an account contact with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Customers(Consumer):
            """Inteface to customers resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                self._base_url = Resource._base_url
                super().__init__(base_url=Resource._base_url, *args, **kw)

            def dealer_provided_information(self):
                return self.__DealerProvidedInformation(self)

            @returns.json
            @get("accounts/customers")
            def list(
                self,
                dealer_account: Query(type=str) = None,
                account_association_uid: Query(type=str) = None,
            ):
                """This call will return detailed customer information for all accounts or for the dealer or account association specified."""

            @headers({"Ocp-Apim-Subscription-Key": key})
            class __DealerProvidedInformation(Consumer):
                """Inteface to dealer-provided information resource for the RockyRoad API."""

                def __init__(self, Resource, *args, **kw):
                    super().__init__(base_url=Resource._base_url, *args, **kw)

                @returns.json
                @get("accounts/customers/dealer-provided-information")
                def list(
                    self,
                    dealer_account: Query = None,
                    dealer_account_uid: Query = None,
                    customer_account: Query = None,
                    customer_account_uid: Query = None,
                ):
                    """This call will return dealer-provided information for the account specified."""

                @returns.json
                @json
                @patch("accounts/customers/dealer-provided-information")
                def update(self, dealer_provided_information: Body):
                    """This call will update dealer-provided information with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Dealers(Consumer):
            """Inteface to dealers resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("accounts/dealers")
            def list(self, customer_account: Query(type=str) = None):
                """This call will return detailed alert request information for the creator's email specified or all alert requests if no email is specified."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Apbs(Consumer):
        """Inteface to APBs resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def status(self):
            return self.__Status(self)

        def requests(self):
            return self.__Requests(self)

        @returns.json
        @get("apbs")
        def list(
            self,
            apb_uid: Query(type=int) = None,
            account: Query(type=str) = None,
            list_apbs_for_dealer_supported_accounts: Query(type=bool) = None,
            list_apbs_for_dealer_supported_machines: Query(type=bool) = None,
            brand: Query(type=str) = None,
            model: Query(type=str) = None,
            serial: Query(type=str) = None,
        ):
            """This call will return detailed APB information for the apb or machine specified or all APBs if nothing is specified."""

        @returns.json
        @json
        @post("apbs")
        def insert(self, new_apb: Body):
            """This call will create an APB with the specified parameters."""

        @returns.json
        @delete("apbs")
        def delete(self, apb_uid: Query(type=str)):
            """This call will delete the APB for the specified APB uid."""

        @returns.json
        @json
        @patch("apbs")
        def update(self, apb: Body):
            """This call will update the APB with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Status(Consumer):
            """Inteface to APB Status resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("apbs/status")
            def list(self, apb_uid: Query(type=str) = None):
                """This call will return detailed APB status information for the specified APB uid."""

            @returns.json
            @delete("apbs/status")
            def delete(self, apb_status_uid: Query(type=str)):
                """This call will delete the APB Status for the specified APB uid and APB Status uid."""

            @returns.json
            @json
            @post("apbs/status")
            def insert(self, new_apb_status: Body):
                """This call will create an alert request with the specified parameters."""

            @returns.json
            @json
            @patch("apbs/status")
            def update(self, apb_status: Body):
                """This call will update the APB status with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Requests(Consumer):
            """Inteface to APB Request resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("apbs/requests")
            def list(self, uid: Query(type=str) = None):
                """This call will return detailed information for APB requests for the specified APB Request uid."""

            @returns.json
            @delete("apbs/requests")
            def delete(self, uid: Query(type=str)):
                """This call will delete the APB Request for the specified APB Request uid."""

            @returns.json
            @json
            @post("apbs/requests")
            def insert(self, new_apb_request: Body):
                """This call will create an APB request with the specified parameters."""

            @returns.json
            @json
            @patch("apbs/requests")
            def update(self, apb_request: Body):
                """This call will update the APB Request with the specified parameters."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Parts(Consumer):
        """Inteface to Parts resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def kits(self):
            return self.__Kits(self)

        @returns.json
        @get("parts")
        def list(
            self,
            uid: Query(type=int) = None,
            partNumber: Query(type=str) = None,
            partName: Query(type=str) = None,
            isKit: Query(type=bool) = None,
            isKitPart: Query(type=bool) = None,
        ):
            """This call will return detailed part information for the part(s) specified or all parts if nothing is specified."""

        @returns.json
        @json
        @post("parts")
        def insert(self, part: Body):
            """This call will create a part with the specified parameters."""

        @returns.json
        @delete("parts")
        def delete(self, uid: Query(type=str)):
            """This call will delete the part for the specified uid."""

        @returns.json
        @json
        @patch("parts")
        def update(self, part: Body):
            """This call will update the part with the specified parameters."""

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Kits(Consumer):
            """Inteface to Kits resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("parts/kits")
            def list(
                self,
                uid: Query(type=str) = None,
                kitPartNumber: Query(type=str) = None,
                partNumber: Query(type=str) = None,
            ):
                """This call will return detailed kit line item information for the specified uid, kitPartNumber, or partNumber."""

            @returns.json
            @delete("parts/kits")
            def delete(self, uid: Query(type=str)):
                """This call will delete the kit line item for the specified uid."""

            @returns.json
            @json
            @post("parts/kits")
            def insert(self, kit: Body):
                """This call will create a kit line item with the specified parameters."""

            @returns.json
            @json
            @patch("parts/kits")
            def update(self, kit: Body):
                """This call will update the kit line item with the specified parameters."""

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Services(Consumer):
        """Inteface to Services resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            self._base_url = Resource._base_url
            super().__init__(base_url=Resource._base_url, *args, **kw)

        def maintenanceIntervals(self):
            return self.__Maintenance_Intervals(self)

        @headers({"Ocp-Apim-Subscription-Key": key})
        class __Maintenance_Intervals(Consumer):
            """Inteface to Maintenance Intervals resource for the RockyRoad API."""

            def __init__(self, Resource, *args, **kw):
                super().__init__(base_url=Resource._base_url, *args, **kw)

            @returns.json
            @get("services/maintenance-intervals")
            def list(
                self,
                uid: Query(type=str) = None,
                hours: Query(type=int) = None,
                brand: Query(type=str) = None,
                model: Query(type=str) = None,
            ):
                """This call will return detailed information for all maintenance intervals or for those for the specified uid, hours, or brand and model."""

            @returns.json
            @delete("services/maintenance-intervals")
            def delete(self, uid: Query(type=str)):
                """This call will delete the maintenance interval for the specified uid."""

            @returns.json
            @json
            @post("services/maintenance-intervals")
            def insert(self, maintenanceInterval: Body):
                """This call will create a maintenance interval with the specified parameters."""

            @returns.json
            @json
            @patch("services/maintenance-intervals")
            def update(self, maintenanceInterval: Body):
                """This call will update the maintenance interval with the specified parameters."""


class EmailServicesResource(object):
    """Inteface to Data Services resources for the RockyRoad API."""

    def __init__(self, *args, **kw):
        base_url = kw["base_url"]
        serviceName = kw["serviceName"]
        version = kw["version"]
        test = kw["test"]
        if test:
            api_base_url = base_url + "/"
        else:
            api_base_url = base_url + "/" + serviceName + "/" + version + "/"
        self._base_url = api_base_url

    def emails(self):
        return self.__Emails(self)

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Emails(Consumer):
        def __init__(self, Resource, *args, **kw):
            super().__init__(base_url=Resource._base_url, *args, **kw)

        @returns.json
        @json
        @post("manual/paths/invoke")
        def send(self, email_message: Body):
            """This call will send an email message with the specified recipient, subject, and html/text body."""
