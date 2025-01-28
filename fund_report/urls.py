from django.urls import path
from .views import  fundsReportAu

urlpatterns = [
    #html render
    path('',  fundsReportAu, name='fundsReportAu'),
]

