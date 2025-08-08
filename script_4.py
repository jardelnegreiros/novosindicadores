# Vou mapear os principais procedimentos SIGTAP mencionados
procedimentos_sigtap = [
    # Procedimentos comuns
    {"codigo": "01.01.04.002-4", "descricao": "Avaliação antropométrica", "categoria": "Antropometria"},
    {"codigo": "01.01.04.008-3", "descricao": "Medição de peso", "categoria": "Antropometria"},
    {"codigo": "01.01.04.007-5", "descricao": "Medição de altura", "categoria": "Antropometria"},
    {"codigo": "03.01.10.003-9", "descricao": "Aferição da pressão arterial", "categoria": "Sinais Vitais"},
    {"codigo": "03.01.01.025-0", "descricao": "Teleconsulta na atenção primária", "categoria": "Consulta"},
    
    # Exames laboratoriais
    {"codigo": "02.02.01.050-3", "descricao": "Dosagem de hemoglobina glicosilada", "categoria": "Exame Laboratorial"},
    {"codigo": "02.14.01.004-0", "descricao": "Teste rápido HIV na gestante", "categoria": "Teste Rápido"},
    {"codigo": "02.14.01.007-4", "descricao": "Teste rápido para sífilis", "categoria": "Teste Rápido"},
    {"codigo": "02.14.01.009-0", "descricao": "Teste rápido hepatite C", "categoria": "Teste Rápido"},
    {"codigo": "02.14.01.010-4", "descricao": "Teste rápido hepatite B", "categoria": "Teste Rápido"},
    
    # Exames de rastreamento
    {"codigo": "02.04.03.018-8", "descricao": "Mamografia bilateral para rastreamento", "categoria": "Rastreamento"},
    {"codigo": "02.03.01.008-6", "descricao": "Exame citopatológico cérvico-vaginal", "categoria": "Rastreamento"},
    {"codigo": "02.01.02.007-6", "descricao": "Coleta de material colo útero HPV", "categoria": "Rastreamento"},
    
    # Procedimentos odontológicos preventivos
    {"codigo": "01.01.02.005-8", "descricao": "Aplicação de cariostático", "categoria": "Odonto Preventivo"},
    {"codigo": "01.01.02.006-6", "descricao": "Aplicação de selante", "categoria": "Odonto Preventivo"},
    {"codigo": "01.01.02.007-4", "descricao": "Aplicação tópica de flúor", "categoria": "Odonto Preventivo"},
    {"codigo": "01.01.02.008-2", "descricao": "Evidenciação de placa bacteriana", "categoria": "Odonto Preventivo"},
    {"codigo": "01.01.02.010-4", "descricao": "Orientação de higiene bucal", "categoria": "Odonto Preventivo"},
    
    # Procedimentos odontológicos curativos
    {"codigo": "03.07.01.003-1", "descricao": "Restauração dente permanente anterior", "categoria": "Odonto Restaurador"},
    {"codigo": "03.07.01.012-0", "descricao": "Restauração dente permanente posterior", "categoria": "Odonto Restaurador"},
    {"codigo": "03.07.01.007-4", "descricao": "Tratamento restaurador atraumático", "categoria": "Odonto Restaurador"},
    
    # Cirurgias odontológicas
    {"codigo": "04.14.02.013-8", "descricao": "Exodontia de dente permanente", "categoria": "Odonto Cirúrgico"},
    {"codigo": "04.14.02.014-6", "descricao": "Exodontia múltipla com alveoloplastia", "categoria": "Odonto Cirúrgico"},
    
    # Consultas odontológicas
    {"codigo": "03.01.01.015-3", "descricao": "Primeira consulta odontológica programática", "categoria": "Odonto Consulta"},
    
    # Procedimentos específicos
    {"codigo": "03.01.04.009-5", "descricao": "Exame do pé diabético", "categoria": "Exame Específico"},
    {"codigo": "03.01.01.026-9", "descricao": "Avaliação do crescimento na puericultura", "categoria": "Puericultura"},
    {"codigo": "03.01.01.027-7", "descricao": "Avaliação desenvolvimento criança puericultura", "categoria": "Puericultura"}
]

print("PRINCIPAIS PROCEDIMENTOS SIGTAP:")
categorias_proc = {}
for proc in procedimentos_sigtap:
    categoria = proc['categoria']
    if categoria not in categorias_proc:
        categorias_proc[categoria] = []
    categorias_proc[categoria].append(proc)

for categoria, procedimentos in categorias_proc.items():
    print(f"\n{categoria}:")
    for proc in procedimentos:
        print(f"  {proc['codigo']}: {proc['descricao']}")

print(f"\nTotal de procedimentos mapeados: {len(procedimentos_sigtap)}")