from dataclasses import dataclass


@dataclass
class PartyData:
    """Дані для створення договору"""

    contract_number: str
    full_name: str
    short_name: str
    address: str
    person_name: str
    phone_number: str
    city: str
    bank_details: str
