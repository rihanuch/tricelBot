import os
import json
from datetime import datetime
from telebot.settings import IG_USER, IG_PWD, IG_FILE_LOC, PROXIES


def judge(update, context, *args):
    # unpack and assign default values
    accounts, *amount = args
    amount = amount[0] if amount else 1

    command = f'instagram-scraper {accounts} -d {IG_FILE_LOC} -n --latest --media-types none --comments --comments -m {amount} --proxies \'{PROXIES}\''
    print(command)
    os.system(command)
    for watched in os.listdir(IG_FILE_LOC):
        if '.keep' in watched:
            continue
        pictures_with_comments(update, context, f'{IG_FILE_LOC}{watched}/{watched}.json')


def pictures_with_comments(update, context, file):
    with open(file) as json_file:
        data = json.load(json_file)
        for image in data['GraphImages']:
            img_url = image['display_url']
            footer = image['edge_media_to_caption']['edges'][0]['node']['text']
            context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=img_url, caption=footer)
            header = f'<b>Comentarios al {datetime.now()}</b>\n' + '~'*30
            comments = [f'<b>{cmt["owner"]["username"]}</b>: {cmt["text"]}' for cmt in image['comments']['data']]
            comments = [f'{i+1}) {cmt}' for i, cmt in enumerate(comments)]
            # TODO: cut if message is over 20 comments long
            update.message.reply_text(f'{header}\n' + '\n'.join(comments), parse_mode='HTML')
