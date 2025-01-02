from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


API_PREFIX = "api/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path(API_PREFIX, include("apps.courses.urls")),
    path(API_PREFIX, include("apps.students.urls")),
]
