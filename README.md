# Algoritmo Genético para Geração de Grade Horária 🧬📅

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](https://github.com)

**Trabalho Acadêmico - Algoritmos Genéticos**  
**Curso de Ciência da Computação - UNIFESO**

Sistema inteligente de geração automática de grades horárias universitárias utilizando Algoritmos Genéticos. Resolve o problema complexo de alocação de disciplinas, professores e horários respeitando múltiplas restrições hard e soft.

---

## 📁 Estrutura do Projeto

```
algoritimos_genericos/
├── algoritmo_genetico_grade.py    # Implementação completa do AG
├── relatorio_tecnico.md           # Documentação técnica detalhada
├── README.md                      
```

### 📦 Arquivos Gerados (após execução)
- `grade_horaria.json` - Grade horária completa em formato JSON
- `melhor_solucao.json` - Melhor solução encontrada pelo AG
- `evolucao_fitness.png` - Visualização da evolução do fitness

---

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/meliga1/algoritimos_genericos.git
cd algoritimos_genericos
```

2. **Instale as dependências**
```bash
pip install numpy matplotlib
```

### Execução

**Executar o algoritmo:**
```bash
python algoritmo_genetico_grade.py
```

O sistema irá:
- Gerar a grade horária automaticamente
- Exibir estatísticas e relatórios
- Criar gráficos de evolução
- Exportar resultados em JSON

---

## 📊 Características do Sistema

### 🎯 Escopo do Problema

| Característica | Quantidade |
|----------------|------------|
| **Disciplinas** | 36 (considerando turmas A e B) |
| **Professores** | 14 (com aderências e disponibilidades) |
| **Períodos Acadêmicos** | 4 (1º, 2º/3º, 4º/5º, 6º/7º) |
| **Dias Úteis** | 5 (Segunda a Sexta) + Sábado (EAD) |
| **Horários** | 1 slot por dia (19:00-22:00) |
| **Turmas** | A, B, e AB (turmas unificadas) |

### ⚙️ Restrições Implementadas

**Restrições Hard (obrigatórias):**
- ✅ Professor não pode lecionar em dois lugares ao mesmo tempo
- ✅ Turma não pode ter duas disciplinas no mesmo horário
- ✅ Disciplinas EAD devem ser aos sábados
- ✅ Professores devem ter aderência às disciplinas

**Restrições Soft (desejáveis):**
- 🎯 Respeitar disponibilidade semanal dos professores
- 🎯 Respeitar dias específicos de cada professor
- 🎯 Distribuição equilibrada de aulas ao longo da semana

---

## 🧬 Algoritmo Genético

### Configuração Otimizada

```python
AlgoritmoGenetico(
    tamanho_populacao=150,
    taxa_mutacao=0.15,
    taxa_cruzamento=0.85,
    elitismo=0.10,
    metodo_selecao='torneio',
    n_geracoes=200
)
```

### Componentes do AG

**1. Representação (Cromossomo)**
- Cada gene = alocação completa (disciplina, professor, dia, horário)
- Codificação direta e intuitiva
- Validação automática durante criação

**2. Função de Fitness**
- Normalizada entre 0 e 1 (quanto maior, melhor)
- Penalização graduada por tipo de violação
- Bônus por distribuição equilibrada
- Sistema de pesos ajustados experimentalmente

**3. Operadores Genéticos**
- **Seleção:** Torneio (k=3) ou Roleta
- **Cruzamento:** Um ponto ou uniforme (85%)
- **Mutação:** Inteligente com validação (15%)
- **Elitismo:** Preserva os melhores 10%

### 📈 Resultados Esperados

| Métrica | Valor Típico |
|---------|--------------|
| **Fitness Final** | 0.85 - 0.92 |
| **Convergência** | 50-100 gerações |
| **Tempo de Execução** | 10-30 segundos |
| **Conflitos Finais** | 0-2 conflitos |
| **Melhoria** | +40-60% vs. solução inicial |

---

## 🎯 Funcionalidades Principais

### 1. **Geração Automática de Grade**
- Alocação inteligente de disciplinas, professores e horários
- Respeito automático às restrições do problema
- Múltiplas soluções viáveis por execução

### 2. **Análise e Visualização**
```python
# Gráficos de evolução do fitness
plotar_evolucao(ag.historico_fitness)

# Estatísticas detalhadas
stats = gerar_estatisticas(melhor_solucao)

# Grade completa formatada
imprimir_grade_completa(melhor_solucao)
```

### 3. **Exportação de Dados**
- **JSON:** Grade completa estruturada e melhor solução
- **PNG:** Gráficos de evolução do fitness

### 4. **Análise e Relatórios**
- Estatísticas completas da solução
- Detecção automática de conflitos
- Validação de todas as restrições
- Relatórios detalhados de execução

### 5. **Validação Robusta**
```python
# Validação completa da solução
validacao = validar_solucao_final(melhor_solucao)
# Verifica: conflitos, aderência, disponibilidade, EAD
```

---

## 🔬 Experimentos e Análises

O sistema é altamente configurável, permitindo experimentação com diferentes parâmetros:

### Configurações Recomendadas

1. **Configuração Padrão** - Parâmetros balanceados (população=150, mutação=15%)
2. **Alta Exploração** - Mutação elevada (25-30%) para maior diversidade
3. **População Grande** - 200+ indivíduos para problemas complexos
4. **Alto Elitismo** - 20-30% para convergência mais rápida
5. **Seleção por Roleta** - Alternativa ao torneio

### Parâmetros para Ajuste

- **Taxa de Mutação:** Teste entre 10% e 30%
- **Tamanho da População:** Varie de 100 a 250 indivíduos
- **Número de Gerações:** Ajuste de 100 a 300 conforme necessário
- **Taxa de Elitismo:** Experimente 5% a 25%

---

## 📝 Exemplo de Saída

```
================================================================================
RELATÓRIO DE EXECUÇÃO DO ALGORITMO GENÉTICO
================================================================================

1. PARÂMETROS DO ALGORITMO:
   • Tamanho da população: 150
   • Taxa de mutação: 15.00%
   • Taxa de cruzamento: 85.00%
   • Taxa de elitismo: 10.00%
   • Método de seleção: torneio
   • Número de gerações: 200

2. ESTATÍSTICAS DA SOLUÇÃO FINAL:
   • Fitness alcançado: 0.8934
   • Total de disciplinas alocadas: 36
   • Disciplinas presenciais: 32
   • Disciplinas EAD: 4

3. ANÁLISE DE CONFLITOS:
   • Conflitos de professor (mesmo horário): 0
   • Conflitos de turma (mesmo horário): 1
   • Violações de disponibilidade: 0

6. ANÁLISE DA EVOLUÇÃO:
   • Fitness inicial: 0.5234
   • Fitness final: 0.8934
   • Melhoria: 70.69%
   • Status: População convergiu
```

---

## 💡 Detalhes Técnicos

### Estruturas de Dados

```python
# Gene - Representa uma alocação
Gene(disciplina_id, professor, dia, horario)

# Cromossomo - Representa uma solução completa
Cromossomo(genes=[Gene1, Gene2, ..., Gene36])

# Disciplina
Disciplina(id, nome, periodo, turma, ead, alunos)
```

### Função de Fitness - Sistema de Penalização

| Violação | Penalidade | Prioridade |
|----------|------------|------------|
| Conflito de professor | -75 | Alta |
| Conflito de turma | -75 | Alta |
| Professor sem aderência | -50 | Alta |
| EAD fora do sábado | -40 | Média |
| Violação de dias específicos | -35 | Média |
| Presencial no sábado | -30 | Baixa |
| Excesso de disponibilidade | -25 | Baixa |

**Bônus:** +30 pontos para distribuição equilibrada de aulas

### Operadores Genéticos Detalhados

**Mutação Inteligente:**
- Escolha aleatória entre 3 tipos: professor, dia, ou ambos
- Validação automática de aderência
- Respeito às restrições de EAD
- Consideração de dias específicos

**Cruzamento:**
- 50% chance de um ponto, 50% chance de uniforme
- Preservação da estrutura dos genes
- Criação de dois filhos por operação

---

## 🔧 Customização

### Modificar Parâmetros do AG

```python
ag = AlgoritmoGenetico(
    tamanho_populacao=200,      # Aumentar para maior diversidade
    taxa_mutacao=0.20,           # Aumentar para mais exploração
    taxa_cruzamento=0.90,        # Aumentar para mais recombinação
    elitismo=0.15,               # Aumentar para preservar mais soluções
    metodo_selecao='roleta'      # Alternar método de seleção
)
```

### Adicionar Novas Disciplinas

Edite a lista `disciplinas` em `algoritmo_genetico_grade.py`:

```python
disciplinas = [
    Disciplina("ID", "Nome da Disciplina", periodo, "turma", ead, alunos),
    # ...
]
```

### Adicionar Novos Professores

Edite o dicionário `professores_aderencia`:

```python
professores_aderencia = {
    "Nome do Professor": {
        "disponibilidade": 3,
        "dias_especificos": {"segunda": "presencial", "quarta": "online"},
        "disciplinas": ["ID1", "ID2", "ID3"]
    },
    # ...
}
```

---

## 🐛 Problemas Conhecidos

- Em casos extremamente restritos, pode haver conflitos residuais (1-2)
- Tempo de execução varia com complexidade da instância

Observação (Windows): se o gráfico não abrir, ele ainda será salvo em `evolucao_fitness.png` no diretório do projeto.

---

## 📄 Licença

Este projeto é um trabalho acadêmico desenvolvido para fins educacionais.

---

## 👨‍💻 Autor

**Carlos Meliga**  
Ciência da Computação - UNIFESO  
Disciplina: Inteligência Artificial e Inteligência Computacional

---

<div align="center">

by Carlos Meliga

</div>