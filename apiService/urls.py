from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('files', views.FileViewSet, basename="file")
router.register('folders', views.FolderViewSet, basename="folder")

urlpatterns = [
    path('api/', include(router.urls), name='router-urls'),
    path('api/get_folder_by_id/<int:id>', views.FolderViewSet.as_view({'get':'get_folder_by_id'}), name='get_folder_by_id'),
    path('api/get_files_from_folder/<int:id>', views.FileViewSet.as_view({'get': 'get_files_from_folder'}), name="get_files_from_folder"),
    path('api/get_parent_id/<int:id>', views.FolderViewSet.as_view({'get':'get_parent_id'}), name='get_parent_id')
]
