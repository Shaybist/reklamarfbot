import telebot
from telebot import types

TOKEN = '8377378580:AAGrtQsO2nwa7bHBxTXg9uFmWMuC19aWejI'

import time
time.sleep(5)

bot = telebot.TeleBot(TOKEN)

welcome_message_id = None
message_ids_to_delete = []

#Приветственное сообщение
@bot.message_handler(commands=['start'])
def welcome(message):
    global welcome_message_id, message_ids_to_delete
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('👨‍💼 Путь КЛИЕНТА')
    btn2 = types.KeyboardButton('👨‍💼 Путь АГЕНТА')
    btn3 = types.KeyboardButton('🔗 Реферальная ссылка')
    btn4 = types.KeyboardButton('👤 Мои данные')
    btn5 = types.KeyboardButton('👑 Купить бот')
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    photo1 = open('photo1.jpg', 'rb')
    voice1 = open('voice1.ogg', 'rb')
    try:
        sent_message = bot.send_photo(message.chat.id, photo1, 'Присоединяйтесь и получайте информацию в:\n\n🅰️ Нашем чате и 🅰️ Нашем канале.\n\n<blockquote>Чтобы получить такого же бота и настроить под свои бизнес ссылки вам необходимо будет оплатить 👑 <b>Подписку PRO</b>, а так же, мы предоставим пошаговые действия АГЕНТА и обучение, чтобы вы вышли на доход более 100 000 рублей в месяц.</blockquote>\n\n♨️ Разверните главное меню и выберите нужные пункты <b>АльфаБОТа</b>👇 начните с 👨‍💼 <b>Путь КЛИЕНТА</b> и выполните все целевые действия.\n\n🗣 Прослушайте <u><b>голосовое сообщение</b></u> и получите в подарок 500 рублей 👇', parse_mode='HTML', reply_markup=markup)
        sent_message = bot.send_voice(message.chat.id, voice1)
        welcome_message_id = sent_message.message_id
        message_ids_to_delete.clear()
    except Exception as e:
        print(f"Ошибка при отправке приветственного сообщения: {str(e)}")

