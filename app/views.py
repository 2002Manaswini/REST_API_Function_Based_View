from django.shortcuts import render
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def school_json_data(request):
    SOD=School.objects.all()
    JSOD=SchoolModelSerializer(SOD,many=True)
    JSON_data=JSOD.data
    return Response(JSON_data)
