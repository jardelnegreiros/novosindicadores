# Agora vou criar informações sobre as vacinas mencionadas
vacinas = [
    {"codigo": "09", "nome": "Vacina hepatite B (HepB)", "indicacao": "Hepatite B"},
    {"codigo": "17", "nome": "Vacina Hib", "indicacao": "Haemophilus influenzae tipo b"},
    {"codigo": "22", "nome": "Vacina polio injetável (VIP)", "indicacao": "Poliomielite inativada"},
    {"codigo": "24", "nome": "Vacina sarampo, caxumba, rubéola (SCR)", "indicacao": "Sarampo, caxumba, rubéola"},
    {"codigo": "26", "nome": "Vacina pneumocócica 10-valente", "indicacao": "Pneumococo"},
    {"codigo": "28", "nome": "Vacina polio oral (VOP)", "indicacao": "Poliomielite oral"},
    {"codigo": "29", "nome": "Vacina penta acelular (DTPa/VIP/Hib)", "indicacao": "DTP, VIP, Hib"},
    {"codigo": "33", "nome": "Vacina influenza trivalente", "indicacao": "Influenza"},
    {"codigo": "39", "nome": "Vacina tetra (DTP/Hib)", "indicacao": "DTP, Hib"},
    {"codigo": "42", "nome": "Vacina penta (DTP/HepB/Hib)", "indicacao": "DTP, HepB, Hib"},
    {"codigo": "43", "nome": "Vacina hexa (DTPa/HepB/VIP/Hib)", "indicacao": "DTP, HepB, VIP, Hib"},
    {"codigo": "46", "nome": "Vacina DTP", "indicacao": "Difteria, tétano, pertussis"},
    {"codigo": "47", "nome": "Vacina DTPa infantil", "indicacao": "Difteria, tétano, pertussis acelular"},
    {"codigo": "56", "nome": "Vacina SCRV", "indicacao": "Sarampo, caxumba, rubéola, varicela"},
    {"codigo": "57", "nome": "Vacina dTpa adulto", "indicacao": "Difteria, tétano, pertussis adulto"},
    {"codigo": "58", "nome": "Vacina tetra acelular (DTPa/VIP)", "indicacao": "DTP acelular, VIP"},
    {"codigo": "67", "nome": "Vacina HPV quadrivalente", "indicacao": "HPV 4 tipos"},
    {"codigo": "77", "nome": "Vacina influenza tetravalente", "indicacao": "Influenza 4 cepas"},
    {"codigo": "93", "nome": "Vacina HPV nonavalente", "indicacao": "HPV 9 tipos"}
]

# CIDs e CIAP2 importantes
condicoes_saude = [
    # Diabetes
    {"codigo": "E10", "tipo": "CID-10", "descricao": "Diabetes mellitus insulino-dependente", "categoria": "Diabetes"},
    {"codigo": "E11", "tipo": "CID-10", "descricao": "Diabetes mellitus não-insulino-dependente", "categoria": "Diabetes"},
    {"codigo": "E14", "tipo": "CID-10", "descricao": "Diabetes mellitus não especificado", "categoria": "Diabetes"},
    {"codigo": "T89", "tipo": "CIAP-2", "descricao": "Diabetes insulino-dependente", "categoria": "Diabetes"},
    {"codigo": "T90", "tipo": "CIAP-2", "descricao": "Diabetes não insulino-dependente", "categoria": "Diabetes"},
    
    # Hipertensão
    {"codigo": "I10", "tipo": "CID-10", "descricao": "Hipertensão essencial", "categoria": "Hipertensão"},
    {"codigo": "I11", "tipo": "CID-10", "descricao": "Doença cardíaca hipertensiva", "categoria": "Hipertensão"},
    {"codigo": "I12", "tipo": "CID-10", "descricao": "Doença renal hipertensiva", "categoria": "Hipertensão"},
    {"codigo": "K86", "tipo": "CIAP-2", "descricao": "Hipertensão sem complicações", "categoria": "Hipertensão"},
    {"codigo": "K87", "tipo": "CIAP-2", "descricao": "Hipertensão com complicações", "categoria": "Hipertensão"},
    
    # Gestação
    {"codigo": "W78", "tipo": "CIAP-2", "descricao": "Gravidez", "categoria": "Gestação"},
    {"codigo": "W84", "tipo": "CIAP-2", "descricao": "Gravidez de alto risco", "categoria": "Gestação"},
    {"codigo": "Z34", "tipo": "CID-10", "descricao": "Supervisão de gravidez normal", "categoria": "Gestação"},
    
    # Saúde Sexual e Reprodutiva
    {"codigo": "Z70", "tipo": "CID-10", "descricao": "Aconselhamento sobre comportamento sexual", "categoria": "Saúde Sexual"},
    {"codigo": "W10", "tipo": "CIAP-2", "descricao": "Contracepção pós-coital", "categoria": "Saúde Sexual"},
    {"codigo": "W11", "tipo": "CIAP-2", "descricao": "Contracepção oral", "categoria": "Saúde Sexual"}
]

print("VACINAS MAPEADAS:")
for vacina in vacinas:
    print(f"{vacina['codigo']}: {vacina['nome']} - {vacina['indicacao']}")

print(f"\nTotal de vacinas: {len(vacinas)}")

print("\nCONDIÇÕES DE SAÚDE:")
categorias_cond = {}
for cond in condicoes_saude:
    categoria = cond['categoria']
    if categoria not in categorias_cond:
        categorias_cond[categoria] = []
    categorias_cond[categoria].append(cond)

for categoria, condicoes in categorias_cond.items():
    print(f"\n{categoria}:")
    for cond in condicoes:
        print(f"  {cond['codigo']} ({cond['tipo']}): {cond['descricao']}")