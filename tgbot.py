import logging
from functools import partial

import telepot
from environs import Env
from telepot.loop import MessageLoop

from logging_handler import TelegramLogsHandler
from detect_intent import detect_intent_texts

logger = logging.getLogger(__name__)


def send_answer(msg, project_id, telegram_bot):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        msg = msg['text']
        if msg == '/start':
            telegram_bot.sendMessage(chat_id, 'Привет, приятель!')
        else:
            answer_text = detect_intent_texts(
                project_id,
                chat_id,
                msg
            )
            telegram_bot.sendMessage(chat_id, answer_text.fulfillment_text)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    env = Env()
    env.read_env()
    admin_id = env.str('TELEGRAM_ADMIN_ID')
    tg_token = env.str("TGTOKEN")
    project_id = env.str("PROJECT_ID")
    telegram_bot = telepot.Bot(tg_token)
    logger.addHandler(TelegramLogsHandler(telegram_bot, admin_id))
    logger.info('Telegram bot started')
    send_answer_with_params = partial(send_answer, project_id=project_id, telegram_bot=telegram_bot)
    try:
        MessageLoop(telegram_bot, send_answer_with_params).run_forever()
    except Exception as e:
        logger.addHandler(TelegramLogsHandler(telegram_bot, admin_id))
        logger.exception(e)


if __name__ == '__main__':
    main()
