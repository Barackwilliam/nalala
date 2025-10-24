# lodge_app/admin.py (For admin panel management)
from django.contrib import admin
from .models import Lodge, Room, Guest, Payment, Staff
from .forms import LodgeForm, RoomForm
from django.utils.safestring import mark_safe  # Add this import



class LodgeAdmin(admin.ModelAdmin):
    form = LodgeForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'logo':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'
    list_display = ('name', 'phone', 'location', 'email', 'image_preview')

admin.site.register(Lodge, LodgeAdmin)





class RoomAdmin(admin.ModelAdmin):
    form = RoomForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'
    list_display = ('lodge', 'name', 'room_type', 'image_preview')

admin.site.register(Room, RoomAdmin)
admin.site.register(Guest)
admin.site.register(Payment)
admin.site.register(Staff)