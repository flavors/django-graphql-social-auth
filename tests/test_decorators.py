from unittest.mock import MagicMock, Mock

from django.test import TestCase, override_settings

from promise import Promise, is_thenable

from graphql_social_auth import decorators, exceptions

from .decorators import social_auth_mock


class DecoratorsTests(TestCase):

    def test_psa_missing_backend(self):

        @decorators.social_auth
        def wrapped(cls, root, info, provider, *args):
            """Social Auth decorated function"""

        with self.assertRaises(exceptions.GraphQLSocialAuthError):
            wrapped(self, None, Mock(), 'unknown', 'token')

    @social_auth_mock
    @override_settings(SOCIAL_AUTH_PIPELINE=[])
    def test_psa_user_not_found(self, *args):

        @decorators.social_auth
        def wrapped(cls, root, info, provider, *args):
            """Social Auth decorated function"""

        with self.assertRaises(exceptions.GraphQLSocialAuthError):
            wrapped(self, None, Mock(), 'google-oauth2', 'token')

    @social_auth_mock
    def test_social_auth_thenable(self, *args):

        @decorators.social_auth
        def wrapped(cls, root, info, provider, *args):
            return Promise()

        result = wrapped(TestCase, None, MagicMock(), 'google-oauth2', 'token')

        self.assertTrue(is_thenable(result))
