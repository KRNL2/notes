import os
import time
from instagrapi import Client

USERNAME = "USERNAME HERE"
PASSWORD = "PASSWORD HERE"

def generate_cookie(USERNAME, PASSWORD):
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(f"{USERNAME}.json")

def send_custom_note(note_text):
    cl = Client()
    cl.load_settings(f"{USERNAME}.json")
    cl.login(USERNAME, PASSWORD)
    cl.create_note(note_text, 0)
    return f"Posted: {note_text}"

def get_dynamic_text():
    texts = [
        "MESSAGE 1 HERE",
        "MESSAGE 2 HERE",
        "MESSAGE 3 HERE",
        "MESSAGE 4 HERE",
        "MESSAGE 5 HERE"
    ]

    return texts[int(time.time()) % len(texts)]

if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{USERNAME}.json")):
    print("Using existing cookies")
else:
    generate_cookie(USERNAME, PASSWORD)
    print("Cookies generated")

previous_note_text = None

while True:
    note_text = get_dynamic_text()

    if previous_note_text != note_text:
        print(send_custom_note(note_text))
        previous_note_text = note_text

    time.sleep(3)
