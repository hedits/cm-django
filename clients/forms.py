from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    """A dummy docstring."""

    class Meta:
        """A dummy docstring."""
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
