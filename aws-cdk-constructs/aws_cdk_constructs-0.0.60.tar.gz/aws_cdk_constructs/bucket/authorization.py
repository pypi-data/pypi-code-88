from cloudcomponents.cdk_cloudfront_authorization import (
    Authorization,
    Mode,
    AuthFlow,
    RetrieveUserPoolClientSecret
)
from aws_cdk import (
    aws_cognito as _cognito,
)

class SpaAuthorization(Authorization):
    @property
    def mode(self):
        return Mode.SPA

    def _create_user_pool_client(self):
        """Returns the S3 bucket

        Returns:
            aws_s3.Bucket: the S3 bucket
        """
        return self.user_pool.add_client('UserPoolClient',
            user_pool_client_name = self.app_name + "-" + self.environment,
            generate_secret = False,
            o_auth = _cognito.OAuthSettings(
                flows =_cognito.OAuthFlows(authorization_code_grant=True),
                scopes = self.oauth_scopes
            ),
            supported_identity_providers= self.identity_providers,
            prevent_user_existence_errors= True,
        )

    def _create_auth_flow(self, log_level):
        """
        """
        return AuthFlow(self, 'AuthFlow',
            log_level=log_level,
            http_headers= self.http_headers,
            user_pool= self.user_pool,
            user_pool_client= self.user_pool_client,
            oauth_scopes= self.oauth_scopes,
            redirect_paths= self.redirect_paths,
            nonce_sgning_secret= self.nonce_sgning_secret,
            cognito_auth_domain= self.cognito_auth_domain,
            cookie_settings= self.cookie_settings if self.cookie_settings else dict(
                id_token= 'Path=/; Secure; HttpOnly; SameSite=Lax',
                access_token= 'Path=/; Secure; HttpOnly; SameSite=Lax',
                refresh_token= 'Path=/; Secure; HttpOnly; SameSite=Lax',
                nonce= 'Path=/; Secure; HttpOnly; SameSite=Lax',
            ),
        )

    def __init__(self, scope: Authorization, id: str, app_name, environment, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        self.app_name = app_name 
        self.environment = environment



# thorization extends IAuthorization {
#   readonly mode: Mode.SPA;
# }

# export type SpaAuthorizationProps = AuthorizationProps;

# export class SpaAuthorization extends Authorization implements ISpaAuthorization {
#   public readonly mode = Mode.SPA;

#   constructor(scope: Construct, id: string, props: SpaAuthorizationProps) {
#     super(scope, id, props);
#   }

#   protected createUserPoolClient(): IUserPoolClient {
#     return this.userPool.addClient('UserPoolClient', {
#       generateSecret: false,
#       oAuth: {
#         flows: {
#           authorizationCodeGrant: true,
#         },
#         scopes: this.oauthScopes,
#       },
#       supportedIdentityProviders: this.identityProviders,
#       preventUserExistenceErrors: true,
#     });
#   }

#   protected createAuthFlow(logLevel: LogLevel): AuthFlow {
#     return new AuthFlow(this, 'AuthFlow', {
#       logLevel,
#       httpHeaders: this.httpHeaders,
#       userPool: this.userPool,
#       userPoolClient: this.userPoolClient,
#       oauthScopes: this.oauthScopes,
#       redirectPaths: this.redirectPaths,
#       nonceSigningSecret: this.nonceSigningSecret,
#       cognitoAuthDomain: this.cognitoAuthDomain,
#       cookieSettings: this.cookieSettings ?? {
#         idToken: 'Path=/; Secure; SameSite=Lax',
#         accessToken: 'Path=/; Secure; SameSite=Lax',
#         refreshToken: 'Path=/; Secure; SameSite=Lax',
#         nonce: 'Path=/; Secure; HttpOnly; SameSite=Lax',
#       },
#     });
#   }
# }