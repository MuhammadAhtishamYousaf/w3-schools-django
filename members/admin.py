from django.contrib import admin

from members.models import Member
# Register your models here.

# admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ('first_name', 'last_name', 'created_at', 'slug')
    # prepopulated_fields = {"slug": ("first_name", "last_name")}


admin.site.register(Member, MemberAdmin)
