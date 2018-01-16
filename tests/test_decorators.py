from unittest.mock import MagicMock

from django.test import TestCase, override_settings

from graphql_social_auth import decorators, exceptions

from .decorators import social_auth_mock


class DecoratorsTests(TestCase):

    def test_missing_backend(self):

        @decorators.social_auth
        def wrapped(self, root, info, provider, *args, **kwargs):
            """Social auth decorated function"""

        mock = MagicMock()

        with self.assertRaises(exceptions.GraphQLSocialError):
            wrapped(self, mock, mock, 'unknown', '-token-')

    def test_do_auth_user_not_found(self):
        @social_auth_mock
        @override_settings(SOCIAL_AUTH_PIPELINE=[])
        @decorators.social_auth
        def wrapped(self, root, info, provider, *args, **kwargs):
            """Social auth decorated function"""

        mock = MagicMock()

        with self.assertRaises(exceptions.GraphQLSocialError):
            wrapped(self, mock, mock, 'google-oauth2', '-token-')
