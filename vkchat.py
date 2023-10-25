import logging

import telepot
from environs import Env
from vk_api.longpoll import VkLongPoll, VkEventType

import random
import vk_api as vk

from logging_handler import TelegramLogsHandler
from detect_intent import detect_intent_texts

logger = logging.getLogger(__name__)


def send_answer(event, vk_api, project_id):
    answer_text = detect_intent_texts(
        project_id,
        event.user_id,
        event.text
    )
    if not answer_text.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer_text.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    env = Env()
    env.read_env()

    vk_api_key = env.str("VK_API_KEY")
    project_id = env.str("PROJECT_ID")
    admin_id = env.str('TELEGRAM_ADMIN_ID')
    telegram_bot = telepot.Bot(env.str('TGTOKEN'))
    vk_session = vk.VkApi(token=vk_api_key)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            try:
                send_answer(event, vk_api, project_id)
            except Exception as e:
                logger.addHandler(TelegramLogsHandler(telegram_bot, admin_id))
                logger.exception(e)
