from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    birthdate = models.DateField()
    nationality = models.CharField(max_length=30)
    languages = ArrayField(models.CharField(max_length=30))
    skills = ArrayField(models.CharField(max_length=30))

    def __str__(self) -> str:
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    company_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    until_present = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    short_description = models.CharField(max_length=40)
    year = models.IntegerField()
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.name


course_type_choices = (("bachelor", "Bachelor"), ("other", "Other"))


class Education(models.Model):
    course = models.CharField(max_length=40)
    course_type = models.CharField(
        max_length=30, choices=course_type_choices, default="other"
    )
    institution_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=False)
    until_present = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.course


class Certificate(models.Model):
    name = models.CharField(max_length=30)
    provider = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=30)
    provider = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=200)
    icon = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return self.name
