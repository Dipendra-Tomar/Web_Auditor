from __future__ import unicode_literals

import json

from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from audit_metrics.api.utils import url_handle, get_basic_audit


@api_view(['POST'])
def url_audit_data_view(request):
    for x in request.POST:
        data = json.loads(x)
    raw_url = data['url_text']
    url = url_handle(raw_url)
    context = get_basic_audit(url)
    import pdb;pdb.set_trace()
    return JsonResponse({'response': "success"}, status=200)
