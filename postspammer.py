import os
import time
from instagrapi import Client

USERNAME = "neutrallows"
PASSWORD = "KING_KIERAN"
photo_path = r"C:\Users\torin\Downloads\white.jpg"
caption = "test"

# Generate cookies and login
def generate_cookie(username, password):
    cl = Client()
    try:
        cl.login(username, password)
        cl.dump_settings(f"{username}.json")
        print("Cookies generated and saved.")
    except Exception as e:
        print(f"Error generating cookies: {e}")
    return cl

# Load cookies if they exist, otherwise generate them
def login_with_cookies(username, password):
    cl = Client()
    settings_path = f"{username}.json"
    try:
        if os.path.exists(settings_path):
            print("Using existing cookies...")
            cl.load_settings(settings_path)
            cl.login(username, password)
        else:
            print("No cookies found, generating new ones...")
            cl = generate_cookie(username, password)
        
        # Check if the login was successful by verifying account info retrieval
        account_info = cl.account_info()
        if account_info:
            print(f"Login successful as {account_info.username}")
            return cl
        else:
            print("Login failed.")
            return None
    except Exception as e:
        print(f"Failed to login with cookies: {e}")
        return None

# Function to upload photo
def upload_photo(client, path, caption_text):
    try:
        client.photo_upload(path, caption_text)
        print("Photo posted successfully!")
    except Exception as e:
        print(f"Failed to post photo: {e}")

# Main
client = login_with_cookies(USERNAME, PASSWORD)

if client:
    while True:
        upload_photo(client, photo_path, caption)
        print("Waiting for the next post...")
        time.sleep(5)  # Wait before posting next photo
else:
    print("Could not log in. Check credentials or try regenerating cookies.")
