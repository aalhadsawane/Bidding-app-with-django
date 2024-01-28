from django.contrib import admin
from .models import Bidder,Bid,Poster,Auction
# Register your models here.
admin.site.register(Bidder)
admin.site.register(Bid)
admin.site.register(Poster)
admin.site.register(Auction)
