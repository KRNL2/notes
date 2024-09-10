# Notes Bot 🤖📝
![Untitled-1]([https://github.com/mishalshanavas/notes-bot/assets/70484516/cdd408dd-fae2-43e5-aa51-b6f61c8c0ffa](https://raw.githubusercontent.com/KRNL2/images/415b0626de95f001ed54deafb5255e510fe073f4/message%201.PNG))
![Untitled-2]([https://raw.githubusercontent.com/KRNL2/images/415b0626de95f001ed54deafb5255e510fe073f4/message2.PNG])


## Description

The **Notes Bot** project is an automated tool written in Python designed to enhance user engagement on Instagram by delivering personalized notification messages to a designated Instagram account at regular intervals.

## Usage 🛠️

1. **Requirements** Install required dependencies with `pip install -r requirements.txt`

2. **Account Configuration:** Provide Instagram credentials (username and password) within the `USERNAME` and `PASSWORD` constants in `main.py`

3. **Customization:** Tailor the bot's messaging approach, interval timings, and notification content by modifying the relevant constants and functions.

4. **Execution:** Upon executing the script, the bot verifies the presence of existing authentication cookies 🍪. If absent, it creates cookies through the login procedure.  Use `python main.py` to start the script
    
5. **Note Dispatch:** The bot operates within an infinite loop ♾️, continuously monitoring the current time. It sends Note featuring updated content based on the current time and the defined interval.

6. **User Engagement:** Followers receive captivating messages that showcase the current time with clock emojis 🕓🕘 and incorporate interactive questions ❓. This fosters user engagement and interactions with the account.

**Note:** The Notes Bot project serves as a foundational code structure that necessitates further refinement and adaptation to ensure compatibility with potential updates to the Instagram API or the `instagrapi` library.
