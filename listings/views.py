from django.shortcuts import render
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator
from .choices import (
    price_choices, bedroom_choices, state_choices
)


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


def search(request):
    results = Listing.objects.order_by('-list_date')
    if 'city' in request.GET and request.GET['city'] is not None:
        results = results.filter(city__iexact=request.GET['city'])
    if 'state' in request.GET and request.GET['state'] is not None:
        results = results.filter(state__iexact=request.GET['state'])
    if 'keywords' in request.GET and request.GET['keywords'] is not None:
        results = results.filter(state__icontains=request.GET['keywords'])
    if 'bedrooms' in request.GET and request.GET['bedrooms'] is not None:
        results = results.filter(state__iexact=request.GET['bedrooms'])
    if 'price' in request.GET and request.GET['price'] is not None:
        results = results.filter(state__iexact=request.GET['price'])

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_results': results
    }
    return render(request, "listings/search.html", context)
