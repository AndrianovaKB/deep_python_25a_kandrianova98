import hashlib
class SomeModel:
    def predict(self, message: str) -> float:
        hash_object = hashlib.sha256(message.encode())
        hex_dig = hash_object.hexdigest()
        hash_int = int(hex_dig, 16)
        max_hash = 2 ** 256 - 1
        return hash_int / max_hash


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    model = SomeModel()
    prediction = model.predict(message)
    if prediction < bad_thresholds:
        return "неуд"
    elif prediction > good_thresholds:
        return "отл"
    else:
        return "норм"

print(SomeModel().predict(""))
# assert predict_message_mood("Чапаев и пустота") == "неуд"
# assert predict_message_mood("Чапаев и пустота", 0.2, 0.99) == "норм"
# assert predict_message_mood("Вулкан") == "норм"