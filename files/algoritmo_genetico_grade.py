import random
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict, namedtuple
from typing import List, Dict, Tuple, Set
import json
from datetime import datetime

# ==================== ESTRUTURAS DE DADOS ====================

Disciplina = namedtuple("Disciplina", ["id", "nome", "periodo", "turma", "ead", "alunos"])
Professor = namedtuple("Professor", ["nome", "disponibilidade", "dias_especificos"])

# ==================== DADOS DO PROBLEMA ====================

# Disciplinas por período
disciplinas = [
    # 1º Período
    Disciplina("LFT_1A", "Laboratórios de Fundamentos em TIC", 1, "A", False, 50),
    Disciplina("LFT_1B", "Laboratórios de Fundamentos em TIC", 1, "B", False, 50),
    Disciplina("RC_1A", "Robótica Computacional", 1, "A", False, 50),
    Disciplina("RC_1B", "Robótica Computacional", 1, "B", False, 50),
    Disciplina("RPC_1A", "Resolução de Problemas Computacionais", 1, "A", False, 50),
    Disciplina("RPC_1B", "Resolução de Problemas Computacionais", 1, "B", False, 50),
    Disciplina("CE_1", "Comunicação e Expressão", 1, "AB", True, 100),  # EAD
    
    # 2º/3º Período
    Disciplina("GAAL_23A", "Geometria Analítica e Álgebra Linear", 23, "A", False, 73),
    Disciplina("GAAL_23B", "Geometria Analítica e Álgebra Linear", 23, "B", False, 27),
    Disciplina("IFTE_23A", "Introdução à Física Teórica e Experimental", 23, "A", False, 73),
    Disciplina("IFTE_23B", "Introdução à Física Teórica e Experimental", 23, "B", False, 27),
    Disciplina("EDP_23A", "Estruturas de Dados e Paradigmas", 23, "A", False, 73),
    Disciplina("EDP_23B", "Estruturas de Dados e Paradigmas", 23, "B", False, 27),
    Disciplina("CDS_23", "Cidadania, Diversidade e Sustentabilidade", 23, "AB", True, 100),  # EAD
    
    # 4º/5º Período
    Disciplina("PE_45A", "Probabilidade e Estatística", 45, "A", False, 57),
    Disciplina("PE_45B", "Probabilidade e Estatística", 45, "B", False, 26),
    Disciplina("C2_45A", "Cálculo II", 45, "A", False, 57),
    Disciplina("C2_45B", "Cálculo II", 45, "B", False, 26),
    Disciplina("BD_45A", "Banco de Dados", 45, "A", False, 57),
    Disciplina("BD_45B", "Banco de Dados", 45, "B", False, 26),
    Disciplina("ES_45A", "Engenharia de Software", 45, "A", False, 57),
    Disciplina("ES_45B", "Engenharia de Software", 45, "B", False, 26),
    Disciplina("PDWF_45A", "Projeto de Desenvolvimento Web Front-End", 45, "A", False, 57),
    Disciplina("PDWF_45B", "Projeto de Desenvolvimento Web Front-End", 45, "B", False, 26),
    Disciplina("EI_45", "Empreendedorismo e Inovação", 45, "AB", True, 83),  # EAD
    
    # 6º/7º Período
    Disciplina("COMP_67A", "Compiladores", 67, "A", False, 55),
    Disciplina("COMP_67B", "Compiladores", 67, "B", False, 41),
    Disciplina("CGPI_67A", "Computação Gráfica e Processamento de Imagens", 67, "A", False, 55),
    Disciplina("CGPI_67B", "Computação Gráfica e Processamento de Imagens", 67, "B", False, 41),
    Disciplina("DAM_67A", "Desenvolvimento de Aplicações Móveis", 67, "A", False, 55),
    Disciplina("DAM_67B", "Desenvolvimento de Aplicações Móveis", 67, "B", False, 41),
    Disciplina("PDMR_67A", "Projeto de Desenvolvimento Mobile e RA", 67, "A", False, 55),
    Disciplina("PDMR_67B", "Projeto de Desenvolvimento Mobile e RA", 67, "B", False, 41),
    Disciplina("TCC1_67A", "TCC 1", 67, "A", False, 55),
    Disciplina("TCC1_67B", "TCC 1", 67, "B", False, 41),
    Disciplina("CCG_67", "Cenários, Cultura e Globalização", 67, "AB", True, 96),  # EAD
]

