import pytest
import tempfile
import os
from task_2 import search_in_file

@pytest.fixture
def create_temp_file():
    """Фикстура для создания временного файла с содержимым."""
    temp_files = []

    def _create_temp_file(content):
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        temp_file.write(content)
        temp_file.close()
        temp_files.append(temp_file.name)
        return temp_file.name

    yield _create_temp_file

    # Удаляем временные файлы после выполнения тестов
    for file_name in temp_files:
        os.remove(file_name)

@pytest.mark.parametrize(
    "content, search_words, stop_words, expected_lines",
   [
       ("Роза биба доба Гена\nжимка пимка светик бобр", ["биба", "жимкА"], ["бобр"], ["Роза биба доба Гена"]),
       ("Роза биба доба Гена\nжимка пимка светик бобр\nкомар повар баклажан\nжеЛудь ИЧИГО Инуро", ["дОба", "пиМка", "повар"], ["гЕна"], ["жимка пимка светик бобр", "комар повар баклажан"]),
       ("Роза биба доба Гена\nжимка пимка светик бобр\nкомар повар баклажан\nжеЛудь ИЧИГО Инуро\nПЕРСЕЙ МИСКА РИСА геншин", ["пиМка", "ичиго", "риса"], ["иЧиго"], ["жимка пимка светик бобр", "ПЕРСЕЙ МИСКА РИСА геншин"]),

    ]
)
def test_search_in_file(create_temp_file, content, search_words, stop_words, expected_lines):
    file_path = create_temp_file(content)
    result = list(search_in_file(file_path, search_words, stop_words))
    assert result == expected_lines
