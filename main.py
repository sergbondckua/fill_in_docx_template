from datetime import datetime
from party_data import PartyData
from contract_generator import ContractGenerator
from template_filler import TemplateFiller

if __name__ == "__main__":
    # Приклад використання
    party_data_src = PartyData(
        contract_number=f"ОСББ-{datetime.now().replace(day=1).strftime('%d%m%Y')}-116",
        full_name='ЖИТЛОВО-БУДІВЕЛЬНИЙ КООПЕРАТИВ № 55 "ЕФІР 2"',
        short_name='ЖБК №55 "ЕФІР-2"',
        address="вулиця Генерала Момота, будинок 15",
        person_name="Мельник Петро Богданович",
        phone_number="067-472-38-50",
        city="Черкаси",
        bank_details="""18034, м. Черкаси, вул. Генерала Момота, 15
IBAN UA583052990000026002011601068
в АТ КБ «ПриватБанк»
МФО 305299
ЄДРПОУ 21368684
т. 067-472-38-50
""",
    )

    contract = ContractGenerator(source_price=50)
    contract_data = contract.get_contract_data(party_data_src)

    template_contract_filler = TemplateFiller(
        "templates/contract_template.docx", "filled_contract.docx"
    )
    template_pax_akt_filler = TemplateFiller(
        "templates/pax_akt_template.docx", "filled_pax_akt.docx"
    )

    template_contract_filler.fill_template(contract_data)
    template_pax_akt_filler.fill_template(contract_data)
