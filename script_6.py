# Agora vou criar o script SQL completo para o banco de dados
sql_script = """
-- ============================================================================
-- SISTEMA DE MONITORAMENTO DE INDICADORES APS - MINISTÉRIO DA SAÚDE
-- Base de Dados para Indicadores de Qualidade da Atenção Primária à Saúde
-- ============================================================================

-- 1. TABELAS MESTRAS
-- ============================================================================

-- Regiões administrativas
CREATE TABLE regioes (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(2) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Unidades Federativas
CREATE TABLE unidades_federativas (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(2) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sigla VARCHAR(2) NOT NULL,
    regiao_id INTEGER REFERENCES regioes(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Municípios
CREATE TABLE municipios (
    id SERIAL PRIMARY KEY,
    codigo_ibge VARCHAR(7) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    uf_id INTEGER REFERENCES unidades_federativas(id),
    populacao INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Estabelecimentos de Saúde (CNES)
CREATE TABLE estabelecimentos (
    id SERIAL PRIMARY KEY,
    codigo_cnes VARCHAR(20) UNIQUE NOT NULL,
    nome VARCHAR(200) NOT NULL,
    municipio_id INTEGER REFERENCES municipios(id),
    tipo_estabelecimento VARCHAR(50),
    endereco TEXT,
    telefone VARCHAR(20),
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tipos de Equipes
CREATE TABLE tipos_equipes (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sigla VARCHAR(20) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descricao TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Equipes de Saúde
CREATE TABLE equipes (
    id SERIAL PRIMARY KEY,
    ine VARCHAR(20) UNIQUE NOT NULL, -- Identificador Nacional de Equipe
    nome VARCHAR(200) NOT NULL,
    tipo_equipe_id INTEGER REFERENCES tipos_equipes(id),
    estabelecimento_id INTEGER REFERENCES estabelecimentos(id),
    data_credenciamento DATE,
    data_descredenciamento DATE,
    ativo BOOLEAN DEFAULT true,
    carga_horaria INTEGER DEFAULT 40,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. TABELAS DE CLASSIFICAÇÕES
-- ============================================================================

-- CBOs (Classificação Brasileira de Ocupações)
CREATE TABLE cbos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    nivel_ensino VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Procedimentos SIGTAP
CREATE TABLE procedimentos_sigtap (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    subcategoria VARCHAR(50),
    complexidade VARCHAR(20),
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Condições de Saúde (CID-10 e CIAP-2)
CREATE TABLE condicoes_saude (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    tipo VARCHAR(10) NOT NULL, -- CID-10 ou CIAP-2
    descricao VARCHAR(300) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vacinas
CREATE TABLE vacinas (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    nome VARCHAR(200) NOT NULL,
    indicacao VARCHAR(200) NOT NULL,
    faixa_etaria_minima INTEGER,
    faixa_etaria_maxima INTEGER,
    doses_recomendadas INTEGER DEFAULT 1,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. TABELAS DE INDICADORES
-- ============================================================================

-- Categorias de Indicadores
CREATE TABLE categorias_indicadores (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    cor_hex VARCHAR(7), -- Para interface visual
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indicadores principais
CREATE TABLE indicadores (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    titulo_resumido VARCHAR(200) NOT NULL,
    titulo_completo VARCHAR(500) NOT NULL,
    categoria_id INTEGER REFERENCES categorias_indicadores(id),
    conceituacao TEXT,
    objetivo TEXT,
    uso_aplicabilidade TEXT,
    interpretacao_saude TEXT,
    polaridade VARCHAR(20) NOT NULL, -- Maior-melhor ou Menor-melhor
    unidade_medida VARCHAR(20) NOT NULL, -- Percentual, Razão, Média
    periodicidade_atualizacao VARCHAR(20) NOT NULL,
    periodicidade_monitoramento VARCHAR(20) NOT NULL,
    periodicidade_avaliacao VARCHAR(20) NOT NULL,
    acumulativo BOOLEAN DEFAULT false,
    restrito BOOLEAN DEFAULT false,
    ativo BOOLEAN DEFAULT true,
    indice_referencia DECIMAL(5,2),
    ano_referencia INTEGER,
    classificacao_gerencial VARCHAR(50),
    classificacao_desempenho VARCHAR(50),
    limitacoes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Boas Práticas dos Indicadores
CREATE TABLE boas_praticas (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    codigo VARCHAR(5) NOT NULL, -- A, B, C, etc.
    descricao TEXT NOT NULL,
    pontos INTEGER NOT NULL DEFAULT 0,
    periodo_avaliacao_dias INTEGER, -- Em quantos dias deve ser cumprida
    faixa_etaria_minima INTEGER,
    faixa_etaria_maxima INTEGER,
    genero VARCHAR(1), -- M, F ou NULL para ambos
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(indicador_id, codigo)
);

-- Relacionamento Indicadores x CBOs válidos
CREATE TABLE indicadores_cbos (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    cbo_id INTEGER REFERENCES cbos(id),
    tipo_uso VARCHAR(20) NOT NULL, -- consulta, procedimento, todos
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(indicador_id, cbo_id, tipo_uso)
);

-- Relacionamento Indicadores x Procedimentos SIGTAP
CREATE TABLE indicadores_procedimentos (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    boa_pratica_id INTEGER REFERENCES boas_praticas(id),
    procedimento_sigtap_id INTEGER REFERENCES procedimentos_sigtap(id),
    obrigatorio BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Relacionamento Indicadores x Condições de Saúde
CREATE TABLE indicadores_condicoes (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    condicao_saude_id INTEGER REFERENCES condicoes_saude(id),
    tipo VARCHAR(20) NOT NULL, -- elegibilidade, exclusao
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Relacionamento Indicadores x Vacinas
CREATE TABLE indicadores_vacinas (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    boa_pratica_id INTEGER REFERENCES boas_praticas(id),
    vacina_id INTEGER REFERENCES vacinas(id),
    doses_minimas INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. TABELAS DE USUÁRIOS E PROFISSIONAIS
-- ============================================================================

-- Usuários do Sistema de Saúde
CREATE TABLE usuarios (
    id BIGSERIAL PRIMARY KEY,
    cns VARCHAR(15) UNIQUE, -- Cartão Nacional de Saúde
    cpf VARCHAR(11) UNIQUE,
    nome VARCHAR(200) NOT NULL,
    data_nascimento DATE,
    genero VARCHAR(1), -- M, F
    municipio_residencia_id INTEGER REFERENCES municipios(id),
    equipe_vinculada_id INTEGER REFERENCES equipes(id),
    data_vinculacao DATE,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Profissionais de Saúde
CREATE TABLE profissionais (
    id SERIAL PRIMARY KEY,
    cns VARCHAR(15) UNIQUE NOT NULL,
    cpf VARCHAR(11) UNIQUE,
    nome VARCHAR(200) NOT NULL,
    cbo_id INTEGER REFERENCES cbos(id),
    registro_profissional VARCHAR(50), -- CRM, COREN, etc.
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Relacionamento Profissionais x Equipes
CREATE TABLE profissionais_equipes (
    id SERIAL PRIMARY KEY,
    profissional_id INTEGER REFERENCES profissionais(id),
    equipe_id INTEGER REFERENCES equipes(id),
    data_inicio DATE NOT NULL,
    data_fim DATE,
    carga_horaria INTEGER DEFAULT 40,
    ativo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(profissional_id, equipe_id, data_inicio)
);

-- 5. TABELAS DE REGISTROS ASSISTENCIAIS
-- ============================================================================

-- Atendimentos Individuais
CREATE TABLE atendimentos (
    id BIGSERIAL PRIMARY KEY,
    usuario_id BIGINT REFERENCES usuarios(id),
    profissional_id INTEGER REFERENCES profissionais(id),
    equipe_id INTEGER REFERENCES equipes(id),
    data_atendimento DATE NOT NULL,
    tipo_demanda VARCHAR(20) NOT NULL, -- espontanea, programada
    modalidade VARCHAR(20) NOT NULL, -- presencial, domiciliar, remoto
    condicao_avaliada_id INTEGER REFERENCES condicoes_saude(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Procedimentos Realizados
CREATE TABLE procedimentos_realizados (
    id BIGSERIAL PRIMARY KEY,
    atendimento_id BIGINT REFERENCES atendimentos(id),
    procedimento_sigtap_id INTEGER REFERENCES procedimentos_sigtap(id),
    quantidade INTEGER DEFAULT 1,
    solicitado BOOLEAN DEFAULT false,
    avaliado BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Visitas Domiciliares
CREATE TABLE visitas_domiciliares (
    id BIGSERIAL PRIMARY KEY,
    usuario_id BIGINT REFERENCES usuarios(id),
    profissional_id INTEGER REFERENCES profissionais(id),
    equipe_id INTEGER REFERENCES equipes(id),
    data_visita DATE NOT NULL,
    motivo_visita VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Atividades Coletivas
CREATE TABLE atividades_coletivas (
    id SERIAL PRIMARY KEY,
    equipe_id INTEGER REFERENCES equipes(id),
    profissional_responsavel_id INTEGER REFERENCES profissionais(id),
    data_atividade DATE NOT NULL,
    tipo_atividade VARCHAR(50) NOT NULL, -- educacao_saude, escovacao_supervisionada, etc.
    tema VARCHAR(100),
    local_atividade VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Participantes das Atividades Coletivas
CREATE TABLE participantes_atividades (
    id BIGSERIAL PRIMARY KEY,
    atividade_coletiva_id INTEGER REFERENCES atividades_coletivas(id),
    usuario_id BIGINT REFERENCES usuarios(id),
    presente BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(atividade_coletiva_id, usuario_id)
);

-- Registros de Vacinação
CREATE TABLE vacinacoes (
    id BIGSERIAL PRIMARY KEY,
    usuario_id BIGINT REFERENCES usuarios(id),
    vacina_id INTEGER REFERENCES vacinas(id),
    profissional_id INTEGER REFERENCES profissionais(id),
    equipe_id INTEGER REFERENCES equipes(id),
    data_aplicacao DATE NOT NULL,
    dose VARCHAR(10), -- 1, 2, 3, R1 (reforço 1), etc.
    lote VARCHAR(50),
    fabricante VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. TABELAS DE CÁLCULO DOS INDICADORES
-- ============================================================================

-- Períodos de Avaliação
CREATE TABLE periodos_avaliacao (
    id SERIAL PRIMARY KEY,
    ano INTEGER NOT NULL,
    quadrimestre INTEGER NOT NULL, -- 1, 2, 3
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    data_extracao DATE,
    processado BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(ano, quadrimestre)
);

-- Denominadores dos Indicadores (população elegível)
CREATE TABLE indicadores_denominadores (
    id BIGSERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    periodo_id INTEGER REFERENCES periodos_avaliacao(id),
    equipe_id INTEGER REFERENCES equipes(id),
    usuario_id BIGINT REFERENCES usuarios(id),
    elegivel BOOLEAN DEFAULT true,
    motivo_inelegibilidade VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(indicador_id, periodo_id, equipe_id, usuario_id)
);

-- Numeradores dos Indicadores (boas práticas cumpridas)
CREATE TABLE indicadores_numeradores (
    id BIGSERIAL PRIMARY KEY,
    denominador_id BIGINT REFERENCES indicadores_denominadores(id),
    boa_pratica_id INTEGER REFERENCES boas_praticas(id),
    cumprida BOOLEAN DEFAULT false,
    pontos_obtidos INTEGER DEFAULT 0,
    data_ultima_ocorrencia DATE,
    detalhes JSONB, -- Detalhes específicos da boa prática
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(denominador_id, boa_pratica_id)
);

-- Resultados Consolidados dos Indicadores
CREATE TABLE indicadores_resultados (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    periodo_id INTEGER REFERENCES periodos_avaliacao(id),
    equipe_id INTEGER REFERENCES equipes(id),
    estabelecimento_id INTEGER REFERENCES estabelecimentos(id),
    municipio_id INTEGER REFERENCES municipios(id),
    uf_id INTEGER REFERENCES unidades_federativas(id),
    regiao_id INTEGER REFERENCES regioes(id),
    denominador INTEGER NOT NULL DEFAULT 0,
    numerador DECIMAL(10,2) NOT NULL DEFAULT 0,
    resultado DECIMAL(8,4) NOT NULL DEFAULT 0,
    meta DECIMAL(8,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(indicador_id, periodo_id, equipe_id)
);

-- 7. TABELAS DE GESTÃO E MONITORAMENTO
-- ============================================================================

-- Log de Processamento
CREATE TABLE processamento_log (
    id SERIAL PRIMARY KEY,
    indicador_id INTEGER REFERENCES indicadores(id),
    periodo_id INTEGER REFERENCES periodos_avaliacao(id),
    data_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_fim TIMESTAMP,
    status VARCHAR(20) NOT NULL, -- processando, concluido, erro
    registros_processados INTEGER DEFAULT 0,
    erros_encontrados INTEGER DEFAULT 0,
    mensagem_erro TEXT,
    tempo_processamento INTERVAL
);

-- Auditoria de Alterações
CREATE TABLE auditoria (
    id BIGSERIAL PRIMARY KEY,
    tabela VARCHAR(50) NOT NULL,
    registro_id BIGINT NOT NULL,
    acao VARCHAR(10) NOT NULL, -- INSERT, UPDATE, DELETE
    dados_anteriores JSONB,
    dados_novos JSONB,
    usuario_sistema VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. ÍNDICES PARA PERFORMANCE
-- ============================================================================

-- Índices principais para consultas rápidas
CREATE INDEX idx_usuarios_cns ON usuarios(cns);
CREATE INDEX idx_usuarios_equipe ON usuarios(equipe_vinculada_id);
CREATE INDEX idx_usuarios_municipio ON usuarios(municipio_residencia_id);
CREATE INDEX idx_usuarios_data_nascimento ON usuarios(data_nascimento);

CREATE INDEX idx_atendimentos_data ON atendimentos(data_atendimento);
CREATE INDEX idx_atendimentos_usuario ON atendimentos(usuario_id);
CREATE INDEX idx_atendimentos_equipe ON atendimentos(equipe_id);
CREATE INDEX idx_atendimentos_profissional ON atendimentos(profissional_id);

CREATE INDEX idx_visitas_data ON visitas_domiciliares(data_visita);
CREATE INDEX idx_visitas_usuario ON visitas_domiciliares(usuario_id);
CREATE INDEX idx_visitas_equipe ON visitas_domiciliares(equipe_id);

CREATE INDEX idx_vacinacoes_data ON vacinacoes(data_aplicacao);
CREATE INDEX idx_vacinacoes_usuario ON vacinacoes(usuario_id);
CREATE INDEX idx_vacinacoes_vacina ON vacinacoes(vacina_id);

CREATE INDEX idx_resultados_indicador_periodo ON indicadores_resultados(indicador_id, periodo_id);
CREATE INDEX idx_resultados_equipe ON indicadores_resultados(equipe_id);
CREATE INDEX idx_resultados_municipio ON indicadores_resultados(municipio_id);

-- Índices compostos para relatórios
CREATE INDEX idx_denominadores_periodo_equipe ON indicadores_denominadores(periodo_id, equipe_id, indicador_id);
CREATE INDEX idx_numeradores_denominador ON indicadores_numeradores(denominador_id, boa_pratica_id);

"""

# Salvar o script em um arquivo
with open('banco_dados_indicadores_aps.sql', 'w', encoding='utf-8') as f:
    f.write(sql_script)

print("Script SQL do banco de dados criado: banco_dados_indicadores_aps.sql")
print(f"Tamanho do script: {len(sql_script)} caracteres")
print("O script inclui:")
print("- 25 tabelas principais")
print("- Estrutura completa para todos os indicadores identificados")
print("- Índices para otimização de consultas")
print("- Tabelas de auditoria e log")
print("- Relacionamentos entre todas as entidades")