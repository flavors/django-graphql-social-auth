import sys
from unittest.mock import patch


def social_auth_mock(f):
    @patch('social_core.backends.base.BaseAuth.get_json')
    @patch('social_core.backends.google.BaseGoogleAuth.get_user_id')
    @patch('graphql_social.decorators.login')
    def wrapper(self, login_mock, get_user_id_mock, *args):
        get_user_id_mock.return_value = 'test'
        return f(self, login_mock, get_user_id_mock, *args)
    return wrapper


class SocialAuthTestsMixin(object):

    @social_auth_mock
    def test_social_auth(self, login_mock, *args):
        response = self.execute({
            'provider': 'google-oauth2',
            'accessToken': '-token-',
        })

        social = response.data['socialAuth']['social']

        login_mock.assert_called_once()
        self.assertEqual('test', social['uid'])


class SocialAuthJWTTestsMixin(object):
    @social_auth_mock
    @patch.dict(sys.modules, {'graphql_jwt.shortcuts': None})
    def test_social_auth_import_error(self, login_mock, *args):
        response = self.execute({
            'provider': 'google-oauth2',
            'accessToken': '-token-',
        })

        login_mock.assert_called_once()
        self.assertTrue(response.errors)
        self.assertIsNone(response.data['socialAuth'])