# Professores e suas aderências
professores_aderencia = {
    "Alberto Angonese": {
        "disponibilidade": 2,
        "dias_especificos": None,
        "disciplinas": ["RC_1A", "RC_1B"]
    },
    "Rodrigo Braga": {
        "disponibilidade": 5,
        "dias_especificos": None,
        "disciplinas": ["LFT_1A", "LFT_1B", "RPC_1A", "RPC_1B", "PDWF_45A", "PDWF_45B"]
    },
    "Antonio Pedrosa": {
        "disponibilidade": 3,
        "dias_especificos": None,
        "disciplinas": ["PDWF_45A", "PDWF_45B", "PDMR_67A", "PDMR_67B"]
    },
    "Chessman Kennedy": {
        "disponibilidade": 5,
        "dias_especificos": None,
        "disciplinas": ["DAM_67A", "DAM_67B", "COMP_67A", "COMP_67B", "BD_45A", "BD_45B"]
    },
    "Victor Thomaz": {
        "disponibilidade": 2,
        "dias_especificos": {"terça": "online", "quarta": "presencial"},
        "disciplinas": ["LFT_1A", "LFT_1B", "TCC1_67A", "TCC1_67B"]
    },
    "Hélio de Paula": {
        "disponibilidade": 2,
        "dias_especificos": None,
        "disciplinas": ["CGPI_67A", "CGPI_67B"]
    },
    "Eugenio Silva": {
        "disponibilidade": 2,
        "dias_especificos": {"quinta": "presencial", "sexta": "online"},
        "disciplinas": ["COMP_67A", "COMP_67B", "TCC1_67A", "TCC1_67B"]
    },
    "Danielle Santos": {
        "disponibilidade": 2,
        "dias_especificos": {"segunda": "presencial", "quarta": "presencial"},
        "disciplinas": ["PE_45A", "PE_45B"]
    },
    "Andre Campos": {
        "disponibilidade": 3,
        "dias_especificos": None,
        "disciplinas": ["ES_45A", "ES_45B"]
    },
    "Rosemberg Brasileiro": {
        "disponibilidade": 4,
        "dias_especificos": None,
        "disciplinas": ["IFTE_23A", "IFTE_23B", "C2_45A", "C2_45B"]
    },
    "Alexandra Raibolt": {
        "disponibilidade": 2,
        "dias_especificos": {"segunda": "presencial", "terça": "presencial"},
        "disciplinas": ["EDP_23A", "EDP_23B"]
    },
    "Leandro Lima": {
        "disponibilidade": 1,
        "dias_especificos": {"quinta": "presencial"},
        "disciplinas": ["GAAL_23A", "GAAL_23B"]
    },
    "Professor Concurso": {
        "disponibilidade": 3,
        "dias_especificos": None,
        "disciplinas": ["C2_45A", "C2_45B", "GAAL_23A", "GAAL_23B"]
    },
    "Professor EAD": {
        "disponibilidade": 1,
        "dias_especificos": {"sábado": "online"},
        "disciplinas": ["CE_1", "CDS_23", "EI_45", "CCG_67"]
    }
}

# Configurações do problema
DIAS_SEMANA = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
HORARIOS = ["19:00-22:00"]  # Uma disciplina ocupa o horário completo (3 horas)
DIAS_UTEIS = 5  # Segunda a Sexta
DIA_EAD = 5  # Sábado (índice)

# ==================== REPRESENTAÇÃO GENÉTICA ====================

class Gene:
    """Representa uma alocação de disciplina"""
    def __init__(self, disciplina_id, professor, dia, horario):
        self.disciplina_id = disciplina_id
        self.professor = professor
        self.dia = dia  # 0-5 (segunda-sábado)
        self.horario = horario  # 0 (19:00-22:00)
    
    def __repr__(self):
        return f"Gene({self.disciplina_id}, {self.professor}, dia={self.dia}, h={self.horario})"
    
    def to_dict(self):
        return {
            'disciplina_id': self.disciplina_id,
            'professor': self.professor,
            'dia': self.dia,
            'horario': self.horario
        }
    
    @staticmethod
    def from_dict(d):
        return Gene(d['disciplina_id'], d['professor'], d['dia'], d['horario'])

