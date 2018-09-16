
class GraphQLSocialAuthError(Exception):
    """Raise GraphQL Social Exception"""


class InvalidTokenError(GraphQLSocialAuthError):
    """Raise Invalid Token Exception"""


class DoAuthError(GraphQLSocialAuthError):

    def __init__(self, message, result):
        super().__init__(message)
        self.result = result
