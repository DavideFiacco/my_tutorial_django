from django.contrib import admin
from .models import Post, MyTofI, MyPriority, MySOinP

admin.site.register(Post)


class MyTofIAdmin(admin.ModelAdmin):
    list_display = ("content",)

class MyPriorityAdmin(admin.ModelAdmin):
    list_display = ("external_id", )

class MySOinPAdmin(admin.ModelAdmin):
    list_display = ("external_id", "priority",)
    filter_horizontal = ( "intervention_type",)


admin.site.register(MyTofI, MyTofIAdmin)
admin.site.register(MyPriority, MyPriorityAdmin)
admin.site.register(MySOinP, MySOinPAdmin)