class Cromossomo:
    """Representa uma solução completa (grade horária)"""
    def __init__(self, genes=None):
        if genes is None:
            self.genes = self._criar_genes_aleatorios()
        else:
            self.genes = genes
        self.fitness = None
    
    def _criar_genes_aleatorios(self):
        """Cria genes aleatórios para todas as disciplinas"""
        genes = []
        for disc in disciplinas:
            # Encontrar professores válidos para esta disciplina
            profs_validos = []
            for prof, info in professores_aderencia.items():
                if disc.id in info["disciplinas"]:
                    profs_validos.append(prof)
            
            if not profs_validos:
                continue  # Pular disciplina sem professor
            
            professor = random.choice(profs_validos)
            
            # Determinar dia baseado se é EAD ou não
            if disc.ead:
                dia = DIA_EAD  # Sábado
            else:
                # Considerar disponibilidade do professor
                info_prof = professores_aderencia[professor]
                if info_prof["dias_especificos"]:
                    dias_possiveis = [DIAS_SEMANA.index(d) for d in info_prof["dias_especificos"].keys() 
                                     if DIAS_SEMANA.index(d) < DIAS_UTEIS]
                    if dias_possiveis:
                        dia = random.choice(dias_possiveis)
                    else:
                        dia = random.randrange(DIAS_UTEIS)
                else:
                    dia = random.randrange(DIAS_UTEIS)
            
            horario = 0  # Apenas um horário (19:00-22:00)
            genes.append(Gene(disc.id, professor, dia, horario))
        
        return genes
    
    def copy(self):
        """Cria uma cópia profunda do cromossomo"""
        new_genes = [Gene(g.disciplina_id, g.professor, g.dia, g.horario) for g in self.genes]
        return Cromossomo(new_genes)

# ==================== FUNÇÃO DE FITNESS ====================

def calcular_fitness(cromossomo):
    """
    Calcula o fitness de um cromossomo (grade horária)
    Quanto MAIOR o valor, MELHOR a solução
    """
    penalidade = 0
    bonus = 0
    
    # Mapear disciplinas por ID para acesso rápido
    disc_map = {d.id: d for d in disciplinas}
    
    # Verificar conflitos e restrições
    professor_horarios = defaultdict(list)
    turma_horarios = defaultdict(list)
    professor_dias = defaultdict(set)
    
    for gene in cromossomo.genes:
        disc = disc_map[gene.disciplina_id]
        chave_horario = (gene.dia, gene.horario)
        
        # 1. Verificar se professor tem aderência à disciplina
        if gene.disciplina_id not in professores_aderencia[gene.professor]["disciplinas"]:
            penalidade += 50  # Reduzido de 100
        
        # 2. Verificar conflitos de professor (mesmo horário)
        professor_horarios[(gene.professor, chave_horario)].append(gene)
        
        # 3. Verificar conflitos de turma (mesmo horário)
        # Considerar período e turma
        chave_turma = (disc.periodo, disc.turma)
        turma_horarios[(chave_turma, chave_horario)].append(gene)
        
        # 4. Verificar disponibilidade do professor
        professor_dias[gene.professor].add(gene.dia)
        
        # 5. Verificar restrições de EAD
        if disc.ead and gene.dia != DIA_EAD:
            penalidade += 40  # Reduzido de 80
        elif not disc.ead and gene.dia == DIA_EAD:
            penalidade += 30  # Reduzido de 60
        
        # 6. Verificar dias específicos do professor
        info_prof = professores_aderencia[gene.professor]
        if info_prof["dias_especificos"]:
            dia_nome = DIAS_SEMANA[gene.dia]
            if dia_nome not in info_prof["dias_especificos"]:
                penalidade += 35  # Reduzido de 70
    
    # Aplicar penalidades por conflitos
    for key, genes in professor_horarios.items():
        if len(genes) > 1:
            penalidade += 75 * (len(genes) - 1)  # Reduzido de 150
    
    for key, genes in turma_horarios.items():
        if len(genes) > 1:
            penalidade += 75 * (len(genes) - 1)  # Reduzido de 150
    
    # Verificar disponibilidade semanal dos professores
    for professor, dias in professor_dias.items():
        disponibilidade = professores_aderencia[professor]["disponibilidade"]
        if len(dias) > disponibilidade:
            penalidade += 25 * (len(dias) - disponibilidade)  # Reduzido de 50
    
    # Bônus por boa distribuição
    # Distribuição uniforme das aulas ao longo da semana
    dias_utilizados = defaultdict(int)
    for gene in cromossomo.genes:
        if gene.dia < DIAS_UTEIS:  # Apenas dias úteis
            dias_utilizados[gene.dia] += 1
    
    if dias_utilizados:
        media = sum(dias_utilizados.values()) / len(dias_utilizados)
        desvio = sum(abs(v - media) for v in dias_utilizados.values())
        bonus += max(0, 30 - desvio)  # Aumentado de 20
    
    # Fitness final - usando escala maior
    fitness = max(0, 2000 - penalidade + bonus)
    return fitness / 2000.0  # Normalizar entre 0 e 1

