# CronoCheck — Estado do Projeto

**Atualizado em:** 2026-10-15  
**Estado:** Fase 00 — descoberta e especificação  
**Gate G0:** **não aprovado**  
**Fase 01:** não iniciada  
**Produto implementado:** nenhum

## Controle de versões

- **PR #1:** baseline documental v1.2 integrada à `main` em 14/10/2026; merge `628880fb01b8e375d46e1d24ccab0f6aea88134f`.
- **PR #2:** OQ-01/OQ-02 e jornada AS-IS/TO-BE integrados à `main`; merge `b4c0a319c5a7dd020affc9991a7cbc9c982b72ec`.
- **PR #3:** contrato XLSX v0 e dez fixtures sintéticas integrados à `main`; merge `4f91d9cb9fb45d86fa129d1fd146caa85532e724`.
- **PR #5:** glossário e invariantes CRONO-003 integrados à `main`; merge `13ca91164ffa07e61e21bfe947d3626b76ba623a`.
- **PR #7:** registro de requisitos e prioridades CRONO-004 integrados à `main`; merge `6d14fad35704ae8c0ae2314a3e00c32707a5f6ac`.
- **PR #9:** fluxos e wireframes CRONO-005 integrados à `main`; merge `f8675dce8dc6338689bc27b5cb29df97e3a406f8`.
- **PR #11:** ADR-001/002 e C4 L1/L2 propostos integrados à `main`; merge `a01118568d2c99c98dbcb3b715d39ce11598b9e8` (propostas ainda sem aceite arquitetural).
- **PR #13:** governança e quality gate integrados à `main` em 15/10/2026; merge `f686831ebb3e9ad5724c1a0a52c56d90cac6104a`.
- **PR #15:** prontidão G0 e matriz de riscos/KPIs integradas à `main`; merge `16af86a1358e5ba942cc1f195dc120a81c86e71e`.
- **Ciclo documental atual:** branch `docs/f00-oq03-and-approved-decisions`, issue #16; atualização das decisões OQ e comparação técnica OQ-04/OQ-05 em revisão, sem merge automático.
- Repositório público; nunca incluir dados reais de clientes ou credenciais.

## Decisões formalmente autorizadas

| ID | Situação | Decisão e alcance |
|---|---|---|
| OQ-01 | **Aprovada** em 14/10/2026 | Prosseguir com personas e cenários hipotéticos, mantendo a validação com usuários pendente. |
| OQ-02 | **Aprovada** em 14/10/2026 | Usar cronogramas integralmente sintéticos para contrato de importação v0 e fixtures; dados reais requerem autorização posterior. |
| OQ-03 | **Diretriz aprovada** em 15/10/2026 | Rejeitada modelagem restrita a FS simples; modelo extensível, sem perda silenciosa, com detalhamento técnico e emenda do PRD pendentes. |
| OQ-04 e OQ-05 | **Pendentes** | Alternativas de stack, autenticação/hospedagem e metas de desempenho em explicação; nenhuma escolha formal. |
| OQ-06 | **Aprovada** em 15/10/2026 | Base AuditEvent transacional em F03-E04, UI de revisão depois, sem reduzir escopo RF-08..11. |
| OQ-07 | **Aprovada** em 15/10/2026 | CU-05 multiprojeto priorizado, ainda sem validação empírica. |
| OQ-08 | **Aprovada** em 15/10/2026 | Convenções válidas para fixtures sintéticas v0, não para calendários profissionais definitivos. |
| OQ-09 | **Aprovada** em 15/10/2026 | Identidade interna distinta de ID externo; preservar ambiguidades; normalização de igualdade ainda a especificar. |

Evidências: `docs/product/decisions-2026-10-14.md` e `docs/product/decisions-2026-10-15.md`, correspondentes às manifestações expressas do responsável pelo produto.

## Entregáveis e andamento

