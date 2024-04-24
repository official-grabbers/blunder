from typing import Any
from django.views.generic import TemplateView
from blunder.utils import FormatNumbers
import requests
import os
from django.conf import settings
import json


class ProfilePageHelper(TemplateView):
    template_name = "profile.html"

    def save_edges_to_json(self, edges_data, page_name):
        JSON_OUTPUT_DIR = os.path.join(settings.BASE_DIR, 'edges_data')  # Define the directory to save JSON files
        json_filename = os.path.join(JSON_OUTPUT_DIR, f"{page_name}_edges.json")
        with open(json_filename, 'w') as json_file:
            json.dump(edges_data, json_file)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_name = kwargs.get('page_name')

        api_url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={page_name}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
        }
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            context['user_name'] = data['data']['user']['username']
            context['profile_picture'] = data['data']['user']['profile_pic_url']
            context['edge_follow'] = data['data']['user']['edge_follow']['count']
            context['edge_followed_by'] = FormatNumbers.format_number(data['data']['user']['edge_followed_by']['count'])
            context['media_count'] = data['data']['user']['edge_owner_to_timeline_media']['count']
            context['edges'] = data['data']['user']['edge_owner_to_timeline_media']['edges']
            context['full_name'] = data['data']['user']['full_name']
            context['category_name'] = data['data']['user']['category_name']
            context['biography'] = data['data']['user']['biography']
            context['external_url'] = data['data']['user']['external_url']

            # Save edges data to a JSON file
            self.save_edges_to_json(data['data']['user']['edge_owner_to_timeline_media'], page_name)
        else:
            error_message = response.json().get('message') if response.headers.get('content-type') == 'application/json' else response.text
            data = error_message

        context['page_name'] = page_name
        return context
