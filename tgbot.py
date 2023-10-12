from aiogram import Bot, types, Dispatcher, F
import asyncio

from aiogram.filters import Command
from environs import Env

env = Env()
env.read_env()

TGTOKEN = env.str("TGTOKEN")

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
    await bot.send_message(msg.from_user.id, msg.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
