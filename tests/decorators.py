from unittest.mock import patch


def social_auth_mock(f):
    @patch('social_core.backends.base.BaseAuth.get_json')
    @patch('social_core.backends.google.BaseGoogleAuth.get_user_id')
    def wrapper(self, get_user_id_mock, *args):
        get_user_id_mock.return_value = 'test'
        return f(self, get_user_id_mock, *args)
    return wrapper