# ==================== OPERADORES GENÉTICOS ====================

def selecao_torneio(populacao, k=3):
    """Seleção por torneio"""
    torneio = random.sample(populacao, min(k, len(populacao)))
    torneio.sort(key=lambda x: x.fitness, reverse=True)
    return torneio[0]

def selecao_roleta(populacao):
    """Seleção por roleta"""
    total_fitness = sum(c.fitness for c in populacao)
    if total_fitness == 0:
        return random.choice(populacao)
    
    r = random.uniform(0, total_fitness)
    acumulado = 0
    for cromossomo in populacao:
        acumulado += cromossomo.fitness
        if acumulado >= r:
            return cromossomo
    return populacao[-1]

def cruzamento_um_ponto(pai1, pai2):
    """Cruzamento de um ponto"""
    if len(pai1.genes) < 2:
        return pai1.copy(), pai2.copy()
    
    ponto = random.randint(1, len(pai1.genes) - 1)
    
    # Criar filhos
    genes_filho1 = [Gene(g.disciplina_id, g.professor, g.dia, g.horario) 
                   for g in pai1.genes[:ponto]] + \
                  [Gene(g.disciplina_id, g.professor, g.dia, g.horario) 
                   for g in pai2.genes[ponto:]]
    
    genes_filho2 = [Gene(g.disciplina_id, g.professor, g.dia, g.horario) 
                   for g in pai2.genes[:ponto]] + \
                  [Gene(g.disciplina_id, g.professor, g.dia, g.horario) 
                   for g in pai1.genes[ponto:]]
    
    return Cromossomo(genes_filho1), Cromossomo(genes_filho2)

def cruzamento_uniforme(pai1, pai2):
    """Cruzamento uniforme"""
    genes_filho1 = []
    genes_filho2 = []
    
    for i in range(len(pai1.genes)):
        if random.random() < 0.5:
            genes_filho1.append(Gene(pai1.genes[i].disciplina_id, 
                                    pai1.genes[i].professor,
                                    pai1.genes[i].dia, 
                                    pai1.genes[i].horario))
            genes_filho2.append(Gene(pai2.genes[i].disciplina_id, 
                                    pai2.genes[i].professor,
                                    pai2.genes[i].dia, 
                                    pai2.genes[i].horario))
        else:
            genes_filho1.append(Gene(pai2.genes[i].disciplina_id, 
                                    pai2.genes[i].professor,
                                    pai2.genes[i].dia, 
                                    pai2.genes[i].horario))
            genes_filho2.append(Gene(pai1.genes[i].disciplina_id, 
                                    pai1.genes[i].professor,
                                    pai1.genes[i].dia, 
                                    pai1.genes[i].horario))
    
    return Cromossomo(genes_filho1), Cromossomo(genes_filho2)

