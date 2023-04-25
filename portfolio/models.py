from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    
    def __str__(self) -> str:
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/testimonials/')
    
    def __str__(self) -> str:
        return self.name
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    value = models.PositiveIntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    svg_path = models.CharField(max_length=1450)
    icon_box = models.CharField(max_length=30)
    aos_delay = models.PositiveIntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(300)])
    icon_name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.title