# Перед запуском
- получите api_hash, api_id можно получить по [инструкции](https://core.telegram.org/api/obtaining_api_id).
- установим инструменты: `pip3 install -r requirements.txt`

# Кто есть кто
- downloading_posts.py: скачает все посты с метаданными
- merging_posts: сольет массивы с постами в один файл.json
- downloading_comments: скачает комментарии
- zen_of_python___Факты.ipynb: рассчитает:
    - Cамые популярные эмоджи
    - Самые популярные технологии
    - Cамых активных подписчиков


## Что отдается про комментарии
Message(id=1715,
        peer_id=PeerChannel(channel_id=1568214466),
        date=datetime.datetime(2023,12,8,14,16,12,
        tzinfo=datetime.timezone.utc),
        message='кажется второе не сильно сложнее, просто схема нагруженная',
        out=False,
        mentioned=False,
        media_unread=False,
        silent=False,
        post=False,
        from_scheduled=False,
        legacy=False,
        edit_hide=True,
        pinned=False,
        noforwards=False,
        invert_media=False,
        from_id=PeerUser(user_id=129131197),
        fwd_from=None,
        via_bot_id=None,
        reply_to=MessageReplyHeader(reply_to_scheduled=False,
        forum_topic=False,
        quote=False,
        reply_to_msg_id=1714,
        reply_to_peer_id=None,
        reply_from=None,
        reply_media=None,
        reply_to_top_id=None,
        quote_text=None,
        quote_entities=[]),
        media=None,
        reply_markup=None,
        entities=[],
        views=None,
        forwards=None,
        replies=None,
        edit_date=datetime.datetime(2023,12,19,12,0,11,tzinfo=datetime.timezone.utc),
        post_author=None,
        grouped_id=None,
        reactions=MessageReactions(results=[ReactionCount(reaction=ReactionEmoji(emoticon='👍'),
        count=1,
        chosen_order=None)],
        min=False,
        can_see_list=True,
        recent_reactions=[MessagePeerReaction(peer_id=PeerUser(user_id=232713498),
        date=datetime.datetime(2023,12,19,12,0,11,tzinfo=datetime.timezone.utc),
        reaction=ReactionEmoji(emoticon='👍'),
        big=False,
        unread=False,
        my=False)]),
        restriction_reason=[],
        ttl_period=None,
        ttl_time=None,
        via_bot_id=None
) 