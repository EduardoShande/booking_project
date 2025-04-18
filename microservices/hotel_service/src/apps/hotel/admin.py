from django.contrib import admin
from .models import Hotel, RoomType, Service, Room

# Register your models here.

admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Service)
admin.site.register(Room)


# Using @admin.register Decorator

# You can also use the @admin.register decorator to register your models. This is particularly useful when you want to customize the admin interface for your models.

# Example:
# from django.contrib import admin
# from .models import YourModel

# @admin.register(YourModel)
# class YourModelAdmin(admin.ModelAdmin):
# pass
