from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def fake_admin(request):
    return HttpResponse("<h1>Login Failed</h1><p>This incident will be reported.</p>", status=403)


# Create your views here.
