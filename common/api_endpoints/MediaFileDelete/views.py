from rest_framework.generics import DestroyAPIView
from rest_framework import permissions
from common.models import MediaFile
from common.api_endpoints.MediaFileDelete.serializers import MediaFileDeleteSerializer


class MediaFileDestroyAPIView(DestroyAPIView):
    """
    Delete a media file by ID
    """
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_destroy(self, instance):
        """
        Override to delete the actual file from storage before deleting the record
        """
        if instance.file:
            instance.file.delete(save=False)
        super().perform_destroy(instance)