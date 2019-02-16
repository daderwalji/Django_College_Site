from django import forms
from .models import Result

class result_form(forms.ModelForm):
    semester = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    first = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    last = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    registration_id = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    subject_1 = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    sub1 = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)
    subject_2 = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    sub2 = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)
    subject_3 = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    sub3 = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)
    subject_4 = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    sub4 = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)
    subject_5 = forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
    sub5 = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)

    class Meta():
        model = Result
        fields = ['semester','first','last','registration_id','subject_1','sub1','subject_2','sub2','subject_3','sub3','subject_4','sub4','subject_5','sub5']