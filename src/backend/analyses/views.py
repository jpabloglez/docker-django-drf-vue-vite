from django.shortcuts import render

# Create your views here.

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, JsonResponse

from analyses.models import Analyses
from analyses.serializers import AnalysesSerializer

"""
import sys
import os.path as op
sys.path.insert(0, op.dirname(op.dirname(op.abspath(__file__))))
from custom_logger import BasicCustomLogger
logger = BasicCustomLogger()

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
"""
# @c_login_required() # This decorator is used to check if the user is logged in
# @csrf_protect # This is to protect the view from cross-site request forgery

# @api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])


from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


################################

@csrf_exempt
def analyses(request):
    '''
    List all analyses operations
    '''
    if(request.method == 'GET'):
        analyses = Analyses.objects.all()
        serializer = AnalysesSerializer(analyses, many=True)
        # logger.log_info(f"JSON RESPONSE: {serializer.data}")
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = AnalysesSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        raise Http404("Method not allowed")


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


class AnalysesView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def analyses_list(self, request):
        # content = {}
        analyses = Analyses.objects.all()
        serializer = AnalysesSerializer(analyses, many=True)
        # logger.log_info(f"JSON RESPONSE: {serializer.data}")

        content = {
           'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }

        print("CONTENT: ", content)
        return JsonResponse(serializer.data, safe=False)
