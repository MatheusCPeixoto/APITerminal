# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FAtividade(models.Model):
    codigo = models.AutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    codcoligada = models.ForeignKey('Coligada', models.DO_NOTHING, db_column='CODCOLIGADA', blank=True, null=True)  # Field name made lowercase.
    codfilial = models.IntegerField(db_column='CODFILIAL', blank=True, null=True)  # Field name made lowercase.
    descatividade = models.CharField(db_column='DESCATIVIDADE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    preparacao = models.TextField(db_column='PREPARACAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    execucao = models.TextField(db_column='EXECUCAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conferencia = models.TextField(db_column='CONFERENCIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idatividade = models.CharField(db_column='IDATIVIDADE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    setup = models.IntegerField(db_column='SETUP', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'F_ATIVIDADE'
