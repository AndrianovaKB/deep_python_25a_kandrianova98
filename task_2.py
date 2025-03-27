def generator_lines(file, search_words, stop_words):
    # Приводим слова для поиска и стоп-слова к нижнему регистру для сравнения
    search_words_lower = {word.lower() for word in search_words}
    stop_words_lower = {word.lower() for word in stop_words}

    # Открываем файл, если передан путь, иначе считаем, что это файловый объект
    need_close = False
    if isinstance(file, str):
        file_obj = open(file, 'r', encoding='utf-8')
        need_close = True
    else:
        file_obj = file

    try:
        for line in file_obj:
            words_in_line = line.split()  # Разбиваем строку на слова
            words_in_line_lower = {word.lower() for word in words_in_line}

            # Проверяем, есть ли в строке стоп-слова
            if words_in_line_lower & stop_words_lower:
                continue  # Пропускаем строку, если есть стоп-слово

            # Проверяем, есть ли в строке хотя бы одно слово из списка поиска
            if words_in_line_lower & search_words_lower:
                yield line  # Возвращаем строку без лишних пробелов
    finally:
        if need_close:
            file_obj.close()

#
# search_words = ["роза", "хочу"]
# stop_words = []
# expected_lines = [
#     "а Роза упала на лапу Азора",
#     "Хочу в отпуск"
# ]
# result_lines = list(generator_lines('text_2_task.txt', search_words, stop_words))
# print(result_lines)
# assert result_lines == expected_lines