from django.shortcuts import render
from listings.models import Listing

def index(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(
        is_published=True
    ).select_related('realtor')[:3]
    return render(
        request, 'pages/index.html', {'latest_listings': latest_listings}
    )


def about(request):
    return render(request, 'pages/about.html')