def mutacao(cromossomo, taxa_mutacao=0.1):
    """Aplica mutação no cromossomo"""
    disc_map = {d.id: d for d in disciplinas}
    
    for gene in cromossomo.genes:
        if random.random() < taxa_mutacao:
            disc = disc_map[gene.disciplina_id]
            
            # Escolher tipo de mutação
            tipo_mutacao = random.choice(['professor', 'dia', 'ambos'])
            
            if tipo_mutacao in ['professor', 'ambos']:
                # Mutar professor
                profs_validos = [p for p, info in professores_aderencia.items() 
                               if gene.disciplina_id in info["disciplinas"]]
                if profs_validos:
                    gene.professor = random.choice(profs_validos)
            
            if tipo_mutacao in ['dia', 'ambos']:
                # Mutar dia (respeitando se é EAD)
                if disc.ead:
                    gene.dia = DIA_EAD
                else:
                    # Tentar respeitar disponibilidade do professor
                    info_prof = professores_aderencia[gene.professor]
                    if info_prof["dias_especificos"]:
                        dias_possiveis = [DIAS_SEMANA.index(d) for d in info_prof["dias_especificos"].keys() 
                                        if DIAS_SEMANA.index(d) < DIAS_UTEIS]
                        if dias_possiveis:
                            gene.dia = random.choice(dias_possiveis)
                        else:
                            gene.dia = random.randrange(DIAS_UTEIS)
                    else:
                        gene.dia = random.randrange(DIAS_UTEIS)
    
    return cromossomo

# ==================== ALGORITMO GENÉTICO PRINCIPAL ====================

class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao=100, taxa_mutacao=0.1, taxa_cruzamento=0.8,
                 elitismo=0.1, metodo_selecao='torneio'):
        self.tamanho_populacao = tamanho_populacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento
        self.elitismo = elitismo
        self.metodo_selecao = metodo_selecao
        self.populacao = []
        self.melhor_individuo = None
        self.historico_fitness = []
        
    def inicializar_populacao(self):
        """Cria a população inicial"""
        self.populacao = [Cromossomo() for _ in range(self.tamanho_populacao)]
        self.avaliar_populacao()
    
    def avaliar_populacao(self):
        """Calcula o fitness de todos os indivíduos"""
        for cromossomo in self.populacao:
            cromossomo.fitness = calcular_fitness(cromossomo)
        
        # Ordenar por fitness
        self.populacao.sort(key=lambda x: x.fitness, reverse=True)
        
        # Atualizar melhor indivíduo
        if self.melhor_individuo is None or (self.melhor_individuo.fitness is None or self.populacao[0].fitness > self.melhor_individuo.fitness):
            self.melhor_individuo = self.populacao[0].copy()
    
    def selecionar(self):
        """Seleciona um indivíduo da população"""
        if self.metodo_selecao == 'torneio':
            return selecao_torneio(self.populacao, k=3)
        elif self.metodo_selecao == 'roleta':
            return selecao_roleta(self.populacao)
        else:
            return random.choice(self.populacao)
    
    def evoluir_geracao(self):
        """Evolui uma geração"""
        nova_populacao = []
        
        # Elitismo - manter os melhores
        n_elite = int(self.tamanho_populacao * self.elitismo)
        for i in range(n_elite):
            nova_populacao.append(self.populacao[i].copy())
        
        # Gerar novos indivíduos
        while len(nova_populacao) < self.tamanho_populacao:
            # Seleção
            pai1 = self.selecionar()
            pai2 = self.selecionar()
            
            # Cruzamento
            if random.random() < self.taxa_cruzamento:
                if random.random() < 0.5:
                    filho1, filho2 = cruzamento_um_ponto(pai1, pai2)
                else:
                    filho1, filho2 = cruzamento_uniforme(pai1, pai2)
            else:
                filho1, filho2 = pai1.copy(), pai2.copy()
            
            # Mutação
            filho1 = mutacao(filho1, self.taxa_mutacao)
            filho2 = mutacao(filho2, self.taxa_mutacao)
            
            nova_populacao.append(filho1)
            if len(nova_populacao) < self.tamanho_populacao:
                nova_populacao.append(filho2)
        
        self.populacao = nova_populacao
        self.avaliar_populacao()
    
    def executar(self, n_geracoes=100, verbose=True):
        """Executa o algoritmo genético"""
        print("\n" + "="*70)
        print("INICIANDO ALGORITMO GENÉTICO PARA GERAÇÃO DE GRADE HORÁRIA")
        print("="*70)
        
        # Inicializar
        self.inicializar_populacao()
        
        # Evolução
        for geracao in range(n_geracoes):
            self.evoluir_geracao()
            
            # Registrar histórico
            melhor_fitness = self.populacao[0].fitness
            media_fitness = np.mean([c.fitness for c in self.populacao])
            self.historico_fitness.append({
                'geracao': geracao,
                'melhor': melhor_fitness,
                'media': media_fitness
            })
            
            # Exibir progresso
            if verbose and (geracao % 10 == 0 or geracao == n_geracoes - 1):
                print(f"Geração {geracao:3d}: Melhor = {melhor_fitness:.4f}, "
                      f"Média = {media_fitness:.4f}")
        
        print("\n" + "="*70)
        print("ALGORITMO GENÉTICO FINALIZADO")
        print("="*70)
        
        return self.melhor_individuo

