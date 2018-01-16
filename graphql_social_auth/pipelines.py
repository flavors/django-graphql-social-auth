
def associate_signed_user(strategy, social=None, *args, **kwargs):
    user = strategy.request.user
    if user.is_authenticated and social is None:
        return {'user': user}
