from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.

@login_required
def notes_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)
    return render(request, 'note_detail.html', {'note': note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
        return redirect('notes')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')

@login_required
def note_edit(request, pk):
    note = Note.objects.get(pk=pk, user=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')  
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form})

    

