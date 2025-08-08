# Agora vou criar estruturas para os tipos de equipes e CBOs
tipos_equipes = [
    {"codigo": "70", "nome": "Equipe de Saúde da Família (eSF)", "categoria": "ESF"},
    {"codigo": "76", "nome": "Equipe de Atenção Primária (eAP)", "categoria": "EAP"},
    {"codigo": "71", "nome": "Equipe de Saúde Bucal (eSB)", "categoria": "ESB"},
    {"codigo": "72", "nome": "Equipe Multiprofissional (eMulti)", "categoria": "EMULTI"},
    {"codigo": "73", "nome": "Equipe de Consultório na Rua (eCR)", "categoria": "ECR"},
    {"codigo": "32", "nome": "Unidade Móvel Fluvial (UBSF)", "categoria": "UBSF"}
]

# CBOs mais utilizados nos indicadores
cbos = [
    {"codigo": "2251-42", "descricao": "Médico da Estratégia de Saúde da Família", "categoria": "Médico"},
    {"codigo": "2251-70", "descricao": "Médico generalista", "categoria": "Médico"},
    {"codigo": "2251-30", "descricao": "Médico de família e comunidade", "categoria": "Médico"},
    {"codigo": "2235-65", "descricao": "Enfermeiro da Estratégia de Saúde da Família", "categoria": "Enfermeiro"},
    {"codigo": "2235-05", "descricao": "Enfermeiro", "categoria": "Enfermeiro"},
    {"codigo": "5151-05", "descricao": "Agente comunitário de saúde", "categoria": "ACS"},
    {"codigo": "3222-55", "descricao": "Técnico em agente comunitário de saúde", "categoria": "TACS"},
    {"codigo": "2232-08", "descricao": "Cirurgião-dentista clínico geral", "categoria": "Dentista"},
    {"codigo": "2232-93", "descricao": "Cirurgião-dentista da ESF", "categoria": "Dentista"},
    {"codigo": "3224-05", "descricao": "Técnico em saúde bucal", "categoria": "TSB"},
    {"codigo": "3224-15", "descricao": "Auxiliar em saúde bucal", "categoria": "ASB"},
    {"codigo": "2516-05", "descricao": "Assistente social", "categoria": "Multiprofissional"},
    {"codigo": "2234-05", "descricao": "Farmacêutico", "categoria": "Multiprofissional"},
    {"codigo": "2236-05", "descricao": "Fisioterapeuta", "categoria": "Multiprofissional"},
    {"codigo": "2237-10", "descricao": "Nutricionista", "categoria": "Multiprofissional"},
    {"codigo": "2515-10", "descricao": "Psicólogo", "categoria": "Multiprofissional"}
]

print("TIPOS DE EQUIPES:")
for equipe in tipos_equipes:
    print(f"{equipe['codigo']}: {equipe['nome']}")

print("\nPRINCIPAIS CBOs:")
for cbo in cbos:
    print(f"{cbo['codigo']}: {cbo['descricao']} ({cbo['categoria']})")