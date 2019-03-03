from django.contrib import admin
from django.urls import path
from main.views import home, menus, nc_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='mainpage'),
    path('menus/', menus, name='menus'),
    path('<int:nc_id>/',nc_detail,name='detail')
]
