import pymorphy3

class NameDeclension:
    """Формуємо повне ім'я з родовим відмінком"""

    def __init__(self, lang="uk"):
        # Ініціалізуємо pymorphy3 лише один раз при створенні об'єкта
        self.morph = pymorphy3.MorphAnalyzer(lang=lang)

    def to_genitive(self, full_name) -> str:
        # Формуємо повне ім'я з родовими відмінками
        genitive_name = " ".join(
            [
                self._get_genitive_form(word)
                for word in full_name.split()
            ]
        ).title()
        return genitive_name

    def _get_genitive_form(self, word: str) -> str:
        # Отримуємо родовий відмінок для кожного слова
        parsed_word = self.morph.parse(word)[0]
        genitive_form = parsed_word.inflect({"gent"})
        return genitive_form.word if genitive_form else word


if __name__ == '__main__':

    # Приклад використання
    name_declension = NameDeclension()
    gen_name = name_declension.to_genitive("Мельник Петро Богданович")
    print(gen_name)
