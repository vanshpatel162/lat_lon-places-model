from django.shortcuts import render

# Create your views here.

from .engine import recommend

def home(request):
    results = []
    q = request.GET.get("q", "").strip()

    if q:   # only if not empty
        # user_lat = 23.0200
        # user_lon = 72.5800
        user_lat = 25.8077250
        user_lon = 82.6915450
        results = recommend(user_lat, user_lon, q)

    return render(request, "index.html", {"results": results})

