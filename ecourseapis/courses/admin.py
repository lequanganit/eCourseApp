from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from django.db.models import Count
from courses.models import Category, Course, Lesson
from django.urls import path
from django import forms
from ckeditor_uploader.widgets \
    import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','subject','created_date','active']
    search_fields = ['subject']
    list_filter = ['id','subject','created_date']
    readonly_fields = ['image_view']
    def image_view(self, course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='120' />")
    class Media:
        css={
            'all': ('/static/css/styles.css',)
        }
class LessonAdmin(admin.ModelAdmin):
    form=LessonForm
class MyAdminSite(admin.AdminSite):
    site_header = 'Ecourse Online'
    site_title = 'Ecourse Admin Portal'
    index_title = 'Welcome to Ecourse Admin Portal'
    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()
    def stats_view(self, request):
        stats = Category.objects.annotate(count=Count('course')).values('id','name','count')
        return TemplateResponse(request, 'admin/stats.html',{'stats':stats})

admin_site = MyAdminSite(name='ecourseadmin')

admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
