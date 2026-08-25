# DataScience

Repositório de estudos em Data Science, Machine Learning, Visão Computacional e áreas correlatas.

> ⚠️ **Diagnóstico técnico:** Este README contém uma análise completa do estado atual do repositório,
> incluindo problemas críticos, riscos metodológicos e um plano de ação para transformá-lo
> em um portfólio profissional de Data Science.

---

## Sumário

- [Visão Geral do Repositório](#visão-geral-do-repositório)
- [Diagnóstico Geral](#diagnóstico-geral)
- [Pontos Fortes](#pontos-fortes)
- [Problemas Críticos](#problemas-críticos)
- [Problemas Médios](#problemas-médios)
- [Melhorias Recomendadas](#melhorias-recomendadas)
- [Riscos Metodológicos](#riscos-metodológicos)
- [Riscos de Reprodutibilidade](#riscos-de-reprodutibilidade)
- [Sugestão de Estrutura Ideal](#sugestão-de-estrutura-ideal)
- [Checklist de Correções](#checklist-de-correções)
- [Plano de Ação Prioritário](#plano-de-ação-prioritário)

---

## Visão Geral do Repositório

| Métrica | Valor |
|---------|-------|
| Total de arquivos (excluindo .git) | ~350+ |
| Scripts Python (`.py`) | **181** |
| Jupyter Notebooks (`.ipynb`) | **42** |
| Arquivos CSV de dados | 4 |
| Modelos treinados (`.h5`, `.pth`) | 2 |
| Diretórios principais | `Code_files/`, `finances-on-python/`, `qc/`, `PDI/` |
| Tamanho do repositório Git | ~74 MB (pack objects) |
| README atual | 2 linhas |
| `.gitignore` | ❌ **Ausente** |
| `requirements.txt` (raiz) | ❌ **Ausente** |
| `LICENSE` | ❌ **Ausente** |

### Conteúdo por diretório

| Diretório | Tamanho | Conteúdo |
|-----------|---------|----------|
| `Code_files/` | 75 MB | 13 semanas de exercícios de Python, NumPy, Pandas, ML clássico, Deep Learning (CNN, RNN, Transformers), TensorFlow, PyTorch |
| `finances-on-python/` | 71 MB | 10 capítulos de um curso de finanças com Python (notebooks grandes com outputs) |
| `PDI/` | 61 MB | Processamento Digital de Imagens: OpenCV, histogramas, filtros, segmentação, Hough, contornos, SVM, MLP |
| `qc/` | 372 KB | 14 aulas introdutórias de Computação Quântica |

---

## Diagnóstico Geral

Este repositório é um **monorepo de estudos** que acumula conteúdo de múltiplos cursos de Data Science,
Visão Computacional (PDI/OpenCV), Finanças Python, Computação Quântica e exercícios de fundamentos
de Python. São aproximadamente **350+ arquivos, 181 scripts .py, 42 notebooks Jupyter** organizados
de forma cronológica (semanas/dias) em vez de temática/funcional. Não há um projeto coeso —
o repositório funciona como um "baú de exercícios".

---

## Pontos Fortes

1. **Diversidade de tópicos** — Abrange desde fundamentos de Python até CNN, RNN, Transformers,
   CatBoost, LightGBM, XGBoost, OpenCV, PyTorch e TensorFlow. Demonstra amplitude de aprendizado.

2. **Código funcional** — A maioria dos scripts executa sem erros. Os projetos de fim de semana
   (`day7_project.py`, `mini_project_*.py`) mostram tentativas reais de aplicar ML end-to-end.

3. **Uso de boas práticas em alguns scripts** — Alguns arquivos usam `ColumnTransformer` com
   `Pipeline`, `cross_val_score`, `GridSearchCV`, `random_state` e `train_test_split`
   (ex.: `Code_files/Week6/Day7/`, `Code_files/Week7/Day5/`).

4. **Sem vazamento de credenciais** — Nenhuma API key, token ou senha encontrada no repositório.

5. **Conteúdo de valor** — Notebooks como `pa1-logistic-regression_corrigida.ipynb` e
   `pa2-multilayer-perceptron_corrigida.ipynb` são assignments acadêmicos bem estruturados
   com instruções claras e testes.

---

## Problemas Críticos

### PC1 — Ausência total de `.gitignore`

Arquivos grandes (MNIST 45MB, CSVs 21MB, modelos .h5/.pth, vídeos MP4, `.rar`, `.zip`,
`__pycache__/`, `desktop.ini`) estão todos versionados. O repositório Git já tem **74MB só
no pack objects**. Isso é insustentável para clonagem e colaboração.

### PC2 — Nenhum arquivo de dependências no diretório raiz

Não há `requirements.txt`, `pyproject.toml`, `environment.yml`, `Pipfile` ou `setup.py`.
Existem **3 requirements diferentes** dentro de `PDI/` com versões conflitantes:
- `opencv-python==4.10.0.84` vs `opencv-python==4.5.3.56`
- `tensorflow==2.16.1` vs `tensorflow==2.10.0`

Isso torna o projeto **impossível de reproduzir** de forma confiável.

### PC3 — README inadequado

O README atual tem **apenas 2 linhas**: "DataScience / Repositorio para estudos em DataScience."
Não há descrição do projeto, instruções de instalação, dependências, estrutura de pastas,
resultados ou próximos passos.

### PC4 — Sem separação entre dados, código e resultados

Dados brutos (CSV, MNIST binário), código-fonte, modelos treinados, notebooks e outputs
intermediários estão todos misturados. Não há pastas `data/`, `notebooks/`, `src/`, `models/`
ou `reports/`.

### PC5 — Notebooks inchados com outputs binários

`finances-on-python/` tem 7 notebooks acima de 5MB, sendo **Chapter 9 com 13MB**.
`l3_linear_regression.ipynb` tem 2MB, `l8_regularization-final.ipynb` tem 2.8MB.
Isso é causado por outputs de base64 de imagens matplotlib armazenados nos notebooks.

---

## Problemas Médios

### PM1 — Data leakage em pipelines de ML

- `Code_files/Week5/Day7/mini_project_day7_telco.py`: `StandardScaler` com `.fit_transform(X)`
  **antes** do `train_test_split` — o scaler vê os dados de teste.
- `Code_files/Week6/Day7/day7_project.py`: `preprocessor.fit_transform(X)` antes de separar
  treino/teste.
- `Code_files/Week5/Day7/mini_project_day7.py`: `LabelEncoder().fit_transform` aplicado no
  **dataset inteiro** antes da separação.

### PM2 — Arquivos temporários e lixo versionados

- **7 arquivos `desktop.ini`** (Windows) espalhados pelo PDI/
- **`__pycache__/`** em `PDI/gabaritos/CCF 394 - CONTORNOS/`
- **`catboost_info/`** com logs de treinamento (JSON, TSV, TF events)
- **Arquivos MP4** (vídeos) — não deveriam estar versionados
- **`.rar` e `.zip`** de gabaritos

### PM3 — Nomes de arquivos inconsistentes

Mistura de português e inglês, espaços em nomes, números de versão entre parênteses
(`l4_linear_regression_vectorized (2).ipynb`), acentos e pastas com `+` (Chapter+1).
Exemplos: `BOA 1 segmentacao caneta webcam.py`, `dat2_ex.py` (typo de "day2").

### PM4 — Código comentado e não utilizado

Vários scripts têm blocos inteiros comentados (`mini_project_day7_telco.py` linhas 53-63,
`mini_project_day7.py` com try/except comentado). Isso polui o código.

### PM5 — Dados duplicados

`Telco-Customer-Churn.csv` aparece em **dois lugares**: `Week5/Day7/` e `Week8/Day7/`.

### PM6 — Notebooks com outputs quebrados

`Checker.ipynb` e `YoutubeSrtScrape.ipynb` têm células com `execution_count: null`
(nunca executadas). `Kaggle_Competition.ipynb` depende de upload manual de `kaggle.json`.

### PM7 — Caminhos hardcoded

`Code_files/Week13/Day7/day7_cv.py` usa `"PATH To DATASET"` literal.
`Kaggle_Competition.ipynb` usa `/content/` (Google Colab). Isso impede execução local.

### PM8 — Tipagem e documentação ausentes

Nenhum dos 181 arquivos .py usa type hints. Docstrings são praticamente inexistentes.

---

## Melhorias Recomendadas

### MR1 — Modularização do código

Os notebooks da raiz (`l3_linear_regression.ipynb`, `pa1-*.ipynb`) contêm implementações
didáticas de regressão logística, backpropagation, MLP, CNN e RNN. Essas implementações
poderiam ser extraídas para módulos Python reutilizáveis em `src/models/`, `src/training/`,
`src/evaluation/`.

### MR2 — Pipeline de dados end-to-end

O notebook `Kaggle_Competition.ipynb` é o mais próximo de um projeto real. Poderia ser
refatorado com:
- Scripts separados para ingestão (`src/data/load.py`), preprocessing
  (`src/features/build_features.py`), modelagem (`src/models/train_model.py`)
- Configurações em YAML/JSON
- Pipeline sklearn de verdade

### MR3 — Adicionar boilerplate de projeto

- `pyproject.toml` ou `requirements.txt` com versões pinadas
- `setup.py` ou `setup.cfg` para instalação do pacote
- `Makefile` com comandos comuns (`make data`, `make train`, `make evaluate`)

### MR4 — Versionamento de modelos e experimentos

Nenhum dos modelos treinados possui metadados (hiperparâmetros, data, métricas, hash dos
dados). Ideal usar MLflow ou pelo menos um logging simples com JSON.

### MR5 — Stripe API key placeholder

`Checker.ipynb` contém `stripe.api_key = ""`. Embora vazio, deve ser removido ou
externalizado para variável de ambiente.

---

## Riscos Metodológicos

### RM1 — Ausência de baseline ingênuo

Nenhum projeto compara o modelo proposto com um baseline simples (ex.: sempre prever a
classe majoritária, média do target). Sem baseline, não é possível saber se o modelo
realmente agrega valor.

### RM2 — Separação treino/teste inadequada

Vários scripts usam apenas acurácia no teste sem validação cruzada ou separação
treino/validação/teste. Modelos podem estar overfitting sem detecção.

### RM3 — Métricas limitadas

A maioria usa apenas `accuracy_score`. Para problemas desbalanceados (churn, Titanic),
accuracy é enganosa. Falta uso de precision, recall, F1-score, AUC-ROC, matriz de confusão.

### RM4 — Sem controle de reprodutibilidade

Embora alguns scripts usem `random_state=42`, não há:
- Seed global com `np.random.seed`, `random.seed`, `tf.random.set_seed`
- Determinação de operações em GPU
- Log de versões das bibliotecas usadas

### RM5 — Escolha de modelo não justificada

Modelos são treinados sem comparação estatística (testes de hipótese, intervalos de
confiança) e sem análise de complexidade vs. performance.

### RM6 — Visualizações não sustentam conclusões

Gráficos existem mas são genéricos (curvas de loss/accuracy). Faltam:
- Análise de resíduos
- Feature importance
- Curvas ROC comparativas
- Distribuições de erros

---

## Riscos de Reprodutibilidade

1. **Impossível instalar dependências** — sem arquivo raiz de requirements, o próximo
   usuário não sabe o que instalar.

2. **Versões conflitantes** — os 3 requirements.txt dentro de PDI têm versões diferentes
   de numpy, tensorflow, opencv.

3. **Caminhos de arquivo hardcoded** — Kaggle notebook usa `/content/`, day7_cv.py usa
   `"PATH To DATASET"`, scripts esperam arquivos CSV em diretórios relativos específicos.

4. **Dados externos não baixáveis** — Telco-Customer-Churn.csv está versionado, mas datasets
   como MNIST foram baixados via `tensorflow.keras.datasets` e não há script para reobtê-los.

5. **Kaggle API key necessária** — O notebook de competição requer upload manual de
   `kaggle.json`.

6. **Sem hashing de dados** — nenhum script verifica integridade dos dados com checksums.

---

## Sugestão de Estrutura Ideal

```
DataScience/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml              # ou requirements.txt + setup.py
├── Makefile
├── .env.example                # variáveis de ambiente (se necessário)
│
├── data/                       # DADOS (adicionar ao .gitignore)
│   ├── raw/                    # dados originais, imutáveis
│   ├── processed/              # dados limpos e transformados
│   └── external/               # dados de fontes externas
│
├── notebooks/                  # NOTEBOOKS ORGANIZADOS
│   ├── 01_exploration/         # EDA e análises exploratórias
│   ├── 02_modeling/            # treinamento e experimentos
│   └── reports/                # notebooks finais para apresentação
│
├── src/                        # CÓDIGO REUTILIZÁVEL
│   ├── __init__.py
│   ├── data/
│   │   ├── load.py             # funções de carregamento
│   │   └── preprocess.py       # limpeza e transformação
│   ├── features/
│   │   └── build_features.py   # engenharia de atributos
│   ├── models/
│   │   ├── train.py            # treinamento
│   │   ├── predict.py          # inferência
│   │   └── evaluate.py         # métricas e validação
│   └── visualization/
│       └── visualize.py        # gráficos padronizados
│
├── models/                     # MODELOS TREINADOS (.gitignore)
│   ├── logistic_regression.pkl
│   └── random_forest.pkl
│
├── reports/                    # RELATÓRIOS
│   ├── figures/                # gráficos finais
│   └── metrics/                # resultados em JSON
│
├── references/                 # artigos, links, docs
│
├── tests/                      # TESTES UNITÁRIOS
│   ├── test_data.py
│   └── test_models.py
│
└── archive/                    # código antigo preservado
    ├── Code_files/
    ├── finances-on-python/
    ├── qc/
    └── PDI/
```

---

## Checklist de Correções

| # | Tarefa | Tipo | Prioridade |
|---|--------|------|------------|
| 1 | Criar `.gitignore` global (`.pyc`, `__pycache__/`, `desktop.ini`, `.zip`, `.rar`, `.mp4`, `.h5`, `.pth`, `catboost_info/`, dados grandes) | Crítico | Imediata |
| 2 | Remover do Git arquivos grandes e desnecessários | Crítico | Imediata |
| 3 | Criar `requirements.txt` raiz com todas as dependências pinadas | Crítico | Imediata |
| 4 | Escrever README.md completo | Crítico | Imediata |
| 5 | Criar estrutura de pastas (`data/`, `notebooks/`, `src/`, `models/`, `reports/`) | Médio | Curto prazo |
| 6 | Mover notebooks para `notebooks/` organizados por assunto | Médio | Curto prazo |
| 7 | Extrair funções reutilizáveis dos notebooks para `src/` | Médio | Curto prazo |
| 8 | Corrigir data leakage nos scripts de ML (scaler/encoder após split) | Médio | Curto prazo |
| 9 | Adicionar seeds globais de reprodutibilidade | Médio | Curto prazo |
| 10 | Adicionar baseline ingênuo nos projetos de ML | Médio | Curto prazo |
| 11 | Expandir métricas (precision, recall, F1, AUC-ROC) além de accuracy | Médio | Curto prazo |
| 12 | Adicionar LICENSE (MIT recomendado para portfólio) | Baixo | Médio prazo |
| 13 | Renomear arquivos com nomes inconsistentes | Baixo | Médio prazo |
| 14 | Remover código comentado de produção | Baixo | Médio prazo |
| 15 | Adicionar validação cruzada onde só existe train/test fixo | Baixo | Médio prazo |
| 16 | Criar `Makefile` com comandos de automação | Baixo | Médio prazo |
| 17 | Adicionar type hints e docstrings nos módulos `src/` | Baixo | Longo prazo |
| 18 | Implementar logging de experimentos (MLflow ou JSON) | Baixo | Longo prazo |
| 19 | Limpar outputs dos notebooks grandes | Baixo | Longo prazo |
| 20 | Adicionar CI básico (GitHub Actions para lint + teste) | Baixo | Longo prazo |

---

## Plano de Ação Prioritário

### Fase 1 — Socorro imediato

1. Criar `.gitignore` e remover do tracking todos os arquivos grandes/temporários
2. Criar `requirements.txt` raiz consolidando as 3 listas existentes
3. Escrever README.md com propósito, estrutura, dependências e instruções

### Fase 2 — Organização estrutural

4. Criar pastas `data/`, `notebooks/`, `src/`, `models/`, `reports/`
5. Mover notebooks para `notebooks/` (separar por assunto: `fundamentos/`, `ml_classico/`,
   `deep_learning/`, `computer_vision/`, `competicoes/`)
6. Mover dados para `data/raw/`
7. Mover scripts Python reutilizáveis para `src/`

### Fase 3 — Qualidade de código e metodologia

8. Corrigir data leakage nos scripts afetados
9. Adicionar baseline e seeds globais
10. Adicionar validação cruzada e métricas expandidas

### Fase 4 — Polimento e portfólio

11. Criar LICENSE
12. Adicionar Makefile
13. Criar um projeto "vitrine" dentre os existentes (recomendado: Kaggle Competition ou
    classificação de churn Telco) com estrutura exemplar
14. Adicionar CI com GitHub Actions

---

## Recomendação Final

Este repositório contém **material de estudo valioso e diverso**, mas está **inapresentável
profissionalmente** como portfólio. É exatamente o que se espera de um estudante dedicado
que aprendeu muito, mas ainda não aprendeu a **organizar e apresentar** o trabalho.

Com as correções propostas, ele pode se transformar em um portfólio de Data Science de
alto nível. O primeiro e mais urgente passo é **conter o dano do Git** com `.gitignore`
adequado e remoção dos binários grandes.

---

*Diagnóstico gerado em Maio de 2026.*
