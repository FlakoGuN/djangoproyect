from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Nueva Tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="hacer en la tarea")

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)