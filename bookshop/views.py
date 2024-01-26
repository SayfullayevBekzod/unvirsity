from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from bookshop.forms import PublisherCreateForm, StoreCreateForm, UserRegisterModelForm, UserLoginForm
from bookshop.models import Publisher, Store

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
    model = Store
    template_name = "bookshop/store_detail.html"
    context_object_name = "store"


class CustomLoginRequiredMixin(LoginRequiredMixin):

    def get_permission_denied_message(self):
        messages.set_level()
        return super().get_permission_denied_message()




class StoreCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Store
    form = StoreCreateForm
    fields = ["name", "books"]
    success_message = 'Store successfully created'
    template_name = "bookshop/store_create.html"


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterModelForm()
        return render(request, "bookshop/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User successfully registered")
            form.save()
            return redirect("bookshop:login")
        else:
            return render(request, "bookshop/register.html", {"form": form})


# class UserLoginView(View):
#     def get(self, request):
#         form = UserLoginForm()
#         return render(request, "bookshop/login.html", {"form": form})

#     def post(self, request):
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 print(request.COOKIES)
#                 messages.success(request, "user successfully logged in")
#                 return redirect("bookshop:home-page")
#             else:
#                 messages.error(request, "Username or password wrong")
#                 return redirect("bookshop:login")

#         else:
#             return render(request, "bookshop/login.html", {"form": form})

def UserLoginView(request):
    if request.method == 'GET':
        form = UserLoginForm
        return render(request, "bookshop/login.html", {"form": form})
    else:
        form = UserLoginForm(request.Post)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.COOKIES)
            messages.success(request, "user successfully logged in")
            return redirect("bookshop:home-page")
        else:
            messages.error(request, "Username or password wrong")
            return redirect("bookshop:login")
    else:
        return render(request, "bookshop/login.html", {"form": form})
    

def UserLogoutView(request):
    if request.method == 'GET':
        return render(request, "bookshop/logout.html")

    else:
        # post(self, request):
        logout(request)
        messages.info(request, "User successfully loged out")
        return redirect("bookshop:home-page")


# class UserLogoutView(View):
#     def get(self, request):
#         return render(request, "bookshop/logout.html")

#     def post(self, request):
#         logout(request)
#         messages.info(request, "User successfully loged out")
#         return redirect("bookshop:home-page")

# fdm7o9wbhvg3zb7akinnu9e6c42yyusu
# fdm7o9wbhvg3zb7akinnu9e6c42yyusu
