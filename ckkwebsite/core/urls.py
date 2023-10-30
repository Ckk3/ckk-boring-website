from core import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path("", views.homepage, name="homepage"),
    # SEO
    # sitemap
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
