from django.contrib import admin
from django.contrib.admin import register
from SessionManager.models import *

# Register your models here.
@register(Session)
class AdminSession(admin.ModelAdmin):
    list_display = ["session_time", "members_count", "ME"]
    list_filter = ["ME"]

@register(BookSession)
class AdminBookedSession(admin.ModelAdmin):
    list_display = ["full_Name", "user", "slot", "slot_date", "created_date"]
    search_fields = ['user']
    list_filter = ('slot', 'created_date', 'slot_date')
    fields = ['slot', 'slot_date']

    def full_Name(self, obj):
        return obj.user.get_full_name()

    def save_model(self, request, obj, form, change):
        print("Entering save_model")
        obj.user = request.user
        print("userdetails : ", obj.user)

        if BookSession.objects.filter(slot=obj.slot, user=request.user, slot_date=obj.slot_date).exists():
            obj.save(is_duplicate=True)
        else:
            super(AdminBookedSession, self).save_model(request, obj, form, change)



admin.site.name = "Cambridge University GYM"
admin.site.site_title = "Cambridge University GYM"
admin.site.site_header = "Cambridge University GYM"