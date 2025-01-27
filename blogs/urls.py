from django.urls import path
from .views import blogPage, fundsReportAu,blogList

urlpatterns = [
    #html render
    path('',  blogPage, name='blogPage'), 
    path('',  fundsReportAu, name='fundsReportAu'),
    #render ajax 
    path('list',  blogList, name='blogList'), 
]