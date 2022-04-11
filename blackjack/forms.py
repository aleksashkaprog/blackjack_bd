from django import forms
from blackjack.models import Object


class BlackJackForm(forms.ModelForm):

    class Meta:
        model = Object
        fields = '__all__'