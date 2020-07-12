from datetime import date
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Position(models.Model):
    POSITION_TITLE_CHOICES = [
            ('SC', 'Secretary'),
            ('JS', 'Joint Secretary'),
            ('US', 'Under Secretary'),
            ('SO', 'Section Officer'),
            ('AO', 'Assistant Officer'),
            ]

    POSITION_SERVICE_CHOICES = [
            ('AD', 'Administration'),
            ('EN', 'Engineering'),
            ('LG', 'Law'),
            ('MS', 'Miscellaneous'),
            ('SE', 'Cabinet'),
            ]
    
    position_title = models.CharField(max_length=2, choices=POSITION_TITLE_CHOICES, default='SO')
    position_service = models.CharField(max_length=200, choices=POSITION_SERVICE_CHOICES)
    position_group = models.CharField(max_length=200, null=True, blank=True)
    position_subgroup = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.position_title

class Employee(models.Model):
    employee_lastname = models.CharField(max_length=200)
    employee_firstname = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=10, unique=True)
    employee_cv = models.FileField(blank=True, null=True, upload_to='resumes', default='/media/resumes/django.pdf')
    employee_photo = models.ImageField(blank=True, null=True, upload_to='photos', default='/media/photos/test_image.png')
    employee_dob = models.DateField('date_of_birth', default=date.today, blank=True, null=True)
    employee_position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def is_over_18(self):
        if(self.employee_dob):
            today = date.today()
            return ( today.year - self.employee_dob.year - ((today.month, today.day) <(self.employee_dob.month, self.employee_dob.day)))

    def photo_or_cv_exists(self):
        if(self.employee_photo and self.employee_cv):
            return True 

    def __str__(self):
        return self.employee_firstname

    
class News(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    published_date = models.DateTimeField()
    short_text = models.CharField(max_length=120)
        
    def __str__(self):
        return self.title

