from django.db import models # type: ignore

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=255)
	mobile = models.IntegerField()
	email = models.EmailField()
	salary = models.FloatField()
	
	def __str__(self):
		return self.name

