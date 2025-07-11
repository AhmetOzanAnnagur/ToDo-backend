from django.contrib import admin
from .models import Task, List
from django.utils.safestring import mark_safe

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "is_done", "user",)
    list_editable = ("is_done", )
    search_fields = ("name", "description")
    # readonly_fields = {"description"}
    list_filter = ("is_done", "lists", )
    
    def selected_lists(self, obj):
        html = "<ul>"
        
        for list in obj.lists.all() :
            html += "<li>" + list.title + "</li>"
             
        html += "</ul>"
        
        return mark_safe(html)

admin.site.register(Task, TaskAdmin)
admin.site.register(List)
