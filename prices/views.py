from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchItem
from .forms import WatchItemForm
import requests

# --- Vista que muestra precio BTC desde CoinGecko ---
def home(request):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd,eur,gbp"}
    data, error = {}, None
    try:
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        data = r.json().get("bitcoin", {})
    except Exception as e:
        error = str(e)
    return render(request, "prices/home.html", {"data": data, "error": error})

# --- CRUD ---
def watch_list(request):
    items = WatchItem.objects.all().order_by("name")
    return render(request, "prices/watch_list.html", {"items": items})

def watch_create(request):
    if request.method == "POST":
        form = WatchItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("watch_list")
    else:
        form = WatchItemForm()
    return render(request, "prices/watch_form.html", {"form": form, "title": "Nuevo activo"})

def watch_update(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    if request.method == "POST":
        form = WatchItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("watch_list")
    else:
        form = WatchItemForm(instance=item)
    return render(request, "prices/watch_form.html", {"form": form, "title": "Editar activo"})

def watch_delete(request, pk):
    item = get_object_or_404(WatchItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("watch_list")
    return render(request, "prices/watch_confirm_delete.html", {"item": item})