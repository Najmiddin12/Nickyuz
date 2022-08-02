from django.shortcuts import render, redirect
from .forms import *
from django.views import View
from .models import *
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.core.paginator import Paginator


class SignUpModelView(View):
    template_name = "auto/Signup.html"

    def get(self, request):
        form = SignUpModelForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        print(request.POST)
        form = SignUpModelForm(data=request.POST)
        if form.is_valid():
            signup = form.save()
            return redirect(to="autosale-sign")

        context = {"form": form}
        return render(request, self.template_name, context)


class SignInModelView(View):
    template_name = 'auto/Signin.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        who = request.POST.get('who')
        password = request.POST.get('password')
        user = SignUp.objects.filter(username=username, who=who, password=password).first()

        if not user:
            return render(request, self.template_name)
        elif who == "seller":
            return redirect(to="create-auto")
        elif who == "buyer":
            return redirect(to="buyer-kabinet")
        return redirect(to='autosale-signup')


class SigninModelView(View):
    template_name = 'auto/Signin2.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        who = request.POST.get('who')
        password = request.POST.get('password')
        user = SignUp.objects.filter(username=username, who=who, password=password).first()

        if not user:
            return render(request, self.template_name)
        elif who == "seller":
            return redirect(to='create-auto')
        elif who == "buyer":
            return redirect(to="buyer-kabinet")
        return redirect(to='autosale-signup')

class CreateAutoModelView(View):
    template_name = "auto/CreateAuto.html"

    def get(self, request):
        form = CreateAutoModelForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        print(request.POST)
        form = CreateAutoModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            createauto = form.save()
            return redirect(to="seller-kabinet", pk=createauto.pk)

        context = {"form": form}
        return render(request, self.template_name, context)



def home(request):
    return render(request, 'auto/home.html')


def seller_detail(request, pk):
    seller = CreateAuto.objects.get(pk=pk)

    return render(request, "auto/Seller_kabinet.html", {"seller": seller})

def seller_kabinet(request, pk):
    auto = CreateAuto.objects.get(pk=pk)

    return render(request, 'auto/Seller_kabinet.html', {"auto": auto})


def buyer_kabinet(request):
    search = request.GET.get("search")

    if search is None:
        auto = CreateAuto.objects.all()
    else:
        auto = CreateAuto.objects.filter(Q(brand__contains=search) | Q(model__contains=search))



    return render(request, 'auto/Buyer_kabinet.html', {"auto": auto, "search": search})

def buyer_detail(request, pk):
    auto = CreateAuto.objects.get(pk=pk)

    return render(request, "auto/Buyer_detail.html", {"auto": auto})

def autoday_gentra(request):
    return render(request, "auto/gentra.html")

def autoday_nexia(request):
    return render(request, "auto/nexia.html")

def autoday_malibu(request):
    return render(request, "auto/malibu.html")

def autoday_equinox(request):
    return render(request, "auto/equinox.html")

def autoday_trailblazer(request):
    return render(request, "auto/trailblazer.html")

def autoday_traverse(request):
    return render(request, "auto/traverse.html")

def nexia3_vs_gentra(request):
    return render(request, "auto/nexia3_vs_gentra.html")

