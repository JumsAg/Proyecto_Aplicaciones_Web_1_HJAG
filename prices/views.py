import time
import requests
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"
CACHE_KEY = "btc_price_usd_eur_gbp"
TTL_SECONDS = 300  # 5 minutos de caché

HEADERS = {
    "User-Agent": "btcapp/1.0 (https://jumsag.pythonanywhere.com)"
}

def fetch_btc_price():
    """Obtiene precio de BTC con reintento suave y User-Agent; retorna dict o lanza."""
    params = {"ids": "bitcoin", "vs_currencies": "usd,eur,gbp"}
    try:
        r = requests.get(COINGECKO_URL, params=params, headers=HEADERS, timeout=6)
        # Manejo básico de rate limit
        if r.status_code == 429:
            # espera corta y reintenta una vez
            time.sleep(2)
            r = requests.get(COINGECKO_URL, params=params, headers=HEADERS, timeout=6)
        r.raise_for_status()
        data = r.json().get("bitcoin", {})
        return {
            "usd": data.get("usd"),
            "eur": data.get("eur"),
            "gbp": data.get("gbp"),
        }
    except Exception as e:
        raise e

def btc_view(request):
    """Vista principal: usa caché; si API falla, muestra último valor en caché con aviso."""
    prices = cache.get(CACHE_KEY)
    api_error = None

    if prices is None:
        try:
            prices = fetch_btc_price()
            # guarda en caché solo si vienen valores
            if prices and prices.get("usd") is not None:
                cache.set(CACHE_KEY, prices, TTL_SECONDS)
        except Exception as exc:
            api_error = str(exc)

    context = {
        "prices": prices,
        "api_error": api_error,
        "cached": prices is not None and api_error is not None,  # true si estamos mostrando caché por error
        "ttl_seconds": TTL_SECONDS,
    }
    return render(request, "prices/index.html", context)
