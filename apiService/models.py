from django.db import models
import os

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="")
    parent = models.ForeignKey('Folder', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def file_extension(self):
        return os.path.splitext(self.file.name)[1]

class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def files(self):
        return File.objects.filter(parent=self)

    @property
    def folders(self):
        return Folder.objects.filter(parent=self)
