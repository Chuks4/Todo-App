from .models import TodoItem
from django.forms import ModelForm

class CreateTask(ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description',]
        
    def __init__(self, *args, **kwargs):
        super(CreateTask, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'})