# ==================== VISUALIZAÇÃO E RELATÓRIO ====================

def gerar_grade_visual(cromossomo):
    """Gera uma representação visual da grade horária"""
    disc_map = {d.id: d for d in disciplinas}
    
    # Organizar por período
    grades_por_periodo = defaultdict(lambda: defaultdict(list))
    
    for gene in cromossomo.genes:
        disc = disc_map[gene.disciplina_id]
        dia_nome = DIAS_SEMANA[gene.dia]
        
        # Criar entrada para a grade
        entrada = {
            'disciplina': disc.nome,
            'turma': disc.turma,
            'professor': gene.professor,
            'dia': dia_nome,
            'horario': HORARIOS[gene.horario],
            'alunos': disc.alunos,
            'ead': disc.ead
        }
        
        periodo_str = f"{disc.periodo}º Período" if disc.periodo < 10 else f"{disc.periodo//10}º/{disc.periodo%10}º Período"
        grades_por_periodo[periodo_str][dia_nome].append(entrada)
    
    return grades_por_periodo

def imprimir_grade_completa(cromossomo):
    """Imprime a grade horária completa de forma organizada"""
    print("\n" + "="*80)
    print("GRADE HORÁRIA GERADA - CURSO DE CIÊNCIA DA COMPUTAÇÃO")
    print("="*80)
    
    grades = gerar_grade_visual(cromossomo)
    
    for periodo in sorted(grades.keys()):
        print(f"\n{'-'*80}")
        print(f"{periodo}")
        print(f"{'-'*80}")
        
        for dia in DIAS_SEMANA:
            if dia in grades[periodo]:
                print(f"\n{dia.upper()}:")
                for aula in sorted(grades[periodo][dia], key=lambda x: (x['turma'], x['horario'])):
                    tipo = "[EAD]" if aula['ead'] else ""
                    print(f"  • {aula['disciplina']} - Turma {aula['turma']} {tipo}")
                    print(f"    Professor: {aula['professor']} | {aula['horario']} | {aula['alunos']} alunos")

def gerar_estatisticas(cromossomo):
    """Gera estatísticas sobre a solução"""
    disc_map = {d.id: d for d in disciplinas}
    stats = {
        'total_disciplinas': len(cromossomo.genes),
        'disciplinas_ead': 0,
        'disciplinas_presenciais': 0,
        'conflitos_professor': 0,
        'conflitos_turma': 0,
        'violacoes_disponibilidade': 0,
        'carga_por_professor': defaultdict(int),
        'distribuicao_dias': defaultdict(int)
    }
    
    # Análise dos genes
    professor_horarios = defaultdict(list)
    turma_horarios = defaultdict(list)
    professor_dias = defaultdict(set)
    
    for gene in cromossomo.genes:
        disc = disc_map[gene.disciplina_id]
        
        # Contar EAD vs Presencial
        if disc.ead:
            stats['disciplinas_ead'] += 1
        else:
            stats['disciplinas_presenciais'] += 1
        
        # Carga por professor
        stats['carga_por_professor'][gene.professor] += 1
        
        # Distribuição por dias
        stats['distribuicao_dias'][DIAS_SEMANA[gene.dia]] += 1
        
        # Verificar conflitos
        chave_horario = (gene.dia, gene.horario)
        professor_horarios[(gene.professor, chave_horario)].append(gene)
        chave_turma = (disc.periodo, disc.turma, chave_horario)
        turma_horarios[chave_turma].append(gene)
        professor_dias[gene.professor].add(gene.dia)
    
    # Contar conflitos
    for genes in professor_horarios.values():
        if len(genes) > 1:
            stats['conflitos_professor'] += len(genes) - 1
    
    for genes in turma_horarios.values():
        if len(genes) > 1:
            stats['conflitos_turma'] += len(genes) - 1
    
    # Verificar violações de disponibilidade
    for professor, dias in professor_dias.items():
        disponibilidade = professores_aderencia[professor]["disponibilidade"]
        if len(dias) > disponibilidade:
            stats['violacoes_disponibilidade'] += len(dias) - disponibilidade
    
    return stats

