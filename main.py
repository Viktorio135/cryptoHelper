import aio_test, post, threading, calculator, os, mysql.connector, time



from aiogram import Bot, Dispatcher, types, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

connection = mysql.connector.connect(host = "localhost", user = "root",passwd = "Pro2216450788_", database = "Users") 

users = []
sub_users = []

TOKEN = '6331446499:AAEUsww44UHeV0Vmz1-sLQEVPM5Rg9VDiGo'


svodka_date = ''
svodka_sob = ''
svodka_otc = ''
ott_text = ''
total_text = ''

svodka_9_sob = ''



bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

class Form(StatesGroup):
    sym = State()


class Coin(StatesGroup):
    sym = State()

class Form_binance15(StatesGroup):
    sym = State()
class Form_binance1h(StatesGroup):
    sym = State()
class Form_binance4h(StatesGroup):
    sym = State()
class Form_binance1d(StatesGroup):
    sym = State()


class Form_bitget15(StatesGroup):
    sym = State()
class Form_bitget1h(StatesGroup):
    sym = State()
class Form_bitget4h(StatesGroup):
    sym = State()
class Form_bitget1d(StatesGroup):
    sym = State()


class Form_coinbase15(StatesGroup):
    sym = State()
class Form_coinbase1h(StatesGroup):
    sym = State()
class Form_coinbase4h(StatesGroup):
    sym = State()
class Form_coinbase1d(StatesGroup):
    sym = State()


class Form_mexc15(StatesGroup):
    sym = State()
class Form_mexc1h(StatesGroup):
    sym = State()
class Form_mexc4h(StatesGroup):
    sym = State()
class Form_mexc1d(StatesGroup):
    sym = State()


class Form_kraken15(StatesGroup):
    sym = State()
class Form_kraken1h(StatesGroup):
    sym = State()
class Form_kraken4h(StatesGroup):
    sym = State()
class Form_kraken1d(StatesGroup):
    sym = State()





############################### Главное меню ##########################################

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):

    if message.from_user.id not in users:
        us = []
        with connection.cursor() as cursor:
            cursor.execute('''SELECT * FROM users''')
            rez = cursor.fetchall()
            for i in rez:
                us.append(i[0])
        if str(message.from_user.id) not in us:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO users (user_id, user_name) VALUES (%s, %s) ", (str(message.from_user.id), str(message.from_user.full_name)))
                connection.commit()
            
    print(sub_users)
    
   
    btn1 = types.KeyboardButton('⚒️ Инструменты')
    btn2 = types.KeyboardButton('📑 Статистические данные')
    btn3 = types.KeyboardButton('ℹ️ Общая информация о рынке')
    btn4 = types.KeyboardButton('🔎 Курс монет')
    btn5 = types.KeyboardButton('📅 Календари')
    #btn6 = types.KeyboardButton('🧮 Расчет средней цены входа')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).row(btn3).row(btn1, btn4, btn5).row(btn2)


    await bot.send_message(message.from_user.id, 'Привет, выберите действия', reply_markup=keyboard)
    
######### Инструменты

@dp.message_handler(filters.Text('⚒️ Инструменты'))
async def instr(message: types.Message):
    if str(message.from_user.id) in sub_users:
        inline_btn1 = types.InlineKeyboardButton(text='📊 TradingView', callback_data='tw')
        inline_btn2 = types.InlineKeyboardButton(text='🧮 Расчет средней цены входа', callback_data='ras')
        inline_btn3 = types.InlineKeyboardButton(text='Уведомления', callback_data='notifications')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1).add(inline_btn2).add(inline_btn3)
        await bot.send_message(message.from_user.id, '⚒️ Инструменты', reply_markup=inline_kb)
    else:
        await bot.send_message(message.from_user.id, 'Купите подписку')
################################### Notifications ###################################

'''

@aiocron.crontab("17 16 * * *")
async def notifications():


    print('asd')

    with connection.cursor() as cursor:
        cursor.execute("""SELECT user_id FROM users WHERE notifications = 1""")
        rows = cursor.fetchall()
        
        print(rows)
        
    capit = post.cap('c')
    vol = post.cap('v')
    domin = post.cap('d')
    fear_ind = post.first_inf('f')
    spx_sv = post.spx_price()
    dow_j = post.dow()
    nasq  = post.nasq()
    bitcoin  = post.btc_price()
    usd_rub = post.usd_price()
    eur_rub = post.eur_price()
    gold_pr = post.gold_price()
    oil_pr = post.gold_price()
    spx_pr = post.spx_price()
    #dxy_pr = post.dxy_price()

    for row in rows:
        await bot.send_photo(row[0], open('photo/ind_100_total_7.jpg', 'rb'), f"{'<b>'}Общая сводка по рынку:{'</b>'} {datetime.now().date()}\n\n{'<u>'}{'<i>'}Сведения по рынку:{'</i>'}{'</u>'}\n\nРыночная капитализация: {capit}\nОбъем за 24ч: {vol}\nДоминирование BTC: {domin}\nИндекс страха и жадности - {fear_ind}\n\n{'<u>'}{'<i>'}Американские индексы:{'</i>'}{'</u>'}\n\nS&P 500: {spx_sv}\nDow Jones: {dow_j}\nNasdaq 100: {nasq}\n\n{'<u>'}{'<i>'}Ключевые события:{'</i>'}{'</u>'}\n\n{svodka_9_sob}\n\nОсновные курсы:\nBitcoin - {bitcoin}\nUSD/RUB - {usd_rub}\nEUR/RUB - {eur_rub}\nGold - {gold_pr}\nOil brent - {oil_pr}\nS&P 500 - {spx_pr}", parse_mode='HTML')
    
'''
   
    



@dp.callback_query_handler(lambda c: c.data == 'notifications')
async def notifications_rez(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id)

    '''with connection.cursor() as cursor:
        cursor.execute(f"""SELECT notifications FROM users WHERE user_id = {callback_query.from_user.id}""")
        rez = cursor.fetchone()[0]
    if rez == 0:
        inline_btn1 = types.InlineKeyboardButton(text='Включить уведомления', callback_data='vkl_not')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1)
        await bot.send_message(callback_query.from_user.id, 'Уведомления', reply_markup=inline_kb)
    if rez == 1:
        inline_btn1 = types.InlineKeyboardButton(text='Выключить уведомления', callback_data='vikl_not')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1)
        await bot.send_message(callback_query.from_user.id, 'Уведомления', reply_markup=inline_kb)
    '''
    await bot.send_message(callback_query.from_user.id, 'Данная функция находится в разработке...')

