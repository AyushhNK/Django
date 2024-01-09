from django.db import models

# Create your models here.

class Product(models.Model):
	image=models.ImageField(upload_to="Product_image")
	name=models.CharField(max_length=20)
	price=models.IntegerField()

	def __str__(self):
		return self.name
