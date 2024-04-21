from django.views.generic import TemplateView
import instaloader
from django.http import JsonResponse


# Create your views here.
class ExampleView(TemplateView):
    template_name = "example.html"


def download_instagram_post(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'URL parameter is required'}, status=400)

    L = instaloader.Instaloader()
    try:
        post = instaloader.Post.from_shortcode(L.context, url.split('/')[-1])
        # post_data = {
        #     attr: getattr(post, attr)
        #     for attr in dir(post)
        #     if not attr.startswith('__') and not callable(getattr(post, attr))
        # }
        # return JsonResponse(post_data)
        L.download_post(post, target='instagram_downloads')
        return JsonResponse({'message': 'Post downloaded successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
