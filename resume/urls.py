
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path('degree/', views.degree, name='degree'),
    path("projects/",views.projects,name="projects"),
    path("experience/", views.experience, name="experience"),
    path("certificate/", views.certificate ,name="certificate"),
    path("contact/", views.contact, name="contact"),
    path("resume/",views.resume,name="resume"),
    path("resume/<path:path>", views.upload, name="upload"),
]
