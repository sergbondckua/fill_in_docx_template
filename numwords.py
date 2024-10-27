from num2words import num2words


class FinancialAmountInUAH:
    """Конвертує числове значення фінансової суми в прописні слова
        українською мовою з відповідними відмінками.
    """

    def __init__(self, amount):
        self.amount = amount
        self.amount_in_words = self._convert_amount_to_words()
        self.pennies = self.extract_pennies()
        self.currency_word = self._get_declension(
            int(self.amount), ["гривня", "гривні", "гривень"])
        self.pennies_word = self._get_declension(
            self.pennies, ["копійка", "копійки", "копійок"])

    def _convert_amount_to_words(self):
        """Перетворює цілу частину суми в пропис (для жіночого роду)"""
        amount_in_words = num2words(int(self.amount), lang="uk")

        # Корекція для числівників "одна" та "дві" для слова "гривня"
        return amount_in_words.replace(" один", " одна").replace(
            " два", " дві"
        )

    def extract_pennies(self) -> int:
        """Відокремлює кількість копійок з суми"""
        return int(round((self.amount - int(self.amount)) * 100))

    @staticmethod
    def _get_declension(amount: int, forms: list) -> str:
        """Визначає правильний відмінок для переданого числа і форм"""
        last_digit = amount % 10
        last_two_digits = amount % 100

        if 11 <= last_two_digits <= 14:
            return forms[2]
        elif last_digit == 1:
            return forms[0]
        elif last_digit in [2, 3, 4]:
            return forms[1]
        else:
            return forms[2]

    def format_result(self) -> str:
        """Форматує остаточний результат"""
        return f"{self.amount_in_words} {self.currency_word} {self.pennies:02d} {self.pennies_word}"


if __name__ == "__main__":

    # Приклад використання
    _amount = 840.01
    _amount_in_words = FinancialAmountInUAH(_amount)
    result = _amount_in_words.format_result()
    print(result)
