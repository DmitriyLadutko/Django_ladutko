from django.contrib import admin

from cw_22.models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'group', 'contact_info', 'diary',)


@admin.register(Group)
class StudentGroup(admin.ModelAdmin):
    list_display = ('serial_number_group', 'start_date', 'finish_date')


@admin.register(ContactInfo)
class StudentContactInfo(admin.ModelAdmin):
    list_display = ('phone', 'address')


@admin.register(Diary)
class StudentDiary(admin.ModelAdmin):
    list_display = ('average_score',)


@admin.register(Hobby)
class StudentHobby(admin.ModelAdmin):
    list_display = ('name_of_hobby',)


@admin.register(Book)
class StudentBook(admin.ModelAdmin):
    list_display = ('name', 'number_of_pages')
