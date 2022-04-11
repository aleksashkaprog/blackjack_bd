import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from django.views.generic import TemplateView
import qrcode
from blackjack.models import Object
import sqlite3
from blackjack.forms import BlackJackForm


def bd_list(request, *args, **kwargs):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("""select number, name, code, inv, price, count, summ, note from blackjack_object""")
    tables = cursor.fetchall()
    my_id = conn.cursor()
    my_id.execute("""select id from blackjack_object""")
    qr = conn.cursor()
    qr.execute("""select id from blackjack_object""")
    return render(request, 'blackjack/object_table.html', {'tables': tables, 'my_id': my_id, 'qr': qr})


class QRView(View):
    def get(self, request, profile_id):
        object = Object.objects.get(id=profile_id)
        blackjackform = BlackJackForm(instance=object)
        return render(request, 'blackjack/qrcode.html',
                      context={'blackjackform': blackjackform, 'profile_id': profile_id})

    def post(self, request, profile_id):
        object = Object.objects.get(id=profile_id)
        blackjackform = BlackJackForm(request.POST, instance=object)

        return render(request, 'blackjack/qrcode.html',
                      context={'blackjackform': blackjackform, 'profile_id': profile_id})



class BJFormView(View):
    def get(self, request):
        blackjackform = BlackJackForm()
        return render(request, 'blackjack/create.html', context={'blackjackform': blackjackform})


    def post(self, request):
        blackjackform = BlackJackForm(request.POST)
        if blackjackform.is_valid():
            Object.objects.create(**blackjackform.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'blackjack/create.html', context={'blackjackform': blackjackform})


class BJEditFormView(View):
    def get(self, request, profile_id):
        object = Object.objects.get(id=profile_id)
        blackjackform = BlackJackForm(instance=object)
        return render(request, 'blackjack/edit.html', context={'blackjackform': blackjackform, 'profile_id': profile_id})

    def post(self, request, profile_id):
        object = Object.objects.get(id=profile_id)
        blackjackform = BlackJackForm(request.POST, instance=object)

        if blackjackform.is_valid():
            object.save()
            return HttpResponseRedirect('/')
        return render(request, 'blackjack/edit.html',
                      context={'blackjackform': blackjackform, 'profile_id': profile_id})




