from django.db import models

class Product(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)
    price = models.BigIntegerField()
    description = models.TextField()

