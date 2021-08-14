from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm


# Create your views here.
@login_required
def person_list(request):
    """A dummy docstring."""
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def person_new(request):
    """A dummy docstring."""
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def person_update(request, pk):
    """A dummy docstring."""
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None,
                      request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def person_delete(request, pk):
    """A dummy docstring."""
    person = get_object_or_404(Person, pk=pk)
    # form = PersonForm(request.POST or None,
    #                   request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})
