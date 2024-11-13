from django.db import models

# Create your models here.

class Skill(models.Model):
    class Category(models.TextChoices):
        PROGRAMMING = "PROGRAMMING", "PROGRAMMING"
        DATABASE = "DATABASE", "DATABASE"
        AIML = "AIML", "AIML"
        DATA_VISUALIZATION = "DATA VISUALIZATION", "DATA VISUALIZATION"
        OTHERS = "OTHERS", "OTHERS"
        SOFT_SKILLS = "SOFT SKILLS", "SOFT SKILLS"
    category = models.CharField(
        max_length=100,
        choices=Category.choices,
        default=Category.OTHERS   
    )
    skills_name = models.CharField(max_length=100)
    def __str__(self):
        return self.skills_name
    

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    last_date = models.DateField(blank=True, null=True)
    description1 = models.CharField(max_length=1000)
    description2 = models.CharField(max_length=1000, blank=True, null=True)
    description3 = models.CharField(max_length=1000, blank=True, null=True)
    description4 = models.CharField(max_length=1000, blank=True, null=True)
    description5 = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.company_name
    

class Academic(models.Model):
    degree = models.CharField(max_length=100)
    school_or_college = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)
    start_date = models.DateField()
    last_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.degree


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_url = models.URLField()
    description1 = models.CharField(max_length=255)
    description2 = models.CharField(max_length=255)
    description3 = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name
    

class Certificate(models.Model):
    certificate_image = models.URLField(max_length=1000)
    certificate_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.certificate_name