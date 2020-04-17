from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import DetailView,ListView,CreateView, DeleteView, UpdateView
from .models import Subject,Notes
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context ={
        'subs': Subject.objects.all()
    }
    return render(request, 'home/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Subject
    fields=['name', 'desc']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    model=Subject
    tmeplate_name='home/home.html'
    context_object_name = 'subs'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Subject

def addnotes(request, pk):
    sub=Subject.objects.get(pk=pk)
    title=request.POST['title']
    notes=request.POST['note']
    additional=request.POST['additional']
    sub.notes_set.create(text=notes, subject=sub.name, author=sub.author, title=title, additional_info=additional)
    sub.save()
    redirectpath= "/"
    return HttpResponseRedirect(redirectpath)

class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Notes
    success_url='/'
    def test_func(self):
        note=self.get_object()
        if(self.request.user==note.author):
            return True
        return False

class SubjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Subject
    success_url='/'
    def test_func(self):
        sub=self.get_object()
        if(self.request.user==sub.author):
            return True
        return False
