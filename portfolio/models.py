from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from solo.models import SingletonModel

# Create your models here.
class Profile(SingletonModel):
    name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    email = models.EmailField()
    address =  models.CharField(max_length=60)

    def __str__(self):
        return "My Profile"

    class Meta:
        verbose_name = "My Profile"
        
class Project(models.Model):
    CATEGORY_CHOICES = [
    ('B', "Backend"),
    ('M', "Mobile"),
    ('F', "Frontend"),
    ('D', "Desktop App"),
    ('S', "Full Stack"),
    ]
    
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default=1,
    )
    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True)
    description = models.CharField(max_length=250)
    tech_stack = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='portfolio/images/projects/')
    
    def __str__(self) -> str:
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/images/projects/')
    
    def __str__(self) -> str:
        return f"{str(self.image)}"

class Testimonial(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/testimonials/')
    
    def __str__(self) -> str:
        return self.name
    

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.PositiveIntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    svg_path = models.CharField(max_length=1450)
    icon_box = models.CharField(max_length=30)
    aos_delay = models.PositiveIntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(300)])
    icon_name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.title
    

