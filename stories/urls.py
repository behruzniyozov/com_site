
from rest_framework.routers import DefaultRouter
from .views import StoryAPIView

router = DefaultRouter()
router.register(r'stories', StoryAPIView, basename='story')

urlpatterns = router.urls
