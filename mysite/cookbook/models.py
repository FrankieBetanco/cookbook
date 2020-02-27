from django.db import models

# Create your models here.
class Contributor(models.Model): 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RecipeType(models.Model):
    name = models.CharField(max_length=100, default='no category')

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(RecipeType, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=True)
    ingredients = models.TextField(max_length=2000, default='none specified')
    instructions = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
