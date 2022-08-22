# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    idcargo = models.AutoField(db_column='idCargo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='idPersona')  # Field name made lowercase.
    idreferido = models.ForeignKey('Referido', models.DO_NOTHING, db_column='idReferido', blank=True, null=True)  # Field name made lowercase.
    iddatoscliente = models.IntegerField(db_column='idDatosCliente', blank=True, null=True)  # Field name made lowercase.
    iddatosfacturacion = models.IntegerField(db_column='idDatosFacturacion', blank=True, null=True)  # Field name made lowercase.
    iddatosfinancieros = models.IntegerField(db_column='idDatosFinancieros', blank=True, null=True)  # Field name made lowercase.
    iddatospreexistencia = models.IntegerField(db_column='idDatosPreexistencia', blank=True, null=True)  # Field name made lowercase.
    idsolicitud = models.IntegerField(db_column='idSolicitud', blank=True, null=True)  # Field name made lowercase.
    contacto = models.IntegerField(blank=True, null=True)
    talla = models.CharField(max_length=45, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    esbeneficiario = models.IntegerField(db_column='esBeneficiario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Clientedependiente(models.Model):
    idclientedependiente = models.AutoField(db_column='idClienteDependiente', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    iddependiente = models.ForeignKey('Dependiente', models.DO_NOTHING, db_column='idDependiente')  # Field name made lowercase.
    parentescocontitular = models.CharField(db_column='parentescoConTitular', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientedependiente'


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


class Contactoprospecto(models.Model):
    idcontactoprospecto = models.AutoField(db_column='idContactoProspecto', primary_key=True)  # Field name made lowercase.
    contenido = models.CharField(max_length=256, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    idprospecto = models.ForeignKey('Prospecto', models.DO_NOTHING, db_column='idProspecto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contactoprospecto'


class Contrato(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    idplan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='idPlan', blank=True, null=True)  # Field name made lowercase.
    idagenteasignado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='idAgenteAsignado', blank=True, null=True)  # Field name made lowercase.
    primaanioactual = models.FloatField(db_column='primaAnioActual', blank=True, null=True)  # Field name made lowercase.
    modalidadprma = models.CharField(db_column='modalidadPrma', max_length=45, blank=True, null=True)  # Field name made lowercase.
    valorcuotaprima = models.FloatField(db_column='valorCuotaPrima', blank=True, null=True)  # Field name made lowercase.
    primaaniosiguiente = models.FloatField(db_column='primaAnioSiguiente', blank=True, null=True)  # Field name made lowercase.
    aumentoprima = models.FloatField(db_column='aumentoPrima', blank=True, null=True)  # Field name made lowercase.
    porcentajeaumento = models.FloatField(db_column='porcentajeAumento', blank=True, null=True)  # Field name made lowercase.
    estadofirmacontrato = models.IntegerField(db_column='estadoFirmaContrato', blank=True, null=True)  # Field name made lowercase.
    diadefirma = models.DateField(db_column='diaDeFirma', blank=True, null=True)  # Field name made lowercase.
    firmado = models.DateField(blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    fechavigencia = models.DateField(db_column='fechaVigencia', blank=True, null=True)  # Field name made lowercase.
    fechapagoprimercuota = models.DateField(db_column='fechaPagoPrimerCuota', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    comisionagente = models.FloatField(db_column='comisionAgente', blank=True, null=True)  # Field name made lowercase.
    porcentajecomision = models.FloatField(db_column='porcentajeComision', blank=True, null=True)  # Field name made lowercase.
    contratocol = models.CharField(db_column='Contratocol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idcotizacion = models.IntegerField(db_column='idCotizacion', blank=True, null=True)  # Field name made lowercase.
    sumaasegurada = models.FloatField(db_column='sumaAsegurada', blank=True, null=True)  # Field name made lowercase.
    endoso = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=45, blank=True, null=True)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    aniomodelo = models.DateField(db_column='anioModelo', blank=True, null=True)  # Field name made lowercase.
    pasajeros = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato'


class Cotizacion(models.Model):
    idcotizacion = models.AutoField(db_column='idCotizacion', primary_key=True)  # Field name made lowercase.
    idprospecto = models.ForeignKey('Prospecto', models.DO_NOTHING, db_column='idProspecto', blank=True, null=True)  # Field name made lowercase.
    idplan = models.IntegerField(db_column='idPlan')  # Field name made lowercase.
    idagente = models.IntegerField(db_column='idAgente', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    modificado = models.DateTimeField(db_column='Modificado')  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cotizacion'


class Deducible(models.Model):
    iddeducible = models.AutoField(db_column='idDeducible', primary_key=True)  # Field name made lowercase.
    idplan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='idPlan')  # Field name made lowercase.
    tipodeducible = models.CharField(db_column='tipoDeducible', max_length=45, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deducible'


class Dependiente(models.Model):
    iddependiente = models.AutoField(db_column='idDependiente', primary_key=True)  # Field name made lowercase.
    talla = models.CharField(max_length=45, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    nombres = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    tipodeidentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroidentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependiente'


class Direccion(models.Model):
    iddireccion = models.AutoField(db_column='idDireccion', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.
    tipodireccion = models.CharField(db_column='tipoDireccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Documentocontrato(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciondocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documentocontrato'


class Documentodependiente(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    iddependiente = models.ForeignKey(Dependiente, models.DO_NOTHING, db_column='idDependiente')  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciondocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documentodependiente'


class Documentoempleado(models.Model):
    iddocumento = models.AutoField(db_column='idDocumento', primary_key=True)  # Field name made lowercase.
    idempleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='idEmpleado')  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripciondocumento = models.CharField(db_column='descripcionDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'documentoempleado'


class Empleado(models.Model):
    idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='idPersona')  # Field name made lowercase.
    fechaingresonoboa = models.DateField(db_column='fechaIngresoNoboa', blank=True, null=True)  # Field name made lowercase.
    idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idCargo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'


class Notificacionventas(models.Model):
    idnotificacion = models.AutoField(db_column='idNotificacion', primary_key=True)  # Field name made lowercase.
    idsupervisor = models.IntegerField(db_column='idSupervisor', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=256, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    contenido = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    creado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notificacionventas'


class Notificacionventasremitentes(models.Model):
    idnotificacion = models.OneToOneField(Notificacionventas, models.DO_NOTHING, db_column='idNotificacion', primary_key=True)  # Field name made lowercase.
    idagente = models.IntegerField(db_column='idAgente')  # Field name made lowercase.
    visto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notificacionventasremitentes'
        unique_together = (('idnotificacion', 'idagente'),)


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    tipodeidentificacion = models.CharField(db_column='tipoDeIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numeroidentificacion = models.CharField(db_column='numeroIdentificacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    estadcivil = models.CharField(db_column='estadCivil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipopersona = models.CharField(db_column='tipoPersona', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Plan(models.Model):
    idplan = models.AutoField(db_column='idPlan', primary_key=True)  # Field name made lowercase.
    idcompania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='idCompania', blank=True, null=True)  # Field name made lowercase.
    tipodeplan = models.CharField(db_column='tipoDePlan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodeseguro = models.CharField(db_column='tipoDeSeguro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombreplan = models.CharField(db_column='nombrePlan', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tienelimite = models.IntegerField(db_column='tieneLimite', blank=True, null=True)  # Field name made lowercase.
    cobertura = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class Prospecto(models.Model):
    idprospecto = models.AutoField(db_column='idProspecto', primary_key=True)  # Field name made lowercase.
    idagente = models.IntegerField(db_column='idAgente', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    edad = models.CharField(max_length=45, blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    proyectadoactual = models.IntegerField(db_column='proyectadoActual', blank=True, null=True)  # Field name made lowercase.
    urlarchivo = models.CharField(db_column='urlArchivo', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prospecto'


class Prospectosesion(models.Model):
    idprospectosesion = models.AutoField(db_column='idProspectoSesion', primary_key=True)  # Field name made lowercase.
    idprospecto = models.ForeignKey(Prospecto, models.DO_NOTHING, db_column='idProspecto', blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField()
    fin = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospectosesion'


class Referido(models.Model):
    idreferido = models.AutoField(db_column='idReferido', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referido'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='idPersona', blank=True, null=True)  # Field name made lowercase.
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    claveusuario = models.CharField(db_column='claveUsuario', max_length=45)  # Field name made lowercase.
    token = models.CharField(max_length=45, blank=True, null=True)
    fotousuario = models.CharField(db_column='fotoUsuario', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
