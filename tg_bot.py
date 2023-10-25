from aiogram import Bot, types, Dispatcher, executor
from random import randint
from main import generate, enviroment, bunker
import keyboards as kb

bot = Bot(token='6186468240:AAGCtRNEnd2zKN7rwwMNtE6qezKDmDEA1x8')
dp = Dispatcher(bot)

gameid = 0
number_of_players = 0
id_list = []


@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, 'Для начала вам нужно добавить меня в беседу. После этого просто напишите число игроков и каждый желающий пусть напишет "Играю" (обязательно с большой буквы!) \n\nПримечание: все желающие поиграть должны написать мне в ЛС, чтобы я мог отправить вам ваши анкеты')


@dp.message_handler(commands=['start'])
async def littleInlineAddition(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('Для начала вам нужно добавить меня в беседу. После этого просто напишите число игроков и каждый желающий пусть напишет "Играю" (обязательно с большой буквы!) \n\nПримечание: все желающие поиграть должны написать мне в ЛС, чтобы я мог отправить вам ваши анкеты')


@dp.message_handler()
async def main(message: types.Message):
    if message.chat.type == 'group':
        if message.text.isdigit():
            global number_of_players, id_list, gameid, chatId
            number_of_players = int(message.text)
            generate(number_of_players)
            id_list = []
            gameid = randint(0, 1000000)
            await bot.send_message(message.chat.id, f'Создал игру на {number_of_players} человек!')
            chatId = message.chat.id
        elif number_of_players:
            if message.text == 'Играю' and message.from_user.id not in id_list and chatId == message.chat.id:
                id_list.append(message.from_user.id)
                if len(id_list) == number_of_players:
                    for i in range(len(id_list)):
                        doc = open('Player' + str(i+1) + '.txt').readline()
                        await bot.send_message(chat_id=id_list[i], text=doc + '\ngameid = ' + str(gameid))
                    await bot.send_message(chat_id=message.chat.id, text=enviroment() +'\n' + bunker() + '\ngameid = ' + str(gameid))
    else:
        await bot.send_message(message.chat.id, 'Используй в групповом чате!')


if __name__ == '__main__':
    executor.start_polling(dp)
