
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biblioteca/', include('biblioteca.urls')),
    path('', include('biblioteca.urls')),  

]
