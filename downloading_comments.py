from telethon.sync import TelegramClient
from asyncio import run
import sys
import json

api_id = 'api_id'
api_hash = "api_hash"
chat = 'https://t.me/zen_of_python'

phone = "+71231234567"
name = "session_name" # TelegramClient положит в текущую директорию логи с таким же именем


async def messages_func(name, api_id, api_hash):
    async with TelegramClient(name, api_id, api_hash) as client:
        async for message in client.iter_messages(chat):
            try:
                async for message in client.iter_messages(chat, reply_to=message.id):
                    sys.stdout=open("comments.json","a")
                    print(json.dumps({"reply_to_msg_id": message.reply_to_msg_id, 
                                      "comment_id": message.id,
                                      "date": str(message.date),
                                      "text": message.text,
                                      "reactions": str(message.reactions),
                                      "from_id": message.from_id.user_id}, indent=4))
                    print(",")
                    sys.stdout.close()
            except Exception:
                    pass

run(messages_func(name, api_id, api_hash))