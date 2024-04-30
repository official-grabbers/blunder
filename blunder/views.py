from django.views.generic import TemplateView
from blunder.helpers import TestAPIHelper, PaginationAPIHandler, ExampleViewHandler, InstagramAuthViewHelper, FacebookAuthViewHelper, IndexViewHelper
from django.views import View
import requests
from django.http import HttpResponse


# Create your views here.
class IndexView(IndexViewHelper):
    pass


class FileRenderer(View):
    def get(self, request):
        # Construct the Firebase Storage URL
        firebase_url = "https://firebasestorage.googleapis.com/v0/b/blunder-grabbers.appspot.com/o/js%2Ftailwind.css?alt=media&token=cf3d9692-a37a-41e0-9c43-421c5cf52eaf"

        # Fetch the file from Firebase Storage
        response = requests.get(firebase_url)

        # Serve the file as the response
        if response.status_code == 200:
            return HttpResponse(response.content, content_type=response.headers['Content-Type'])
        else:
            return HttpResponse("File not found", status=response.status_code)


class ExampleView(ExampleViewHandler):
    pass


class InstagramAuthView(InstagramAuthViewHelper):
    pass


class FacebookAuthView(FacebookAuthViewHelper):
    pass


class LandingView(TemplateView):
    template_name = "api.html"


class TestAPI(TestAPIHelper):
    pass


class PaginationAPI(PaginationAPIHandler):
    pass


class LoginView(TemplateView):
    template_name = "login.html"
