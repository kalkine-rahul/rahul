from django.shortcuts import render
from django.http import JsonResponse
    
    
from .models import Report
# from .serializers import BlogsSerializer

def fundsReportAu(request):
    report = Report.objects.first() 
    context = {
        'image_url': report.image.url if report and report.image else None,
        'now': report.hero_updated_at if report else None,
    }
    return render(request, 'funds-report-au.html', context)