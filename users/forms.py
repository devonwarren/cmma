from django.forms import ModelForm
from training_log.models import Entry
from django.forms.extras.widgets import SelectDateWidget

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['date', 'hours', 'description']
