
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views import View
from book.forms import AllbooksModelForm
from book.models import Allbooks
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from student.models import BorrowedBook



class CreateAllbooksView(View):

    def get(self, request):
        form = AllbooksModelForm()
        return render(request, 'book/allbooks/create.html', {'form': form})

    def post(self, request):
        form =AllbooksModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("object added")

        return render(request, 'book/allbooks/create.html', {'form': form})


class CreateAllbooksGenericView(CreateView):
    form_class = AllbooksModelForm
    template_name = 'book/allbooks/create.html'
    success_url = '../allbooks'


class AllbooksListGenericView(ListView):
    model = Allbooks
    template_name = 'book/allbooks/index.html'
    context_object_name = 'allbooks'

    #  to display some

    # def queryset(self):
    #     return Categories.objects.filter(id__gt=7)


class AllbooksDetailGenericView(DetailView):
    model = Allbooks
    template_name = 'book/allbooks/show.html'


class UpdateAllbooksGenericView(UpdateView):
    model = Allbooks
    form_class = AllbooksModelForm
    template_name = 'book/allbooks/edit.html'
    success_url = '../allbooks'


class DeleteAllbooksGenericView(DeleteView):
    model = Allbooks
    template_name = 'book/allbooks/delete.html'
    success_url = '../allbooks'


def welcome(request):
    return render(request, 'book/welcome.html')


def view(request):
    all_borrowed_books = BorrowedBook.objects.all()
    return render(request, 'book/allbooks/borrowedbooks.html', {'all_borrowed_books': all_borrowed_books})
