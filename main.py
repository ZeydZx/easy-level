import os
import requests
import random
import time

from keep_alive import keep_alive
keep_alive()

# جلب التوكن من أسرار Replit
user_token = os.environ['DISCORD_TOKEN']
channel_id = "1362751829376635020"

# الكلمات العشوائية
words = [
    "هلا", "تمام", "لول", "برو", "سبام", "ديجيتال", "مستوى", "جرب", "رفع", "تشغيل"
]

# رأس الطلب
headers = {
    "Authorization": user_token,
    "Content-Type": "application/json"
}

# رابط إرسال الرسائل
url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

# تكرار الإرسال
while True:
    content = random.choice(words)
    payload = {"content": content}
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"[تم الإرسال] >> {content}")
    else:
        print(f"[خطأ] {response.status_code}: {response.text}")

    time.sleep(10)