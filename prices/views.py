import time
import requests
from django.core.cache import cache
from django.shortcuts import render, redirect, get_object_or_404  # <- get_object_or_404 AQUÍ
from .forms import WatchItemForm                                    # <- IMPORTA EL FORM
from .models import WatchItem                                       # <- IMPORTA EL MODELO

# --- Configuración CoinGecko ---
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"
CACHE_KEY = "btc_price_usd_eur_gbp"
TTL_SECONDS = 300
HEADERS = {"User-Agent": "btcapp/1.0 (https://jumsag.pythonanywhere.com)"}

def fetch_btc_price():
    params = {"ids": "bitcoin", "vs_currencies": "usd,eur,gbp"}
    r = requests.get(COINGECKO_URL, params=params, headers=HEADERS, timeout=6)
    if r.status_code == 429:
        time.sleep(2)
        r = requests.get(COINGECKO_URL, params=params, headers=HEADERS, timeout=6)
    r.raise_for_status()
    data = r.json().get("bitcoin", {})
    return {"usd": data.get("usd"), "eur": data.get("eur"), "gbp": data.get("gbp")}

def btc_view(request):
    prices = cache.get(CACHE_KEY)
    api_error = None
    if prices is None:
        try:
            prices = fetch_btc_price()
            if prices and prices.get("usd") is not None:
                cache.set(CACHE_KEY, prices, TTL_SECONDS)
        except Exception as exc:
            api_error = str(exc)
    context = {
        "prices": prices,
        "api_error": api_error,
        "cached": prices is not None and api_error is not None,
        "ttl_seconds": TTL_SECONDS,
        "data": prices,
        "error": api_error,
    }
    return render(request, "prices/home.html", context)

# -------- CRUD real con BD --------
def watch_list(request):
    items = WatchItem.objects.all().order_by("name")
    return render(request, "prices/watch_list.html", {"items": items})

def watch_create(request):
    if request.method == "POST":
        form = WatchItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("prices:watch_list")
    else:
        form = WatchItemForm()
    return render(request, "prices/watch_form.html", {"title": "Nuevo activo", "form": form})

def watch_update(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    if request.method == "POST":
        form = WatchItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("prices:watch_list")
    else:
        form = WatchItemForm(instance=item)
    return render(request, "prices/watch_form.html", {"title": "Editar activo", "form": form})

def watch_delete(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("prices:watch_list")
    return render(request, "prices/watch_confirm_delete.html", {"item": item})