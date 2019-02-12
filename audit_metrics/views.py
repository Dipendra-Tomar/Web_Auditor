# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def enter_url_view(request):
    return render(request, 'audit_metrics/enter_url.html')
