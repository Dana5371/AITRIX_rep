from django.db import models

from account.models import User

# Create your models here.

class Category(models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=50, 
                             unique=True)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=50, 
                             unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey(Category, blank=True, 
                                null=True, 
                                on_delete=models.CASCADE,
                                related_name='children')

    def __str__(self) -> str:
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title
    
class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health')
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='prod_images')
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE,
                                 related_name='products')
    price = models.CharField(max_length=250)
    
    created = models.DateTimeField()
    

    def __str__(self):
        return self.title