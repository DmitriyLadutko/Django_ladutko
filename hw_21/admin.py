from django.contrib import admin

from hw_21.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
    fields = ('first_name', 'last_name', 'age', 'profession')
    readonly_fields = ('age', )

