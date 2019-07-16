from django import forms
from . models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'estimated_time', 'worked_time']
        labels: { 'title': 'Título', 'description': 'Ddescripción', 'estimated_time': 'Tiempo estimado en horas', 'worked_time': 'Tiempo trabajado en horas'}

class AddWorkedTimeForm(forms.Form):
    task_id = forms.IntegerField()
    worked_time = forms.FloatField()