from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy$', views.buy),
    url(r'^checkout$', views.checkout),
    # url(r'^(?P<courseid>\d+)/comment$', views.comment),
    # url(r'^(?P<courseid>\d+)/comment/new$', views.newcomment),
    # url(r'^(?P<course_id>\d+)/destroy$', views.destroy),
    # url(r'^(?P<course_id>\d+)/deletecourse$', views.deletecourse),
]