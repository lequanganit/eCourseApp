from courses.models import Course, Category, Lesson
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'description', 'image', 'created_date','category_id']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image']=instance.image.url
        return data
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject',  'created_date']
