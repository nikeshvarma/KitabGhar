from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def get_image_path(instance, filename):
    return '{0}/{1}'.format(instance.category, filename)


class ProductCategory(models.Model):
    CATEGORY = [
        ('Course_Book', 'Course Book'),
        ('Novel', 'Novel'),
        ('Comics', 'Comics'),
        ('Story_Book', 'Story Book'),
        ('Biography', 'Biography')
    ]
    category = models.CharField(choices=CATEGORY, max_length=20)


class Product(models.Model):
    BOOK_TYPE = [
        ('Peperback', 'Peperback'),
        ('Soft_Copy', 'Soft Copy')
    ]

    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='product_category')
    MRP = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    price = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)])
    type = models.CharField(choices=BOOK_TYPE, max_length=20)
    quantity = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    out_of_stock = models.BooleanField(default=False)
    description = models.TextField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to=get_image_path)
    make_cover_image = models.BooleanField(default=False)
