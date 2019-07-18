from django import forms
from . models import Task

class TaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    estimated_time = forms.IntegerField()
    worked_time = forms.FloatField()
    
class AddWorkedTimeForm(forms.Form):
    task_id = forms.IntegerField()
    worked_time = forms.FloatField()