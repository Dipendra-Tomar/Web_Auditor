from django.conf.urls import url

from audit_metrics import views


urlpatterns = [
	url(r'^EnterUrl/$', views.enter_url_view, name='enter_url'),
]