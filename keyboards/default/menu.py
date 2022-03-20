from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='english-rusian'),
            KeyboardButton(text='english-uzbek')
        ],
        [
            KeyboardButton(text='ubek-english'),
            KeyboardButton(text='руский-узбекский')
        ],
        [
            KeyboardButton(text="O'zbekcha-inglizcha"),
            KeyboardButton(text="O'zbekcha-ruscha")
        ]

    ], resize_keyboard=True
)
