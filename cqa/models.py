# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        user = self.model(
            username = username,
            account_id = CustomUser.objects.count() + 1
        )
        print(user.id)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    account_id = models.IntegerField(blank=True, null=True, unique=True)
    display_name = models.CharField(max_length=255)

    password = models.CharField(max_length=255)
    reputation = models.IntegerField(default=0)
    views = models.IntegerField(blank=True, null=True)
    down_votes = models.IntegerField(blank=True, null=True)
    up_votes = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=512, blank=True, null=True)
    profile_image_url = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, db_column='is_admin')
    last_login = models.DateField(auto_now=True, db_column='last_access_date')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    class Meta:
        managed = False
        db_table = 'users'

class Badges(models.Model):
    user_id = models.IntegerField()
    class_field = models.SmallIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=64)
    tag_based = models.BooleanField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'badges'


class Comments(models.Model):
    post_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    score = models.SmallIntegerField()
    content_license = models.CharField(max_length=64)
    user_display_name = models.CharField(max_length=64, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'

class PostHistory(models.Model):
    post_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    post_history_type_id = models.SmallIntegerField()
    user_display_name = models.CharField(max_length=64, blank=True, null=True)
    content_license = models.CharField(max_length=64, blank=True, null=True)
    revision_guid = models.UUIDField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'post_history'


class PostLinks(models.Model):
    related_post_id = models.IntegerField()
    post_id = models.IntegerField()
    link_type_id = models.SmallIntegerField()
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'post_links'


class Posts(models.Model):
    owner_user_id = models.IntegerField(blank=True, null=True)
    last_editor_user_id = models.IntegerField(blank=True, null=True)
    post_type_id = models.SmallIntegerField()
    accepted_answer_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    answer_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    owner_display_name = models.CharField(max_length=64, blank=True, null=True)
    last_editor_display_name = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    tags = models.CharField(max_length=512, blank=True, null=True)
    content_license = models.CharField(max_length=64)
    body = models.TextField(blank=True, null=True)
    favorite_count = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    community_owned_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    last_activity_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Tags(models.Model):
    excerpt_post_id = models.IntegerField(blank=True, null=True)
    wiki_post_id = models.IntegerField(blank=True, null=True)
    tag_name = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'

class Votes(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    post_id = models.IntegerField()
    vote_type_id = models.SmallIntegerField()
    bounty_amount = models.SmallIntegerField(blank=True, null=True)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'votes'
