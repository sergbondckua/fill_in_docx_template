from datetime import datetime
from party_data import PartyData
from contract_generator import ContractGenerator
from template_filler import TemplateFiller

if __name__ == "__main__":
    # Приклад використання
    party_data_src = PartyData(
        contract_number=f"ОСББ-{datetime.now().replace(day=1).strftime('%d%m%Y')}-105",
        full_name='ОБ\'ЄДНАННЯ СПІВВЛАСНИКІВ БАГАТОКВАРТИРНОГО БУДИНКУ ЮГОСЛАВСЬКИЙ',
        short_name='ОСББ "ЮГОСЛАВСЬКИЙ"',
        address="вулиця Пастерівська, будинок 11",
        person_name="Розпутня Юлія Іванівна",
        phone_number="096-404-98-06",
        city="Черкаси",
        bank_details="""18016, м.Черкаси, вул.Пастерівська , 11
р/р UA343052990000026002021604334
в АТ КБ "Приватбанк"
МФО 305299
ЄДРПОУ 40726671
т. 097-507-40-46
""",
    )

    contract = ContractGenerator(source_price=7100*0.03)
    contract_data = contract.get_contract_data(party_data_src)

    template_contract_filler = TemplateFiller(
        "templates/contract_template.docx", "filled_contract.docx"
    )
    template_pax_akt_filler = TemplateFiller(
        "templates/pax_akt_template.docx", "filled_pax_akt.docx"
    )

    template_contract_filler.fill_template(contract_data)
    template_pax_akt_filler.fill_template(contract_data)
