from django import forms
from tasks.models import Task, TaskDetail

class TaskForm(forms.Form):
  title = forms.CharField(max_length=250, label="Task Title")
  description = forms.CharField(widget=forms.Textarea, label="Task Description")
  due_date = forms.DateField(widget=forms.SelectDateWidget)
  assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label='Assigned To')

  def __init__(self, *args, **kwargs):
    employees = kwargs.pop("employees", [])
    super().__init__(*args, **kwargs)
    self.fields['assigned_to'].choices = [
      (emp.id, emp.name) for emp in employees
    ]

class StyledFormMixing:
  form_style_1 = "border border-gray-400 w-full px-2 py-1 mb-2"
  form_style_2 = "border border-gray-400 px-2 py-1 mb-2"

  def apply_styled_widgets(self):
    for field_name, field in self.fields.items():
      if isinstance(field.widget, forms.TextInput):
        field.widget.attrs.update({
          'class': self.form_style_1,
          'placeholder': f"Enter {field.label.lower()}"
        })
      elif isinstance(field.widget, forms.Textarea):
        field.widget.attrs.update({
          'class': self.form_style_1,
          'placeholder': f"Enter {field.label.lower()}",
          'rows': 5
        })
      elif isinstance(field.widget, forms.SelectDateWidget):
        field.widget.attrs.update({
          'class': self.form_style_2
        })
      elif isinstance(field.widget, forms.CheckboxSelectMultiple):
        field.widget.attrs.update({
          'class': self.form_style_2
        })

class TaskModelForm(StyledFormMixing, forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'due_date', 'assigned_to']
    widgets = {
      'due_date': forms.SelectDateWidget,
      'assigned_to': forms.CheckboxSelectMultiple
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.apply_styled_widgets()

class TaskDetailModelForm(StyledFormMixing, forms.ModelForm):
  class Meta:
    model = TaskDetail
    fields = ['priority', 'notes']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.apply_styled_widgets()