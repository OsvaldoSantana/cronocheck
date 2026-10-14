# CronoCheck — Estado do Projeto

**Atualizado em:** 2026-10-14  
**Estado:** Fase 00 — descoberta e especificação  
**Gate G0:** **não aprovado**  
**Fase 01:** não iniciada  
**Produto implementado:** nenhum

## Controle de versões

- **PR #1:** baseline documental v1.2 integrada à `main` em 14/10/2026; merge `628880fb01b8e375d46e1d24ccab0f6aea88134f`.
- **Ciclo documental atual:** branch `docs/f00-xlsx-contract-fixtures` para F00-E04/CRONO-002; conteúdo em revisão por PR, sem merge autorizado.
- Repositório público; nunca incluir dados reais de clientes ou credenciais.

## Decisões formalmente autorizadas

| ID | Situação | Decisão e alcance |
|---|---|---|
| OQ-01 | **Aprovada** em 14/10/2026 | Prosseguir com personas e cenários hipotéticos, mantendo a validação com usuários pendente. |
| OQ-02 | **Aprovada** em 14/10/2026 | Usar cronogramas integralmente sintéticos para contrato de importação v0 e fixtures; dados reais requerem autorização posterior. |
| OQ-03 a OQ-08 | Pendentes | Não presumir aprovação das recomendações. |

Evidência: `docs/product/decisions-2026-10-14.md`, com base em autorização explícita do responsável pelo produto na conversa.

## Entregáveis e andamento

| Item | Estado |
|---|---|
| Blueprint v1.0 | Versionado; planejamento, não implementação |
| `docs/product/prd.md` (v1.2) | Versionado; **aguardando validação técnica e aprovação formal** |
| `docs/product/personas-jtbd.md` | Versionado; hipóteses, sem entrevistas confirmatórias |
| `docs/product/open-questions.md` | OQ-01 e OQ-02 aprovadas; demais pendentes |
| `docs/product/traceability-matrix.md` | Planejada; sem testes ou funcionalidades implementadas |
| F00-E01 | Hipóteses redigidas; entrevistas não realizadas |
| **F00-E02** | **Em elaboração**: mapa AS-IS hipotético / TO-BE proposto em `docs/product/journey-as-is-to-be.md`, aguardando revisão e validação |
| F00-E03 / CRONO-001 | PRD redigido; aprovação formal pendente |
| F00-E04 / CRONO-002 | Contrato XLSX v0 e 10 fixtures sintéticas criados em `docs/f00-xlsx-contract-fixtures`; validação em CI e aceite humano ainda pendentes |
| F00-E05 | Riscos e métricas preliminares; aprovação pendente |
| Gate G0 | Não aprovado |

**Numeração preservada:** `CRONO-002` já denomina a tarefa de fixtures XLSX no blueprint (seção L). A atualização pós-merge é uma atividade de governança da Fase 00, não renomeia esse ticket.

## Próximos passos

1. Revisar e validar o rascunho AS-IS/TO-BE da F00-E02, distinguindo hipóteses de fatos observados.
2. Planejar entrevistas/validação dos cenários quando participantes estiverem disponíveis.
3. Revisar o contrato XLSX v0, os arquivos de teste e a verificação automatizada; deliberar a OQ-08 antes de estabilizar a semântica para F04.
4. Revisar formalmente PRD, decisões abertas e checklist do Gate G0.

## Limitações observadas

Não há código de aplicação, testes funcionais, CI validado, deploy ou métricas de produto. A publicação de documentos e a aprovação das duas decisões não comprovam funcionamento do software ou conclusão da Fase 00.
