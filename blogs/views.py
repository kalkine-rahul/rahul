from django.shortcuts import render
from django.http import JsonResponse
    
    
from .models import Blogs
from .serializers import BlogsSerializer


def blogPage(request):
    return render(request, 'blogs.html')

def fundsReportAu(request):
    return render(request, 'funds-report-au.html')

def blogList(request):
    blog_objs = Blogs.objects.all()
    if blog_objs:
        blogs = BlogsSerializer(blog_objs, many=True).data  
    else:
        blogs = [] 

    return JsonResponse({"status": True, "blogs": blogs})
