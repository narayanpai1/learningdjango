from django.contrib import admin
from django.urls import path
from main.views import home, menus, nc_detail, current_items
from django.conf.urls import url


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            url('preview', menus, name="preview"),
        ]
        return urls + custom_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='mainpage'),
    path('menus/', menus, name='menus'),
    path('<int:nc_id>/',nc_detail,name='detail'),
    path('admin/currentitems/<int:nc_id>',current_items, name="current_items")

]

