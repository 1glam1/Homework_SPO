# Подключение модулей
import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(
    filename="t.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",)

logger = logging.getLogger("LOGGER")
logger = logging.LoggerAdapter(logger, {"app": "тестовое приложение"})
logger.info('Программа запустилась.')

# Читает тест из файла и возвращает список вопросов с ответами.
def read_test_file(filename): 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            questions = []
            num_questions = int(file.readline().strip())
            for _ in range(num_questions):
                question_text = file.readline().strip()
                num_answers = int(file.readline().strip())
                correct_answer_index = int(file.readline().strip())
                answers = [file.readline().strip() for _ in range(num_answers)]
                questions.append((question_text, correct_answer_index, answers))
            logger.info("Тестовый файл прочитан успешно.")
            return questions
    except Exception as e:
        logger.error(f"Ошибка чтения тестового файла: {e}")
        return None
    
# Запускает тест, задавая вопросы пользователю и проверяя ответы.
def run_test(questions): 
    correct_count = 0
    for i, (question, correct_index, answers) in enumerate(questions, start=1):
        print(f"Вопрос {i}: {question}")
        logger.info(f"Вопрос {i}: {question}")
        for idx, answer in enumerate(answers, start=1):
            print(f"{idx}. {answer}")
        try:
            user_answer = int(input("Ваш ответ (номер варианта): "))
            if user_answer == correct_index:
                print("Правильно!\n")
                logger.info(f"Правильный ответ на вопрос {i}.")
                correct_count += 1
            else:
                print(f"Неправильно. Правильный ответ: {correct_index}\n")
                logger.info(f"Неправильный ответ на вопрос {i}. Правильный ответ {correct_index}.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите номер ответа.\n")
            logger.error(f"Неверный ввод для вопроса {i}.")
    return correct_count


filename = "test2.txt"
questions = read_test_file(filename)
if questions:
    total_questions = len(questions)
    correct_answers = run_test(questions)
    score_percent = (correct_answers / total_questions) * 100
    print(f"Ваш результат: {correct_answers} из {total_questions} ({score_percent:.2f}%)")
    logger.info(f"Тест завершен. Счет: {score_percent:.2f}% ({correct_answers}/{total_questions})")
    input('\nНажмите Enter чтобы чтобы завершить работу')
