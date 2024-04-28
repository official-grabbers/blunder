from django.views.generic import TemplateView
from blunder.helpers import TestAPIHelper, PaginationAPIHandler, ExampleViewHandler, InstagramAuthViewHelper


# Create your views here.
class ExampleView(ExampleViewHandler):
    pass


class InstagramAuthView(InstagramAuthViewHelper):
    pass


class LandingView(TemplateView):
    template_name = "index.html"


class TestAPI(TestAPIHelper):
    pass


class PaginationAPI(PaginationAPIHandler):
    pass


class LoginView(TemplateView):
    template_name = "login.html"
