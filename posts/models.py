from django.db import models

# Create your models here.

from cqa.models import *


# class Posts(models.Model):
#     owner_user_id = models.IntegerField(blank=True, null=True)
#     last_editor_user_id = models.IntegerField(blank=True, null=True)
#     post_type_id = models.SmallIntegerField()
#     accepted_answer_id = models.IntegerField(blank=True, null=True)
#     score = models.IntegerField()
#     parent_id = models.IntegerField(blank=True, null=True)
#     view_count = models.IntegerField(blank=True, null=True)
#     answer_count = models.IntegerField(blank=True, null=True)
#     comment_count = models.IntegerField(blank=True, null=True)
#     owner_display_name = models.CharField(max_length=64, blank=True, null=True)
#     last_editor_display_name = models.CharField(max_length=64, blank=True, null=True)
#     title = models.CharField(max_length=512, blank=True, null=True)
#     tags = models.CharField(max_length=512, blank=True, null=True)
#     content_license = models.CharField(max_length=64)
#     body = models.TextField(blank=True, null=True)
#     favorite_count = models.IntegerField(blank=True, null=True)
#     creation_date = models.DateTimeField()
#     community_owned_date = models.DateTimeField(blank=True, null=True)
#     closed_date = models.DateTimeField(blank=True, null=True)
#     last_edit_date = models.DateTimeField(blank=True, null=True)
#     last_activity_date = models.DateTimeField(blank=True, null=True)