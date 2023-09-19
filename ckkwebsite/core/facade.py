from core import models


def get_all_models():
    return {
        "person": models.Person.objects.first(),
        "works": models.Work.objects.all(),
        "projects": models.Project.objects.all(),
        "educations": models.Education.objects.all(),
        "awards": models.Award.objects.all(),
        "social_links": models.SocialLink.objects.all(),
    }
