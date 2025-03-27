import tempfile
import os
import pytest

from task_2 import generator_lines


@pytest.fixture
def create_file():
    file = tempfile.NamedTemporaryFile(mode = "w+", delete = False, encoding = "utf-8")
    file.write("А роза упала на лапу Азора\n")
    file.write("ярко розовые розы просто отвал всего\n")
    file.write("АЗОРУ ветер унес\n")
    file.write("Хочу в отпуск\n")
    yield file.name
    file.close()
    os.unlink(file.name)

def test_1(create_file):
    search_words = ["роза", "хочу"]
    stop_words = []
    expected_lines = [
        "а Роза упала на лапу Азора",
        "Хочу в отпуск"
    ]
    print(generator_lines(create_file, search_words, stop_words))
    result_lines = list(generator_lines(create_file, search_words, stop_words))
    assert result_lines == expected_lines