from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, ProductReview


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class UpdateUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name',]


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ['review', 'rating']
        exclude = ['user', 'product']