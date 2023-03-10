from django.db import models
from accounts.models import Users

# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='students')
    admission_number = models.CharField(max_length=1000)
    roll_number = models.CharField(max_length=100)

    class Meta:
        unique_together = ['user', 'admission_number']
        ordering = ['admission_number']

    def __str__(self) -> str:
        return f"Student Username: {self.user.username}"

class Admin(models.Model):
    user = models.ForeignKey(to=Users, related_name='admins', on_delete=models.CASCADE)
    department = models.CharField(max_length=1000)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Admin Username: {self.user.username}"
    
class Editor(models.Model):
    user = models.ForeignKey(to=Users, related_name='editors', on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Editor Username: {self.user.username}"
    
class Staff(models.Model):
    user = models.ForeignKey(to=Users, related_name='staffs', on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Staff Username: {self.user.username}"
