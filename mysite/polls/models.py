from django.db import models
from django.db.models.fields import EmailField


class Client(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cuentaFacebook = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=200)
    fechaNacimiento = models.DateField('Fecha de Nacimiento')
    privilegios = models.BooleanField()

    def __str__(self):
        return self.nombre


class Subscription(models.Model):
    nombre = models.CharField(max_length=200)
    precioMensual = models.FloatField()
    caracteristicas = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
     
class Dayweek(models.Model):
    dia = models.CharField(max_length=200)

    def __str__(self):
        return self.dia


class ContactForm(models.Model):
    nombre = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', verbose_name='logo', default='noneyo')

    def __str__(self):
        return self.nombre

class Heading(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Business(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fotoNegocio = models.ImageField(upload_to='images/', verbose_name='Foto del Negocio')
    fotoLogotipo = models.ImageField(upload_to='images/', verbose_name='Logo del Negocio')
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    rubros = models.ManyToManyField(Heading, through='BusinessArea')
    formasContacto = models.ManyToManyField(ContactForm, through='BusinessContactForm')
    diasSemana = models.ManyToManyField(Dayweek, through='Businesshourday')

    def __str__(self):
        return self.nombre



class Businesshourday(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    diaSemana = models.ForeignKey(Dayweek, on_delete=models.CASCADE)
    horaAbre = models.TimeField(blank=True, null=True, verbose_name='Hora Abre')
    horaCierra = models.TimeField(blank=True, null=True, verbose_name='Hora Cierra')

    def __str__(self):
        return self.negocio.nombre


class BusinessArea(models.Model):
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    rubro = models.ForeignKey(Heading, on_delete=models.CASCADE)

    def __str__(self):
        return self.negocio.nombre



class BusinessContactForm(models.Model):
    formaContacto = models.ForeignKey(ContactForm, on_delete=models.CASCADE)
    negocio = models.ForeignKey(Business, on_delete=models.CASCADE)
    datosContacto = models.CharField(max_length=200, help_text= 'para número, ingrese el codigo de area seguido del 15 y luego el numero')

    def __str__(self):
        return self.negocio.nombre
    
    def getNumber(self):
        numero = ''
        if (self.formaContacto.nombre == 'Facebook'):
            numero = ''
        else:
            separados = self.datosContacto.split("15", 1)
            separados.insert(0,'549')

            for item in separados:
                numero = numero + item
                # print(numero)
        return numero