def plotar_evolucao(historico):
    """Plota a evolução do fitness ao longo das gerações"""
    geracoes = [h['geracao'] for h in historico]
    melhores = [h['melhor'] for h in historico]
    medias = [h['media'] for h in historico]
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(geracoes, melhores, 'b-', label='Melhor Fitness', linewidth=2)
    plt.plot(geracoes, medias, 'r--', label='Fitness Médio', linewidth=1)
    plt.xlabel('Geração')
    plt.ylabel('Fitness')
    plt.title('Evolução do Fitness ao Longo das Gerações')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico de convergência
    plt.subplot(1, 2, 2)
    convergencia = [melhores[i] - medias[i] for i in range(len(melhores))]
    plt.plot(geracoes, convergencia, 'g-', linewidth=2)
    plt.xlabel('Geração')
    plt.ylabel('Diferença (Melhor - Média)')
    plt.title('Convergência da População')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('evolucao_fitness.png', dpi=300, bbox_inches='tight')
    print("\nGráfico salvo como 'evolucao_fitness.png'")
    plt.show()

def exportar_grade_json(cromossomo, filename='grade_horaria.json'):
    """Exporta a grade horária para formato JSON"""
    disc_map = {d.id: d for d in disciplinas}
    grade_json = {
        'fitness': cromossomo.fitness,
        'data_geracao': datetime.now().isoformat(),
        'aulas': []
    }
    
    for gene in cromossomo.genes:
        disc = disc_map[gene.disciplina_id]
        aula = {
            'disciplina_id': disc.id,
            'disciplina_nome': disc.nome,
            'periodo': disc.periodo,
            'turma': disc.turma,
            'professor': gene.professor,
            'dia': DIAS_SEMANA[gene.dia],
            'horario': HORARIOS[gene.horario],
            'ead': disc.ead,
            'alunos': disc.alunos
        }
        grade_json['aulas'].append(aula)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(grade_json, f, ensure_ascii=False, indent=2)
    
    print(f"\nGrade exportada para '{filename}'")

