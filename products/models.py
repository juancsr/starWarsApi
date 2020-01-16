from django.db import models

# Create your models here.
class ProductModel(models):
    title = models.TextField()
    image = models.ImageField(_(""), upload_to="static/images", height_field=None, width_field=None, max_length=None)
    price = models.NumberField()
    description = models.TextField()

