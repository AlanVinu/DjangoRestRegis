from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentUserView.as_view(), name='student-view'),
    path('admin/', views.AdminUserView.as_view(), name='admin-view'),
    path('editor/', views.EditorUserView.as_view(), name='editor-view'),
    path('staff/', views.StaffUserView.as_view(), name='staff-view'),
]