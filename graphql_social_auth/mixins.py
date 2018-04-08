import graphene


class SocialAuthMixin:

    @classmethod
    def __init_subclass_with_meta__(cls, name=None, **options):
        assert getattr(cls, 'resolve', None), (
            '{name}.resolve method is required in a SocialAuthMutation.'
        ).format(name=name or cls.__name__)

        super().__init_subclass_with_meta__(name=name, **options)


class ResolveMixin:

    @classmethod
    def resolve(cls, *args, **kwargs):
        return cls()


class JSONWebTokenMixin:
    token = graphene.String()

    @classmethod
    def resolve(cls, root, info, social, **kwargs):
        try:
            from graphql_jwt.shortcuts import get_token
        except ImportError:
            raise ImportError(
                'django-graphql-jwt not installed.\n'
                'Use `pip install \'django-graphql-social-auth[jwt]\'`.')

        return cls(token=get_token(social.user))
