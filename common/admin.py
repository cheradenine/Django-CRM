from django.contrib import admin
from common.models import User, Address, Comment, Comment_Files
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	search_fields = ['username', 'email']

admin.site.register(User, UserAdmin)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(Comment_Files)
