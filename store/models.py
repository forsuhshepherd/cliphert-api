from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from cliphert.utils import _slug_generator


class PaymentMethod(models.Model):
    Status_Choices = [
        ('active', 'active'),
        ('inactive', 'inactive'),
    ]
    title = models.CharField(verbose_name='Name', max_length=255, blank=True, default=None)
    status = models.CharField(verbose_name='Status', max_length=20,
        choices=Status_Choices,
        default=Status_Choices[1], null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    logo = models.URLField(verbose_name='Logo', max_length=500, null=True)    
    timestamp = models.DateTimeField(verbose_name='Timestamp',
        auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Payment Method')
        verbose_name_plural = ('Payment Methods')
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = _slug_generator(self)
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Slug', max_length=255, blank=True)
    description = models.TextField(verbose_name='Description', default='', blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

def _slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = _slug_generator(instance)

pre_save.connect(_slug_save, sender=Category)


class Product(models.Model):
    STATUS_CHOICES = [
        ('on-sale', 'on sale'),
        ('pending', 'pending'),
        ('sold', 'sold')
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=255)
    slug = models.SlugField(verbose_name='Slug', max_length=255, blank=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    price = models.FloatField(verbose_name='Price')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='date created')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Seller', to_field='username', on_delete=models.CASCADE, related_name='seller_products', blank=True, null=True)
    status = models.CharField(max_length=255, verbose_name='Status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0], null=True)

    def __str__(self):
        return self.title
    
def _slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = _slug_generator(instance)

pre_save.connect(_slug_save, sender=Product)


class Profile(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="assets/images/", blank=True)

    def __str__(self):
        return f'{self.id}'

