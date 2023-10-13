import logging

import telepot
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

import random
import vk_api as vk

from utils import detect_intent_texts_vk, TelegramLogsHandler

logger = logging.getLogger(__name__)
env = Env()
env.read_env()

VK_API_KEY = env.str("VK_API_KEY")
PROJECT_ID = env.str("PROJECT_ID")


def echo(event, vk_api):
    answer_text = detect_intent_texts_vk(
        PROJECT_ID,
        event.user_id,
        event.text
    )
    if answer_text:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    admin_id = env.str('TELEGRAM_ADMIN_ID')
    telegram_bot = telepot.Bot(env.str('TGTOKEN'))
    vk_session = vk.VkApi(token=VK_API_KEY)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            try:
                echo(event, vk_api)
            except Exception as e:
                logger.addHandler(TelegramLogsHandler(telegram_bot, admin_id))
                logger.exception(e)