#Кнопки на клавиатуре
@bot.message_handler()
def a2(message):
    global welcome_message_id, message_ids_to_delete

    if message.message_id != welcome_message_id:
        message_ids_to_delete.append(message.message_id)

    btn = types.InlineKeyboardMarkup()
    bot_message = None

    try:
        if message.text == '👨‍💼 Путь КЛИЕНТА':
            btn.add(types.InlineKeyboardButton('🅰️ Дебетовая карта', callback_data='card'))
            btn.add(types.InlineKeyboardButton('🧠 Памятка клиента', url='https://telegra.ph/AlfaMLM---pamyatka-klienta-11-15'))
            btn.add(types.InlineKeyboardButton('👌 Я получил карту', callback_data='getcard'))
            photo2 = open('photo2.jpg', 'rb')
            bot_message = bot.send_photo(message.chat.id, photo2,'<b><u>Данный раздел сопровождает КЛИЕНТОВ</u> и дает пошаговые действия, чтобы ваша карта была бесплатной и с максимальными бонусами.</b>\n\n1️⃣ Предварительно ознакомьтесь и воспользуйтесь памяткой клиента во время получения карты.\n\n2️⃣ После получения карты, нажмите кнопку внизу 👌 <b>Я получил карту</b>.\n\n<blockquote><b>Контакты вашего пригласителя:</b>\n================\nВас пригласил ___ ___\nТелефон: ___________\nE-mail: ___\n================</blockquote>', parse_mode='HTML', reply_markup=btn)

        elif message.text == '👨‍💼 Путь АГЕНТА':
            btn.add(types.InlineKeyboardButton('🅰️ Стать агентом', callback_data='beagent'))
            btn.add(types.InlineKeyboardButton('👛 ПЕРЕЙТИ К ОПЛАТЕ', callback_data='pay'))
            photo4 = open('photo4.jpg', 'rb')
            bot_message = bot.send_photo(message.chat.id, photo4, '⛔️ У вас ограниченный доступ к разделу 👨‍💼 <b>Путь АГЕНТА</b>. Перейдите к оплате и получите полный доступ.\nРаздел 🎓 <b>Обучение</b> доступен по 👑 <b>Подписке PRO</b>\n\n<blockquote><b>Контакты вашего пригласителя:</b>\n================\nВас пригласил ___ ___\nТелефон: ___________\nE-mai: ___\n================</blockquote>', parse_mode='HTML', reply_markup=btn)


        elif message.text == '🔗 Реферальная ссылка':
            btn.add(types.InlineKeyboardButton('👛 ПЕРЕЙТИК ОПЛАТЕ', callback_data='pay'))
            photo11 = open('photo11.jpg', 'rb')
            voice5 = open('voice5.ogg', 'rb')
            bot_message = bot.send_photo(message.chat.id, photo11, 'Все кто перейдет по вашей реферальной ссылке, будут закреплены за вами.\n\n⛔️ <b>У вас нету доступа к реферальной ссылке. Передите к оплате и получите полный доступ.</b>', parse_mode='HTML')
            bot_message = bot.send_voice(message.chat.id, voice5, reply_markup=btn)

        elif message.text == '👤 Мои данные':
            btn = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('💲 Баланс', callback_data='balance')
            btn2 = types.InlineKeyboardButton('⚙️ Настройки', callback_data='settings')
            btn3 = types.InlineKeyboardButton('👛 ПЕРЕЙТИ К ОПЛАТЕ', callback_data='pay')
            btn.add(btn1,btn2)
            btn.add(btn3)
            photo13 = open('photo13.jpg', 'rb')
            bot_message = bot.send_photo(message.chat.id, photo13, 'Ваш 🆔 в боте: \n\nФИО: \nТелефон: \nE-mail: \n\n⛔️ <b>У вас ограниченный доступ к AльфаБОТу. Перейдите к оплате и получите полный доступ.</b>', parse_mode='HTML', reply_markup=btn)


        elif message.text == '👑 Купить бот':
            btn.add(types.InlineKeyboardButton('💳 Перевод или СБП', callback_data='pay'))
            photo9 = open('photo9.jpg', 'rb')
            voice9 = open('voice9.ogg', 'rb')
            bot_message = bot.send_photo(message.chat.id, photo9,  '<b>Активируйте себе бота с вашими реферальными ссылками на:</b>\n\n1️⃣ Дебетовая карта\n2️⃣ Агентская ссылка\n\n<b><u>Вы получаете % от оплат ваших партнеров:</u>\n1 линия (лично приглашенные)</b> - 15% от суммы оплаты (Подписка, дополнительные услуги, обучение и курсы).\n<b>2 линия</b> - 10% от суммы оплаты\n<b>3 линия</b> - 5% от суммы оплаты\n\nВы можете приглашать агентов и получить за них вознаграждения. Создавать пассивный доход с 🅰️льфаБОТ.\n\nВопросы и ответы | Договор Оферты | Политика\n\nНажмите внизу 💳 <b>Перевод или СБП</b> и выберите удобный тариф 👇', parse_mode='HTML')
            bot_message = bot.send_voice(message.chat.id, voice9, reply_markup=btn)

        else:
            bot_message = bot.send_message(message.chat.id, "Команда не распознана.")

        if bot_message:
            message_ids_to_delete.append(bot_message.message_id)

        for msg_id in message_ids_to_delete[:-2]:
            if msg_id != welcome_message_id:
                try:
                    bot.delete_message(message.chat.id, msg_id)
                except Exception as e:
                    print(f"Не удалось удалить сообщение {msg_id}: {str(e)}")

        message_ids_to_delete = [welcome_message_id] + message_ids_to_delete[-2:]
    except Exception as e:
        print(f"Ошибка при обработке сообщения: {str(e)}")

