from django.contrib import admin
from .models import Member
from .models import Student

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "joined_date")
class StudentAdmin(admin.ModelAdmin):
    list_display = ("adı", "soyadı", "yurt", "sınıf", "seviye")
admin.site.register(Member, MemberAdmin)
admin.site.register(Student, StudentAdmin)
