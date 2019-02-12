from django.conf.urls import url

from audit_metrics.api.views import url_audit_data_view

urlpatterns = [
    url(r'^url_audit_data/$', url_audit_data_view,
        name = 'url_audit_data')
]