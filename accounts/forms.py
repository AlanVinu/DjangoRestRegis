# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from pytz import country_names


# # Create your forms here.

# class NewUserForm(UserCreationForm):
# 	STUDENT = 'student'
# 	STAFF = 'staff'
# 	ADMIN = 'admin'
# 	EDITOR = 'editor'
# 	USER_ROLE_OPTIONS = [
#         (STUDENT, 'Student'),
#         (STAFF, 'Staff'),
#         (ADMIN, 'Admin'),
#         (EDITOR, 'Editor'),
#     ]
# 	email = forms.EmailField(required=True)
# 	role = forms.ChoiceField(choices=USER_ROLE_OPTIONS)
# 	country = forms.ChoiceField(choices=country_names.items())
# 	nationality = forms.ChoiceField(choices=country_names.items())
# 	mobile = forms.IntegerField(max_value=20, min_value=3)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "role", "country", "nationality", "mobile", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user