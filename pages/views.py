from django.shortcuts import render
from listings.models import Listing
from listings.choices import (
    price_choices, bedroom_choices, state_choices
)
from realtors.models import Realtor


def index(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(
        is_published=True
    ).select_related('realtor')[:3]
    context = {
        'latest_listings': latest_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(
        request, 'pages/index.html', context
    )


def about(request):
    realtors = Realtor.objects.all()
    seller_of_the_month = Realtor.objects.filter(
        is_seller_of_the_month=True
    ).first()
    return render(
        request, 'pages/about.html', {
            'realtors': realtors,
            'seller_of_the_month': seller_of_the_month
        }
    )
