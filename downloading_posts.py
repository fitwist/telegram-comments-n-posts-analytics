from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import json

BATCHES = 3000 # Число итераций
CHANNEL_ID = 'zen_of_python'

api_id = 'api_id' # Идентификатор приложения
api_hash = 'api_hash'

name = 'session_name' # Название сессии


client = TelegramClient('data_analysis_session',
                    api_id,
                    api_hash)

client.connect()

# Авторизуемся
if not client.is_user_authorized():
    client.send_code_request('+71231234567')
    me = client.sign_in('+71231234567', input('Введи код (отправлен в Telegam): '))

channel_username=CHANNEL_ID
channel_entity=client.get_entity(channel_username)

batch_count = 0 # Номер пакета записей

while batch_count <= BATCHES:
    # Отправим запрос на получение массивов о постах
    posts = client(GetHistoryRequest(
        peer=channel_entity,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=batch_count,
        hash=0))

    i = 0

    
    while i <= len(posts.messages) - 1:
        emojis = []
        j = 0

        # Выделим число реакций и их типы
        while j <= 10:
            try:
                reaction = {
                    "emojis": posts.messages[i].reactions.results[j].reaction.emoticon,
                    "emoji_count": posts.messages[i].reactions.results[j].count,
                }
                emojis.append(reaction)
                j += 1
            except (AttributeError, TypeError, IndexError) as error:
                j += 1
        
        # Выделим число комментариев и заполним пустоты
        try:
            replies = posts.messages[i].replies.replies
        except AttributeError:
            replies = 0

        post = {
            "id": posts.messages[i].id,
            "date": str(posts.messages[i].date),
            "message": posts.messages[i].message,
            "views": posts.messages[i].views,
            "forwards": posts.messages[i].forwards,
            "replies": replies,
            "reactions": emojis
        }

        with open(f"{post['id']}.json", "w") as outfile:
            json.dump(post, outfile, ensure_ascii=False)
        
        i += 1
    batch_count += 1