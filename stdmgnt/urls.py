from django.urls import path

from .views import student, staff

urlpatterns = [
    path('student/', student),
    path('staff/', staff)

]
