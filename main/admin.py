from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# to add nc number for each admin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(filter)


@admin.register(nc)
class ncAdmin(admin.ModelAdmin):
    list_display = ['name','phone_no']

    def phone_no(self,obj):
        return obj.phno


@admin.register(dishes)
class dishesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','nc__name']
    list_filter = ['nc__name']
    search_fields = ['name']

    def get_queryset(self, request):
        qs = super(dishesAdmin, self).get_queryset(request)
        if request.user.profile.ncnumber == 0:
            return qs
        else:
            return qs.filter(nc__id=request.user.profile.ncnumber)

    def nc__name(self, obj):
        return obj.nc.name
