import os
import asyncio
from aiogram import Bot,Dispatcher,F
import logging

from dotenv import load_dotenv
from app.handlers import router





async def main():
    load_dotenv()
    # обьект самого ТГ бота
    bot = Bot(token=os.getenv("TG_TOKEN"))
    #диспетчер для обработки запросов(сообщений и т.д.)
    dp = Dispatcher()
    #процесс полинга по боту
    # (бот отправляет запрос на сервера ТГ и спрашивает пришло ли обновление)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print("Exit")