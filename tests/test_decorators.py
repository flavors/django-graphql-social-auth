from unittest.mock import MagicMock

from django.test import TestCase, override_settings

from graphql_social_auth import decorators, exceptions

from .decorators import social_auth_mock


class DecoratorsTests(TestCase):

    def test_psa_missing_backend(self):

        @decorators.social_auth
        def wrapped(self, root, info, provider, *args):
            """Social auth decorated function"""

        mock = MagicMock()

        with self.assertRaises(exceptions.GraphQLSocialAuthError):
            wrapped(self, mock, mock, 'unknown', '-token-')

    @social_auth_mock
    @override_settings(SOCIAL_AUTH_PIPELINE=[])
    def test_psa_user_not_found(self, *args):

        @decorators.social_auth
        def wrapped(self, root, info, provider, *args):
            """Social auth decorated function"""

        mock = MagicMock()
        with self.assertRaises(exceptions.GraphQLSocialAuthError):
            wrapped(self, mock, mock, 'google-oauth2', '-token-')
