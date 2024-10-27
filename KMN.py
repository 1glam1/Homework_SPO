#Подключение модулей
import logging 
from random import choice

logging.basicConfig(
    filename="kmn.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",)
logger = logging.getLogger("LOGGER")
logger = logging.LoggerAdapter(logger, {"app": "тестовое приложение"})
logger.info('Программа запустилась.')

while True:
    try:
        score = int(input('До скольки побед вы хотите играть? ')) # Выбор количества побед
        logger.info('Было введено количество побед.')
        user_score = 0
        rand_score = 0
        while score != user_score and score != rand_score:
            user = input("Камень, ножницы или бумага(строчными буквами)? ") # Выбор пользователя
            logger.info(f'Пользователь ввел {user}')
            list_play = ['камень', 'ножницы', 'бумага']
            # Начисление очков
            if user in list_play:
                rand = choice(list_play) # Выбор компьютера
                logger.info(f'Компьютер ввел {rand}')
                if rand == 'камень' and user == 'ножницы':
                    rand_score += 1
                if rand == 'камень' and user == 'бумага':
                    user_score += 1
                if rand == 'ножницы' and user == 'камень':
                    user_score += 1
                if rand == 'ножницы' and user == 'бумага':
                    rand_score += 1
                if rand == 'бумага' and user == 'ножницы':
                    user_score += 1
                if rand == 'бумага' and user == 'камень':
                    rand_score += 1  
                # Вывод выбора пользователя и компьютера
                print(f'Компьютер: {rand}')
                print(f'Вы выбрали {user}, компьютер выбрал {rand}.')
                logger.info(f'Пользователь выбрал {user}, компьютер выбрал {rand}.')
                # Вывод количества баллов пользователя и компьютера
                print(f'Ваши баллы - {user_score}. Баллы компьютера - {rand_score}.')
                logger.info(f'Баллы пользователя - {user_score}. Баллы компьютера - {rand_score}.')
            else:
                # Проверка ввода
                print('Неправильный ввод!')    
                logger.error('Неправильный ввод!')
        # Вывод результатов
        if score == rand_score:
            print('Конец игры! Компьютер победил!')
            break
        elif score == user_score:
            print('Конец игры! Пользователь победил!')
            break
        else:
            # Проверка ввода
            print('Неправильный ввод!')
            logger.error('Неправильный ввод!')
    except ValueError:
        # Проверка ввода
        print('Неправильный ввод!')
        logger.error('Неправильный ввод!')
input('\nНажмите Enter чтобы закрыть программу')
