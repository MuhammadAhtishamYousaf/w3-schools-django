from django.contrib import admin

from members.models import Member
# Register your models here.

# admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at')


admin.site.register(Member, MemberAdmin)
