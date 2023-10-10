from django.contrib import admin
from core import models

all_models = [
    models.Person,
    models.Work,
    models.Project,
    models.Education,
    models.Award,
    models.SocialLink,
]
# Register your models here.
for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
