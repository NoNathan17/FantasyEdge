from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.

def notes_view(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.save()
        return redirect('/notes')
    else:
        form = NoteForm()

    return render(request, 'note_form.html', {'form': form})
    

