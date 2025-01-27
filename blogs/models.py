# from django.db import models

# # Create your models here.
# class Blogs(models.Model):
#     title = models.CharField(max_length=100)
#     image =  models.ImageField(upload_to='image/')
#     description =  models.TextField()
#     date = models.DateField()
    
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         db_table = "blogs"
#         verbose_name = "Blog"
#         verbose_name_plural = "Blogs"

from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.title

    class Meta:
        db_table = "blogs"
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

  