def gerar_relatorio_completo(ag, melhor_solucao):
    """Gera um relatório completo da execução"""
    print("\n" + "="*80)
    print("RELATÓRIO DE EXECUÇÃO DO ALGORITMO GENÉTICO")
    print("="*80)
    
    # Parâmetros utilizados
    print("\n1. PARÂMETROS DO ALGORITMO:")
    print(f"   • Tamanho da população: {ag.tamanho_populacao}")
    print(f"   • Taxa de mutação: {ag.taxa_mutacao:.2%}")
    print(f"   • Taxa de cruzamento: {ag.taxa_cruzamento:.2%}")
    print(f"   • Taxa de elitismo: {ag.elitismo:.2%}")
    print(f"   • Método de seleção: {ag.metodo_selecao}")
    print(f"   • Número de gerações: {len(ag.historico_fitness)}")
    
    # Calcular fitness se não existir
    if melhor_solucao.fitness is None:
        melhor_solucao.fitness = calcular_fitness(melhor_solucao)
    
    # Estatísticas da solução
    stats = gerar_estatisticas(melhor_solucao)
    
    print("\n2. ESTATÍSTICAS DA SOLUÇÃO FINAL:")
    print(f"   • Fitness alcançado: {melhor_solucao.fitness:.4f}")
    print(f"   • Total de disciplinas alocadas: {stats['total_disciplinas']}")
    print(f"   • Disciplinas presenciais: {stats['disciplinas_presenciais']}")
    print(f"   • Disciplinas EAD: {stats['disciplinas_ead']}")
    
    print("\n3. ANÁLISE DE CONFLITOS:")
    print(f"   • Conflitos de professor (mesmo horário): {stats['conflitos_professor']}")
    print(f"   • Conflitos de turma (mesmo horário): {stats['conflitos_turma']}")
    print(f"   • Violações de disponibilidade: {stats['violacoes_disponibilidade']}")
    
    print("\n4. DISTRIBUIÇÃO DE CARGA POR PROFESSOR:")
    for prof in sorted(stats['carga_por_professor'].keys()):
        carga = stats['carga_por_professor'][prof]
        disp = professores_aderencia[prof]["disponibilidade"]
        status = "⚠️" if carga > disp else "✓"
        print(f"   {status} {prof}: {carga} disciplina(s) (máx: {disp} dias)")
    
    print("\n5. DISTRIBUIÇÃO POR DIA DA SEMANA:")
    for dia in DIAS_SEMANA:
        if dia in stats['distribuicao_dias']:
            print(f"   • {dia}: {stats['distribuicao_dias'][dia]} disciplina(s)")
    
    # Análise da evolução
    if ag.historico_fitness:
        print("\n6. ANÁLISE DA EVOLUÇÃO:")
        fitness_inicial = ag.historico_fitness[0]['melhor']
        fitness_final = ag.historico_fitness[-1]['melhor']
        melhoria = ((fitness_final - fitness_inicial) / fitness_inicial) * 100 if fitness_inicial > 0 else 0
        
        print(f"   • Fitness inicial: {fitness_inicial:.4f}")
        print(f"   • Fitness final: {fitness_final:.4f}")
        print(f"   • Melhoria: {melhoria:.2f}%")
        
        # Taxa de convergência
        ultimas_10 = ag.historico_fitness[-10:] if len(ag.historico_fitness) >= 10 else ag.historico_fitness
        variacao = max(h['melhor'] for h in ultimas_10) - min(h['melhor'] for h in ultimas_10)
        print(f"   • Variação nas últimas 10 gerações: {variacao:.4f}")
        
        if variacao < 0.001:
            print("   • Status: População convergiu")
        elif variacao < 0.01:
            print("   • Status: População quase convergida")
        else:
            print("   • Status: População ainda evoluindo")

# ==================== FUNÇÃO PRINCIPAL ====================

def main():
    """Função principal para executar o algoritmo genético"""
    
    print("\n" + "="*80)
    print("SISTEMA DE GERAÇÃO AUTOMÁTICA DE GRADE HORÁRIA")
    print("Curso de Ciência da Computação - UNIFESO")
    print("="*80)
    
    # Configurar parâmetros
    print("\nConfigurando parâmetros do algoritmo genético...")
    
    # Criar instância do AG
    ag = AlgoritmoGenetico(
        tamanho_populacao=150,
        taxa_mutacao=0.15,
        taxa_cruzamento=0.85,
        elitismo=0.1,
        metodo_selecao='torneio'
    )
    
    # Executar algoritmo
    print("\nExecutando algoritmo genético...")
    melhor_solucao = ag.executar(n_geracoes=200, verbose=True)
    
    # Gerar relatório completo
    gerar_relatorio_completo(ag, melhor_solucao)
    
    # Imprimir grade completa
    imprimir_grade_completa(melhor_solucao)
    
    # Plotar evolução
    print("\nGerando gráficos de evolução...")
    plotar_evolucao(ag.historico_fitness)
    
    # Exportar para JSON
    exportar_grade_json(melhor_solucao)
    
    print("\n" + "="*80)
    print("PROCESSO FINALIZADO COM SUCESSO!")
    print("="*80)
    
    return ag, melhor_solucao

# ==================== EXECUÇÃO ====================

if __name__ == "__main__":
    # Definir seed para reprodutibilidade (opcional)
    random.seed(42)
    np.random.seed(42)
    
    # Executar
    ag, melhor_solucao = main()
    
    # Salvar melhor solução
    with open('melhor_solucao.json', 'w', encoding='utf-8') as f:
        genes_dict = [g.to_dict() for g in melhor_solucao.genes]
        json.dump({
            'fitness': melhor_solucao.fitness,
            'genes': genes_dict
        }, f, ensure_ascii=False, indent=2)
    
    print("\nMelhor solução salva em 'melhor_solucao.json'")
    print("\nTodos os arquivos foram gerados com sucesso!")
