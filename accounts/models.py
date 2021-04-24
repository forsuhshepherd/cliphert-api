from django.db import models
from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)

#Customised system user
from django.conf import settings

class User(AbstractUser):
    full_name = models.CharField(blank=True, max_length=150, verbose_name='full name')
    contact = models.CharField(verbose_name='Contact Number', max_length=13, blank=True)

    REQUIRED_FIELDS = ['full_name']
    def __str__(self):
        return f'{self.full_name}'


#describes additional user characteristics
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #avatar = models.ImageField(upload_to='var/www/media/images/')
    bio = models.TextField('Biography', max_length=500, blank=True, null=True)
    contact = models.CharField('Contact', max_length=20, default=None, blank=True, null=True)
    address = models.CharField('Address', max_length=255, blank=True, null=True)
