# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from .models import Project

from .serializers import ProjectSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