@dp.callback_query_handler(lambda c: c.data == 'vkl_not')
async def vkl_not(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id)

    with connection.cursor() as cursor:
        cursor.execute(f"""UPDATE users set notifications = 1 where user_id = {callback_query.from_user.id}""")
        connection.commit()
    
    await bot.send_message(callback_query.from_user.id, 'Данные сохранены')


@dp.callback_query_handler(lambda c: c.data == 'vikl_not')
async def vkl_not(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id)

    with connection.cursor() as cursor:
        cursor.execute(f"""UPDATE users set notifications = 0 where user_id = {callback_query.from_user.id}""")
        connection.commit()
    
    await bot.send_message(callback_query.from_user.id, 'Данные сохранены')


        
########################################################################################

####################################### Статистические данные ###########################

@dp.message_handler(filters.Text('📑 Статистические данные'))
async def cmd_test(message: types.Message):
    if str(message.from_user.id) in sub_users:
        inline_btn1 = types.InlineKeyboardButton(text='🫧 Cryptobubbles', callback_data='Cryptobubbles')
        inline_btn2 = types.InlineKeyboardButton(text='💸 Отток/приток средств криптовалютных фондов', callback_data='ott')
        inline_btn3 = types.InlineKeyboardButton(text='❗️ Liquidations', callback_data='Liquidations')
        inline_btn4 = types.InlineKeyboardButton(text='Altcoin season', callback_data='alt')
        inline_btn5 = types.InlineKeyboardButton(text='Индекс 100 криптовалют', callback_data='ind_100')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn4).add(inline_btn2).add(inline_btn3, inline_btn5)
        
        await bot.send_message(message.from_user.id, '📑 Статистические данные', reply_markup=inline_kb)
    else:
        await bot.send_message(message.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100')
async def ind_100(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        inline_btn1 = types.InlineKeyboardButton(text='7D', callback_data='ind_100_7')
        inline_btn2 = types.InlineKeyboardButton(text='30D', callback_data='ind_100_30')

        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#### 7D

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        inline_btn1 = types.InlineKeyboardButton(text='Блокчейн инфраструктура', callback_data='int_100_7_infr')
        inline_btn2 = types.InlineKeyboardButton(text='Валюта', callback_data='ind_100_7_val')
        inline_btn3 = types.InlineKeyboardButton(text='Мемы', callback_data='ind_100_7_mem')
        inline_btn4 = types.InlineKeyboardButton(text='DeFi', callback_data='ind_100_7_defi')
        inline_btn5 = types.InlineKeyboardButton(text='CeFi', callback_data='ind_100_7_cefi')
        inline_btn6 = types.InlineKeyboardButton(text='Блокчейн сервисы', callback_data='ind_100_7_service')
        inline_btn7 = types.InlineKeyboardButton(text='Игровая индустрия', callback_data='ind_100_7_game')
        inline_btn8 = types.InlineKeyboardButton(text='Total', callback_data='ind_100_7_total')

        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1).add(inline_btn2, inline_btn3, inline_btn4).add(inline_btn6, inline_btn5).add(inline_btn8, inline_btn7)

        await bot.send_message(callback_query.from_user.id, 'Индекс 100 криптовалют', reply_markup=inline_kb)
    else:
        bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'int_100_7_infr')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/block_infr_7.jpg', 'rb'), 'Блокчейн инфраструктура')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_val')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/valuta_7.jpg', 'rb'), 'Валюта')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_mem')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/mems_7.jpg', 'rb'), 'мемы')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_defi')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/defi_7.jpg', 'rb'), 'DeFi')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_cefi')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/cefi_7.jpg', 'rb'), 'CeFi')
    else:
        bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_service')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/block_serv_7.jpg', 'rb'), 'Блокчейн сервисы')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_game')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/games_7.jpg', 'rb'), 'Игровая индустрия')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_7_total')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/ind_100_total_7.jpg', 'rb'), 'Total')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

###

### 30D

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        inline_btn1 = types.InlineKeyboardButton(text='Блокчейн инфраструктура', callback_data='int_100_30_infr')
        inline_btn2 = types.InlineKeyboardButton(text='Валюта', callback_data='ind_100_30_val')
        inline_btn3 = types.InlineKeyboardButton(text='Мемы', callback_data='ind_100_30_mem')
        inline_btn4 = types.InlineKeyboardButton(text='DeFi', callback_data='ind_100_30_defi')
        inline_btn5 = types.InlineKeyboardButton(text='CeFi', callback_data='ind_100_30_cefi')
        inline_btn6 = types.InlineKeyboardButton(text='Блокчейн сервисы', callback_data='ind_100_30_service')
        inline_btn7 = types.InlineKeyboardButton(text='Игровая индустрия', callback_data='ind_100_30_game')
        inline_btn8 = types.InlineKeyboardButton(text='Total', callback_data='ind_100_30_total')

        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1).add(inline_btn2, inline_btn3, inline_btn4).add(inline_btn6, inline_btn5).add(inline_btn8, inline_btn7)

        await bot.send_message(callback_query.from_user.id, 'Индекс 100 криптовалют', reply_markup=inline_kb)
    else:
        bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'int_100_30_infr')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/block_infr_30.jpg', 'rb'), 'Блокчейн инфраструктура')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_val')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/valuta_30.jpg', 'rb'), 'Валюта')
    else:
        await bot.send_media_group(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_mem')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/mems_30.jpg', 'rb'), 'Мемы')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_defi')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/defi_30.jpg', 'rb'), 'DeFi')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_cefi')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/cefi_30.jpg', 'rb'), 'CeFi')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_service')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/block_serv_30.jpg', 'rb'), 'Блокчейн сервисы')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_game')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/games_30.jpg', 'rb'), 'Игровая индустрия')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'ind_100_30_total')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/ind_100_total_30.jpg', 'rb'), 'Total')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')





