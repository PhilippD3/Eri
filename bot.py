import asyncio

from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config import TOKEN, three_sigma, rk2

buid = "BAACAgIAAxkBAAMfZzjRE4xM0C1Rw7ns8yZwX5BEYjcAAopjAAJOnwABSWM1C_62KxgDNgQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()



register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="ТриСигмы"
        )
        
    ],
    [
        KeyboardButton(
            text="Рк2"
        )
        
    ]



], resize_keyboard=True)


class bebra(StatesGroup):
    sigma = State()
    rkk2 = State()

def isn(input_string):
    try:
        cleaned_string = input_string.strip()
        if not cleaned_string:
            return False

        numbers = cleaned_string.split()
        for number in numbers:
            float(number) # Пробуем преобразовать в float (поддерживает и целые, и десятичные)
        return True
    except ValueError:
        return False



@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_video(video=buid, caption="Привет, Напиши или нажми на кнопку ТриСигмы или Рк2. Взависимости от того что тебе надо, если бот тебе не ответил попробуй написать еще",reply_markup=register_keyboard)

@dp.message(F.text == "ТриСигмы")
async def tri (message: Message, state = FSMContext):
    await state.set_state(bebra.sigma)
    await message.answer("Введи X через пробел")


@dp.message(bebra.sigma)
async def sigmi (message: Message, state = FSMContext):
    if isn(message.text):
        a = three_sigma(message.text)
        s = ""
        for i in range(len(a)):
            s = s+ a[i]+'\n'
        await message.answer(s)
        await state.clear()
    else:
       await message.answer("Еще раз хуйню напишешь, я Левиеву расскажу что ты списываешь.СКАЗАНО ЧИСЛА ЧЕРЕЗ ПРОБЕЛ") 


@dp.message(F.text == "Рк2")
async def Rki (message: Message, state = FSMContext):
    await state.set_state(bebra.rkk2)
    await message.answer("Введи X через пробел")


@dp.message(bebra.rkk2)
async def sigmi (message: Message, state = FSMContext):
    if isn(message.text):
        a = rk2(message.text)
        s = ""
        for i in range(len(a)):
            s = s+ a[i]+'\n'
        await message.answer(s)
        await state.clear()
    else:
       await message.answer("Еще раз хуйню напишешь, я Левиеву расскажу что ты списываешь.СКАЗАНО ЧИСЛА ЧЕРЕЗ ПРОБЕЛ") 






async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
