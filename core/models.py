from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from account.models import CustomUser

class List(models.Model):
    title= models.CharField(max_length=100)
    image = models.ImageField(upload_to="listimages", null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
       
       
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)   
        
        
class Task(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="taskimages", null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    description = RichTextField()
    is_done = models.BooleanField(default=False)
    deadline = models.CharField(max_length=100)
    lists = models.ManyToManyField(List, blank=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
   
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
        