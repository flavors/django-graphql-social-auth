Django GraphQL Social Auth
==========================

|Pypi| |Wheel| |Build Status| |Codecov| |Code Climate|

`Python Social Auth`_ support for `Django GraphQL`_


.. _Python Social Auth: http://python-social-auth.readthedocs.io/
.. _Django GraphQL: https://github.com/graphql-python/graphene-django


Dependencies
------------

* Python ≥ 3.4
* Django ≥ 1.11


Installation
------------

Install last stable version from Pypi.

.. code:: sh

    pip install django-graphql-social-auth


See the `documentation`_ for further guidance on setting *Python Social Auth*.

.. _documentation: http://python-social-auth.readthedocs.io/en/latest/configuration/django.html


Add the ``SocialAuth`` mutation to your GraphQL schema.

.. code:: python

    import graphene
    import graphql_social_auth


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.SocialAuth.Field()

`Session`_ authentication via *access_token*.

.. _Session: https://docs.djangoproject.com/en/2.0/topics/http/sessions/


.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
          extraData
        }
      }
    }


JSON Web Token (JWT)
--------------------

Authentication solution based on `JSON Web Token`_.

.. _JSON Web Token: https://jwt.io/

Install additional requirements.

.. code:: sh

    pip install 'django-graphql-social-auth[jwt]'


Add the ``SocialAuthJWT`` mutation to your GraphQL schema.

.. code:: python

    import graphene
    import graphql_social_auth


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.SocialAuthJWT.Field()


Authenticate via *access_token* to obtain a JSON Web Token.

.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
        }
        token
      }
    }


Relay
-----

Complete support for `Relay`_.

.. _Relay: https://facebook.github.io/relay/

.. code:: python

    import graphene
    import graphql_social_auth


    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.relay.SocialAuth.Field()


``graphql_social_auth.relay.SocialAuthJWT`` for `JSON Web Token (JWT)`_ authentication.


Customizing
-----------

If you want to customize the ``SocialAuth`` behavior, you'll need to customize the ``.do_auth()`` method on a subclass of ``SocialAuthMutation`` or ``.relay.SocialAuthMutation.``

.. code:: python

    import graphene
    import graphql_social_auth


    class SocialAuth(graphql_social_auth.SocialAuthMutation):
        user = graphene.Field(UserType)

        @classmethod
        def do_auth(cls, info, social, **kwargs):
            return cls(user=social.user)


Authenticate via *access_token* to obtain the *user id*.

.. code:: graphql

    mutation SocialAuth($provider: String!, $accessToken: String!) {
      socialAuth(provider: $provider, accessToken: $accessToken) {
        social {
          uid
        }
        user {
          id
        }
      }
    }

----

Gracias `Matías`_.

.. _Matías: https://github.com/omab


.. |Pypi| image:: https://img.shields.io/pypi/v/django-graphql-social-auth.svg
   :target: https://pypi.python.org/pypi/django-graphql-social-auth

.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-graphql-social-auth.svg
   :target: https://pypi.python.org/pypi/django-graphql-social-auth

.. |Build Status| image:: https://travis-ci.org/flavors/django-graphql-social-auth.svg?branch=master
   :target: https://travis-ci.org/flavors/django-graphql-social-auth

.. |Codecov| image:: https://img.shields.io/codecov/c/github/flavors/django-graphql-social-auth.svg
   :target: https://codecov.io/gh/flavors/django-graphql-social-auth

.. |Code Climate| image:: https://api.codeclimate.com/v1/badges/c579bcfde0fbb7f6334c/maintainability
   :target: https://codeclimate.com/github/flavors/django-graphql-social-auth
