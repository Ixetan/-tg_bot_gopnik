import asyncio 
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from dotenv import dotenv_values
from tg_bot_gopnik.utills import generate_random_ip

config = dotenv_values('.env')

bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message):
    await message.answer(f'Твой IP: {generate_random_ip()}')
    await message.answer("За тобой выехади. Не сопротивляйтесь.")

async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())

