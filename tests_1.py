import pytest
from task_1 import predict_message_mood


def test_1():
    message=""
    assert predict_message_mood(message) == "отл"

def test_2():
    message="Вулкан"
    assert predict_message_mood(message) == "норм"

def test_3():
    message="Чапаев и пустота"
    assert predict_message_mood(message) == "неуд"