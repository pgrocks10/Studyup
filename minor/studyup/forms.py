from .models import User, Question, Choice, Answer
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):   
   #area_choices = (('CS', 'Computer Science'),('Maths', 'Mathematics'),('Phy', 'Physics'),('Chem','Chemistry'),('Bio', 'Biology'))	
   #area = forms.MultipleChoiceField(label=('Areas of Interest'), choices = area_choices, widget = forms.CheckboxSelectMultiple) 
   class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'sex', 'contact', 'email', 'category', 'qualification', 'current_institution', 'about', 'password']

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=20)
	
	def clean_email(self):
		try:
			user = User.objects.get(email__iexact=self.cleaned_data['email']) 
		except User.DoesNotExist:
			raise forms.ValidationError("User does not exist!")
	
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
		    field.widget.attrs['class'] = 'form-control'
