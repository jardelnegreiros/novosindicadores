# Agora vou criar estruturas detalhadas das boas práticas por indicador
boas_praticas = {
    "C3": [  # Cuidado da Gestante e Puérpera
        {"codigo": "A", "descricao": "Primeira consulta de pré-natal até 12 semanas", "pontos": 9},
        {"codigo": "B", "descricao": "Pelo menos 07 consultas durante gestação", "pontos": 10},
        {"codigo": "C", "descricao": "Pelo menos 07 registros de pressão arterial", "pontos": 9},
        {"codigo": "D", "descricao": "Pelo menos 07 registros de peso e altura", "pontos": 9},
        {"codigo": "E", "descricao": "Pelo menos 03 visitas domiciliares do ACS/Tacs", "pontos": 9},
        {"codigo": "F", "descricao": "Registro de dose dTpa a partir da 20ª semana", "pontos": 9},
        {"codigo": "G", "descricao": "Testes rápidos no primeiro trimestre", "pontos": 9},
        {"codigo": "H", "descricao": "Testes rápidos no terceiro trimestre", "pontos": 9},
        {"codigo": "I", "descricao": "Consulta durante puerpério", "pontos": 9},
        {"codigo": "J", "descricao": "Visita domiciliar durante puerpério", "pontos": 9},
        {"codigo": "K", "descricao": "Avaliação odontológica durante gestação", "pontos": 9}
    ],
    "C4": [  # Cuidado da pessoa com diabetes
        {"codigo": "A", "descricao": "Consulta médica/enfermeiro nos últimos 6 meses", "pontos": 20},
        {"codigo": "B", "descricao": "Medição de pressão arterial nos últimos 6 meses", "pontos": 15},
        {"codigo": "C", "descricao": "2 visitas domiciliares por ACS/Tacs em 12 meses", "pontos": 20},
        {"codigo": "D", "descricao": "Registro de peso e altura nos últimos 12 meses", "pontos": 15},
        {"codigo": "E", "descricao": "Registro de hemoglobina glicada nos últimos 12 meses", "pontos": 15},
        {"codigo": "F", "descricao": "Avaliação dos pés nos últimos 12 meses", "pontos": 15}
    ],
    "C5": [  # Cuidado da pessoa com hipertensão
        {"codigo": "A", "descricao": "Consulta médica/enfermeiro nos últimos 6 meses", "pontos": 25},
        {"codigo": "B", "descricao": "Aferição de pressão arterial nos últimos 6 meses", "pontos": 25},
        {"codigo": "C", "descricao": "2 visitas domiciliares por ACS/Tacs em 12 meses", "pontos": 25},
        {"codigo": "D", "descricao": "Registro de peso e altura nos últimos 12 meses", "pontos": 25}
    ],
    "C6": [  # Cuidado da pessoa idosa
        {"codigo": "A", "descricao": "Consulta médica/enfermeiro nos últimos 12 meses", "pontos": 25},
        {"codigo": "B", "descricao": "2 registros de peso e altura nos últimos 12 meses", "pontos": 25},
        {"codigo": "C", "descricao": "2 visitas domiciliares por ACS nos últimos 12 meses", "pontos": 25},
        {"codigo": "D", "descricao": "Dose da vacina influenza nos últimos 12 meses", "pontos": 25}
    ],
    "C2": [  # Cuidado no desenvolvimento infantil
        {"codigo": "A", "descricao": "1ª consulta até 30º dia de vida", "pontos": 20},
        {"codigo": "B", "descricao": "Pelo menos 09 consultas até 2 anos", "pontos": 20},
        {"codigo": "C", "descricao": "Pelo menos 09 registros de peso e altura", "pontos": 20},
        {"codigo": "D", "descricao": "2 visitas domiciliares (30 dias e 6 meses)", "pontos": 20},
        {"codigo": "E", "descricao": "Vacinação completa conforme calendário", "pontos": 20}
    ],
    "C7": [  # Cuidado da mulher na prevenção do câncer
        {"codigo": "A", "descricao": "Exame colo útero (25-64 anos) últimos 36 meses", "pontos": 20},
        {"codigo": "B", "descricao": "Vacina HPV (9-14 anos) pelo menos 1 dose", "pontos": 30},
        {"codigo": "C", "descricao": "Saúde sexual/reprodutiva (14-69 anos) últimos 12 meses", "pontos": 30},
        {"codigo": "D", "descricao": "Exame mama (50-69 anos) últimos 24 meses", "pontos": 20}
    ]
}

print("BOAS PRÁTICAS POR INDICADOR:")
for codigo, praticas in boas_praticas.items():
    print(f"\n{codigo}:")
    for pratica in praticas:
        print(f"  {pratica['codigo']}: {pratica['descricao']} ({pratica['pontos']} pontos)")