from blunder.utils import FormatNumbers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from blunder.constants import GlobalPaths, StaticFiles
import requests
import os


class IndexViewHelper(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tailwind'] = GlobalPaths.FIREBASE_STROAGE_URL + StaticFiles.TAILWIND_CSS
        context['banner'] = GlobalPaths.FIREBASE_STROAGE_URL + StaticFiles.INDEX_BANNER_IMAGE
        return context


class InstagramAuthViewHelper(View):
    def get(self, request, *args, **kwargs):
        instagram_auth_url = "https://api.instagram.com/oauth/authorize"

        client_id = os.environ.get('CLIENT_ID')
        redirect_uri = os.environ.get('REDIRECT_URL')
        scope = "user_profile,user_media"
        response_type = "code"

        authorization_url = f"{instagram_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}"
        return HttpResponseRedirect(authorization_url)


class FacebookAuthViewHelper(View):
    def get(self, request, *args, **kwargs):
        facebook_auth_url = "https://www.facebook.com/v19.0/dialog/oauth"

        client_id = os.environ.get('BUSINESS_CLIENT_ID')
        redirect_uri = os.environ.get('BUSINESS_REDIRECT_URL')
        state = os.environ.get('BUSINESS_STATE')
        config_id = os.environ.get('BUSINESS_CONFIG_ID')

        authorization_url = f"{facebook_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&config_id={config_id}&state={state}"
        return HttpResponseRedirect(authorization_url)


class ExampleViewHandler(TemplateView):
    template_name = "example.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth_code = self.request.GET.get('code')
        context['auth_code'] = auth_code

        if auth_code:
            instagram_endpoint = "https://api.instagram.com/oauth/access_token"

            # Define your app's credentials and other required parameters
            client_id = os.environ.get('CLIENT_ID')
            client_secret = os.environ.get('CLIENT_SECRET')
            redirect_uri = os.environ.get('REDIRECT_URL')
            grant_type = "authorization_code"

            # Prepare the data to be sent in the POST request
            data = {
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": grant_type,
                "redirect_uri": redirect_uri,
                "code": auth_code
            }

            response = requests.post(instagram_endpoint, data=data)
            context['instagram_response'] = response.json()
        return context


class TestAPIHelper(APIView):

    def get(self, request, *args, **kwargs):
        page_name = kwargs.get('page_name')

        api_url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={page_name}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            user_data = data.get('data', {}).get('user', {})
            context = {
                'id': user_data.get('id'),
                'user_name': user_data.get('username'),
                'profile_picture': user_data.get('profile_pic_url'),
                'edge_follow': user_data.get('edge_follow', {}).get('count'),
                'edge_followed_by': FormatNumbers.format_number(user_data.get('edge_followed_by', {}).get('count')),
                'media_count': user_data.get('edge_owner_to_timeline_media', {}).get('count'),
                'edges': user_data.get('edge_owner_to_timeline_media', {}).get('edges'),
                'full_name': user_data.get('full_name'),
                'category_name': user_data.get('category_name'),
                'biography': user_data.get('biography'),
                'external_url': user_data.get('external_url'),
                'page_name': page_name,
                'page_info': user_data.get('edge_owner_to_timeline_media', {}).get('page_info'),
            }

            return Response(context)
        else:
            error_message = response.json().get('message') if response.headers.get('content-type') == 'application/json' else response.text
            return Response({'error': error_message}, status=response.status_code)


class PaginationAPIHandler(APIView):
    def get(self, request, *args, **kwargs):
        document_id = request.query_params.get('document_id')
        user_id = request.query_params.get('user_id')
        end_cursor = request.query_params.get('end_cursor')

        api_url = f'https://www.instagram.com/graphql/query/?hl=en&doc_id={document_id}&variables={{"id":"{user_id}","after":"{end_cursor}","first":12}}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
        }

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return Response({
                'status': True,
                'message': "Data fetched successfully",
                'data': data,
            })
        else:
            error_message = response.json().get('message') if response.headers.get('content-type') == 'application/json' else response.text
            return Response({'error': error_message}, status=response.status_code)
