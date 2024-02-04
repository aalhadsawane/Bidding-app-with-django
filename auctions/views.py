from django.shortcuts import render, redirect
from django import forms
import json
import paho.mqtt.client as mqtt
import datetime
from .forms import BidForm, AuctionForm
from .models import Bidder,Bid,Poster,Auction
from . import mqtt_pub as pub
from . import mqtt_sub as sub


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
        #print(str(request.POST))
        # print(json.loads(request.body))
        # TODO : change everything from querydict to json remove all froms only Auction.create(json data)
        auctionform=AuctionForm(request.POST)
        if auctionform.is_valid():
            auctionform.save()
            pub.pub_msg(topic=str(request.POST.get('title',"")), content=str(request.POST.get('reqs')))
            sub.sub_topic(topic=str(request.POST.get('title',"")))
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
