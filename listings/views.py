from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator


def listings(request):
    listings_list = Listing.objects.all().select_related('realtor')
    paginator = Paginator(listings_list, per_page=3)
    requested_page = request.GET.get('page')
    listings_page = paginator.get_page(requested_page)
    return render(
        request, 'listings/listings.html', context={'listings': listings_page}
    )


def listing(request, listing_id):
    return render(request, 'listings/listing.html')
