from rest_framework import serializers

from . import models

class FileSerializer(serializers.HyperlinkedModelSerializer):
    parent = serializers.HyperlinkedRelatedField(view_name='folder-detail', queryset=models.Folder.objects.all())
    file_extension = serializers.SerializerMethodField()
    class Meta:
        model = models.File
        fields = ['url', 'id', 'name', 'file', 'parent', 'file_extension']
    def get_file_extension(self, obj):
        return obj.file_extension

class FolderSerializer(serializers.HyperlinkedModelSerializer):
    files = serializers.SerializerMethodField()
    folders = serializers.SerializerMethodField()
    parent = serializers.HyperlinkedRelatedField(view_name='folder-detail', queryset=models.Folder.objects.all(), allow_null=True, required=False)

    class Meta:
        model = models.Folder
        fields = ['url', 'id', 'name', 'parent', 'files', 'folders']

    def get_files(self, obj):
        files = obj.files
        return FileSerializer(files, many=True, context=self.context).data

    def get_folders(self, obj):
        folders = obj.folders
        return FolderSerializer(folders, many=True, context=self.context).data
