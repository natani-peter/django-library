from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ['title', ]


@admin.register(models.Reader)
class ReaderAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "date_of_birth", "password1", "password2"),
            },
        ),
    )


admin.site.register(models.AuthorAward)
admin.site.register(models.Author)
admin.site.register(models.BookCopy)
admin.site.register(models.LibrayRecords)
