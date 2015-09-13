import json

from django.forms import ModelForm
from django.views.decorators.http import re

from .models import CompropagoCharge

class ChargeForm(ModelForm):
    class Meta:
        model = CompropagoCharge

@require_POST
def compropago_webhook(request):
    payload = json.loads(request.body)
    form = ChargeForm(payload)
    #verificar el cargo con el id
    #Actualizar el cargo si existe