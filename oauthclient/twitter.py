from .base import OAuthHttp
from oauth import oauth

class TwitterHttp(OAuthHttp):
    request_token_url = 'http://twitter.com/oauth/request_token'
    access_token_url = 'http://twitter.com/oauth/access_token'
    authorization_url = 'http://twitter.com/oauth/authorize'
    callback_url = None
    default_scheme = 'https'
