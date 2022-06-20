from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
    inlines = [ProfileInline]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
