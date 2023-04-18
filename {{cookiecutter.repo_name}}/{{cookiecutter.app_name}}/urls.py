from django.urls import path,include
from {{cookiecutter.app_name}} import views
urlpatterns = [
    path("status/", views.StatusView.as_view(), name="api_view"),
    path("sample/", views.SampleView.as_view(), name="sample_view"),
]