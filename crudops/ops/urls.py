from django.urls import path, include
from rest_framework import routers
from ops import views

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSets)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]