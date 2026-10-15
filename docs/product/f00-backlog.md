# CronoCheck — Backlog detalhado da Fase 00 — v1.9

## Legenda de estados
Não iniciado · Em elaboração · Redigido, aguardando validação técnica · Tecnicamente validado ·
Aguardando aprovação · Aprovado · Bloqueado.
Regra: texto gerado NÃO comprova validação técnica. "Tecnicamente validado" exige revisão humana
registrada; "Aprovado" exige aprovação do responsável pelo produto com data.

## Estado de persistência (após merge do PR #1)
| Documento | Origem | Versionado na `main` |
|---|---|---|
| docs/product/prd.md | Baseline ZIP v1.2 | Sim (PR #1, 14/10/2026) |
| docs/product/personas-jtbd.md | Baseline ZIP v1.2 | Sim (PR #1, 14/10/2026) |
| docs/product/open-questions.md | Baseline ZIP v1.2 | Sim (PR #1, 14/10/2026) |
| docs/product/f00-backlog.md | Baseline ZIP v1.2 | Sim (PR #1, 14/10/2026) |
| docs/product/traceability-matrix.md | Baseline ZIP v1.2 | Sim (PR #1, 14/10/2026) |

## F00-E01 — Entrevistar usuários-alvo e registrar cenários reais
Aceite (blueprint): 3–5 cenários priorizados e validados, ou limitações explicitadas.

| ID | Descrição | Objetivo | Dependências | Entregável | Critério de aceite verificável | Evidência esperada | Estado |
|---|---|---|---|---|---|---|---|
| T-E01-01 | Redigir personas hipotéticas | Ponto de partida para validação | — | personas-jtbd.md §1 | 3 personas com objetivos, responsabilidades, necessidades, tarefas, fricções e critérios | Arquivo revisado por humano | Redigido, aguardando validação técnica |
| T-E01-02 | Consolidar 3–5 cenários com os 11 atributos | Entrada para F00-E02 e testes | T-E01-01 | personas-jtbd.md §2 | Cada CU possui os 11 campos preenchidos | Arquivo revisado por humano | Redigido, aguardando validação técnica |
| T-E01-03 | Separar hipótese/desconhecido/evidência/validação | Evitar hipótese lida como fato | T-E01-01 | personas-jtbd.md §3 | 4 categorias explícitas | Arquivo revisado por humano | Redigido, aguardando validação técnica |
| T-E01-04 | Entrevistar usuários reais | Validar ou refutar hipóteses | Acesso a usuários (OQ-01 já aprovada) | Notas de entrevista | 3–5 cenários validados ou limitação registrada | Notas/roteiros anexados | Não iniciado — participantes ainda não confirmados |

## F00-E02 — Jornada AS-IS / TO-BE
| ID | Descrição | Dependências | Entregável | Estado |
|---|---|---|---|---|
| T-E02-01 | Mapa AS-IS/TO-BE a partir de CU-01..CU-05 | T-E01-02; OQ-01 aprovada | `journey-as-is-to-be.md` | Em elaboração — rascunho hipotético publicado para revisão; sem validação real |

## F00-E03 — MVP, fora de escopo e matriz de requisitos
| ID | Descrição | Objetivo | Dependências | Entregável | Critério de aceite verificável | Evidência esperada | Estado |
|---|---|---|---|---|---|---|---|
| T-E03-01 | PRD com RF-01..11 e RNF-01..10 por extenso | Escopo testável | — | prd.md §5–§9 | 21 requisitos com critério em 4 partes | Revisão humana registrada | Redigido, aguardando validação técnica |
| T-E03-02 | Separar obrigatoriedade MVP x ordem de implementação | Corrigir MoSCoW da v1.1 | T-E03-01 | prd.md §7 | Nenhum item do MVP fora do escopo de lançamento | Revisão humana registrada | Redigido, aguardando validação técnica |
| T-E03-03 | Dependências entre requisitos | Sequenciamento válido | T-E03-01 | prd.md §10 | Cadeia sem ciclos | Revisão humana | Redigido, aguardando validação técnica |
| T-E03-04 | Matriz de rastreabilidade | Controle de mudança/teste | T-E03-01, T-E01-02 | traceability-matrix.md | 21 requisitos ligados a etapa EAP, sem órfãos | Revisão humana | Redigido, aguardando validação técnica |
| T-E03-05 | Aprovação formal do PRD (CRONO-001) | Fechar escopo | T-E03-01..04 | Registro de aprovação | Aprovação nominal e datada | Ata/registro | Não iniciado (depende de validação técnica) |

## F00-E04 — Formato XLSX de referência, calendário e regras
| ID | Descrição | Dependências | Entregável | Critério de aceite verificável | Estado |
|---|---|---|---|---|---|
| T-E04-01 | Layout de colunas de referência | OQ-02 aprovada; semântica OQ-08 pendente | `docs/product/xlsx-import-contract-v0.md` | Tipos e obrigatoriedade por coluna documentados | Redigido, aguardando validação técnica; semântica ainda provisória |
| T-E04-02 | Fixtures sintéticas representativas | T-E04-01 (provisória) | `tests/fixtures/*.xlsx`, README e expected-results.json | OOXML íntegro, 10 planilhas sintéticas e casos esperados | Em elaboração; 10 XLSX versionados, verificação estrutural CI aprovada (run 38629233298); revisão humana pendente |

| T-E04-03 | Teste de integridade do pacote de fixtures | T-E04-02 | `validate_fixtures.py` e `.github/workflows/fixtures-validation.yml` | Pipeline lê 10 OOXML, confere categorias estruturais/manifesto e diff | Em elaboração; CI estrutural aprovado (run 38629233298); revisão humana ainda pendente |

## CRONO-003 — Glossário e semântica do domínio (atividade transversal da Fase 00)
Escopo previsto no blueprint L: modelar conceitos de atividade, calendário, duração, dependência e versão antes de implementar a aplicação.

| ID | Descrição | Dependências | Entregável | Critério de aceite verificável | Estado |
|---|---|---|---|---|---|
| CRONO-003-01 | Glossário de atividades, versões, auditoria, calendários e vínculos | Blueprint C.5–C.7, PRD, F00-E04 sintética | `docs/product/domain-glossary.md` | Termos, exemplos, origens e pendências documentados | Redigido, aguardando validação técnica e revisão humana |
| CRONO-003-02 | Invariantes e cenários de verificação | CRONO-003-01 | `docs/product/domain-invariants.md` | Erros vs achados, proveniência, integridade e segurança discriminados | Redigido, aguardando validação técnica |
| CRONO-003-03 | Deliberar semântica de IDs/duração/predecessoras | OQ-03, OQ-08 e OQ-09 | Decisões documentadas em `open-questions.md` | Aprovação com data, responsável e evidência, sem alteração implícita da semântica do MVP | Pendente |
| CRONO-003-04 | Revisão final e aceite documental | CRONO-003-01 a 03 | Registro de aceite na issue CRONO-003 / PR | Critérios revisados pelo responsável, referências coerentes | Aguardando aprovação |

**Nota:** este trabalho não equivale à etapa F04-E01 de implementação do esquema canônico em C#; o Gate G0 ainda depende dos demais entregáveis F00.

## CRONO-004 — RF/RNF e prioridades MoSCoW (atividade transversal da Fase 00)

Consolidar RF/RNF da baseline em formato humano e legível por máquinas. A classificação de
obrigatoriedade para lançamento é **proposta**, não aprovação tácita do PRD (OQ-06 pendente).

| ID | Descrição | Dependências | Entregável | Critério de aceite verificável | Estado |
|---|---|---|---|---|---|
| CRONO-004-01 | Consolidar RF-01..11 e RNF-01..10, com linha de corte MVP | Blueprint, PRD, CRONO-003 | `requirements-register.json`, `requirements-prioritization.md` | 21 entradas únicas; 11 RF Must e 10 RNF Must propostos; nenhuma funcionalidade removida | Redigido, aguardando revisão humana |
| CRONO-004-02 | Sincronizar rastreabilidade humana | CRONO-004-01, F00-E04 | `traceability-matrix.md` | Critérios, etapas, cenários e fixtures existentes referenciados sem presumir execução de testes C# | Redigido, aguardando revisão humana |
| CRONO-004-03 | Validar integridade documental automaticamente | CRONO-004-01/02 | `tests/documentation/validate_requirements.py` e workflow GitHub Actions | Checagem automática de 21 requisitos, IDs e referências bem-sucedida | Verificação documental executada com sucesso no GitHub Actions (run 38632240223); revisão humana pendente |
| CRONO-004-04 | Aprovar prioridades e registrar ressalvas | OQ-05, OQ-06 e PRD | Aprovação formal no PR + `open-questions.md` | Aceite humano datado, sem aprovar Gate G0 tacitamente | Pendente |

O registro de prioridades distingue `Must` como obrigatoriedade **proposta para a release**
de ordem técnica e de calibração de performance (RNF-03/04/08). Nenhum requisito foi implementado.

## CRONO-005 — Fluxos de UX e wireframes de baixa fidelidade (preparação F02)

Entrega antecipada de documentação de descoberta, **não** execução da Fase 02.
Os cenários de uso permanecem hipotéticos, sem entrevistas e sem protótipo clicável.

| ID | Objetivo | Dependências | Artefato | Critério de aceite | Estado |
|---|---|---|---|---|---|
| CRONO-005-01 | Definir arquitetura de informação e navegação contextual | Blueprint D.1–D.2, CU-01..05, F00-E02 | `docs/ux/flows.md` | Seis seções de navegação e contexto do projeto/versão, cinco fluxos e estados de erro documentados | Redigido, aguardando validação técnica |
| CRONO-005-02 | Desenhar wireframes de baixa fidelidade desktop/mobile | CRONO-005-01 | `docs/ux/wireframes.md` | W-01..W-11 cobrem nove telas mínimas, wizard e detalhe de achado; sem omitir acessibilidade/retorno | Redigido, aguardando validação técnica |
| CRONO-005-03 | Preparar verificação de usabilidade e acessibilidade | CRONO-005-02 | `docs/ux/usability-review.md` | UXT-01..10 com critérios verificáveis, sem relatos de entrevista inventados | Redigido, aguardando revisão humana |
| CRONO-005-04 | Adicionar verificação documental automatizada | CRONO-005-01..03 | `tests/documentation/validate_ux_flows.py` e workflow CI | Links/IDs/estados/gates presentes; CI verde, com logs do PR | CI de UX/documentação aprovado (run 38634317016); revisão humana pendente |
| CRONO-005-05 | Revisão final de nomenclatura, hipóteses e decisões | OQ-03, OQ-07, OQ-08, OQ-09 | Registro na issue #8 e no PR | Aceite humano com data e pendências explícitas; Gate G0 segue independente | Aguardando aprovação |

**Nota:** F02-E02 prevê protótipo clicável; wireframes Markdown não satisfazem esse aceite e não
podem ser marcados como interface/protótipo implementados.

## CRONO-006 — Propostas arquiteturais ADR-001/ADR-002 (preparação F01)

Esta etapa antecipa **análise e comparação**, não início formal da Fase 01.
A escolha final de Vite/Next.js, provedor OIDC e hosting pertence à OQ-04; revisão e aceitação expressas são necessárias.

| ID | Atividade | Dependência | Entrega | Critério verificável | Estado |
|---|---|---|---|---|---|
| CRONO-006-01 | Comparar monólito modular, camadas sem fronteiras e microsserviços | Blueprint C.1–C.7, CRONO-003 | `docs/architecture/adr/ADR-001-modular-monolith.md` | Alternativas, forças, ownership, proibições e trade-offs | Redigido; proposta sem aceite |
| CRONO-006-02 | Comparar React SPA/Vite, Next.js/BFF e frontend acoplado | Blueprint C.2, CRONO-005, OQ-04 | `docs/architecture/adr/ADR-002-frontend-boundary.md` | Auth/CORS/CSRF, API, UX e deploy analisados sem decidir infraestrutura automaticamente | Redigido; proposta sem aceite |
| CRONO-006-03 | Modelar contexto e contêineres C4 L1/L2 | ADR-001/002 | `docs/architecture/context-and-containers.md` | Atores, fronteiras de confiança, componentes e invariantes explícitos | Redigido; aguardando revisão |
| CRONO-006-04 | Validar referências e estados documentais | CRONO-006-01..03 | Validador + workflow GitHub Actions | Teste de estrutura e links verde, sem confundir com testes de arquitetura C# | Validação estrutural documental aprovada no GitHub Actions (run 38635987543); revisão humana e decisão arquitetural pendentes |
| CRONO-006-05 | Ratificar ou rejeitar ADRs / definir cronograma de OQ-04 | OQ-04, F00/G0 | Registro de decisões e aceite do responsável | Data, autoridade, consequências e ADRs atualizados; Gate G0 permanece independente | Pendente |

**Nota:** os ADRs registram alternativas preferidas **provisoriamente**. Publicá-los ou dar merge
neste PR não aprova OQ-04 nem inicia F01-E01/G1.

## CRONO-007 — Governança do repositório (Fase 00)

Repositório GitHub **já criado e público**. A referência do blueprint a "criar
repositório privado" foi tratada como decisão administrativa **pendente GOV-01**,
sem alterar visibilidade nem direitos de acesso. Regras administrativas da
`main` também exigem deliberação (GOV-02).

| ID | Trabalho | Entregável | Critério de aceite verificável | Estado |
|---|---|---|---|---|
| CRONO-007-01 | Padronizar issues | `.github/ISSUE_TEMPLATE/` | Templates para defeitos, funcionalidades e tarefas, sem dados reais | Redigido na branch; revisão pendente |
| CRONO-007-02 | Padronizar PR e owners | `.github/PULL_REQUEST_TEMPLATE.md`, `.github/CODEOWNERS` | Rastreabilidade, testes realmente executados e cautela para mantenedor único | Redigido na branch; revisão pendente |
| CRONO-007-03 | Definir política de contribuição e segurança | `CONTRIBUTING.md`, `SECURITY.md`, `docs/engineering/repository-governance.md` | Conduta Git, reporte privado e restrições claras de dados sintéticos | Redigido na branch; revisão pendente |
| CRONO-007-04 | Unificar CI em todos os PRs | `.github/workflows/repository-quality-gate.yml`, `tests/documentation/validate_governance.py` | Executar requisitos, UX, arquitetura, fixtures e governança num job único | CI unificado executado com sucesso no GitHub Actions (run 38637316391); revisão humana pendente |
| CRONO-007-05 | Deliberar visibilidade e enforcement | GOV-01 e GOV-02, regras de branch GitHub | Aprovação explícita + comprovação de configuração efetivamente aplicada | **Pendente**; nenhuma mudança administrativa |

**Limitações:** consulta de rulesets vazia e leitura de proteção clássica com HTTP 403
não comprovam desproteção da `main`. `CODEOWNERS` não torna aprovação obrigatória
sem configuração de branch protection. Publicação de política não aprova Gate G0.

## F00-E05 — Riscos, prioridades e definição de sucesso
| ID | Descrição | Dependências | Entregável | Critério de aceite verificável | Estado |
|---|---|---|---|---|---|
| T-E05-01 | Registro operacional R-01..R-09 | — | prd.md §12 | 9 riscos com 10 atributos; classificação original preservada | Redigido, aguardando validação técnica |
| T-E05-02 | Métricas de sucesso propostas | T-E03-01 | prd.md §11 | Métricas sem dado inventado | Redigido, aguardando validação técnica |
| T-E05-03 | Gate G0 | F00-E01..E05 | Registro de gate | Checklist de gate do blueprint completo | Não iniciado — não aprovado nesta execução |

Nenhuma entrevista ou teste foi realizado. Somente OQ-01 e OQ-02 receberam aprovação explícita do responsável pelo produto em 14/10/2026 (`decisions-2026-10-14.md`); PRD, F00-E02 e Gate G0 continuam sem aprovação.
