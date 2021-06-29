import zcrmsdk.src.com.zoho.crm.api.dc as DC
import zcrmsdk.src.com.zoho.crm.api.user as User
import zcrmsdk.src.com.zoho.api.authenticator.oauth_token as OAuthToken
import zcrmsdk.src.com.zoho.crm.api.initializer as Init
import zcrmsdk.src.com.zoho.crm.api.record as Record
import zcrmsdk.src.com.zoho.api.authenticator.store.db_store as DBStore
import zcrmsdk.src.com.zoho.api.authenticator.store.file_store as FileStore
import zcrmsdk.src.com.zoho.crm.api.contact_roles as CR

class Call():
    @staticmethod
    def test():
        environment = DC.USDataCenter.SANDBOX()
        user = User.UserSignature('raja.k@zohocorp.com')
        # store = DBStore.DBStore(None, None, None, "raja@7453", None)
        store = FileStore.FileStore("/Users/aswin-7455/Desktop/python-tokens.txt")
        token = OAuthToken.OAuthToken("1000.1RGSB1XEI2FVG0TYVWPZ864L7KI3DH",
                                      "550045e5e5a4722aa39326e3af819c84683f94cb2a",
                                      "https://www.zoho.com",
                                      "1000.b632a2d7439abfd8b50147886b8a2f41.6547e4cba91550e5006de16da7fc2401",
                                      OAuthToken.TokenType.refresh)

        Init.Initializer.initialize(user, environment, token, store, None)

        CR.ContactRolesOperations().get_contact_roles()

Call.test()
