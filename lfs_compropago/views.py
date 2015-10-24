import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_POST

from .models import CompropagoTransaction

@login_required
def status_view(request, tx_id):
    t = get_object_or_404(CompropagoTransaction, pk=tx_id)
    if request.user != t.order.user or request.user.is_superuser is False:
        raise PermissionDenied("Sorry, you are in the wrong place.")
    template_name='compropago/status.html'
    if t.payment_type == 'OXXO':
        template_name='compropago/status_oxxo.html'
    template_vars = {
        'transaction': t,
        'instructions': json.loads(t.payment_instructions),
        'order': t.order,
    }
    return render_to_response(
        template_name,
        RequestContext(request, template_vars)
    )


@require_POST
def web_hook_view(request):
    payload = json.loads(request.body)
    form = ChargeForm(payload)
    #verificar el cargo con el id
    #Actualizar el cargo si existe
