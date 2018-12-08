from django.db import models

# Create your models here.

class Ontology(models.Model):
    name = models.CharField(max_length=40,null=False,blank=False) 
    uri = models.URLField(max_length=200,null=False)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to='uploads/ontologies/',blank=True)
    license = models.CharField(max_length=100,blank=True)
    authors = models.ManyToManyField('Author',blank=True)
    def __str__(self):
        return self.name

class Author(models.Model):
	name = models.CharField(max_length=20) 
	introduction = models.TextField(max_length=1000)
	def __str__(self):
		return self.name


