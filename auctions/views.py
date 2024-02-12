from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from decimal import Decimal

from .models import User,Listing,Category,Bid


def index(request):
    listing=Listing.objects.all()
    return render(request, "auctions/index.html",{
        'listing':listing,
        'empty':'The shop is currently empty!! We are sorry for any inconvinience.'
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_list(request):
    if request.method == 'GET':
        return render(request,'auctions/create.html',{
            'category':Category.objects.all()
        })
    else:
        title = request.POST['title']
        description = request.POST['description']
        starting_bid = request.POST['starting_bid']
        image = request.POST['image']


        listing=Listing(title=title,description=description,starting_bid=starting_bid,image=image)
        listing.save()
        return HttpResponseRedirect(reverse('index'))
    
# Displaying categories present.
def category(request):
    category_present=Category.objects.all()
    contest={
        'category':category_present,
        'message':"The category is still empty!!"
    }
    return render(request, 'auctions/category.html', contest)

# Displying items in each category

def items(request, each):
    item_in_each_category=Listing.objects.filter(category=each)
    return render(request, 'auctions/items.html',{
        'items':item_in_each_category,
        'message':'There is no item here'
    })

def detailed(request, item):
    item=Listing.objects.get(id=item)
    user=request.user
    present=user in item.wachlist.all()
    return render(request,'auctions/detailed.html',{
        'item':item,
        'present':present
    })

def addTowatchlist(request, item):
    item=Listing.objects.get(id=item)
    user=request.user
    item.wachlist.add(user)
    # present=user in item.wachlist.all()
    return HttpResponseRedirect(reverse('index'))

def removeFromWatchlist(request, item):
    item=Listing.objects.get(id=item)
    user=request.user
    item.wachlist.remove(user)
    # present=user in item.wachlist.all()
    return HttpResponseRedirect(reverse('index'))

def placebid(request, item):
    item=Listing.objects.get(id=item)
    user=request.user
    if request.method == "POST":
        new_amount=request.post['bidamount']
        amount=Bid(
            bid_amount=new_amount,
            user=user,
            listing=item
        )
        amount.save()
    else:
        return render(request,'auctions/placebid.html')