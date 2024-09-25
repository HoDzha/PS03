import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_words():
    url = "https://randomword.com/"
    translator = Translator()
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        words = translator.translate(english_words, dest='ru').text

        # Получаем описание слова
        english_word_definition = soup.find("div", id="random_word_definition").text.strip()
        word_definition = translator.translate(english_word_definition, dest='ru').text

        # Чтобы программа возвращала словарь
        return {
            "words": words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_words()
        word = word_dict.get("words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()