| Item | Estado |
|---|---|
| Blueprint v1.0 | Versionado; planejamento, não implementação |
| `docs/product/prd.md` (v1.2) | Versionado; **aguardando validação técnica e aprovação formal** |
| `docs/product/personas-jtbd.md` | Versionado; hipóteses, sem entrevistas confirmatórias |
| `docs/product/open-questions.md` | OQ-01/02/06/07/08/09 aprovadas e diretriz OQ-03 aprovada; OQ-04/05 pendentes, detalhamento OQ-03 aberto |
| `docs/product/traceability-matrix.md` | Planejada; sem testes ou funcionalidades implementadas |
| F00-E01 | Hipóteses redigidas; entrevistas não realizadas |
| **F00-E02** | **Em elaboração**: mapa AS-IS hipotético / TO-BE proposto em `docs/product/journey-as-is-to-be.md`, aguardando revisão e validação |
| F00-E03 / CRONO-001 | PRD redigido; aprovação formal pendente |
| F00-E04 / CRONO-002 | Contrato XLSX v0 e 10 fixtures sintéticas integrados à `main` pelo PR #3; verificação estrutural CI aprovada, revisão semântica/OQ-08 e aceite humano ainda pendentes |
| CRONO-003 / Issue #4 | Glossário e invariantes integrados à `main` no PR #5; semântica OQ-03/OQ-08/OQ-09 e aceite humano pendentes |
| CRONO-004 / Issue #6 | RF/RNF, proposta MoSCoW e registro estruturado integrados à `main` pelo PR #7; validação documental CI aprovada, aceite do PRD e decisões pendentes |
| CRONO-005 / Issue #8 | Fluxos, wireframes e roteiro de usabilidade integrados à `main` no PR #9; validação documental CI aprovada; testes com usuários e aceite humano pendentes |
| CRONO-006 / Issue #10 | ADR-001/002 propostos integrados à `main` no PR #11; CI documental aprovado; aceitação formal das ADRs, OQ-04, hospedagem e identidade pendentes |
| CRONO-007 / Issue #12 | Templates, políticas e quality gate integrados à `main` pelo PR #13; nenhum ruleset nem mudança de visibilidade aplicado; GOV-01/GOV-02 pendentes |
| F00-E05 / Issue #14 | Dossiê de prontidão G0 e plano de riscos/KPIs integrados à `main` no PR #15; Gate G0 não aprovado |
| Decisões 15/10 / Issue #16 | OQ-03 (diretriz) e OQ-06..09 aprovadas; OQ-04/OQ-05 abertas; exige emenda e aprovação da baseline PRD antes de G0 |

| Gate G0 | Não aprovado |

**Numeração preservada:** `CRONO-002` já denomina a tarefa de fixtures XLSX no blueprint (seção L). A atualização pós-merge é uma atividade de governança da Fase 00, não renomeia esse ticket.

## Governança administrativa (ainda sem decisão)

- **GOV-01 — Visibilidade:** o repositório permanece **público**. O blueprint menciona repositório privado; nenhuma alteração de visibilidade foi autorizada ou efetuada.
- **GOV-02 — Proteções da `main`:** listagem de rulesets retornou `[]`; a leitura da proteção clássica retornou 403 (`Resource not accessible by integration`). Portanto, a proteção clássica não está verificada. Nenhuma regra administrativa foi aplicada nesta etapa.
- **Quality gate de PR:** workflow integrado à `main` pelo PR #13; execução GitHub Actions 38637436783 **aprovada** na branch do PR (cinco validadores). Checagens apenas documentais/fixtures; não foi comprovado que o job é obrigatório na `main`.

## Próximos passos

1. Revisar e validar o rascunho AS-IS/TO-BE da F00-E02, distinguindo hipóteses de fatos observados.
2. Planejar entrevistas/validação dos cenários quando participantes estiverem disponíveis.
3. Revisar F00-E05: `docs/product/g0-readiness.md`, `risk-kpi-plan.md` e `decision-brief-f00.md`; registrar lacunas e condições, sem declarar G0 aprovado.
4. Deliberar OQ-04/OQ-05 e especificar cobertura técnica de OQ-03, calendários e validação de campos antes da implementação correspondente.
5. Preparar emenda formal ao PRD v1.2 compatível com OQ-03 e submetê-la a aceite; depois solicitar decisão expressa sobre G0, riscos e limitações.
6. Somente após autorização expressa, avaliar GOV-01/GOV-02 e verificar na interface GitHub as regras efetivamente ativas.

## Limitações observadas

Não há código de aplicação, protótipo clicável, testes de usabilidade com pessoas, testes funcionais da aplicação, deploy ou métricas de produto. Existem checagens de fixtures OOXML aprovadas no GitHub Actions, mas não constituem testes funcionais do CronoCheck. A publicação de documentos e a aprovação das decisões de produto não comprovam funcionamento do software ou conclusão da Fase 00.
