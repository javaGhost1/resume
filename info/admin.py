from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(About)
admin.site.register(Testimonial)
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['course', 'slug']
    prepopulated_fields = {'slug': ('course',)}

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}