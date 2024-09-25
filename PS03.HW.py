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
        english_word = soup.find("div", id="random_word").text.strip()
      #   print(f'Оригинал {english_word}')
        translated_word = translator.translate(english_word, dest='ru').text
        #   print(f'Перевод {translated_word}')
        # Получаем описание слова
        english_word_definition = soup.find("div", id="random_word_definition").text.strip()
        translated_word_definition = translator.translate(english_word_definition, dest='ru').text
        # print(f"Оригинал значение слова {english_word_definition}")
        # print(f"Перевод значения слова {translated_word_definition}")
        # Чтобы программа возвращала словарь
        return {
            "translated_word": translated_word,  # Переведенное слово
            "translated_word_definition": translated_word_definition,  # Переведённое определение
            "original_word": english_word  # Оригинальное слово
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_words()
        if word_dict is None:
            print("Не удалось получить данные. Попробуйте позже.")
            break
        translated_word = word_dict.get("translated_word")
        translated_word_definition = word_dict.get("translated_word_definition")

        # Начинаем игру
        print(f"Значение слова: {translated_word_definition}")
        user_input = input("Что это за слово (на русском)? ")

        # Сравниваем введённое пользователем слово с переводом
        if user_input.strip().lower() == translated_word.strip().lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильное слово было: {translated_word}")

        # Возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н ")
        if play_again.lower() != "д":
            print("Спасибо за игру!")
            break


word_game()
