from django.shortcuts import render

# Create your views here.

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from analyses.models import Analyses
from analyses.serializers import AnalysesSerializer


@csrf_exempt
def analyses(request):
    '''
    List all analyses operations
    '''
    if(request.method == 'GET'):
        analyses = Analyses.objects.all()
        serializer = AnalysesSerializer(analyses, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = AnalysesSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def analyses_detail(request, pk):
    """
    List all analyses elements
    """
    try:
        analysis = Analyses.objects.get(pk=pk) # get analysis with this id
    except:
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = AnalysesSerializer(analysis, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        analysis.delete() 
        return HttpResponse(status=204) 
