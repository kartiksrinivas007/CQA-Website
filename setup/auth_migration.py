from ..mysite.cqa.models import Users
from django.contrib.auth.models import User as AuthUser

def code_used():
    users = Users.objects.all()
    for user in users:
        username = user.display_name + str(user.id)
        auth_user = AuthUser.objects.create_user(username=username, password=username)
        auth_user.save()
