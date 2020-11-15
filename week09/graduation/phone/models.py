# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=2000, blank=True, null=True)
    favorable_rate = models.CharField(max_length=50, blank=True, null=True)
    top_word = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'good'


class GoodComment(models.Model):
    good_id = models.IntegerField()
    comment = models.CharField(max_length=2000, blank=True, null=True)
    positive = models.IntegerField()
    create_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'good_comment'
