from django.contrib import admin
from django.urls import path
from main.views import home, menus, current, contact_us
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
    path('admin/currentitems/<int:nc_id>',current, name="current_items"),
    path('contact', contact_us, name="contact"),
    path('api', api, name="api"),
    path('menu_api', menu_api)
]

