
from django.contrib import admin
from django.urls import path
from P7.views import reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',reg),
]
