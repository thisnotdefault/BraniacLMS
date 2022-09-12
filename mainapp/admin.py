from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 5
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]
    search_fields = ["title", "description"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "get_courses"]
    list_select_related = True

    def get_courses(self, obj):
        return ", ".join((i.name for i in obj.course.all()))

    get_courses.short_description = _("Courses")
