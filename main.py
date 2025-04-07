import re


def censor_confidential_data(text):
    # Шаблон для поиска телефонных номеров
    phone_pattern = r'(\+?\d{1,3})?[\s\-]?\(?\d{2,4}\)?[\s\-]?\d{2,4}[\s\-]?\d{2,4}'

    # Шаблон для поиска имён и фамилий (два слова с заглавной буквы)
    name_pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]+ [A-ZА-ЯЁ][a-zа-яё]+\b'

    # Примерный шаблон геоданных (город, улица, проспект, etc.)
    geo_pattern = r'\b(ул\.|улица|проспект|пр-т|город|г\.)\s?[A-ZА-ЯЁ][a-zа-яё]+'

    # Цензура найденных данных
    text = re.sub(phone_pattern, '[censored]', text)
    text = re.sub(name_pattern, '[censored]', text)
    text = re.sub(geo_pattern, '[censored]', text)

    return text


def main():
    # Чтение исходного текста
    with open('input.txt', 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Обработка
    output_text = censor_confidential_data(input_text)

    # Запись результата
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(output_text)


if __name__ == "__main__":
    main()
