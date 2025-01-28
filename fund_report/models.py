
from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=200)
    section1_title =models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    hero_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
 

    class Meta:
        db_table = 'report'
        verbose_name = "Report"
        verbose_name_plural = "Reports"

  
