from django.db import models
from django.contrib.auth.models import  AbstractUser,User, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, rut, first_name,password,is_staff,is_superuser,**extra_fields): 
        user= self.model(
            username=username,
            rut=rut,
            first_name=first_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,username,rut,first_name,password=None,**extra_fields):
        return self._create_user(username,rut,first_name,password,False,False,**extra_fields)
    
    def create_superuser(self,username,rut,first_name,password=None,**extra_fields):
        return self._create_user(username,rut,first_name,password,True,True,**extra_fields)
     


class User(AbstractUser):
    username= models.CharField('Nombre de Usuario', unique=True, max_length=100)
    first_name= models.CharField('Nombres', max_length=200, blank=True, null=True)
    last_name= models.CharField('Apellidos', max_length=200, blank=True, null=True)
    is_active= models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rut = models.CharField(max_length=12, unique=True, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rut', 'first_name', 'last_name']

    def __str__(self) :
        return f'{self.first_name}, {self.last_name}'
    