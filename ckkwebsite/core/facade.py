from core import models


def get_all_models():
    return {
        "person": models.Person.objects.first(),
        "works": models.Work.objects.all().order_by("-until_present", "-end_date"),
        "projects": models.Project.objects.all().order_by("-year"),
        "educations": models.Education.objects.all().order_by(
            "-until_present", "-end_date", "-start_date"
        ),
        "awards": models.Award.objects.all().order_by("-year"),
        "social_links": models.SocialLink.objects.all().order_by("name"),
    }