#Коллбэки кнопок
@bot.callback_query_handler(func=lambda callback: True)
def a3(callback):
    global welcome_message_id, message_ids_to_delete

    if callback.message.message_id != welcome_message_id:
        message_ids_to_delete.append(callback.message.message_id)

    btn = types.InlineKeyboardMarkup()
    bot_message = None

    try:
        if callback.data == 'card':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('❤️ Любимый кэшбек', url='https://alfabank.ru/lp/retail/dc/flexible-agent/?platformId=alfapartners_msv_DC-flexible_221520_4005636&utm_source=alfapartners&utm_medium=msv&utm_term=DC-flexible&utm_campaign=221520be&utm_content=alfapartners_msv_DC-flexible_221520_4005636')
            btn2 = types.InlineKeyboardButton('👨‍💼 Для своих', url='https://xplatform.alfabank.ru/universal-dc-form-web-ui/msv-questionnaire/offer?utm=DC-msv_221520_4005604_utm_source=alfapartners_utm_medium=msv_utm_term=DC-msv_utm_campaign=221520_utm_content=alfapartners_msv_DC-msv_221520_4005604')
            btn3 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back1')
            btn4 = types.InlineKeyboardButton('👌 Получить карту', callback_data='getcard')
            markup.add(btn1, btn2)
            markup.add(btn3, btn4)
            photo3 = open('photo3.jpg', 'rb')
            voice2 = open('voice2.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo3, '1️⃣<b> Ниже вы можете просмотреть видео и выбрать свою Альфа-карту:</b>',  parse_mode='HTML')
            bot_message = bot.send_message(callback.message.chat.id, '📺 <a href="https://youtu.be/lVKRcgSEcVc">Смотрите видео</a> 👇', parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice2, '<blockquote>Карта ❤️ <b><u>Любимый кэшбэк</u></b> только для новых клиентов.\nЕсли вы ранее были клиентом банка, вам выгоднее выбрать карту 👨‍💼<b><u> Для своих.</u></b></blockquote>\n\n2️⃣ <b>Оформите</b> подходящую вам <b>Альфа-карту </b>👇', parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'getcard':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back1')
            markup.add(btn1)
            photo2 = open('photo2.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo2, '<b><u>Выполните все действия и вы получите высокую одобряемость кредитов и пониженные ставки, а так же, дополнительные индивидуальные предложения от Альфа Банка:</u></b>\n\n1️⃣ <b>Госуслуги</b> - инструкция подключения.\n\n2️⃣ <b>Основной СБП</b> - инструкция подключения.\n\n3️⃣ <b>Выбираем кэшбек</b> - инструкция как выбрать категории и крутить барабан 100%.\n4️⃣ <b>Первая транзакция:</b>\n- Пополняем карту на более 1000₽\n- Совершаем первую транзакцию в магазине или маркетплейсе на сумму более 1000₽\n\n<b><u>Дополнительные полезные материалы:</u></b>\n\n5️⃣ <b>Оплата Штрафов ГИБДД</b> - инструкция оплаты.\n\n6️⃣ <b>Оплата ЖКУ/ЖКХ</b> - инструкция оплаты.\n\n<b><u>Используйте дебетовую карту по максимум и вы не разочаруетесь, такое дает только Альфа Банк</u></b>', parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'step3':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('💻 Личный кабинет👨‍💼', url='https://www.google.com')
            btn2 = types.InlineKeyboardButton('✅ Готовые ответы👨‍💻', url='https://telegra.ph/Testirovanie-Agenta-11-18')
            btn3 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back3')
            btn4 = types.InlineKeyboardButton('🎓 Обучение', callback_data='lesson')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3, btn4)
            photo7 = open('photo7.jpg', 'rb')
            voice4 = open('voice4.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo7, f'<b>💰 Получите первые 2️⃣ балла (от <u>200</u> рублей)?</b>\n\n1️⃣ Перейдите в личный кабинет 👨‍💼<b> АГЕНТА</b>:\n<blockquote>🔻 Выберите в меню<b> ОБУЧЕНИЕ</b>\n🔻 Начните <b>тестирование</b>\n🔻 Ответьте на 10 вопросов</blockquote>\n\n✅ Мы подготовили для вас готовые ответы на тестирование.', parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice4, reply_markup=markup)

        elif callback.data == 'lesson':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('1️⃣ Знакомство', callback_data='pro')
            btn2 = types.InlineKeyboardButton('2️⃣ Касание', callback_data='pro')
            btn3 = types.InlineKeyboardButton('3️⃣ Соц. сети', callback_data='pro')
            btn4 = types.InlineKeyboardButton('4️⃣ Таргетинг', callback_data='pro')
            btn5 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back5')
            markup.add(btn1,btn2)
            markup.add(btn3,btn4)
            markup.add(btn5)
            photo8 = open('photo8.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo8, f'Каждый пункт - это ваш путь к успеху, как работать и продвигать вашу модель бизнеса!', parse_mode='HTML',reply_markup=markup)


        elif callback.data == 'pro':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('👑 Купить подписку PRO', callback_data='pay'))
            markup.add(types.InlineKeyboardButton('📄 Истроия оплат', callback_data='history'))
            photo9 = open('photo9.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo9, f'Чтобы воспользоваться всеми преимуществами нашего бота, нужно приобрести 👑 подписку PRO.', parse_mode='HTML', reply_markup=markup)


        elif callback.data == 'history':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton('⬅️ Назад', callback_data='back7'))
            photo10 = open('photo10.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo10, f'История оплаты платной подписки:\n\nВы еще не оплачивали платную подписку', parse_mode='HTML', reply_markup=btn)


        elif callback.data == 'pay':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('1 мес.', url='https://t.me/gyuzel_fayzrahmanova')
            btn2 = types.InlineKeyboardButton('3 мес.', url='https://t.me/gyuzel_fayzrahmanova')
            btn3 = types.InlineKeyboardButton('6 мес.', url='https://t.me/gyuzel_fayzrahmanova')
            btn4 = types.InlineKeyboardButton('12 мес.', url='https://t.me/gyuzel_fayzrahmanova')
            btn5 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back5')
            markup.add(btn1, btn2)
            markup.add(btn3, btn4)
            markup.add(btn5)
            photo12 = open('photo12.jpg', 'rb')
            voice6 = open('voice6.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo12, f'<b><u>Выберите на какой период вы хотите активировать АльфаБОТ и отправьте ваш 🆔</u></b>.\n\n1 мес. - <b>600 руб./мес.</b>\n3 мес. - <b>1620 руб. (540 руб./мес.)</b>\n6 мес. - <b>3060 руб. (510 руб./мес.)</b>\n12 мес. - <b>4690 руб. (390 руб/мес.)</b>\n\n<b>Это ваш 🆔: </b>\n\n<i>Если не получилось перейти по кнопке, пишите 👉 </i>', parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice6, reply_markup=markup)

        elif callback.data == 'balance':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('💵 Продлить подписку', callback_data='buypro'))
            markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data='back6'))
            photo14 = open('photo14.jpg', 'rb')
            voice7 = open('voice7.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo14, f'<b>Ваш баланс: 0 ₽</b>\n\nБаланс накапливается за счет активности ваших действий и покупка услуг по вашей реферальной ссылке.\n\n<b>За рекомендацию АльфаБОТ, вы будете получать вознаграждение:</b> \n✔️ 1-ая линия 15%\n✔️ 2-ая линия 10%\n✔️ 3-я линия 5%\n\nИспользуйте вашу реферальную ссылку на АльфаБОТ и получайте не только новых клиентов и агентов, но и вознаграждение за рекомендации.', parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice7, reply_markup=markup)

        elif callback.data == 'settings':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('👛 ПЕРЕЙТИК ОПЛАТЕ', callback_data='pay'))
            markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data='back6'))
            photo18 = open('photo18.jpg', 'rb')
            voice8 = open('voice8.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo18, f'Здесь вы можете настроить вашего бота.\n\n⛔️ У вас нету доступа к настройкам бота. Перейдите к оплате и получите полный доступ для установке собственных реферальных ссылок в бота и открыть реферальную программу.', parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice8, reply_markup=markup)

        elif callback.data == 'buypro':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('На 1 месяц', callback_data='month')
            btn2 = types.InlineKeyboardButton('На 3 месяц', callback_data='month')
            btn3 = types.InlineKeyboardButton('На 6 месяц', callback_data='month')
            btn4 = types.InlineKeyboardButton('На 12 месяц', callback_data='month')
            btn5 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back8')
            markup.add(btn1, btn2)
            markup.add(btn3, btn4)
            markup.add(btn5)
            photo15 = open('photo15.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo15, 'Ваш баланс:<b> 0 ₽</b>\n\n<b>Вы можете продлить платную подписку с Вашего баланса</b>\n\n1 мес. - <b>600 руб./мес.</b>\n3 мес. -<b> 1620 руб. (540 руб./мес.)</b>\n6 мес. - <b>3060 руб. (510 руб./мес.)</b>\n12 мес. - <b>4690 руб. (390 руб/мес.)</b>\n\nВаш баланс пополняется автоматически с оплат ваших партнеров. Продвигайте вашу реферальную ссылку.', parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'month':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton('👛 ПЕРЕЙТИ К ОПЛАТЕ', callback_data='pay'))
            btn.add(types.InlineKeyboardButton('🔗 Моя ссылка на АльфаБОТ', callback_data='alfa'))
            btn.add(types.InlineKeyboardButton('⬅️ Назад', callback_data='back9'))
            photo16 = open('photo16.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo16, '☹️ У вас недостаточно бонусов для оплаты или продления 👑 Подписки PRO\n\nПродвигайте вашу реферальную ссылку АльфаБОТа и получайте вознаграждения с оплат.\n\nПродление вашей 👑 Подписки PRO сейчас можно сделать только по переводу.',parse_mode='HTML', reply_markup=btn)

        elif callback.data == 'alfa':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton('👛 ПЕРЕЙТИ К ОПЛАТЕ', callback_data='pay'))
            photo17 = open('photo17.jpg', 'rb')
            voice5 = open('voice5.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo17, 'Все кто перейдет по вашей реферальной ссылке, будут закреплены за вами.\n\n⛔️ <b>У вас нету доступа к реферальной ссылке. Передите к оплате и получите полный доступ.</b>', parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice5, reply_markup=btn)

        elif callback.data == 'beagent':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('ЗАРЕГИСТРИРОВАТЬСЯ', url='https://svoy.alfabank.ru/ref/221520')
            btn2 = types.InlineKeyboardButton('💸 Примеры дохода', url='https://t.me/+B9fPAqoSVho3MWZi')
            btn3 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back2')
            btn4 = types.InlineKeyboardButton('✅ ШАГ 3 ➡️', callback_data='step3')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3, btn4)
            photo5 = open('photo5.jpg', 'rb')
            voice3 = open('voice3.ogg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo5, '1️⃣ <b>Регистрируйтесь в проекте Свой в Альфе и получайте доход еще до получения Aльфа-карты.</b>\n\n🤩 Вы рекомендуете продукты банка и получаете трёхуровневые вознаграждения с бонусами.\n<blockquote>🔻 За приглашенного клиента вы получите от 2000 рублей\n🔻 Если ваш друг пригласит друга, то еще от 1000 рублей\n🔻 А за третий уровень рекомендации еще от 500 рублей</blockquote>\n\n2️⃣<b> Что делаем во время регистрации?</b>\n<blockquote>🔻 <i>Указываем полное ФИО\n🔻 Подтверждаем E-mail и телефон\n🔻 Заполняем профиль как в паспорте\n🔻 Выбираем <u>САМОЗАНЯТОГО</u> или <u>ИП</u></i></blockquote>\n\n3️⃣ Посмотрите 📺 <a href="https://youtu.be/EGeuAChJHlw"><b>видео системы дохода</b></a> или загрузите <a href="https://smlm.ru/wa-data/public/site/telegrambot/voice/alfa/PDF/marketing-new.pdf"><b>слайды в PDF</b></a>',parse_mode='HTML')
            bot_message = bot.send_voice(callback.message.chat.id, voice3, reply_markup=markup)

        elif callback.data == 'back1':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton('🅰️ Дебетовая карта', callback_data='card'))
            btn.add(types.InlineKeyboardButton('🧠 Памятка клиента', url='https://telegra.ph/AlfaMLM---pamyatka-klienta-11-15'))
            btn.add(types.InlineKeyboardButton('👌 Я получил карту', callback_data='getcard'))
            photo2 = open('photo2.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo2,'<b><u>Данный раздел сопровождает КЛИЕНТОВ</u> и дает пошаговые действия, чтобы ваша карта была бесплатной и с максимальными бонусами.</b>\n\n1️⃣ Предварительно ознакомьтесь и воспользуйтесь памяткой клиента во время получения карты.\n\n2️⃣ После получения карты, нажмите кнопку внизу 👌 <b>Я получил карту</b>.\n\n<blockquote><b>Контакты вашего пригласителя:</b>\n================\nВас пригласил ___ ___\nТелефон: ___________\nE-mail: ___\n================</blockquote>',parse_mode='HTML', reply_markup=btn)

        elif callback.data == 'back2':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton('🅰️ Стать агентом', callback_data='beagent'))
            btn.add(types.InlineKeyboardButton('👛 ПЕРЕЙТИК ОПЛАТЕ', callback_data='pay'))
            photo4 = open('photo4.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo4,'⛔️ У вас ограниченный доступ к разделу 👨‍💼 <b>Путь АГЕНТА</b>. Перейдите к оплате и получите полный доступ.\nРаздел 🎓 <b>Обучение</b> доступен по 👑 <b>Подписке PRO</b>\n\n<blockquote><b>Контакты вашего пригласителя:</b>\n================\nВас пригласил ___ ___\nТелефон: ___________\nE-mai: ___\n================</blockquote>',parse_mode='HTML', reply_markup=btn)

        elif callback.data == 'back3':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('ЗАРЕГИСТРИРОВАТЬСЯ', url='https://www.google.com')
            btn2 = types.InlineKeyboardButton('💸 Примеры дохода', url='https://www.google.com')
            btn3 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back2')
            btn4 = types.InlineKeyboardButton('✅ ШАГ 3 ➡️', callback_data='step3')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3, btn4)
            photo5 = open('photo5.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo5,'1️⃣ <b>Регистрируйтесь в проекте Свой в Альфе и получайте доход еще до получения Aльфа-карты.</b>\n\n🤩 Вы рекомендуете продукты банка и получаете трёхуровневые вознаграждения с бонусами.\n<blockquote>🔻 За приглашенного клиента вы получите от 2000 рублей\n🔻 Если ваш друг пригласит друга, то еще от 1000 рублей\n🔻 А за третий уровень рекомендации еще от 500 рублей</blockquote>\n\n2️⃣<b> Что делаем во время регистрации?</b>\n<blockquote>🔻 Указываем полное ФИО\n🔻 Подтверждаем E-mail и телефон\n🔻 Заполняем профиль как в паспорте\n🔻 Выбираем САМОЗАНЯТОГО или ИП</blockquote>\n\n3️⃣ Посмотрите 📺 видео системы дохода или загрузите слайды в PDF', parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'back4':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('💻 Личный кабинет 👨‍💼', url='https://t.me/gyuzel_fayzrahmanova')
            btn2 = types.InlineKeyboardButton('✅ Готовые ответы 👨‍💻', url='https://telegra.ph/Testirovanie-Agenta-11-18')
            btn3 = types.InlineKeyboardButton('⬅️ Наза', callback_data='back3')
            btn4 = types.InlineKeyboardButton('🎓 Обучение', callback_data='lesson')
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3, btn4)
            bot_message = bot.edit_message_text(f'<b>💰 Получите первые 2️⃣ балла (от <u>200</u> рублей)?</b>\n\n1️⃣ Перейдите в личный кабинет 👨‍💼<b> АГЕНТА</b>:\n<blockquote>🔻 Выберите в меню ОБУЧЕНИЕ\n🔻 Начните тестирование\n🔻 Ответьте на 10 вопросов</blockquote>\n\n✅ Мы подготовили для вас готовые ответы на тестирование.',callback.message.chat.id, callback.message.message_id, parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'back5':
            btn = types.InlineKeyboardMarkup()
            btn.add(types.InlineKeyboardButton('💳 Перевод или СБП', callback_data='pay'))
            photo9 = open('photo9.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo9,'<b>Активируйте себе бота с вашими реферальными ссылками на:</b>\n\n1️⃣ Дебетовая карта\n2️⃣ Агентская ссылка\n\n<b><u>Вы получаете % от оплат ваших партнеров:</u>\n1 линия (лично приглашенные)</b> - 15% от суммы оплаты (Подписка, дополнительные услуги, обучение и курсы).\n<b>2 линия</b> - 10% от суммы оплаты\n<b>3 линия</b> - 5% от суммы оплаты\n\nВы можете приглашать агентов и получить за них вознаграждения. Создавать пассивный доход с 🅰️льфаБОТ.\n\nВопросы и ответы | Договор Оферты | Политика\n\nНажмите внизу 💳 <b>Перевод или СБП</b> и выберите удобный тариф 👇', parse_mode='HTML', reply_markup=btn)

        elif callback.data == 'back6':
            btn = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('💲 Баланс', callback_data='balance')
            btn2 = types.InlineKeyboardButton('⚙️ Настройки', callback_data='settings')
            btn3 = types.InlineKeyboardButton('👛 ПЕРЕЙТИ К ОПЛАТЕ', callback_data='pay')
            btn.add(btn1, btn2)
            btn.add(btn3)
            photo13 = open('photo13.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo13,'Ваш 🆔 в боте: \n\nФИО: \nТелефон: \nE-mail: \n\n⛔️ У вас ограниченный доступ к AльфаБОТу. Перейдите к оплате и получите полный доступ.',parse_mode='HTML', reply_markup=btn)

        elif callback.data == 'back7':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('👑 Купить подписку PRO', callback_data='pay'))
            markup.add(types.InlineKeyboardButton('📄 Истроия оплат', callback_data='history'))
            photo9 = open('photo9.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo9,f'Чтобы воспользоваться всеми преимуществами нашего бота, нужно приобрести 👑 подписку PRO.',parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'back8':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('💵 Продлить подписку', callback_data='buypro'))
            markup.add(types.InlineKeyboardButton('⬅️ Назад', callback_data='back6'))
            photo14 = open('photo14.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo14,f'<b>Ваш баланс: 0 ₽</b>\n\nБаланс накапливается за счет активности ваших действий и покупка услуг по вашей реферальной ссылке.\n\n<b>За рекомендацию АльфаБОТ, вы будете получать вознаграждение:</b> \n✔️ 1-ая линия 15%\n✔️ 2-ая линия 10%\n✔️ 3-я линия 5%\n\nИспользуйте вашу реферальную ссылку на АльфаБОТ и получайте не только новых клиентов и агентов, но и вознаграждение за рекомендации.',parse_mode='HTML', reply_markup=markup)

        elif callback.data == 'back9':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('На 1 месяц', callback_data='month')
            btn2 = types.InlineKeyboardButton('На 3 месяц', callback_data='month')
            btn3 = types.InlineKeyboardButton('На 6 месяц', callback_data='month')
            btn4 = types.InlineKeyboardButton('На 12 месяц', callback_data='month')
            btn5 = types.InlineKeyboardButton('⬅️ Назад', callback_data='back8')
            markup.add(btn1, btn2)
            markup.add(btn3, btn4)
            markup.add(btn5)
            photo15 = open('photo15.jpg', 'rb')
            bot_message = bot.send_photo(callback.message.chat.id, photo15,'Ваш баланс:<b> 0 ₽</b>\n\n<b>Вы можете продлить платную подписку с Вашего баланса</b>\n\n1 мес. - <b>600 руб./мес.</b>\n3 мес. -<b> 1620 руб. (540 руб./мес.)</b>\n6 мес. - <b>3060 руб. (510 руб./мес.)</b>\n12 мес. - <b>4690 руб. (390 руб/мес.)</b>\n\nВаш баланс пополняется автоматически с оплат ваших партнеров. Продвигайте вашу реферальную ссылку.',parse_mode='HTML', reply_markup=markup)

        else:
            bot_message = bot.send_message(callback.message.chat.id, "Команда не распознана.")

        if bot_message:
            message_ids_to_delete.append(bot_message.message_id)

        for msg_id in message_ids_to_delete[1:]:
            if msg_id != welcome_message_id:
                try:
                    bot.delete_message(callback.message.chat.id, callback.message.message_id)
                except Exception as e:
                    print(f"Не удалось удалить сообщение {msg_id}: {str(e)}")

        message_ids_to_delete = [welcome_message_id] + message_ids_to_delete[-2:]
    except Exception as e:
        print(f"Ошибка при обработке сообщения: {str(e)}")


bot.polling(non_stop=True)