import locale
import platform
from datetime import datetime
from dataclasses import dataclass
from declension import NameDeclension
from numwords import FinancialAmountInUAH
from party_data import PartyData

# Встановлюємо українську локаль
if platform.system() == "Windows":
    locale.setlocale(locale.LC_TIME, "Ukrainian")
else:
    locale.setlocale(locale.LC_TIME, "uk_UA.UTF-8")


@dataclass
class ContractGenerator:
    """Генерація договору"""

    source_price: float
    from_date: str = datetime.now().replace(day=1).strftime('"%d" %B %Y')

    def __post_init__(self):
        """Підготовка даних до генерації договору"""

        self.price = int(self.source_price)
        self.pennies = FinancialAmountInUAH(
            self.source_price
        ).extract_pennies()
        self.total_price = self.source_price * 12
        self.total_pennies = FinancialAmountInUAH(
            self.total_price
        ).extract_pennies()
        self.price_text = FinancialAmountInUAH(
            self.source_price
        ).format_result()
        self.total_price_text = FinancialAmountInUAH(
            self.total_price
        ).format_result()
        self.genitive_name = NameDeclension()

    def get_contract_data(self, party_data: PartyData) -> dict:
        """Повертає дані для генерації договору"""

        part_person_name = party_data.person_name.split()
        short_name = f"{part_person_name[1]} {part_person_name[0].upper()}"
        return {
            "contract_number": party_data.contract_number,
            "city": party_data.city,
            "from_date": self.from_date,
            "party_one": party_data.full_name.upper(),
            "party_one_short_name": (
                party_data.short_name.upper()
                if party_data.short_name
                else party_data.full_name.upper()
            ),
            "person_party_one": party_data.person_name,
            "short_name": short_name,
            "genitive_name": self.genitive_name.to_genitive(
                party_data.person_name
            ),
            "address": party_data.address,
            "price": str(self.price),
            "pennies": f"{self.pennies}0"[:2],
            "price_text": self.price_text,
            "total_price_text": self.total_price_text,
            "total_price": f"{int(self.total_price)}",
            "total_pennies": f"{self.total_pennies}0"[:2],
            "person_party_one_phonenumber": party_data.phone_number,
            "bank_details": party_data.bank_details,
        }

    def __repr__(self):
        return f"ContractGenerator(source_price={self.source_price})"
