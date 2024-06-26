from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from .serializers import *

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = FileSerializer

    @action(detail=True, methods=['get'])
    def get_files_from_folder(self, request, id):
        if id > 0:
            folder = models.Folder.objects.get(id=id)
            serializer = self.get_serializer(folder.files, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            files = models.File.objects.filter(parent=None)
            serializer = self.get_serializer(files, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class FolderViewSet(viewsets.ModelViewSet):
    queryset = models.Folder.objects.all()
    serializer_class = FolderSerializer

    @action(detail=True, methods=['get'])
    def get_folder_by_id(self, request, id):
        if id > 0:
            folder = models.Folder.objects.get(id=id)
            serializer = self.get_serializer(folder.folders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            folders = models.Folder.objects.filter(parent=None)
            serializer = self.get_serializer(folders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_parent_id(self, request, id):
        if id > 0:
            folder = models.Folder.objects.get(id=id)
            serializer = self.get_serializer(folder.parent, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_200_OK)
