from django.shortcuts import render, redirect
from ops.models import Notes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets
from ops.serializers import NotesSerializer

# Create your views here.
class NoteViewSets(viewsets.ModelViewSet):
    queryset = Notes.objects.all().order_by('title')
    serializer_class = NotesSerializer
def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')
@login_required
def dashboard(request):
    
    
        current_user = request.user
        print (current_user.id)
        notes = Notes.objects.filter(userid=current_user.id)
        context={
            'notes': notes,
            'user_id': current_user.id,
        }
        return render(request, "dashboard.html", context)
    
    
    

def postsignin(request):
    name = request.POST.get('name')
    password = request.POST.get('pass')
    user = authenticate(username=name, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect(dashboard)
    else:
        return redirect(signin)
    
def signup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('pass')

    user = User.objects.create_user(name, email, password)
    user.save()
    return redirect(signin)

def savingNotes(request):
    title = request.POST.get('title')
    text = request.POST.get('note')
    userid = request.POST.get('userid')
    notes = Notes(title=title, text=text, userid=userid)
    notes.save()

    return redirect(dashboard) 
def deleteNote(request, id):
    note = Notes.objects.get(id=id)
    note.delete()
    return redirect(dashboard)
def editNote(request, id):
    note = Notes.objects.get(id=id)
    title = note.title
    text = note.text

    context={
        'id': id,
        'title': title,
        'text': text,

    }
    return render(request, 'editNote.html', context)
def updateNote(request, id):
    note = Notes.objects.get(id=id)
    note.title = request.POST.get('title')
    note.text = request.POST.get('note')
    
    note.save()
    return redirect(dashboard)
def logout_view(request):
    logout(request)
    return redirect(index)