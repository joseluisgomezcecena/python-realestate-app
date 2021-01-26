from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# index view.
def index(request):
    lisings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings': lisings
    }
    return render(request, 'pages/index.html', context)




# about view.
def about(request):

    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)    