from rest_framework import generics, exceptions
from mainapp.serializers import StudentSerializer, AdminSerializer, EditorSerializer, StaffSerializer
from mainapp.models import Student, Admin, Editor, Staff
# Create your views here.

class StudentUserView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_permissions(self):
        if self.request.user.is_anonymous:
            raise exceptions.AuthenticationFailed(detail="Anonymous User")
        if self.request.user.role != "student":
            raise exceptions.PermissionDenied(detail="Only students can view")
        return super().get_permissions()

class AdminUserView(generics.ListCreateAPIView):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()

    def get_permissions(self):
        if self.request.user.is_anonymous:
            raise exceptions.AuthenticationFailed(detail="Anonymous User")
        if self.request.user.role != "admin":
            raise exceptions.PermissionDenied(detail="Only admins can view")
        return super().get_permissions()
    

class EditorUserView(generics.ListCreateAPIView):
    serializer_class = EditorSerializer
    queryset = Editor.objects.all()

    def get_permissions(self):
        if self.request.user.is_anonymous:
            raise exceptions.AuthenticationFailed(detail="Anonymous User")
        if self.request.user.role != "editor":
            raise exceptions.PermissionDenied(detail="Only editors can view")
        return super().get_permissions()

class StaffUserView(generics.ListCreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

    def get_permissions(self):
        if self.request.user.is_anonymous:
            raise exceptions.AuthenticationFailed(detail="Anonymous User")
        if self.request.user.role != "staff":
            raise exceptions.PermissionDenied(detail="Only staff can view")
        return super().get_permissions()
