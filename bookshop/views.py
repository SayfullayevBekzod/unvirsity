from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from bookshop.forms import PublisherCreateForm, StoreCreateForm, AuthorCreateForm
from bookshop.models import Publisher, Store, Author

"""
function based views 
class based views 
    View
    generic
"""


class HomePageView(View):
    def get(self, request):
        return render(request, "bookshop/home.html")


class PublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all().order_by("-created_at")[:5]
        form = PublisherCreateForm()
        context = {
            "publishers": publishers,
            "form": form
        }
        return render(request, "bookshop/publisher.html", context=context)

    def post(self, request):
        publishers = Publisher.objects.all().order_by("-created_at")[:5]
        form = PublisherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookshop:publisher-page")
        else:
            return render(request, "bookshop/publisher.html", context={
                "publishers": publishers,
                "form": form
            })

class StoreListView(ListView):
    model = Store
    context_object_name = "stores"
    template_name = "bookshop/store_list.html"

class StoreDetialView(DetailView):
    model= Store
    template_name = "bookshop/store_detail.html"
    context_object_name = "store"

class StoreCreateView(CreateView):
    model = Store
    form = StoreCreateForm
    fields = ["name", "books"]
    template_name = "bookshop/store_create.html"


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "bookshop/authore_list.html"

class AuthorDetialView(DetailView):
    model= Author
    template_name = "bookshop/author_detail.html"
    context_object_name = "author"

class AuthorCreateView(CreateView):
    model = Author
    form = StoreCreateForm
    fields = ["age", "address"]
    template_name = "bookshop/author_create.html"

    def post(self, request):
        authors = Author.objects.all().order_by("-created_at")[:5]
        form = AuthorCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookshop:author-page")
        else:
            return render(request, "bookshop/publisher.html", context={
                "authors": authors,
                "form": form
            })