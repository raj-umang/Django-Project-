from django.contrib import admin
from django.urls import path, include
from DjangoTut.views import showlist,greet, hello, home, squares, book_list, find_mode, table_of_squares
from django.conf import settings
from django.conf.urls.static import static

 

urlpatterns = [
  path('admin/',admin.site.urls),
  path('showlist/', showlist),
  path('greet/<str:user>/',greet),
  path('hello/', hello),
  path('', home),
  path('cts/<int:s>/<int:n>', table_of_squares),
  path('chai/', include('chai.urls')),
  path('<int:num1>/<int:num2>/', squares, name='squares'),
  path('books/', book_list, name='book_list'),
  path('fm/<str:numbers>', find_mode, name='find_mode'),

  path("__reload__/", include("django_browser_reload.urls"))
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
