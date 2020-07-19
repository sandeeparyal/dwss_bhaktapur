from datetime import date
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Position(models.Model):
    POSITION_TITLE_CHOICES = [
            ('1CH', 'डिभिजन प्रमुख'),
            ('2SE', 'सुई'),
            ('3SDE', 'सिडिई'),
            ('4ERE', 'ईन्जिनियर आठौं'),
            ('5ERS', 'ईन्जिनियर सातौं'),
            ('6AOS', 'प्रशासन अधिकृत छैठौं'),
            ('7ACOS', 'लेखा अधिकृत छैठौं'),
            ('8CO', 'कम्प्युटर अधिकृत छैठौं'),
            ('9OT', 'अधिकृत छैठौं'),
            ('10SUBE', 'सब ईन्जिनियर'),
            ('11TEC', 'खा पा स टे'),
            ]

    POSITION_SERVICE_CHOICES = [
            ('AD', 'Administration'),
            ('EN', 'Engineering'),
            ('LG', 'Law'),
            ('ACC', 'Account'),
            ('MSC', 'Miscellaneous'),
            ]
    
    position_title = models.CharField(max_length=10, choices=POSITION_TITLE_CHOICES, default='5ERS')
    position_service = models.CharField(max_length=200, choices=POSITION_SERVICE_CHOICES)
    position_group = models.CharField(max_length=200, null=True, blank=True)
    position_subgroup = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.position_title

class Employee(models.Model):
    employee_lastname = models.CharField(max_length=200)
    employee_firstname = models.CharField(max_length=200)
    employee_section = models.CharField(max_length=100, unique=False, default=' ')
    employee_telephone = models.CharField(max_length=10, unique=False, default=' ')
    employee_position = models.ForeignKey(Position, on_delete=models.CASCADE)


    def __str__(self):
        return self.employee_firstname

    
class News(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    published_date = models.DateTimeField()
    short_text = models.CharField(max_length=120)
        
    def __str__(self):
        return self.title

class Document(models.Model):
    DOCUMENT_TITLE_CHOICES = [
            ('LAW', 'ऐन'),
            ('TN', 'टेन्डर आव्ह्वान'),
            ('OD', 'अन्य दस्तावेजहरु'),
            ]
    document_path = models.FileField(blank=True, null=True, upload_to='documents', default='/media/documents/django.pdf')
    document_category= models.CharField(max_length=50, choices=DOCUMENT_TITLE_CHOICES, default='OD')
    document_title = models.CharField(max_length=200, null=False)
    document_date = models.DateField('date created', default=date.today, blank=True, null=True)
    
    def __str__(self):
        return self.document_title
    








