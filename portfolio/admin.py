from django.contrib import admin
from .models import Project, Testimonial, Skill, Service, Profile, ProjectImage
from solo.admin import SingletonModelAdmin
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Testimonial)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(ProjectImage)



admin.site.register(Profile, SingletonModelAdmin)
