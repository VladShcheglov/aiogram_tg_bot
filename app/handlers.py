from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(F.text == "проверка роутера")
async def check_router(message:Message):
    await message.answer("Все ок!")


@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("Добро пожаловать!")

@router.message(Command("help"))
async def cmd_help(message:Message):
    await message.answer("Пока что бот не умеет ничего")

@router.message(F.text == "Привет!")
async def hello(message:Message):
    await message.reply("Как дела?")

#ловим фото 
@router.message(F.photo)
async def handle_photo(message:Message):
    # из сообщения достаем последнее фото(самое лучшее) и извлекаем его file_id
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id,caption="вот твое фото!")


@router.message(F.sticker)
async def handle_sticker(message:Message):
    file_id = message.sticker.file_id
    await message.answer_sticker(file_id)