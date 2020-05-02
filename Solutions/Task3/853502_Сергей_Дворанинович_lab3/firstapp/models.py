from django.db import models
from django import forms
from django.views.generic import ListView
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from django.contrib.auth.models import User


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"myfield"}))
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()



class New_User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='users/', blank=True)

class New_User_Comment(models.Model):
    user = models.ForeignKey(New_User, on_delete = models.CASCADE, blank=True)
    time = models.CharField(max_length=30)
    text = models.CharField(max_length=300)



class New_Archi(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='archi/', blank=True)

class New_Style(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to='style/', blank=True)

class New_Building(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    archi = models.ForeignKey(New_Archi, on_delete = models.CASCADE, blank=True)
    style = models.ForeignKey(New_Style, on_delete = models.CASCADE, blank=True)
    text = models.CharField(max_length=2000)

class new_Building_photo(models.Model):
    building = models.ForeignKey(New_Building, on_delete = models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='buildings/', blank=True)

class Test_User_Info(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='users/', blank=True)

class Test_User_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    building = models.ForeignKey(New_Building, on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to='comment_photo/', blank=True)

class My_New_User_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    building = models.ForeignKey(New_Building, on_delete=models.CASCADE, blank=True)
    text = models.TextField(max_length=2000)
    is_edited = models.BooleanField()
    time = models.DateTimeField()
    photo = models.ImageField(upload_to='comment_photo/', blank=True)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea,
                              required = True,
                              help_text = "Введите комментарий")

    def clean_renewal_date(self):
        data = self.cleaned_data['comment']

        if data == "оскорбление":
            raise ValidationError(_('Invalid date - unacceptable text'))

        return data

class EditCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea,
                              required = True,
                              help_text = "Введите комментарий")

    def clean_renewal_date(self):
        data = self.cleaned_data['comment']

        if data != " ":
            raise ValidationError(_('Invalid date - unacceptable text'))

        return data









# Create your models here.


class Building(models.Model):
    name = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    archi_name = models.CharField(max_length=20)
    archi_id = models.CharField(max_length=20)
    style = models.CharField(max_length=20)
class Archi(models.Model):
    name = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    photo = models.ImageField()
class UserProfile(models.Model):
  profile_img = models.ImageField(upload_to='images/', blank=True, null=True)
  profile_text = models.TextField()
  profile_title = models.CharField(max_length=300)
class ProfileForm(forms.Form):
  class Meta:
    model = UserProfile
    fields = ['profile_img', 'profile_title']
class Test(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='products/', blank=True)
class test1(models.Model):
    user = models.ForeignKey(New_User, on_delete = models.CASCADE)
    time = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='users/', blank=True)
class User_Comment(models.Model):
    user_id = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
class Building_photo(models.Model):
    building_id = models.CharField(max_length=20)
    photo = models.ImageField()
class New_User_Building_Comment(models.Model):
    user = models.ForeignKey(New_User, on_delete = models.CASCADE, blank=True)
    user = models.ForeignKey(New_Building, on_delete=models.CASCADE, blank=True)
    time = models.CharField(max_length=30)
    text = models.CharField(max_length=300)

class BuildingForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    date = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    archi_name = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    archi_id = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
