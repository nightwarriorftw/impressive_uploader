from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from upload.views import (
    HomeView,
    TaskView
)

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('task/<str:task_id>/', TaskView.as_view(), name='task'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
