from django.views.generic import TemplateView
from blunder.helpers import TestAPIHelper, PaginationAPIHandler


# Create your views here.
class ExampleView(TemplateView):
    template_name = "example.html"


class LandingView(TemplateView):
    template_name = "index.html"


class TestAPI(TestAPIHelper):
    pass


class PaginationAPI(PaginationAPIHandler):
    pass


class LoginView(TemplateView):
    template_name = "login.html"
