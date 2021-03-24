from django.contrib import admin
from .models import Todo, Category, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_editable = ('done',)
    list_filter = ('done', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile',)

    def get_location(self, instance):
        return instance.profile.location

    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
