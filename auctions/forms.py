from django import forms
from django.db import models
from .models import Bid, Bidder, Auction



class BidForm(forms.ModelForm):
    bidder=forms.ModelChoiceField(Bidder.objects.all())
    class Meta:
        model = Bid
        fields = '__all__'

class AuctionForm(forms.ModelForm):
    
    class Meta:
        model = Auction
        fields='__all__'


