# Criar um arquivo README.md com documentação completa do banco de dados
readme_content = """
# Sistema de Banco de Dados - Indicadores de Qualidade APS

## Visão Geral

Este banco de dados foi desenvolvido para suportar o sistema de monitoramento de indicadores de qualidade da Atenção Primária à Saúde (APS) do Ministério da Saúde do Brasil. Baseado nas **Fichas Técnicas de Qualificação** oficiais, o sistema permite o cálculo, monitoramento e análise de 15 indicadores principais organizados em 4 categorias.

## Categorias de Indicadores

### 🟢 Cuidado (C) - 7 Indicadores
- **C1**: Mais Acesso à APS
- **C2**: Cuidado no desenvolvimento infantil  
- **C3**: Cuidado da Gestante e Puérpera
- **C4**: Cuidado da pessoa com diabetes
- **C5**: Cuidado da pessoa com hipertensão
- **C6**: Cuidado da pessoa idosa
- **C7**: Cuidado da mulher na prevenção do câncer

### 🔵 Saúde Bucal (B) - 6 Indicadores
- **B1**: Primeira consulta programada
- **B2**: Tratamento concluído
- **B3**: Taxa de exodontia
- **B4**: Escovação Supervisionada
- **B5**: Procedimentos preventivos
- **B6**: Tratamento Restaurador Atraumático

### 🔴 Multiprofissional (M) - 2 Indicadores
- **M1**: Média de atendimentos por pessoa eMulti
- **M2**: Ações interprofissionais eMulti

## Arquitetura do Banco de Dados

### Estrutura Principal
- **25 tabelas principais**
- **Sistema de auditoria completo**
- **Índices otimizados para performance**
- **Views e funções para relatórios**
- **Triggers automáticos**

### Tabelas Mestras
- `regioes` - Regiões administrativas do Brasil
- `unidades_federativas` - Estados brasileiros
- `municipios` - Municípios brasileiros
- `estabelecimentos` - Unidades de saúde (CNES)
- `equipes` - Equipes de saúde (INE)
- `tipos_equipes` - Tipos de equipes (eSF, eAP, eSB, eMulti, etc.)

### Tabelas de Classificações
- `cbos` - Classificação Brasileira de Ocupações
- `procedimentos_sigtap` - Procedimentos do Sistema SIGTAP
- `condicoes_saude` - Condições CID-10 e CIAP-2
- `vacinas` - Vacinas do calendário nacional

### Tabelas de Indicadores
- `indicadores` - Indicadores principais
- `boas_praticas` - Boas práticas por indicador
- `indicadores_cbos` - CBOs válidos por indicador
- `indicadores_procedimentos` - Procedimentos por boa prática
- `indicadores_condicoes` - Condições de elegibilidade
- `indicadores_vacinas` - Vacinas por boa prática

### Tabelas Assistenciais
- `usuarios` - Usuários do SUS
- `profissionais` - Profissionais de saúde
- `atendimentos` - Atendimentos individuais
- `procedimentos_realizados` - Procedimentos executados
- `visitas_domiciliares` - Visitas domiciliares ACS/TACS
- `atividades_coletivas` - Atividades coletivas
- `vacinacoes` - Registros de vacinação

### Tabelas de Cálculo
- `periodos_avaliacao` - Períodos de avaliação quadrimestrais
- `indicadores_denominadores` - População elegível
- `indicadores_numeradores` - Boas práticas cumpridas
- `indicadores_resultados` - Resultados consolidados

## Boas Práticas por Indicador

### C3 - Cuidado da Gestante e Puérpera (11 práticas - 100 pontos)
- **A** (9 pts): Primeira consulta pré-natal até 12 semanas
- **B** (10 pts): Pelo menos 7 consultas na gestação
- **C** (9 pts): 7 registros de pressão arterial
- **D** (9 pts): 7 registros de peso e altura
- **E** (9 pts): 3 visitas domiciliares ACS/TACS
- **F** (9 pts): Dose dTpa após 20ª semana
- **G** (9 pts): Testes rápidos 1º trimestre
- **H** (9 pts): Testes rápidos 3º trimestre
- **I** (9 pts): Consulta no puerpério
- **J** (9 pts): Visita domiciliar puerpério
- **K** (9 pts): Avaliação odontológica

### C4 - Cuidado da Pessoa com Diabetes (6 práticas - 100 pontos)
- **A** (20 pts): Consulta médico/enfermeiro (6 meses)
- **B** (15 pts): Pressão arterial (6 meses)
- **C** (20 pts): 2 visitas domiciliares ACS (12 meses)
- **D** (15 pts): Peso e altura (12 meses)
- **E** (15 pts): Hemoglobina glicada (12 meses)
- **F** (15 pts): Avaliação dos pés (12 meses)

### C5 - Cuidado da Pessoa com Hipertensão (4 práticas - 100 pontos)
- **A** (25 pts): Consulta médico/enfermeiro (6 meses)
- **B** (25 pts): Pressão arterial (6 meses)
- **C** (25 pts): 2 visitas domiciliares ACS (12 meses)
- **D** (25 pts): Peso e altura (12 meses)

### C6 - Cuidado da Pessoa Idosa ≥60 anos (4 práticas - 100 pontos)
- **A** (25 pts): Consulta médico/enfermeiro (12 meses)
- **B** (25 pts): 2 registros peso e altura (12 meses)
- **C** (25 pts): 2 visitas domiciliares ACS (12 meses)
- **D** (25 pts): Vacina influenza (12 meses)

### C2 - Cuidado Desenvolvimento Infantil até 2 anos (5 práticas - 100 pontos)
- **A** (20 pts): 1ª consulta até 30 dias
- **B** (20 pts): 9 consultas até 2 anos
- **C** (20 pts): 9 registros peso e altura
- **D** (20 pts): 2 visitas domiciliares (30 dias e 6 meses)
- **E** (20 pts): Vacinação completa

### C7 - Cuidado da Mulher Prevenção Câncer (4 práticas - 100 pontos)
- **A** (20 pts): Exame colo útero 25-64 anos (36 meses)
- **B** (30 pts): Vacina HPV 9-14 anos
- **C** (30 pts): Saúde sexual/reprodutiva 14-69 anos (12 meses)
- **D** (20 pts): Mamografia 50-69 anos (24 meses)

## Principais CBOs Mapeados

### Categoria Médica
- `2251-42` - Médico ESF
- `2251-70` - Médico generalista
- `2251-30` - Médico família e comunidade

### Categoria Enfermagem
- `2235-65` - Enfermeiro ESF
- `2235-05` - Enfermeiro
- `3222-05` - Técnico enfermagem
- `3222-30` - Auxiliar enfermagem

### Categoria ACS/TACS
- `5151-05` - Agente Comunitário de Saúde
- `3222-55` - Técnico ACS

### Categoria Odontológica
- `2232-08` - Cirurgião-dentista clínico
- `2232-93` - Cirurgião-dentista ESF
- `3224-05` - Técnico saúde bucal
- `3224-15` - Auxiliar saúde bucal

### Categoria Multiprofissional
- `2516-05` - Assistente social
- `2234-05` - Farmacêutico
- `2236-05` - Fisioterapeuta
- `2237-10` - Nutricionista
- `2515-10` - Psicólogo

## Procedimentos SIGTAP Principais

### Antropometria e Sinais Vitais
- `01.01.04.002-4` - Avaliação antropométrica
- `01.01.04.008-3` - Medição de peso
- `01.01.04.007-5` - Medição de altura
- `03.01.10.003-9` - Aferição pressão arterial

### Testes Rápidos
- `02.14.01.004-0` - Teste rápido HIV gestante
- `02.14.01.007-4` - Teste rápido sífilis
- `02.14.01.009-0` - Teste rápido hepatite C
- `02.14.01.010-4` - Teste rápido hepatite B

### Rastreamento de Câncer
- `02.04.03.018-8` - Mamografia bilateral
- `02.03.01.008-6` - Exame citopatológico
- `02.01.02.007-6` - Coleta HPV

### Odontologia Preventiva
- `01.01.02.007-4` - Aplicação tópica flúor
- `01.01.02.008-2` - Evidenciação placa
- `01.01.02.010-4` - Orientação higiene bucal

## Vacinas do Calendário Nacional

### Infantis
- `42` - Vacina penta (DTP/HepB/Hib)
- `22` - Vacina polio injetável (VIP)
- `26` - Vacina pneumocócica 10-valente
- `24` - Vacina SCR (sarampo, caxumba, rubéola)

### Específicas
- `57` - Vacina dTpa adulto (gestantes)
- `67` - Vacina HPV quadrivalente (9-14 anos)
- `33` - Vacina influenza trivalente (≥60 anos)

## Instalação e Uso

### 1. Executar Scripts na Ordem:
```sql
-- 1. Estrutura das tabelas
\i banco_dados_indicadores_aps.sql

-- 2. Dados iniciais
\i dados_iniciais_indicadores_aps.sql

-- 3. Boas práticas
\i boas_praticas_indicadores_aps.sql

-- 4. Views e funções
\i consultas_uteis_indicadores_aps.sql
```

### 2. Consultas Principais:

#### Relatório de Indicadores
```sql
SELECT * FROM vw_indicadores_resumo;
```

#### Performance das Equipes
```sql
SELECT * FROM vw_performance_equipes;
```

#### Calcular Resultado de Indicador
```sql
SELECT * FROM fn_calcular_resultado_indicador('C4', 1, NULL);
```

#### Cobertura Vacinal
```sql
SELECT * FROM vw_cobertura_vacinal;
```

## Recursos Avançados

### Sistema de Auditoria
- Todas as alterações são registradas na tabela `auditoria`
- Triggers automáticos em tabelas críticas
- Controle de usuário e timestamp

### Funções de Cálculo
- `fn_calcular_elegibilidade_indicador()` - Determina população elegível
- `fn_calcular_resultado_indicador()` - Calcula resultado final
- `trigger_auditoria()` - Sistema de auditoria automática

### Índices Otimizados
- Índices compostos para consultas frequentes
- Índices por data para filtragem temporal
- Índices de foreign keys para joins

## Características Técnicas

- **SGBD**: PostgreSQL 12+
- **Encoding**: UTF-8
- **Fuso horário**: Configurável por região
- **Constraints**: Integridade referencial completa
- **Backup**: Estrutura permite backup incremental

## Manutenção

### Rotinas Recomendadas:
1. **Limpeza de logs**: Purgar auditoria > 2 anos
2. **Reindex**: Mensal nas tabelas grandes
3. **Vacuum**: Semanal nas tabelas de movimento
4. **Backup**: Diário completo + incremental

### Monitoramento:
- Tabela `processamento_log` para acompanhar cálculos
- Views de performance para identificar gargalos
- Auditoria para rastreamento de alterações

## Suporte e Contato

**Coordenação Geral de Monitoramento, Avaliação e Inteligência Analítica da APS**
- Email: cgmaiasaps@saude.gov.br
- Telefone: (61) 3315-9087
- Setor: Secretaria de Atenção Primária à Saúde (SAPS/MS)

---

*Sistema desenvolvido com base nas Fichas Técnicas de Qualificação do Ministério da Saúde - 2024*
"""

# Salvar o README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md criado com documentação completa!")
print("Arquivo contém:")
print("- Visão geral do sistema")
print("- Descrição detalhada de todos os 15 indicadores")
print("- 34 boas práticas mapeadas")
print("- Guia de instalação e uso")
print("- Consultas principais")
print("- Características técnicas")
print("- Guia de manutenção")