## DO NOT RUN THIS FILE ##
from django.contrib.auth.hashers import make_password, check_password
from cqa.models import Users

print('Hi')

for u in Users.objects.all():
    temp = u.password
    u.password = make_password(temp)
    u.save()


"""
Note:
Due to the long execution time, we terminated the hashing after a few thousand users.
Hence, not all passwords of existing users are hashed.
"""