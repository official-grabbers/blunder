import os


class GlobalPaths:
    FIREBASE_STROAGE_URL = os.environ.get('FIREBASE_STORAGE_URL')


class SubRoutes:
    ROOT = ''


class RouteGroups:
    API_ROUTES = 'api/'


class StaticFiles:
    INDEX_BANNER_IMAGE = "images%2Fbackground.jpg?alt=media&token=8f467341-e708-40a0-af7a-8bae7143336f"
    TAILWIND_CSS = "js%2Ftailwind.css?alt=media&token=cf3d9692-a37a-41e0-9c43-421c5cf52eaf"
