import urllib.request,json
from .models import Sources

#getting the api key
api_key = None

#getting the news base url
base_url = None

def configure_request(app):
	global api_key,base_url
	api_key = app.config['NEWS_API_KEY']
	base_url = app.config['NEWS_SOURCES_BASE_URL']