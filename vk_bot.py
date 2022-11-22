import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from datetime import datetime
import time
import wikipedia
wikipedia.set_lang("RU")

# токен здесь - https://vkhost.github.io/
session = vk_api.VkApi(token='???')
session_api = session.get_api()
longpoll = VkLongPoll(session)

greeting_list = ('Привет',
                 'Привет!',
                 'Здравствуй',
                 'Привет',
                 'Доброго времени суток')

photo = ("photo-32328515_457385698",
         "photo-32328515_457385707",
         "photo-32328515_457385697",
         "photo-32328515_457385451",
         "photo-32328515_457385717",
         "photo-32328515_457385703",
         "photo-32328515_457385460",
         "photo-32328515_457385719",
         "photo-32328515_457385712",
         "photo-32328515_457385686",
         "photo-32328515_457385466",
         "photo-32328515_457385471",
         "photo-32328515_457385287",
         "photo-32328515_457385705",
         "photo-32328515_457385858",
         "photo-32328515_456323307",
         "photo-32328515_457385292",
         "photo-32328515_457385314",
         "photo-32328515_457385750",
         "photo-32328515_457385329",
         "photo-32328515_457385751",
         "photo-32328515_457385365",
         "photo-52507111_457242714",
         "photo-52507111_457242717",
         "photo-52507111_457242701",
         "photo-52507111_457242646",
         "photo-52507111_457242654",
         "photo-52507111_457242642",
         "photo-52507111_457242638",
         "photo-52507111_457242624",
         "photo-52507111_457242627",
         "photo-52507111_457242607",
         "photo-52507111_457242552",
         "photo-52507111_457242352",
         "photo-52507111_457242353",)

films = ("Темный рыцарь (2008)",
         "Трилогия Властелин Колец",
         "Бойцовский клуб (1999)",
         "Начало (2010)",
         "Матрица (1999)",
         "Семь (1995)",
         "Город бога (2002)",
         "Жизнь прекрасна (1997)",
         "Спасти рядового Райана (1998)",
         "Унесённые призраками (2001)",
         "Зеленая миля (1999)",
         "Паразиты (2019)",
         "Интерстеллар (2014)",
         "Подозрительные лица (1995)",
         "Пианист (2002)",
         "Американская история Х (1998)",
         "Отступники (2006)",
         "Гладиатор (2000)",
         "Гамильтон (2020)",
         "1+1 (2011)",
         "Одержимость (2013)",
         "Престиж (2006)",
         "Помни (2000)",
         "Чужой (1979)",
         "Апокалипсис сегодня (1979)",
         "Аватар (2009)",
         "Назад в будущее (1985)",
         "Пустоши (1973)",
         "Крёстный отец (1972)",
         "Унесённые ветром (1939)",
         "Голдфингер (1964)",
         "Кинг Конг (1933)",
         "Пролетая над гнездом кукушки (1975)",
         "Кролик Джождо (2019)",
         "Омерзительная восьмёрка (2015)",
         "Бесславные ублюдки (2009)",
         "Цельнометаллическая оболочка (1987)")

cat = ("photo-43228812_457352214",
       "photo-43228812_457352198",
       "photo-43228812_457352209",
       "photo-43228812_457352146",
       "photo-43228812_457352163",
       "photo-43228812_457352135",
       "photo-43228812_457352061",
       "photo-43228812_457351983",
       "photo-43228812_457351966",
       "photo-43228812_457351940",)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ', event.datetime)
            print('Текст сообщения: ', event.text)
            response = event.text.lower()
            if event.from_user and not event.from_me:

                if response.find('привет') >= 0 or response.find('здравствуй') >= 0 or response.find(
                        'hello') >= 0 or response.find('йо') >= 0:
                    #time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send',
                                   {'user_id': event.user_id,
                                    'message': random.choice(greeting_list),
                                    'random_id': '0'})

                elif response.find('как дела') >= 0:
                    #time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send',
                                   {'user_id': event.user_id,
                                    'message': '',
                                    'random_id': '0',
                                    'sticker_id': '126'})

                elif response.find('фото') >= 0:
                    #time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send',
                                   {'user_id': event.user_id,
                                    'message': '',
                                    'random_id': '0',
                                    'attachment': random.choice(photo)})

                elif response.find('фильм') >= 0 or response.find('кино') >= 0:
                    #time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send',
                                   {'user_id': event.user_id,
                                    'message': random.choice(films),
                                    'random_id': '0'})

                elif response.find('кот') >= 0 or response.find('кош') >= 0:
                    #time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send',
                                   {'user_id': event.user_id,
                                    'message': '',
                                    'random_id': '0',
                                    'attachment': random.choice(cat)})
                elif response == 'википедия' or response == 'вики' or response == 'wikipedia' or response == 'wiki':  # если нам пришло сообщение с текстом Википедия или Вики или ... или wiki
                    if event.from_user:  # Если написали в ЛC
                        session.method('messages.send', {'user_id': event.user_id,
                                                         'message': 'Введите запрос',
                                                         'random_id': 0})
                    try:
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # Пинаем longpoll
                                if event.from_user:
                                    session.method('messages.send', {'user_id': event.user_id,
                                                                     'message': 'Вот что я нашёл: \n' + str(wikipedia.summary(event.text)),
                                                                     'random_id': 0})
                                    break
                                break
                        continue
                    except:
                        session.method('messages.send', {'user_id': event.user_id,
                                                         'message': 'Не найдено или неправильно задан запрос.',
                                                         'random_id': 0})
                else:
                    #time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send',
                                   {'user_id': event.user_id,
                                    'message': 'Не знаю что ответить на это', 'random_id': 0})
