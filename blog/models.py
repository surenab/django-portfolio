from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateTimeField()
    pdf_file = models.FileField(upload_to="blog/pdfes", blank=True)
    is_popular = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title