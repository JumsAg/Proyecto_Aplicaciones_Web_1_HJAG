from django import forms
from .models import WatchItem

class WatchItemForm(forms.ModelForm):
    class Meta:
        model = WatchItem
        fields = ["name", "symbol", "target_price", "notes"]
