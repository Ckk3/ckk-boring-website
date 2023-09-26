from core import models


def get_all_models():
    all_awards = models.Award.objects.all().order_by("-year")
    return {
        "person": models.Person.objects.first(),
        "works": models.Work.objects.all().order_by("-until_present", "-end_date"),
        "projects": models.Project.objects.all().order_by("-year"),
        "educations": models.Education.objects.all().order_by(
            "-until_present", "-end_date", "-start_date"
        ),
        "awards": all_awards.filter(type="AWARD"),
        "certificates": all_awards.filter(type="CERTIFICATE"),
        "social_links": models.SocialLink.objects.all().order_by("name"),
    }
