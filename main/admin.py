from django.contrib import admin
from .models import Category,News,Comment,Contact,Teacher,Student

# Register your models here.
class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time')
admin.site.register(News,AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('news','email','comment','status')
admin.site.register(Comment,AdminComment) 

class AdminContact(admin.ModelAdmin):
    list_display=('full_name','email','phone','title','full_text')
admin.site.register(Contact,AdminContact) 

class AdminTeacher(admin.ModelAdmin):
    list_display = ('full_name','image','pthone_number','bio')
admin.site.register(Teacher,AdminTeacher)

class AdminStudent(admin.ModelAdmin):
    list_display = ('full_name','image','pthone_number','bio')
admin.site.register(Student,AdminStudent)
