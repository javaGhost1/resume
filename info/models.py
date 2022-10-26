from django.db import models
from phone_field import PhoneField
class About(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    job_role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    desc = models.TextField()
    birth_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    city = models.CharField(max_length=50)
    skills_desc = models.TextField()
    skill_one = models.CharField(max_length=50)
    skill_two = models.CharField(max_length=50)
    skill_three = models.CharField(max_length=50)
    skill_four = models.CharField(max_length=50)
    skill_five = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name

class Education(models.Model):
    course = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    start_year = models.DateTimeField(auto_now=False, auto_now_add=False)
    completion_year = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.course

class Work(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)
    start_year = models.DateTimeField(auto_now=False, auto_now_add=False)
    company = models.CharField(max_length=50)
    completion_year = models.DateTimeField(auto_now=False, auto_now_add=False)
    role_one = models.TextField()
    role_two = models.TextField()
    role_three = models.TextField()
    role_four = models.TextField()

    def __str__(self) -> str:
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    date_done = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    comment = models.TextField()
    def __str__(self) -> str:
        return self.name