from django.shortcuts import render
from .models import Listing


def listings(request):
    listings_list = Listing.objects.all().select_related('realtor')
    return render(
        request, 'listings/listings.html', context={'listings': listings_list}
    )


def listing(request, listing_id):
    return render(request, 'listings/listing.html')