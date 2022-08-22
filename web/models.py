from django.db import models

class Compania(models.Model):
    idcompania = models.AutoField(db_column='idCompania', primary_key=True)  # Field name made lowercase.
    nombrecompania = models.CharField(db_column='nombreCompania', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ruc = models.CharField(max_length=45, blank=True)
    nombrecoordinador = models.CharField(db_column='nombreCoordinador', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compania'
    def __str__(self):
        return self.nombrecompania