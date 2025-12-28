def is_super_admin(user):
    return user.is_superuser


def is_admin(user):
    return user.groups.filter(name='admin').exists()


def is_serwisant(user):
    return user.groups.filter(name='serwisant').exists()
