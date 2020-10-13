from django.shortcuts import render

from rest_framework import viewsets, authentication, permissions

from .models import Sprint
from .serializers import SprintSerializer

# Create your views here.

class DefaultMixin(object):
    """Default settings for view authentication, permission, filtering, and pagination"""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param= 'page_size'
    max_paginate_by = 100



class SprintViewSet(DefaultMixin,viewsets.ModelViewSet):
    """API endpoints for listing and creating sprints"""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer

