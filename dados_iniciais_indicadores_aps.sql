
-- ============================================================================
-- DADOS INICIAIS - SISTEMA DE INDICADORES APS
-- ============================================================================

-- REGIÕES DO BRASIL
INSERT INTO regioes (codigo, nome) VALUES 
('NO', 'Norte'),
('NE', 'Nordeste'),
('CO', 'Centro-Oeste'),
('SE', 'Sudeste'),
('SU', 'Sul');

-- CATEGORIAS DE INDICADORES
INSERT INTO categorias_indicadores (codigo, nome, descricao, cor_hex) VALUES 
('C', 'Cuidado', 'Indicadores de qualidade do cuidado específico por condição ou ciclo de vida', '#2E8B57'),
('B', 'Saúde Bucal', 'Indicadores específicos de saúde bucal e odontologia', '#1E90FF'),
('M', 'Multiprofissional', 'Indicadores relacionados às equipes multiprofissionais', '#FF6347'),
('A', 'Acesso', 'Indicadores de acesso aos serviços de saúde', '#9370DB');

-- TIPOS DE EQUIPES
INSERT INTO tipos_equipes (codigo, nome, sigla, categoria) VALUES 
('70', 'Equipe de Saúde da Família', 'eSF', 'ESF'),
('76', 'Equipe de Atenção Primária', 'eAP', 'EAP'),
('71', 'Equipe de Saúde Bucal', 'eSB', 'ESB'),
('72', 'Equipe Multiprofissional', 'eMulti', 'EMULTI'),
('73', 'Equipe de Consultório na Rua', 'eCR', 'ECR'),
('32', 'Unidade Básica de Saúde Fluvial', 'UBSF', 'UBSF');

-- CBOs PRINCIPAIS
INSERT INTO cbos (codigo, descricao, categoria, nivel_ensino) VALUES 
('2251-42', 'Médico da Estratégia de Saúde da Família', 'Médico', 'Superior'),
('2251-70', 'Médico generalista', 'Médico', 'Superior'),
('2251-30', 'Médico de família e comunidade', 'Médico', 'Superior'),
('2251-25', 'Médico clínico', 'Médico', 'Superior'),
('2235-65', 'Enfermeiro da Estratégia de Saúde da Família', 'Enfermeiro', 'Superior'),
('2235-05', 'Enfermeiro', 'Enfermeiro', 'Superior'),
('5151-05', 'Agente comunitário de saúde', 'ACS', 'Médio'),
('3222-55', 'Técnico em agente comunitário de saúde', 'TACS', 'Médio'),
('3222-05', 'Técnico de enfermagem', 'Técnico Enfermagem', 'Médio'),
('3222-45', 'Técnico de enfermagem da ESF', 'Técnico Enfermagem', 'Médio'),
('3222-30', 'Auxiliar de enfermagem', 'Auxiliar Enfermagem', 'Médio'),
('3222-50', 'Auxiliar de enfermagem da ESF', 'Auxiliar Enfermagem', 'Médio'),
('2232-08', 'Cirurgião-dentista clínico geral', 'Dentista', 'Superior'),
('2232-93', 'Cirurgião-dentista da ESF', 'Dentista', 'Superior'),
('2232-72', 'Cirurgião-dentista de saúde coletiva', 'Dentista', 'Superior'),
('3224-05', 'Técnico em saúde bucal', 'TSB', 'Médio'),
('3224-25', 'Técnico em saúde bucal da ESF', 'TSB', 'Médio'),
('3224-15', 'Auxiliar em saúde bucal', 'ASB', 'Médio'),
('3224-30', 'Auxiliar em saúde bucal da ESF', 'ASB', 'Médio'),
('2516-05', 'Assistente social', 'Multiprofissional', 'Superior'),
('2234-05', 'Farmacêutico', 'Multiprofissional', 'Superior'),
('2234-45', 'Farmacêutico hospitalar e clínico', 'Multiprofissional', 'Superior'),
('2236-05', 'Fisioterapeuta', 'Multiprofissional', 'Superior'),
('2238-10', 'Fonoaudiólogo', 'Multiprofissional', 'Superior'),
('2237-10', 'Nutricionista', 'Multiprofissional', 'Superior'),
('2241-40', 'Profissional de educação física na saúde', 'Multiprofissional', 'Superior'),
('2515-10', 'Psicólogo', 'Multiprofissional', 'Superior'),
('1312-25', 'Sanitarista', 'Multiprofissional', 'Superior'),
('2239-05', 'Terapeuta ocupacional', 'Multiprofissional', 'Superior'),
('5153-05', 'Arte-educador', 'Multiprofissional', 'Superior'),
('2251-05', 'Médico acupunturista', 'Multiprofissional', 'Superior'),
('2251-20', 'Médico cardiologista', 'Multiprofissional', 'Superior'),
('2251-35', 'Médico dermatologista', 'Multiprofissional', 'Superior'),
('2251-55', 'Médico endocrinologista', 'Multiprofissional', 'Superior'),
('2251-80', 'Médico geriatra', 'Multiprofissional', 'Superior'),
('2252-50', 'Médico ginecologista/obstetra', 'Multiprofissional', 'Superior'),
('2251-95', 'Médico homeopata', 'Multiprofissional', 'Superior'),
('2251-03', 'Médico infectologista', 'Multiprofissional', 'Superior'),
('2251-24', 'Médico pediatra', 'Multiprofissional', 'Superior'),
('2251-33', 'Médico psiquiatra', 'Multiprofissional', 'Superior'),
('2233-05', 'Médico veterinário', 'Multiprofissional', 'Superior');

-- PROCEDIMENTOS SIGTAP PRINCIPAIS
INSERT INTO procedimentos_sigtap (codigo, descricao, categoria, subcategoria) VALUES 
-- Antropometria e Sinais Vitais
('01.01.04.002-4', 'Avaliação antropométrica', 'Antropometria', 'Medidas'),
('01.01.04.008-3', 'Medição de peso', 'Antropometria', 'Peso'),
('01.01.04.007-5', 'Medição de altura', 'Antropometria', 'Altura'),
('03.01.10.003-9', 'Aferição da pressão arterial', 'Sinais Vitais', 'Pressão'),

-- Consultas
('03.01.01.025-0', 'Teleconsulta na atenção primária', 'Consulta', 'Remota'),

-- Exames Laboratoriais
('02.02.01.050-3', 'Dosagem de hemoglobina glicosilada', 'Exame Laboratorial', 'Glicemia'),

-- Testes Rápidos
('02.14.01.004-0', 'Teste rápido para detecção de HIV na gestante ou pai/parceiro', 'Teste Rápido', 'HIV'),
('02.14.01.005-8', 'Teste rápido para detecção de infecção pelo HIV', 'Teste Rápido', 'HIV'),
('02.14.01.007-4', 'Teste rápido para sífilis', 'Teste Rápido', 'Sífilis'),
('02.14.01.008-2', 'Teste rápido para sífilis na gestante ou pai/parceiro', 'Teste Rápido', 'Sífilis'),
('02.14.01.009-0', 'Teste rápido para detecção de hepatite c', 'Teste Rápido', 'Hepatite C'),
('02.14.01.010-4', 'Teste rápido para detecção de infecção pelo hbv', 'Teste Rápido', 'Hepatite B'),

-- Rastreamento
('02.04.03.018-8', 'Mamografia bilateral para rastreamento', 'Rastreamento', 'Câncer Mama'),
('02.03.01.008-6', 'Exame citopatológico cérvico vaginal/microflora-rastreamento', 'Rastreamento', 'Câncer Colo'),
('02.03.01.001-9', 'Exame citopatológico cérvico-vaginal/microflora', 'Rastreamento', 'Câncer Colo'),
('02.01.02.007-6', 'Coleta de material do colo do útero para exame molecular de detecção de HPV', 'Rastreamento', 'HPV'),
('02.01.02.008-4', 'Entrega de material obtido por auto coleta para exame molecular para detecção de HPV', 'Rastreamento', 'HPV'),
('02.01.02.003-3', 'Coleta de citopatológico de colo uterino', 'Rastreamento', 'Câncer Colo'),

-- Procedimentos Específicos
('03.01.04.009-5', 'Exame do pé diabético', 'Exame Específico', 'Diabetes'),
('03.01.01.026-9', 'Avaliação do crescimento na puericultura', 'Puericultura', 'Crescimento'),
('03.01.01.027-7', 'Avaliação do desenvolvimento da criança na puericultura', 'Puericultura', 'Desenvolvimento'),

-- Odontologia Preventiva
('01.01.02.005-8', 'Aplicação de cariostático (por dente)', 'Odonto Preventivo', 'Prevenção Cárie'),
('01.01.02.006-6', 'Aplicação de selante (por dente)', 'Odonto Preventivo', 'Selante'),
('01.01.02.007-4', 'Aplicação tópica de flúor (individual por sessão)', 'Odonto Preventivo', 'Flúor'),
('01.01.02.008-2', 'Evidenciação de placa bacteriana', 'Odonto Preventivo', 'Educação'),
('01.01.02.009-0', 'Selamento provisório de cavidade dentária', 'Odonto Preventivo', 'Urgência'),
('01.01.02.010-4', 'Orientação de higiene bucal', 'Odonto Preventivo', 'Educação'),

-- Odontologia Restauradora
('03.07.01.001-5', 'Capeamento pulpar', 'Odonto Restaurador', 'Endodontia'),
('03.07.01.003-1', 'Restauração de dente permanente anterior com resina composta', 'Odonto Restaurador', 'Restauração'),
('03.07.01.006-6', 'Tratamento inicial do dente traumatizado', 'Odonto Restaurador', 'Trauma'),
('03.07.01.007-4', 'Tratamento restaurador atraumático (TRA/ART)', 'Odonto Restaurador', 'ART'),
('03.07.01.008-2', 'Restauração de dente decíduo posterior com resina composta', 'Odonto Restaurador', 'Restauração'),
('03.07.01.010-4', 'Restauração de dente decíduo posterior com ionômero de vidro', 'Odonto Restaurador', 'Restauração'),
('03.07.01.011-2', 'Restauração de dente decíduo anterior com resina composta', 'Odonto Restaurador', 'Restauração'),
('03.07.01.012-0', 'Restauração de dente permanente posterior com resina composta', 'Odonto Restaurador', 'Restauração'),
('03.07.01.013-9', 'Restauração de dente permanente posterior com amálgama', 'Odonto Restaurador', 'Restauração'),

-- Endodontia
('03.07.02.001-0', 'Acesso à polpa dentária e medicação (por dente)', 'Odonto Endodontia', 'Tratamento Canal'),
('03.07.02.002-9', 'Curativo de demora com ou sem preparo biomecânico', 'Odonto Endodontia', 'Tratamento Canal'),
('03.07.02.007-0', 'Pulpotomia dentária', 'Odonto Endodontia', 'Pulpotomia'),

-- Periodontia
('03.07.03.002-4', 'Raspagem e alisamento subgengivais (por sextante)', 'Odonto Periodontia', 'Raspagem'),
('03.07.03.004-0', 'Profilaxia / remoção da placa bacteriana', 'Odonto Periodontia', 'Profilaxia'),
('03.07.03.005-9', 'Raspagem, alisamento e polimento supragengivais (por sextante)', 'Odonto Periodontia', 'Raspagem'),
('03.07.03.006-7', 'Tratamento de gengivite ulcerativa necrosante aguda (GUNA)', 'Odonto Periodontia', 'Gengivite'),
('03.07.03.007-5', 'Tratamento de lesões da mucosa oral', 'Odonto Periodontia', 'Mucosa'),
('03.07.03.008-3', 'Tratamento de pericoronarite', 'Odonto Periodontia', 'Pericoronarite'),

-- Cirurgia Odontológica
('04.14.02.013-8', 'Exodontia de dente permanente', 'Odonto Cirúrgico', 'Extração'),
('04.14.02.014-6', 'Exodontia múltipla com alveoloplastia por sextante', 'Odonto Cirúrgico', 'Extração'),

-- Consultas Odontológicas
('03.01.01.015-3', 'Primeira consulta odontológica programática', 'Odonto Consulta', 'Primeira Consulta');


-- CONDIÇÕES DE SAÚDE (CID-10 e CIAP-2)
INSERT INTO condicoes_saude (codigo, tipo, descricao, categoria) VALUES 
-- Diabetes (CID-10)
('E10.0', 'CID-10', 'Diabetes mellitus insulino-dependente com coma', 'Diabetes'),
('E10.1', 'CID-10', 'Diabetes mellitus insulino-dependente com cetoacidose', 'Diabetes'),
('E10.2', 'CID-10', 'Diabetes mellitus insulino-dependente com complicações renais', 'Diabetes'),
('E10.9', 'CID-10', 'Diabetes mellitus insulino-dependente sem complicações', 'Diabetes'),
('E11.0', 'CID-10', 'Diabetes mellitus não-insulino-dependente com coma', 'Diabetes'),
('E11.1', 'CID-10', 'Diabetes mellitus não-insulino-dependente com cetoacidose', 'Diabetes'),
('E11.2', 'CID-10', 'Diabetes mellitus não-insulino-dependente com complicações renais', 'Diabetes'),
('E11.9', 'CID-10', 'Diabetes mellitus não-insulino-dependente sem complicações', 'Diabetes'),
('E14.0', 'CID-10', 'Diabetes mellitus não especificado com coma', 'Diabetes'),
('E14.9', 'CID-10', 'Diabetes mellitus não especificado sem complicações', 'Diabetes'),

-- Diabetes (CIAP-2)
('T89', 'CIAP-2', 'Diabetes insulino-dependente', 'Diabetes'),
('T90', 'CIAP-2', 'Diabetes não insulino-dependente', 'Diabetes'),

-- Hipertensão (CID-10)
('I10', 'CID-10', 'Hipertensão essencial (primária)', 'Hipertensão'),
('I11.0', 'CID-10', 'Doença cardíaca hipertensiva com insuficiência cardíaca', 'Hipertensão'),
('I11.9', 'CID-10', 'Doença cardíaca hipertensiva sem insuficiência cardíaca', 'Hipertensão'),
('I12.0', 'CID-10', 'Doença renal hipertensiva com insuficiência renal', 'Hipertensão'),
('I12.9', 'CID-10', 'Doença renal hipertensiva sem insuficiência renal', 'Hipertensão'),
('I15.0', 'CID-10', 'Hipertensão renovascular', 'Hipertensão'),
('I15.9', 'CID-10', 'Hipertensão secundária não especificada', 'Hipertensão'),

-- Hipertensão (CIAP-2)
('K86', 'CIAP-2', 'Hipertensão sem complicações', 'Hipertensão'),
('K87', 'CIAP-2', 'Hipertensão com complicações', 'Hipertensão'),

-- Gestação (CID-10)
('O10.0', 'CID-10', 'Hipertensão essencial pré-existente complicando gravidez', 'Gestação'),
('O11', 'CID-10', 'Distúrbio hipertensivo pré-existente com proteinúria', 'Gestação'),
('Z34.0', 'CID-10', 'Supervisão de gravidez normal primeiro trimestre', 'Gestação'),
('Z34.8', 'CID-10', 'Supervisão de outros tipos de gravidez normal', 'Gestação'),
('Z34.9', 'CID-10', 'Supervisão de gravidez normal não especificada', 'Gestação'),
('Z33', 'CID-10', 'Estado de gravidez incidental', 'Gestação'),

-- Gestação (CIAP-2)
('W71', 'CIAP-2', 'Infecções que complicam a gravidez', 'Gestação'),
('W78', 'CIAP-2', 'Gravidez', 'Gestação'),
('W79', 'CIAP-2', 'Gravidez não desejada', 'Gestação'),
('W84', 'CIAP-2', 'Gravidez de alto risco', 'Gestação'),
('W85', 'CIAP-2', 'Diabetes gestacional', 'Gestação'),

-- Puerpério (CID-10)
('F53.0', 'CID-10', 'Transtornos mentais e comportamentais leves associados ao puerpério', 'Puerpério'),
('F53.1', 'CID-10', 'Transtornos mentais e comportamentais graves associados ao puerpério', 'Puerpério'),
('O85', 'CID-10', 'Sepse puerperal', 'Puerpério'),
('O90', 'CID-10', 'Complicações do puerpério não classificadas em outra parte', 'Puerpério'),
('Z39.1', 'CID-10', 'Exame e cuidados da lactante', 'Puerpério'),
('Z39.2', 'CID-10', 'Exame de rotina do puerpério', 'Puerpério'),

-- Puerpério (CIAP-2)
('W90', 'CIAP-2', 'Parto sem complicação', 'Puerpério'),
('W92', 'CIAP-2', 'Complicações do puerpério', 'Puerpério'),

-- Saúde Sexual e Reprodutiva (CID-10)
('Z70.0', 'CID-10', 'Aconselhamento sobre atitude sexual em relação ao sexo', 'Saúde Sexual'),
('Z70.1', 'CID-10', 'Aconselhamento sobre comportamento sexual heterossexual', 'Saúde Sexual'),
('Z70.2', 'CID-10', 'Aconselhamento sobre comportamento sexual homossexual', 'Saúde Sexual'),
('Z70.3', 'CID-10', 'Aconselhamento sobre comportamento sexual bissexual', 'Saúde Sexual'),
('Z70.8', 'CID-10', 'Aconselhamento sobre outros comportamentos sexuais', 'Saúde Sexual'),
('Z70.9', 'CID-10', 'Aconselhamento sobre comportamento sexual não especificado', 'Saúde Sexual'),

-- Saúde Sexual e Reprodutiva (CIAP-2)
('P07', 'CIAP-2', 'Diminuição do desejo sexual', 'Saúde Sexual'),
('P08', 'CIAP-2', 'Diminuição da satisfação sexual', 'Saúde Sexual'),
('W10', 'CIAP-2', 'Contracepção pós-coital', 'Saúde Sexual'),
('W11', 'CIAP-2', 'Contracepção oral', 'Saúde Sexual'),
('W12', 'CIAP-2', 'Contracepção intrauterina (DIU)', 'Saúde Sexual'),
('W13', 'CIAP-2', 'Esterilização', 'Saúde Sexual'),
('W14', 'CIAP-2', 'Contracepção outros', 'Saúde Sexual'),
('W15', 'CIAP-2', 'Infertilidade/subfertilidade', 'Saúde Sexual'),
('X01', 'CIAP-2', 'Dor genital', 'Saúde Sexual'),
('X04', 'CIAP-2', 'Relação sexual dolorosa na mulher', 'Saúde Sexual');

-- VACINAS
INSERT INTO vacinas (codigo, nome, indicacao, faixa_etaria_minima, faixa_etaria_maxima, doses_recomendadas) VALUES 
('09', 'Vacina hepatite B (HepB)', 'Hepatite B', 0, NULL, 3),
('17', 'Vacina Hib', 'Haemophilus influenzae tipo b', 0, 60, 3),
('22', 'Vacina polio injetável (VIP)', 'Poliomielite inativada', 0, 60, 3),
('24', 'Vacina sarampo, caxumba, rubéola (SCR)', 'Sarampo, caxumba, rubéola', 12, NULL, 2),
('26', 'Vacina pneumocócica 10-valente (conjugada)', 'Pneumococo', 0, 60, 3),
('28', 'Vacina polio oral (VOP)', 'Poliomielite oral', 0, 60, 3),
('29', 'Vacina penta acelular (DTPa/VIP/Hib)', 'DTP, VIP, Hib', 0, 60, 3),
('33', 'Vacina influenza trivalente', 'Influenza', 720, NULL, 1), -- 60 anos em meses
('39', 'Vacina tetra (DTP/Hib)', 'DTP, Hib', 0, 60, 3),
('42', 'Vacina penta (DTP/HepB/Hib)', 'DTP, HepB, Hib', 0, 60, 3),
('43', 'Vacina hexa (DTPa/HepB/VIP/Hib)', 'DTP, HepB, VIP, Hib', 0, 60, 3),
('46', 'Vacina DTP', 'Difteria, tétano, pertussis', 0, 60, 3),
('47', 'Vacina DTPa infantil', 'Difteria, tétano, pertussis acelular', 0, 60, 3),
('56', 'Vacina sarampo, caxumba, rubéola e varicela (SCRV)', 'Sarampo, caxumba, rubéola, varicela', 12, NULL, 2),
('57', 'Vacina dTpa adulto', 'Difteria, tétano, pertussis adulto', 140, NULL, 1), -- A partir de 20ª semana gestacional
('58', 'Vacina tetra acelular (DTPa/VIP)', 'DTP acelular, VIP', 0, 60, 3),
('67', 'Vacina HPV quadrivalente', 'HPV 4 tipos', 108, 168, 1), -- 9-14 anos em meses
('77', 'Vacina influenza tetravalente', 'Influenza 4 cepas', 720, NULL, 1), -- 60 anos em meses
('93', 'Vacina HPV nonavalente', 'HPV 9 tipos', 108, 168, 1); -- 9-14 anos em meses

-- INDICADORES PRINCIPAIS
INSERT INTO indicadores (codigo, titulo_resumido, titulo_completo, categoria_id, polaridade, unidade_medida, 
periodicidade_atualizacao, periodicidade_monitoramento, periodicidade_avaliacao, acumulativo, ativo) VALUES 

('C3', 'Cuidado da Gestante e Puérpera', 
'Cuidado à Gestante e Puérpera na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'C'), 
'Maior-melhor', 'Percentual', 'Quadrimestral', 'Mensal', 'Quadrimestral', true, true),

('C4', 'Cuidado da pessoa com diabetes', 
'Cuidado da pessoa com diabetes na Atenção Primária à Saúde', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'C'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', true, true),

('C5', 'Cuidado da pessoa com hipertensão', 
'Cuidado da pessoa com hipertensão na Atenção Primária à Saúde', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'C'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', true, true),

('C6', 'Cuidado da pessoa idosa', 
'Cuidado Integral à Pessoa Idosa na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'C'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('C2', 'Cuidado no desenvolvimento infantil', 
'Cuidado no desenvolvimento infantil na Atenção Primária à Saúde', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'C'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('C7', 'Cuidado da mulher na prevenção do câncer', 
'Cuidado da mulher na prevenção do câncer na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'C'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('C1', 'Mais Acesso à APS', 
'Mais Acesso à Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'A'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('M1', 'Média de atendimentos por pessoa assistida pela eMulti', 
'Média de atendimentos por pessoa assistida pela eMulti na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'M'), 
'Maior-melhor', 'Média', 'Mensal', 'Mensal', 'Quadrimestral', true, true),

('M2', 'Ações interprofissionais realizadas pela eMulti', 
'Ações interprofissionais realizadas pela eMulti na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'M'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', true, true),

('B1', 'Primeira consulta programada', 
'Cobertura de primeira consulta odontológica programada por equipe de Saúde Bucal (eSB) na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'B'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('B2', 'Tratamento concluído', 
'Razão entre tratamentos concluídos por equipe de Saúde Bucal (eSB) na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'B'), 
'Maior-melhor', 'Razão', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('B3', 'Taxa de exodontia', 
'Taxa de exodontias realizadas por equipe de Saúde Bucal (eSB) na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'B'), 
'Menor-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('B4', 'Escovação Supervisionada em faixa etária escolar', 
'Escovação Supervisionada por equipes de Saúde Bucal (eSB) em faixa etária escolar (de 6 a 12 anos) no âmbito da Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'B'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true),

('B5', 'Procedimentos odontológicos preventivos na APS', 
'Procedimentos odontológicos preventivos por equipes de Saúde Bucal (eSB) na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'B'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestre', false, true),

('B6', 'Tratamento Restaurador Atraumático', 
'Tratamentos Restauradores Atraumáticos (ART) realizados por equipe de Saúde Bucal (eSB) na Atenção Primária à Saúde (APS)', 
(SELECT id FROM categorias_indicadores WHERE codigo = 'B'), 
'Maior-melhor', 'Percentual', 'Mensal', 'Mensal', 'Quadrimestral', false, true);

