from aiogram import Bot, types, Dispatcher, F
import asyncio
from aiogram.filters import Command
from environs import Env

from flow_utils import detect_intent_texts

env = Env()
env.read_env()

TGTOKEN = env.str("TGTOKEN")
PROJECT_ID = env.str("PROJECT_ID")

bot = Bot(token=TGTOKEN)
dp = Dispatcher()


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
