from django.db import models
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    birthdate = models.DateField()
    nationality = models.CharField(max_length=30)
    languages = ArrayField(models.CharField(max_length=30))
    stack = ArrayField(models.CharField(max_length=30))
    profile_pic = models.ImageField(upload_to="images/", null=True, blank=True)
    pronoums = models.CharField(max_length=13, blank=True, default="he/him")
    nickname = models.CharField(max_length=30, blank=True, default="")

    def __str__(self) -> str:
        return self.name

    @property
    def age(self):
        from datetime import date

        today = date.today()
        return (
            today.year
            - self.birthdate.year
            - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        )

    @property
    def stack_text(self):
        return str(self.stack).replace("[", "").replace("]", "").replace("'", "")


class Work(models.Model):
    title = models.CharField(max_length=30)
    stack = ArrayField(models.CharField(max_length=15))
    description = models.TextField()
    company_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    until_present = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.company_name} - {self.title}"

    @property
    def stack_text(self):
        return str(self.stack).replace("[", "").replace("]", "").replace("'", "")


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    short_description = models.CharField(max_length=40)
    year = models.IntegerField()
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.name


course_type_choices = (("BACHELOR", "Bachelor"), ("OTHER", "Other"))


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


award_type_choices = (("AWARD", "Award"), ("CERTIFICATE", "Certificate"))


class Award(models.Model):
    name = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    year = models.IntegerField()
    type = models.CharField(max_length=30, choices=award_type_choices)

    def __str__(self) -> str:
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, null=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
