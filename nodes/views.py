import json
from django.views.generic import View
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from restapi.serializers import DataSerializer, NodeSerializer
from restapi.models import Data, Node
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.
class Map(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'node1.html')
