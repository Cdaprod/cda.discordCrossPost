import os
import requests

def post_to_facebook(message: str):
    page_id = os.getenv("FACEBOOK_PAGE_ID")
    access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")

    # ... (rest of the code)
