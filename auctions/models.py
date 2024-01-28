from django.db import models
import datetime

# Create your models here.
class Poster(models.Model):
    username = models.CharField(max_length = 100)
    def __str__(self):
        return self.username

class Bidder(models.Model):
    username = models.CharField(max_length=100)
    specs = models.TextField(null=True, blank=True)
    def __str__(self): return self.username


class Auction(models.Model):
    
    title = models.CharField(blank=True, default="Job name", max_length=150)
    end_time= models.DateTimeField(default=datetime.datetime(2024, 12, 12))
    poster= models.ForeignKey(Poster, on_delete=models.CASCADE)
    reqs= models.TextField(null=True, blank=True)
    bids=[]

    def is_valid(self, specs=None):
        # check if specs == job.req
        if datetime.now() < self.end_time:
            print("bid made within auction time")
            return True
        
    def __str__(self):
        a="Auction for '"
        b=self.title 
        return a+b+"'"

    def get_highest_bid(self):
        max = 0
        max_bid = None
        for bid in self.bids:
            print(bid)
            if bid.bid_amt >= max:
                max = bid.bid_amt
                max_bid = bid
        return max_bid
    
    def get_highest_bid_amt(self):
        max = 0
        for bid in self.bids:
            print(bid)
            if bid.bid_amt >= max:
                max = bid.bid_amt
        return str(max)
    

class Bid(models.Model):
    id=models.AutoField(primary_key=True)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    bid_amt = models.IntegerField()
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.bidder)