@dp.callback_query_handler(lambda c: c.data == 'alt')
async def alt(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/alt.jpg', 'rb'), 'Altcoin season')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'Liquidations')
async def liquid(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        inline_btn1 = types.InlineKeyboardButton(text='Liquidation Heatmap', callback_data='Heatmap')
        inline_btn2 = types.InlineKeyboardButton(text='Total Liquidations', callback_data='Total')
        inline_btn3 = types.InlineKeyboardButton(text='Потенциальные уровни ликвидации', callback_data='pot_liq')
        inline_btn4 = types.InlineKeyboardButton(text='Ликвидация крупных заявок', callback_data='kr_liq')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn3).add(inline_btn1, inline_btn2).add(inline_btn4)
        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, '❗️ Liquidations', reply_markup=inline_kb)
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'pot_liq')
async def pot_liq(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/poten_liq.jpg', 'rb'), 'Потенциальные уровни ликвидации')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
@dp.callback_query_handler(lambda c: c.data == 'kr_liq')
async def pot_liq(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/kr_liq.jpg', 'rb'), 'Ликвидация крупных заявок')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'Heatmap')
async def heatmap(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/Heatmap.jpg', 'rb'), 'Liquidation Heatmap')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'Total')
async def total(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, total_text)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'Cryptobubbles')
async def bubbles(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/bubbles.png', 'rb'), '🫧 Cryptobubbles')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'ott')
async def ott(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/ott.jpg', 'rb'), ott_text)
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


#########################################################################################

#################################### Расчет средней цены входа ############################


@dp.callback_query_handler(lambda c: c.data == 'ras')
async def cmd_sr(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        inline_btn1 = types.InlineKeyboardButton(text='2', callback_data='2')
        inline_btn2 = types.InlineKeyboardButton(text='3', callback_data='3')
        inline_btn3 = types.InlineKeyboardButton(text='4', callback_data='4')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2).add(inline_btn3)

        await bot.send_message(callback_query.from_user.id, 'Выберите количество позиций', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

######## Для 2 позиций
class SrForm1(StatesGroup):
    poz_1 = State()
    cl_1 = State()
    poz_2 = State()
    cl_2 = State()


@dp.callback_query_handler(lambda c: c.data == '2')
async def second(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await SrForm1.poz_1.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите цену входа первой позиции, для отмены напишите "cancel"')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.message_handler(state=SrForm1.poz_1)
async def step1(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_1'] = message.text

    if data['poz_1'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm1.next()

        await bot.send_message(message.from_user.id, 'Введите количество первой позиции')

@dp.message_handler(state=SrForm1.cl_1)
async def step1(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_1'] = message.text
    
    if data['cl_1'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Рассчет средней цены входа отменен')
    else:
        await SrForm1.next()

        await bot.send_message(message.from_user.id, 'Введите цену входа второй позиции')

@dp.message_handler(state=SrForm1.poz_2)
async def step1(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_2'] = message.text

    if data['poz_2'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm1.next()

        await bot.send_message(message.from_user.id, 'Введите количество второй позиции')

@dp.message_handler(state=SrForm1.cl_2)
async def step1(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_2'] = message.text

    if data['cl_2'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await state.finish()

        out = calculator.math2(data['poz_1'], data['cl_1'], data['poz_2'], data['cl_2'])
        await bot.send_message(message.from_user.id, f'Средняя цена открытия сделки - {out}')

#########

###### Для 3 позиций

class SrForm2(StatesGroup):
    poz_1 = State()
    cl_1 = State()
    poz_2 = State()
    cl_2 = State()
    poz_3 = State()
    cl_3 = State()

@dp.callback_query_handler(lambda c: c.data == '3')
async def second(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await SrForm2.poz_1.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите цену входа первой позиции, для отмены напишите "cancel"')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=SrForm2.poz_1)
async def step2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_1'] = message.text

    if data['poz_1'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:

        await SrForm2.next()

        await bot.send_message(message.from_user.id, 'Введите количество первой позиции')

@dp.message_handler(state=SrForm2.cl_1)
async def step2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_1'] = message.text

    if data['cl_1'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm2.next()

        await bot.send_message(message.from_user.id, 'Введите цену входа второй позиции')

@dp.message_handler(state=SrForm2.poz_2)
async def step2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_2'] = message.text

    if data['poz_2'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm2.next()

        await bot.send_message(message.from_user.id, 'Введите количество второй позиции')

@dp.message_handler(state=SrForm2.cl_2)
async def step2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_2'] = message.text

    if data['cl_2'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm2.next()

        await bot.send_message(message.from_user.id, 'Введите цену входа третей позиции')

@dp.message_handler(state=SrForm2.poz_3)
async def step2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_3'] = message.text

    if data['poz_3'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm2.next()

        await bot.send_message(message.from_user.id, 'Введите количество третей позиции')

@dp.message_handler(state=SrForm2.cl_3)
async def step2(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_3'] = message.text
    
    if data['cl_3'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await state.finish()

        out = calculator.math3(data['poz_1'], data['cl_1'], data['poz_2'], data['cl_2'], data['poz_3'], data['cl_3'])

        await bot.send_message(message.from_user.id, f'Средняя цена открытия сделки - {out}')


#############

##### Для 4 позиций


class SrForm3(StatesGroup):
    poz_1 = State()
    cl_1 = State()
    poz_2 = State()
    cl_2 = State()
    poz_3 = State()
    cl_3 = State()
    poz_4 = State()
    cl_4 = State()


@dp.callback_query_handler(lambda c: c.data == '4')
async def second(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await SrForm3.poz_1.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите цену входа первой позиции')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=SrForm3.poz_1)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_1'] = message.text
    
    if data['poz_1'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите количество первой позиции')

@dp.message_handler(state=SrForm3.cl_1)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_1'] = message.text

    if data['cl_1'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите цену входа второй позиции')

@dp.message_handler(state=SrForm3.poz_2)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_2'] = message.text

    if data['poz_2'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите количество второй позиции')

@dp.message_handler(state=SrForm3.cl_2)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_2'] = message.text

    if data['cl_2'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите цену входа третей позиции')

@dp.message_handler(state=SrForm3.poz_3)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_3'] = message.text

    if data['poz_3'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите количество третей позиции')

@dp.message_handler(state=SrForm3.cl_3)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_3'] = message.text

    if data['cl_3'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите цену входа четвертой позиции')

@dp.message_handler(state=SrForm3.poz_4)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['poz_4'] = message.text

    if data['poz_4'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await SrForm3.next()

        await bot.send_message(message.from_user.id, 'Введите количество четвертой позиции')

@dp.message_handler(state=SrForm3.cl_4)
async def step3(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['cl_4'] = message.text
    
    if data['cl_4'].lower() == 'cancel':
        await state.finish()
        await bot.send_message(message.from_user.id, 'Расчет средней цены входа отменен')
    else:
        await state.finish()

        out = calculator.math4(data['poz_1'], data['cl_1'], data['poz_2'], data['cl_2'], data['poz_3'], data['cl_3'], data['poz_4'], data['cl_4'])

        await bot.send_message(message.from_user.id, f'Средняя цена открытия сделки - {out}')
        
##############################################################################################

################################## Календари ###############################


@dp.message_handler(filters.Text('📅 Календари'))
async def cmd_calendar(message: types.Message):
    if str(message.from_user.id) in sub_users:

        inline_btn1 = types.InlineKeyboardButton(text='Экономический календарь', callback_data='econom')
        inline_btn2 = types.InlineKeyboardButton(text='Календарь дивидендов', callback_data='div')
        inline_btn3 = types.InlineKeyboardButton(text='Календарь отчетности', callback_data='otch')
        inline_btn4 = types.InlineKeyboardButton(text='IDO/IEO/ICO', callback_data='ido')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1).add(inline_btn2).add(inline_btn3).add(inline_btn4)

        await bot.send_message(message.from_user.id, '📅 Календари', reply_markup=inline_kb)
    else:
         await bot.send_message(message.from_user.id, 'Купите подписку')


###### IDO/IEO/ICO

@dp.callback_query_handler(lambda c: c.data == 'ido')
async def ido(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        inline_btn1 = types.InlineKeyboardButton(text='Предстоящие IDO/IEO/ICO', callback_data='pred')
        inline_btn2 = types.InlineKeyboardButton(text='Текущие IDO/IEO/ICO', callback_data='tek')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1).add(inline_btn2)
        await bot.send_message(callback_query.from_user.id, 'IDO/IEO/ICO', reply_markup=inline_kb)
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'tek')
async def pred(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/ido_tek.jpg', 'rb'), 'Текущие IDO/IEO/ICO')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'pred')
async def pred(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/ido_pred.jpg', 'rb'), 'Предстоящие IDO/IEO/ICO')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')  


##### Экономический календарь
@dp.callback_query_handler(lambda c: c.data == 'econom')
async def econom(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        inline_btn1 = types.InlineKeyboardButton(text='Понедельник', callback_data='mon')
        inline_btn2 = types.InlineKeyboardButton(text='Вторник', callback_data='tue')
        inline_btn3 = types.InlineKeyboardButton(text='Среда', callback_data='wen')
        inline_btn4 = types.InlineKeyboardButton(text='Четверг', callback_data='th')
        inline_btn5 = types.InlineKeyboardButton(text='Пятница', callback_data='fr')
        
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.send_message(callback_query.from_user.id, 'Экономический календарь', reply_markup=inline_kb)
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'mon')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Никаких событий нет')
        #await bot.send_photo(callback_query.from_user.id, open('photo/calendar/econom/Monday.jpeg', 'rb'))
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'tue')
async def tue(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/econom_tuesday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'wen')
async def wen(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/econom_wednesday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
        


@dp.callback_query_handler(lambda c: c.data == 'th')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/econom_thursday.jpg', 'rb'))
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'fr')
async def fr(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/econom_friday.jpg', 'rb'))
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

###



### Календарь дивидендов

@dp.callback_query_handler(lambda c: c.data == 'div')
async def div(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        inline_btn1 = types.InlineKeyboardButton(text='Понедельник', callback_data='mon2')
        inline_btn2 = types.InlineKeyboardButton(text='Вторник', callback_data='tu2')
        inline_btn3 = types.InlineKeyboardButton(text='Среда', callback_data='wen2')
        inline_btn4 = types.InlineKeyboardButton(text='Четверг', callback_data='th2')
        inline_btn5 = types.InlineKeyboardButton(text='Пятница', callback_data='fr2')
        
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.send_message(callback_query.from_user.id, 'Календарь дивидендов', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'mon2')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/div_monday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'tu2')
async def tue(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/div_tuesday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'wen2')
async def wen(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/div_wednesday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'th2')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/div_thursday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'fr2')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/div_friday.jpg', 'rb'))
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


#########

#### Календарь отчетности


@dp.callback_query_handler(lambda c: c.data == 'otch')
async def div(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        inline_btn1 = types.InlineKeyboardButton(text='Понедельник', callback_data='mon3')
        inline_btn2 = types.InlineKeyboardButton(text='Вторник', callback_data='tu3')
        inline_btn3 = types.InlineKeyboardButton(text='Среда', callback_data='wen3')
        inline_btn4 = types.InlineKeyboardButton(text='Четверг', callback_data='th3')
        inline_btn5 = types.InlineKeyboardButton(text='Пятница', callback_data='fr3')
        
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.send_message(callback_query.from_user.id, 'Календарь отчетности', reply_markup=inline_kb)
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'mon3')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/otch_monday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'tu3')
async def tue(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/otch_tuesday.jpg', 'rb'))
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'wen3')
async def wen(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/otch_wednesday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'th3')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/otch_thursday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'fr3')
async def mon(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/otch_friday.jpg', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

########


#########################################################################################

#################################### Обработка курсов монет ############################

@dp.message_handler(filters.Text('🔎 Курс монет'))
async def cmd_coins(message: types.Message):
    if str(message.from_user.id) in sub_users:
        inline_btn1 = types.InlineKeyboardButton(text='BTC', callback_data='btn1')
        inline_btn2 = types.InlineKeyboardButton(text='ETH', callback_data='btn2')
        inline_btn3 = types.InlineKeyboardButton(text='LTC', callback_data='btn3')
        inline_btn4 = types.InlineKeyboardButton(text='XRP', callback_data='btn4')
        inline_btn5 = types.InlineKeyboardButton(text='ADA', callback_data='btn5')
        inline_btn6 = types.InlineKeyboardButton(text='SOL', callback_data='btn6')
        inline_btn7 = types.InlineKeyboardButton(text='BNB', callback_data='btn7')
        inline_btn8 = types.InlineKeyboardButton(text='TRX', callback_data='btn8')
        inline_btn9 = types.InlineKeyboardButton(text='Своя монета', callback_data='btn9')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn3).add(inline_btn4, inline_btn5, inline_btn6).add(inline_btn7, inline_btn8).add(inline_btn9)

        await bot.send_message(message.from_user.id, 'Выберите монету из списка или найдите свою', reply_markup=inline_kb)
    else:
        await bot.send_message(message.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'btn1')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('BTCUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}BTC/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn2')
async def eth(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('ETHUSDT')
        
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}ETH/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn3')
async def ltc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('LTCUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}LTC/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn4')
async def xrp(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('XRPUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}XRP/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn5')
async def ada(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('ADAUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}ADA/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
         await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn6')
async def sol(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('SOLUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}SOL/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

        
@dp.callback_query_handler(lambda c: c.data == 'btn7')
async def bnb(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('BNBUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}BNB/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn8')
async def trx(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.search_binance('TRXUSDT')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}TRX/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'btn9')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await Coin.sym.set()

        await bot.answer_callback_query(callback_query.id)
        
        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.message_handler(state=Coin.sym)
async def search(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text

    await state.finish()

    inline_btn9 = types.InlineKeyboardButton(text='Вывести курс еще одной монеты', callback_data='btn9')
    inline_kb = types.InlineKeyboardMarkup().add(inline_btn9)

    out = post.search_binance(f'{data["sym"]}USDT')

    await bot.send_message(message.from_user.id, f"{'<i>'}{data['sym'].upper()}/USDT{'</i>'} - {'<b>'}{out}${'</b>'}", reply_markup=inline_kb, parse_mode='HTML')

#########################################################################################

################################### Поиск по тв #########################################


@dp.callback_query_handler(lambda c: c.data == 'tw')
async def cmd_tw(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)

        inline_btn1 = types.InlineKeyboardButton(text='BTC', callback_data='btn_tw1')
        inline_btn2 = types.InlineKeyboardButton(text='ETH', callback_data='btn_tw2')
        inline_btn3 = types.InlineKeyboardButton(text='LTC', callback_data='btn_tw3')
        inline_btn4 = types.InlineKeyboardButton(text='XRP', callback_data='btn_tw4')
        inline_btn6 = types.InlineKeyboardButton(text='SOL', callback_data='btn_tw6')
        inline_btn7 = types.InlineKeyboardButton(text='BNB', callback_data='btn_tw7')
        inline_btn9 = types.InlineKeyboardButton(text='Своя монета', callback_data='btn_tw9')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn3).add(inline_btn4, inline_btn6, inline_btn7).add(inline_btn9)

        await bot.send_message(callback_query.from_user.id, 'Введите название криптовалюты или выберите из списка ниже', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

############# BTC

@dp.callback_query_handler(lambda c: c.data == 'btn_tw1')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
    
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_btc')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_btc')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_btc')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_btc')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_btc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_b_btc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_b_btc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_b_btc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_b_btc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '15m_b_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BINANCE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_b_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BINANCE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '4h_b_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BINANCE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1d_b_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BINANCE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_bi_btc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_bi_btc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_bi_btc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_bi_btc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '15m_bi_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BITGET', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_bi_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BITGET', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '4h_bi_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BITGET', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1d_bi_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BITGET', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
####

#### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_c_btc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_c_btc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_c_btc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_c_btc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '15m_c_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('COINBASE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_c_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('COINBASE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_c_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('COINBASE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1d_c_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('COINBASE', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_k_btc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_k_btc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_k_btc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_k_btc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '15m_k_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('KRAKEN', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_k_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('KRAKEN', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_k_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('KRAKEN', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_k_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('KRAKEN', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

#### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_btc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_btc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_btc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_btc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('MEXC', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_m_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('MEXC', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_m_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('MEXC', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_m_btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('MEXC', 'BTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

###############




############# ETH

@dp.callback_query_handler(lambda c: c.data == 'btn_tw2')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_eth')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_eth')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_eth')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_eth')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_eth')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_b_eth')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_b_eth')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_b_eth')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_b_eth')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_b_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BINANCE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_b_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BINANCE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_b_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BINANCE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_b_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BINANCE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_bi_eth')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_bi_eth')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_bi_eth')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_bi_eth')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_bi_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BITGET', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_bi_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BITGET', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_bi_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BITGET', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_bi_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BITGET', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
####

#### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_c_eth')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_c_eth')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_c_eth')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_c_eth')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_c_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('COINBASE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_c_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('COINBASE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_c_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('COINBASE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_c_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('COINBASE', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_k_eth')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_k_eth')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_k_eth')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_k_eth')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_k_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('KRAKEN', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_k_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('KRAKEN', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_k_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('KRAKEN', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_k_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('KRAKEN', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

    #####

#### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_eth')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_eth')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_eth')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_eth')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('MEXC', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_m_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('MEXC', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_m_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('MEXC', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_m_eth')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('MEXC', 'ETHUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id)
###############


############# LTC

@dp.callback_query_handler(lambda c: c.data == 'btn_tw3')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
    
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_ltc')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_ltc')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_ltc')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_ltc')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_ltc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_b_ltc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_b_ltc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_b_ltc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_b_ltc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_b_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BINANCE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id)

@dp.callback_query_handler(lambda c: c.data == '1h_b_ltc')
async def btc(callback_query: types.CallbackQuery):
    aio_test.tw_grapth1h('BINANCE', 'LTCUSDT')
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))

@dp.callback_query_handler(lambda c: c.data == '4h_b_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BINANCE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_b_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BINANCE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_bi_ltc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_bi_ltc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_bi_ltc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_bi_ltc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_bi_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BITGET', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_bi_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BITGET', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_bi_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BITGET', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_bi_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BITGET', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
####

#### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_c_ltc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_c_ltc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_c_ltc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_c_ltc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_c_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('COINBASE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите юодписку')

@dp.callback_query_handler(lambda c: c.data == '1h_c_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('COINBASE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_c_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('COINBASE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_c_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('COINBASE', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


#####

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_k_ltc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_k_ltc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_k_ltc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_k_ltc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_k_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('KRAKEN', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_k_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('KRAKEN', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_k_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('KRAKEN', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_k_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('KRAKEN', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

#### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_ltc')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_ltc')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_ltc')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_ltc')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '15m_m_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('MEXC', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_m_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('MEXC', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_m_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('MEXC', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_m_ltc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('MEXC', 'LTCUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
###############


############# XRP

@dp.callback_query_handler(lambda c: c.data == 'btn_tw4')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
    
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_xrp')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_xrp')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_xrp')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_xrp')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_xrp')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_b_xrp')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_b_xrp')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_b_xrp')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_b_xrp')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_b_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BINANCE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_b_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BINANCE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_b_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BINANCE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_b_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BINANCE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_bi_xrp')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_bi_xrp')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_bi_xrp')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_bi_xrp')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_bi_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BITGET', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_bi_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BITGET', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_bi_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BITGET', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_bi_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BITGET', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

####

#### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_c_xrp')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_c_xrp')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_c_xrp')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_c_xrp')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_c_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('COINBASE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_c_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('COINBASE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_c_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('COINBASE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_c_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('COINBASE', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_k_xrp')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_k_xrp')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_k_xrp')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_k_xrp')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_k_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('KRAKEN', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_k_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('KRAKEN', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_k_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('KRAKEN', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_k_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('KRAKEN', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

#### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_xrp')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_xrp')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_xrp')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_xrp')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('MEXC', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_m_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('MEXC', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_m_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('MEXC', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_m_xrp')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('MEXC', 'XRPUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

###############


############# SOL

@dp.callback_query_handler(lambda c: c.data == 'btn_tw6')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
    
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_sol')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_sol')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_sol')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_sol')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_sol')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_b_sol')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_b_sol')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_b_sol')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_b_sol')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_b_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BINANCE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_b_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BINANCE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_b_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BINANCE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_b_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BINANCE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_bi_sol')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_bi_sol')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_bi_sol')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_bi_sol')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_bi_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BITGET', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_bi_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BITGET', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подпису')

@dp.callback_query_handler(lambda c: c.data == '4h_bi_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BITGET', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_bi_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BITGET', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

####

#### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_c_sol')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_c_sol')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_c_sol')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_c_sol')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_c_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('COINBASE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '1h_c_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('COINBASE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_c_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('COINBASE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_c_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('COINBASE', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_k_sol')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_k_sol')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_k_sol')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_k_sol')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_k_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('KRAKEN', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_k_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('KRAKEN', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_k_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('KRAKEN', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_k_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('KRAKEN', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
#####

#### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_sol')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_sol')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_sol')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_sol')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('MEXC', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_m_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('MEXC', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
        
@dp.callback_query_handler(lambda c: c.data == '4h_m_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('MEXC', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_m_sol')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('MEXC', 'SOLUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

###############


############# BNB

@dp.callback_query_handler(lambda c: c.data == 'btn_tw7')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
    
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_bnb')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_bnb')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_bnb')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_bnb')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_bnb')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_b_bnb')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_b_bnb')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_b_bnb')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_b_bnb')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_b_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BINANCE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_b_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BINANCE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
        
@dp.callback_query_handler(lambda c: c.data == '4h_b_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BINANCE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_b_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BINANCE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_bi_bnb')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_bi_bnb')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_bi_bnb')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_bi_bnb')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == '15m_bi_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('BITGET', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_bi_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('BITGET', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_bi_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('BITGET', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_bi_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('BITGET', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

####

#### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_c_bnb')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_c_bnb')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_c_bnb')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_c_bnb')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_c_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('COINBASE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_c_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('COINBASE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_c_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('COINBASE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_c_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('COINBASE', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_k_bnb')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_k_bnb')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_k_bnb')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_k_bnb')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_k_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('KRAKEN', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_k_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('KRAKEN', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_k_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('KRAKEN', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_k_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('KRAKEN', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

#####

#### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_bnb')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_bnb')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_bnb')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_bnb')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth15('MEXC', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1h_m_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1h('MEXC', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '4h_m_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth4h('MEXC', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '1d_m_bnb')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        aio_test.tw_grapth1d('MEXC', 'BNBUSDT')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, open('photo/tw.png', 'rb'))
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подпсику')

###############

############# Своя монета


@dp.callback_query_handler(lambda c: c.data == 'btn_tw9')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
    
        inline_btn1 = types.InlineKeyboardButton(text='Binance', callback_data='binance_s')
        inline_btn2 = types.InlineKeyboardButton(text='Bitget', callback_data='bitget_s')
        inline_btn3 = types.InlineKeyboardButton(text='Сoinbase', callback_data='coinbase_s')
        inline_btn4 = types.InlineKeyboardButton(text='MEXC', callback_data='mexc_s')
        inline_btn5 = types.InlineKeyboardButton(text='Kraken', callback_data='kraken_s')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2, inline_btn5).add(inline_btn3, inline_btn4)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select exchange', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

##### Binance

@dp.callback_query_handler(lambda c: c.data == 'binance_s')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_s_b')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_s_b')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_s_b')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_s_b')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')
        
@dp.callback_query_handler(lambda c: c.data == '15m_m_s_b')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_binance15.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_binance15.sym)
async def binance_s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth15('BINANCE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

@dp.callback_query_handler(lambda c: c.data == '1h_m_s_b')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_binance1h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_binance1h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1h('BINANCE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '4h_m_s_b')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_binance4h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_binance4h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth4h('BINANCE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '1d_m_s_b')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_binance1d.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_binance1d.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1d('BINANCE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######


##### Bitget

@dp.callback_query_handler(lambda c: c.data == 'bitget_s')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_s_bi')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_s_bi')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_s_bi')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_s_bi')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)
        
        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_s_bi')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_bitget15.sym.set()
        
        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_bitget15.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth15('BITGET', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

@dp.callback_query_handler(lambda c: c.data == '1h_m_s_bi')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_bitget1h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_bitget1h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1h('BITGET', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '4h_m_s_bi')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_bitget4h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_bitget4h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth4h('BITGET', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '1d_m_s_bi')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_bitget1d.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_bitget1d.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1d('BITGET', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

##### Coinbase

@dp.callback_query_handler(lambda c: c.data == 'coinbase_s')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_s_c')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_s_c')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_s_c')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_s_c')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_s_c')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_coinbase15.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_coinbase15.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth15('COINBASE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

@dp.callback_query_handler(lambda c: c.data == '1h_m_s_c')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_coinbase1h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'купите подписку')

@dp.message_handler(state=Form_coinbase1h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1h('COINBASE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '4h_m_s_c')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_coinbase4h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_coinbase4h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth4h('COINBASE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '1d_m_s_c')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_coinbase1d.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_coinbase1d.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1d('COINBASE', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

##### MEXC

@dp.callback_query_handler(lambda c: c.data == 'mexc_s')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_s_m')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_s_m')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_s_m')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_s_m')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_s_m')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_mexc15.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_mexc15.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth15('MEXC', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

@dp.callback_query_handler(lambda c: c.data == '1h_m_s_m')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_mexc1h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_mexc1h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1h('MEXC', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '4h_m_s_m')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_mexc4h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_mexc4h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth4h('MEXC', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '1d_m_s_m')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_mexc1d.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_mexc1d.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1d('MEXC', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

##### Kraken

@dp.callback_query_handler(lambda c: c.data == 'kraken_s')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        inline_btn2 = types.InlineKeyboardButton(text='15 minutes', callback_data='15m_m_s_k')
        inline_btn3 = types.InlineKeyboardButton(text='1 hour', callback_data='1h_m_s_k')
        inline_btn4 = types.InlineKeyboardButton(text='4 hours', callback_data='4h_m_s_k')
        inline_btn5 = types.InlineKeyboardButton(text='1 day', callback_data='1d_m_s_k')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn2, inline_btn3).add(inline_btn4, inline_btn5)

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Select TimeFrame',reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == '15m_m_s_k')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_kraken15.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_kraken15.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth15('KRAKEN', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######

@dp.callback_query_handler(lambda c: c.data == '1h_m_s_k')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_kraken1h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_kraken1h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1h('KRAKEN', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '4h_m_s_k')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_kraken4h.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_kraken4h.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth4h('KRAKEN', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

####

@dp.callback_query_handler(lambda c: c.data == '1d_m_s_k')
async def btc(callback_query: types.CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) in sub_users:

        await Form_kraken1d.sym.set()

        await bot.answer_callback_query(callback_query.id)

        await bot.send_message(callback_query.from_user.id, 'Введите монету в формате: "btc или BTC и т.д"')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.message_handler(state=Form_kraken1d.sym)
async def s(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['sym'] = message.text
    
    await state.finish()

    aio_test.tw_grapth1d('KRAKEN', f'{data["sym"]}USDT')

    await bot.send_photo(message.from_user.id, open('photo/tw.png', 'rb'))

######




#######################################################################################

################################### Общая информация о рынке ###########################


@dp.message_handler(filters.Text('ℹ️ Общая информация о рынке'))
async def general_information(message: types.Message):
    if str(message.from_user.id) in sub_users:

        inline_btn1 = types.InlineKeyboardButton(text='Капитализация рынка', callback_data='cap')
        inline_btn2 = types.InlineKeyboardButton(text='📌 Индекс доминирования BTC', callback_data='dom')
        inline_btn3 = types.InlineKeyboardButton(text='Индекс страха и жадности', callback_data='fear')
        inline_btn4 = types.InlineKeyboardButton(text='Объем за 24 часа', callback_data='volue')
        inline_btn5 = types.InlineKeyboardButton(text='Основные котировки', callback_data='bitcoin')
        inline_btn6 = types.InlineKeyboardButton(text='Сводка по SPX', callback_data='svodka')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn5, inline_btn1).add(inline_btn6, inline_btn2, inline_btn4).add(inline_btn3)
        
        await bot.send_message(message.from_user.id, 'Select', reply_markup=inline_kb)
    else:
        await bot.send_message(message.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'svodka')
async def svodka(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)

        await bot.send_photo(callback_query.from_user.id, open('photo/spx.png', 'rb'), f"{'<b>'}SPX 500{'</b>'} {post.spx_price()}$\n\nКлючевые события: {'<b>'}{svodka_date}{'</b>'}\n\n{svodka_sob}\n\nКлючевые отчетности: {'<b>'}{svodka_date}{'</b>'}\n\n{svodka_otc}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')



@dp.callback_query_handler(lambda c: c.data == 'cap')
async def cap(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.cap('c')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Капитализация рынка{'</i>'} - {'<b>'}{out}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')


@dp.callback_query_handler(lambda c: c.data == 'dom')
async def dom(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.cap('d')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Индекс доминирования BTC - {'</i>'}{'<b>'}{out[5:]}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'volue')
async def volue(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.cap('v')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Объем за 24 часа{'</i>'} - {'<b>'}{out}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'fear')
async def fear(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.first_inf('f')
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Индекс страха и жадности{'</i>'} - {'<b>'}{out}%{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'bitcoin')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        

        inline_btn1 = types.InlineKeyboardButton(text='Bitcoin', callback_data='btc')
        inline_btn2 = types.InlineKeyboardButton(text='USD/RUB', callback_data='usdrub')
        inline_btn3 = types.InlineKeyboardButton(text='EUR/RUB', callback_data='eurrub')
        inline_btn4 = types.InlineKeyboardButton(text='Gold', callback_data='gold')
        inline_btn5 = types.InlineKeyboardButton(text='Oil brent', callback_data='oil')
        inline_btn6 = types.InlineKeyboardButton(text='S&P 500', callback_data='spx')
        inline_btn7 = types.InlineKeyboardButton(text='DXY', callback_data='dxy')
        inline_kb = types.InlineKeyboardMarkup().add(inline_btn1, inline_btn2).add(inline_btn3, inline_btn4, inline_btn5).add(inline_btn6, inline_btn7)

        await bot.send_message(callback_query.from_user.id, 'Select', reply_markup=inline_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'btc')
async def btc(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.btc_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Bitcoin{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'usdrub')
async def usd(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.usd_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}USD/RUB{'</i>'} -{'<b>'}{out}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'eurrub')
async def eur(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.eur_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}EUR/RUB{'</i>'} - {'<b>'}{out}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'gold')
async def gold(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:

        await bot.answer_callback_query(callback_query.id)
        out = post.gold_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Gold{'</i>'} - {'<b>'}{out}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'oil')
async def oil(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.oil_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}Oil brent{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'spx')
async def spx(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.spx_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}S&P 500{'</i>'} - {'<b>'}{out}${'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписку')

@dp.callback_query_handler(lambda c: c.data == 'dxy')
async def dxy(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) in sub_users:
        await bot.answer_callback_query(callback_query.id)
        out = post.dxy_price()
        await bot.send_message(callback_query.from_user.id, f"{'<i>'}DXY{'</i>'} - {'<b>'}{out}{'</b>'}", parse_mode='HTML')
    else:
        await bot.send_message(callback_query.from_user.id, 'Купите подписки')



################################# Админ-панель #######################################

class Photo(StatesGroup):
    name = State()

admin_users = [705894431, 797705042]

names = ['alt', 'div_friday', 'div_monday', 'div_thursday', 'div_tuesday', 'div_wednesday', 'econom_friday', 'econom_monday', 'econom_thursday', 'econom_tuesday', 'econom_wednesday', 'Heatmap', 'ido_pred', 'ido_tek', 'otch_monday', 'otch_thursday', 'otch_tuesday', 'otch_wednesday', 'ott', 'block_infr_7', 'block_serv_7', 'cefi_7', 'defi_7', 'games_7', 'mems_7', 'ind_100_total_30', 'ind_100_total_7', 'valuta_7', 'block_infr_30', 'block_serv_30', 'cefi_30', 'defi_30', 'games_30', 'mems_30', 'valuta_30', 'kr_liq', 'poten_liq', 'otch_friday']

@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message, state: FSMContext):
    if message.from_user.id in admin_users:
        await Photo.name.set()
        await bot.send_message(message.from_user.id, f'Ведите имя файла\n\n{names}')
        await message.photo[-1].download(destination_file='/Users/viktorshpakovskij/Step/Crypto_tg/photo/ggg.jpg')
    

@dp.message_handler(state=Photo.name)
async def rename(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['name'] = message.text
    
    await state.finish()

    if data['name'] in names:
        
        os.remove(f'/Users/viktorshpakovskij/Step/Crypto_tg/photo/{data["name"]}.jpg')

        os.rename('/Users/viktorshpakovskij/Step/Crypto_tg/photo/ggg.jpg', f'/Users/viktorshpakovskij/Step/Crypto_tg/photo/{data["name"]}.jpg')

        await bot.send_message(message.from_user.id, '[INFO] CОХРАНЕНИЕ ПРОИЗОШЛО УСПЕШНО')

    else:
        await bot.send_message(message.from_user.id, '[INFO] ДОПУЩЕНА ОШИБКА В ИМЕНИ!')


class Svod(StatesGroup):
    date = State()
    sob = State()
    otc = State()

@dp.message_handler(commands=['svodka_spx'])
async def svodka(message: types.Message):
    if message.from_user.id in admin_users:

        await Svod.date.set()

        await bot.send_message(message.from_user.id, 'Введите дату в формате: 17 августа')

@dp.message_handler(state=Svod.date)
async def date(message: types.Message, state: FSMContext):
    global svodka_date

    async with state.proxy() as data:
        data['date'] = message.text

    svodka_date = data['date']

    await Svod.next()

    await bot.send_message(message.from_user.id, 'Введите ключевые события')

@dp.message_handler(state=Svod.sob)
async def sob(message: types.Message, state: FSMContext):
    global svodka_sob

    async with state.proxy() as data:
        data['sob'] = message.text
    
    svodka_sob = data['sob']

    await Svod.next()

    await bot.send_message(message.from_user.id, 'Введите ключевые отчетности')

@dp.message_handler(state=Svod.otc)
async def otc(message: types.Message, state: FSMContext):
    global svodka_otc

    async with state.proxy() as data:
        data['otc'] = message.text

    svodka_otc = data['otc']

    await state.finish()

    await bot.send_message(message.from_user.id, 'Данные сохранены!')


class Ott(StatesGroup):
    text_ott = State()

@dp.message_handler(commands=['ott'])
async def ott_pr(message: types.Message):
    if message.from_user.id in admin_users:
        await Ott.text_ott.set()

        await bot.send_message(message.from_user.id, 'Введите текст')

@dp.message_handler(state=Ott.text_ott)
async def ott_pr2(message: types.Message, state: FSMContext):
    global ott_text

    async with state.proxy() as data:
        data['text_ott'] = message.text

    await state.finish()

    ott_text = data['text_ott']

    await bot.send_message(message.from_user.id, 'Gotovo!')

class Total_liq(StatesGroup):
    total = State()

@dp.message_handler(commands=['total_liq'])
async def total_liq(message: types.Message):
    if message.from_user.id in admin_users:

        await Total_liq.total.set()

        await bot.send_message(message.from_user.id, 'Введите текст')

@dp.message_handler(state=Total_liq.total)
async def total_liq2(message: types.Message, state: FSMContext):
    global total_text

    async with state.proxy() as data:
        data['total'] = message.text
    
    await state.finish()

    total_text = data['total']

    await bot.send_message(message.from_user.id, 'Gotovo!')


class Svodka_9(StatesGroup):
    sob = State()


@dp.message_handler(commands=['svodka_9'])
async def svodka_9(message: types.Message):
    if message.from_user.id in admin_users:

        await Svodka_9.sob.set()

        await bot.send_message(message.from_user.id, 'Введите ключевые события')

@dp.message_handler(state=Svodka_9.sob)
async def svodka_9_state(message: types.Message, state: FSMContext):
    global svodka_9_sob

    async with state.proxy() as data:
        data['sob'] = message.text

    svodka_9_sob = data['sob']

    await state.finish()

    await bot.send_message(message.from_user.id, 'Gotovo!')

class Add_user(StatesGroup):
    user = State()


@dp.message_handler(commands=['add_user'])
async def add_user(message: types.Message):

    if message.from_user.id in admin_users:

        await Add_user.user.set()

        await bot.send_message(message.from_user.id, 'Введите id пользователя')


@dp.message_handler(state=Add_user.user)
async def add_state(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['id'] = message.text

    await state.finish()

    with connection.cursor() as cursor:
        cursor.execute(f"""UPDATE users set subscription = 0 where user_id = {str(data['id'])}""")
    
    await bot.send_message(message.from_user.id, '[INFO] База данный обновлена')


class Del_user(StatesGroup):
    user = State()

@dp.message_handler(commands=['del_user'])
async def del_user(message: types.Message):

    if message.from_user.id in admin_users:

        await Del_user.user.set()

        await bot.send_message(message.from_user.id, 'Введите id пользователя')

@dp.message_handler(state=Del_user.user)
async def del_state(message: types.Message, state: FSMContext):


    async with state.proxy() as data:
        data['id'] = message.text

    await state.finish()

    with connection.cursor() as cursor:
        cursor.execute(f"""UPDATE users set subscription = 1 where user_id = {str(data['id'])}""")
    
    await bot.send_message(message.from_user.id, '[INFO] База данный обновлена')





def db():
    global sub_users
    us = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT user_id FROM users WHERE subscription = 0''')
        rez = cursor.fetchall()
        for i in rez:
                us.append(i[0])
    print(us)
    sub_users = us
    time.sleep(60)
    db()
    

#############################################################################################

if __name__ == '__main__':

    try:

        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM users""")
            rows = cursor.fetchall()
            if len(rows) != 0:
                for row in rows:
                    if row[0] not in users:
                        users.append(row[0])
        print('[INFO] Database started successfully')
        print(sub_users)
           

        thr1 = threading.Thread(target=aio_test.bubbles)
        thr2 = threading.Thread(target=db)
        thr1.start()
        thr2.start()
        executor.start_polling(dp, skip_updates=True)
    except:
        print('[INFO] Error')
    