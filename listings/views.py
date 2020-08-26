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
    results = Listing.objects.all().order_by('-list_date')

    if request.GET.get('city', ''):
        results = results.filter(city__iexact=request.GET['city'])

    if request.GET.get('state', ''):
        results = results.filter(state__iexact=request.GET['state'])

    if request.GET.get('keywords', ''):
        results = results.filter(description__icontains=request.GET['keywords'])

    if request.GET.get('bedrooms', ''):
        results = results.filter(bedrooms__iexact=request.GET['bedrooms'])

    if request.GET.get('price', ''):
        results = results.filter(price__iexact=request.GET['price'])

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_results': results
    }
    return render(request, "listings/search.html", context)
