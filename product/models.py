from django.db import models


def get_image_path(instance, filename):
    return 'products/{}/{}'.format(instance.pk, filename)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to=get_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['name', 'price']

    def __str__(self):
        return '{} - {}'.format(self.name, self.description[:30])
