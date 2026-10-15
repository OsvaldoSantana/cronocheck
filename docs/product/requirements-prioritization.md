# CronoCheck — MoSCoW e priorização de requisitos (CRONO-004)

> **Atualização de 15/10/2026:** OQ-03 (diretriz abrangente) e OQ-06 a OQ-09 aprovadas com limites; OQ-04/OQ-05 pendentes de deliberação. Este documento é uma proposta histórica de priorização, não um PRD aprovado. Ver `decisions-2026-10-15.md`.

**Status:** proposta em revisão humana · **Data:** 2026-10-14 · **Issue:** [#6 — CRONO-004](https://github.com/OsvaldoSantana/cronocheck/issues/6).  
**Autoridade:** blueprint v1.0 §A.5 e §B; PRD v1.2 §§7–10 (não aprovado formalmente); decisões OQ-01/02 aprovadas, OQ-03..09 pendentes.  
**Artefato legível por máquinas:** [`requirements-register.json`](requirements-register.json); **matriz de rastreabilidade:** [`traceability-matrix.md`](traceability-matrix.md).

## 1. A distinção necessária

A classificação **MoSCoW** responde à pergunta *“este requisito integra a linha de corte da release MVP?”*. Ela **não** determina uma ordenação de implementação, nem substitui análise de riscos, dependências ou decisões de arquitetura.

| Eixo | O que controla | Fonte / regra de governança |
|---|---|---|
| **Obrigatoriedade de release** | Presença do requisito no MVP | Todos os RF-01..11 são obrigatórios conforme PRD §7; as obrigações não funcionais RNF-01..10 integram gates de qualidade da baseline proposta. |
| **MoSCoW** | Must / Should / Could / Won't para **a release** | Proposta **Must** para todos os 21 itens catalogados; nenhuma exclusão unilateral. |
| **Ordem técnica** | Dependências/etapas e entregas incrementais | F01..F08 do blueprint, não MoSCoW; propostas registradas e revisáveis. |
| **Situação de métricas** | Limites mensuráveis aceitos vs ainda provisórios | RNF-03, RNF-04 e RNF-08 são metas **propostas** e exigem calibração; não são SLAs. |
| **Status de validação** | Evidência de que o software cumpre o requisito | Nenhum RF/RNF implementado ou homologado; CI de fixtures testa apenas o material sintético. |

**Não houve aprovação do PRD ou Gate G0.** A palavra “Must” identifica uma **proposta fiel ao escopo já descrito**, não um aceite de lançamento.

## 2. Matriz MoSCoW para lançamento (proposta)

| ID | Requisito | Classe MoSCoW | Primeira etapa técnica | Observação |
|---|---|---|---|---|
| RF-01 | Autenticar usuário e verificar permissões em cada projeto | **Must** (proposta) | `F03-E01` | — |
| RF-02 | Cadastrar, listar e consultar projetos | **Must** (proposta) | `F03-E02` | — |
| RF-03 | Receber XLSX e validar extensão, conteúdo, limites e permissões | **Must** (proposta) | `F04-E02` | — |
| RF-04 | Mapear colunas e mostrar prévia antes da gravação | **Must** (proposta) | `F04-E03` | — |
| RF-05 | Persistir original, hash e snapshot normalizado versionado | **Must** (proposta) | `F04-E04` | — |
| RF-06 | Executar regras de auditoria determinísticas e versionadas | **Must** (proposta) | `F05-E01` | — |
| RF-07 | Exibir regra, evidências e tarefas relacionadas em cada achado | **Must** (proposta) | `F05-E06` | — |
| RF-08 | Classificar, atribuir, comentar e decidir achados | **Must** (proposta) | `F06-E01` | — |
| RF-09 | Comparar versões e sinalizar alterações relevantes | **Must** (proposta) | `F07-E03` | — |
| RF-10 | Exportar resultados de auditoria em formato legível e estruturado | **Must** (proposta) | `F07-E04` | — |
| RF-11 | Consultar histórico de ações e execuções | **Must** (proposta) | `F03-E04` | Base em F03; consulta depois |
| RNF-01 | UX: fluxo principal compreensível e estados recuperáveis | **Must** (proposta) | `F02-E05` | — |
| RNF-02 | Acessibilidade WCAG 2.2 AA nos fluxos essenciais | **Must** (proposta) | `F02-E06` | — |
| RNF-03 | Resposta p95 de consultas usuais no cenário de referência | **Must** (proposta) | `F08-E02` | Meta numérica provisória |
| RNF-04 | Processamento de referência XLSX com 5.000 atividades | **Must** (proposta) | `F05-E07` | Meta numérica provisória |
| RNF-05 | Idempotência de importação/auditoria e concorrência | **Must** (proposta) | `F04-E05` | — |
| RNF-06 | Segurança: ausência de vulnerabilidades críticas/altas não mitigadas | **Must** (proposta) | `F04-E06` | — |
| RNF-07 | AuditEvent transacional para mutações críticas | **Must** (proposta) | `F03-E04` | — |
| RNF-08 | Backup e restauração com objetivos provisórios RPO/RTO | **Must** (proposta) | `F08-E03` | Meta numérica provisória |
| RNF-09 | Correlação de traces/logs durante operações críticas | **Must** (proposta) | `F01-E06` | — |
| RNF-10 | Contratos OpenAPI e verificação de mudanças incompatíveis no CI | **Must** (proposta) | `F01-E05` | — |
 
**Contagem:** 11 RF e 10 RNF; 21 Must propostos, 0 Should, 0 Could, 0 Won't. A distribuição
reflete o escopo do blueprint e não sugere que todas as tarefas tenham a mesma urgência.
Para decisões pós-MVP, consulte §A.6 do blueprint (integração nativa MPP, CPM multicritério,
Monte Carlo, IA, multiempresa etc.); elas não foram convertidas em novos RF-12+.

## 3. Sequência de implementação sem rebaixamento

| Incremento do blueprint | Trabalho inicial | Função de negócio habilitada |
|---|---|---|
| F01 — Engenharia | Instrumentação RNF-09, contratos RNF-10, base segura | Plataforma reproduzível, não produto funcional |
| F02 — UX/UI | RNF-01 e RNF-02, fluxos e estados | Jornada compreensível, não validação de usuários já realizada |
| F03 — Núcleo | RF-01, RF-02, **fundação RF-11/RNF-07** | Acesso por projeto e AuditEvent transacional |
| F04 — Importação | RF-03, RF-04, RF-05, RNF-05/06 | Upload, mapeamento e versão imutável |
| F05 — Regras | RF-06, RF-07 e ensaios RNF-04 | Achados com evidências e regras versionadas |
| F06 — Revisões | RF-08 e acesso ao histórico RF-11 | Decisões e trilha auditável consultável |
| F07 — Insights | RF-09, RF-10, UX final | Comparação de versões, relatórios |
| F08 — Release | RNF-03, RNF-04, RNF-08, segurança e homologação | Gates de publicação e métricas calibradas |

**OQ-06 foi aprovada em 15/10/2026:** a posição “11” da antiga sequência RF-01 a RF-11 no PRD
não pode postergar a infraestrutura de `AuditEvent` prevista para F03-E04. A fundação
de auditabilidade antecede funcionalidades de revisão; a **consulta completa**
e as telas podem ser incrementais. Essa distinção é um planejamento técnico, não
uma decisão de rebaixar RF-11.

## 4. Dependências e ambiguidade explícita

- **OQ-03** — determinar tipos de precedência FS/SS/FF/SF, defasagens e tratamento dos não suportados.
- **OQ-05** — definir mecanismo de calibração das metas RNF-03 (p95), RNF-04 (5.000 atividades) e RNF-08 (RPO/RTO).
- **OQ-06** — formalizar ordem técnica da base de auditoria e do histórico consultável.
- **OQ-08** — validar datas, duração e fórmulas em XLSX, evitando assumir dias corridos inclusivos como regra profissional.
- **OQ-09** — igualdade de IDs, identidade canônica e referências ambíguas entre versões.
- **OQ-01/02** já aprovadas **somente** para avançar com hipóteses e dados sintéticos; não representam validação empírica.

A decisão OQ-04 permanece pendente; OQ-07 (CU-05) foi priorizada, mas não
modificam a linha de corte do MVP nesta proposta.

## 5. Evidências, rastreabilidade e estado

O registro JSON contém cada ID, escopo, MoSCoW, primeiro marco, etapas EAP, cenários
CU-01..05 (quando aplicável), dependências, fonte dos critérios de aceite, metas
provisórias e referências às fixtures sintéticas de preparação.

O PRD mantém o texto dos critérios de aceite. A matriz de rastreabilidade não deve
duplicar critérios de forma divergente: referencia `prd.md` e associa requisitos
às fases, às evidências preparatórias e aos futuros testes de aplicação.

- **Fixtures existentes:** arquivos sintéticos em `tests/fixtures/*.xlsx`, manifesto
  `expected-results.json` e verificação OOXML em CI. **Não são** evidência de
  conformidade de RF-03 a RF-06: não existe importador nem motor C#.
- **Plano de testes de produto:** IDs de cenários T-DOM-xx são **propostas documentais**,
  não testes automatizados existentes.
- **RNF-08/09/10:** são operacionais e podem não ter cenário de usuário CU; continuam
  rastreados a etapas técnicas e procedimentos de avaliação.

## 6. Critérios de aceitação de CRONO-004

- [x] 11 RF e 10 RNF representados sem lacunas, IDs estáveis.
- [x] Prioridade de **release** distinta da **ordem técnica**.
- [x] RF-08 a RF-11 mantidos no MVP sem rebaixamento.
- [x] RNF-03/04/08 identificados como provisórios, sem SLA assumido.
- [x] Fontes de aceite, etapas EAP, dependências, cenários e evidências rastreáveis.
- [x] Verificação estrutural documental aprovada em [GitHub Actions run #38632240223](https://github.com/OsvaldoSantana/cronocheck/actions/runs/38632240223) (21 requisitos, referências, metas provisórias, grafo sem ciclos).
- [ ] Revisão técnica/humana do PR, incluindo o tratamento da decisão OQ-06.
- [ ] Aprovação formal do PRD e do Gate G0 (não concedidas por este trabalho).

**Nenhum requisito foi implementado.** O marco da Fase 00 não é um release de software.
