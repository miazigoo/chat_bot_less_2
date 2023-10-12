from aiogram import Bot, types, Dispatcher, F
import asyncio
from aiogram.filters import Command
from environs import Env
from google.cloud import dialogflow


env = Env()
env.read_env()

TGTOKEN = env.str("TGTOKEN")
PROJECT_ID = env.str("PROJECT_ID")

bot = Bot(token=TGTOKEN)
dp = Dispatcher()


def detect_intent_texts(project_id, session_id, text, language_code='ru'):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text



@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message(Command('help'))
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message(F.text)
async def echo_message(msg: types.Message):
    answer_text = detect_intent_texts(
        PROJECT_ID,
        msg.from_user.id,
        msg.text
    )
    await bot.send_message(msg.from_user.id, answer_text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
