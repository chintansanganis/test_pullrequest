"""
Admin registration for homepage_content Addon
"""
from django.contrib import admin
from .models import Reviews, HomepageCourses, ComptiaCourses


# @admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'rating', 'is_active']

    MAX_OBJECTS = 10

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

@admin.register(HomepageCourses)
class HomepageCoursesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']
    MAX_OBJECTS = 4

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


@admin.register(ComptiaCourses)
class ComptiaCoursesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']
    MAX_OBJECTS = 40

    def has_add_permission(self, request):
        if self.model.objects.count() >= self.MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
