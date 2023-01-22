from django.shortcuts import render
from django.http import HttpResponse
from bankaccount.models import Account


# def home_page(request):
#     return HttpResponse("Welcome to TODAY'S Project")


def real_home_page(request):
    accounts = Account.objects.all()
    context = {
        "accounts": accounts
    }
    return render(request, "bankaccount/home.html", context)