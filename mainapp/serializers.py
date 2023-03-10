from rest_framework import serializers
from mainapp.models import Student, Admin, Editor, Staff

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'