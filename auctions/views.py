from django.shortcuts import render, redirect
from django import forms
import datetime
from .forms import BidForm, AuctionForm
from .models import Bidder,Bid,Poster,Auction

# Create your views here.
def home(request):
    auctions = Auction.objects.all()
    for auction in auctions:
        auction.bids = auction.bid_set.all()
    context = {'auctions':auctions}
    return render(request,'auctions/list.html', context)

def create_job(request):

    auctionform=AuctionForm()

    if request.method == 'POST':

        auctionform=AuctionForm(request.POST)
        if auctionform.is_valid():
            auctionform.save()

            return redirect('/')
        else: 

            print(auctionform.error)

    context = {'form': auctionform}
    return render(request, 'auctions/create_job.html', context)


def make_bid(request):

    form = BidForm()

    if request.method == 'POST':

        form=BidForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('home')
        
        else: print(form.errors)

    context = {'form': form}
    return render(request, 'auctions/make_bid.html', context)
