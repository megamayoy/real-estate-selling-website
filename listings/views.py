from django.shortcuts import render
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator


def listings(request):
    listings_list = Listing.objects.order_by('-list_date').filter(
        is_published=True
    ).select_related('realtor')
    paginator = Paginator(listings_list, per_page=3)
    requested_page = request.GET.get('page')
    listings_page = paginator.get_page(requested_page)
    return render(
        request, 'listings/listings.html', context={'listings': listings_page}
    )


def listing(request, listing_id):
    listing = Listing.objects.filter(pk=listing_id).select_related(
        'realtor'
    ).first()
    return render(
        request,
        'listings/listing.html',
        {'listing': listing,}
    )
