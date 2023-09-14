from core import models


def get_all_models():
    return {
        "person": models.Person.objects.first(),
        "works": models.Work.objects.all(),
        "projects": models.Project.objects.all(),
        "educations": models.Education.objects.all(),
        "certificates": models.Certificate.objects.all(),
    }
