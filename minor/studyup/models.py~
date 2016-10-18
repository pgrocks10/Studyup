from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	sex_choices=(('M', 'Male'), ('F', 'Female'))
	category_choices=(('S', 'Student'),('T', 'Teacher'),('G', 'Guardian'))
	qual_choices = (('a', 'Secondary'),('b', 'Senior Secondary'),('c', 'Undergraduate'),('d', 'Postgraduate'))
	area_choices = (('CS', 'Computer Science'),('Maths', 'Mathematics'),('Phy', 'Physics'),('Chem','Chemistry'),('Bio', 'Biology'))	
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.PositiveSmallIntegerField()
	sex = models.CharField(max_length=1, choices=sex_choices)
	contact = models.CharField(max_length=10)
	email = models.EmailField(unique=True)
	
	category = models.CharField(max_length=1, choices=category_choices)
	qualification = models.CharField(max_length=1, choices=qual_choices)
	area = models.CharField(max_length=5, choices=area_choices, null=True)	
	current_institution = models.CharField(max_length=30)
	about = models.TextField(null=True)
	
	password = models.CharField(max_length=20)

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    question_image = models.ImageField(blank=True, null=True, upload_to = 'pics/')
    user_id = models.ForeignKey(User)
    time_stamp = models.DateField(auto_now_add = True)
    polls = models.BooleanField() 

class Choice(models.Model):
    question_id = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

class Answer(models.Model):
    question_id = models.ForeignKey(Question)
    user_id = models.ForeignKey(User)
    answer_text = models.CharField(max_length=500)
    answer_image = models.ImageField(blank=True, null=True, upload_to = 'pics/')
    time_stamp = models.DateField(auto_now_add = True)

