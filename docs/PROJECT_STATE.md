# CronoCheck — Estado do Projeto

**Atualizado em:** 2026-10-14  
**Estado:** Fase 00 — descoberta e especificação  
**Gate G0:** **não aprovado**  
**Fase 01:** não iniciada  
**Produto implementado:** nenhum

## Controle de versões

- **PR #1:** baseline documental v1.2 integrada à `main` em 14/10/2026; merge `628880fb01b8e375d46e1d24ccab0f6aea88134f`.
- **PR #2:** OQ-01/OQ-02 e jornada AS-IS/TO-BE integrados à `main`; merge `b4c0a319c5a7dd020affc9991a7cbc9c982b72ec`.
- **PR #3:** contrato XLSX v0 e dez fixtures sintéticas integrados à `main`; merge `4f91d9cb9fb45d86fa129d1fd146caa85532e724`.
- **PR #5:** glossário e invariantes CRONO-003 integrados à `main`; merge `13ca91164ffa07e61e21bfe947d3626b76ba623a`.
- **Ciclo documental atual:** branch `docs/f00-requirements-moscow` para CRONO-004 (Issue #6); prioridades e matriz em revisão por PR, sem merge automático.
- Repositório público; nunca incluir dados reais de clientes ou credenciais.

## Decisões formalmente autorizadas

| ID | Situação | Decisão e alcance |
|---|---|---|
| OQ-01 | **Aprovada** em 14/10/2026 | Prosseguir com personas e cenários hipotéticos, mantendo a validação com usuários pendente. |
| OQ-02 | **Aprovada** em 14/10/2026 | Usar cronogramas integralmente sintéticos para contrato de importação v0 e fixtures; dados reais requerem autorização posterior. |
| OQ-03 a OQ-09 | Pendentes | Não presumir aprovação das recomendações. |

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
| F00-E04 / CRONO-002 | Contrato XLSX v0 e 10 fixtures sintéticas integrados à `main` pelo PR #3; verificação estrutural CI aprovada, revisão semântica/OQ-08 e aceite humano ainda pendentes |
| CRONO-003 / Issue #4 | Glossário e invariantes integrados à `main` no PR #5; semântica OQ-03/OQ-08/OQ-09 e aceite humano pendentes |
| CRONO-004 / Issue #6 | RF/RNF, proposta MoSCoW e registro legível por máquinas preparados na branch; validação estrutural CI aprovada (run 38632240223); aceite humano ainda pendente |
| F00-E05 | Riscos e métricas preliminares; aprovação pendente |
| Gate G0 | Não aprovado |

**Numeração preservada:** `CRONO-002` já denomina a tarefa de fixtures XLSX no blueprint (seção L). A atualização pós-merge é uma atividade de governança da Fase 00, não renomeia esse ticket.

## Próximos passos

1. Revisar e validar o rascunho AS-IS/TO-BE da F00-E02, distinguindo hipóteses de fatos observados.
2. Planejar entrevistas/validação dos cenários quando participantes estiverem disponíveis.
3. Revisar CRONO-004: matriz dos 21 RF/RNF, proposta MoSCoW, premissas e evidências; deliberar OQ-05/OQ-06 antes de ratificar prioridades.
4. Revisar CRONO-003 e decidir OQ-03/OQ-08/OQ-09 antes de estabilizar tipos, unidades e política de identidade para F04.
5. Revisar formalmente PRD, decisões abertas e checklist do Gate G0.

## Limitações observadas

Não há código de aplicação, testes funcionais da aplicação, deploy ou métricas de produto. Existem checagens de fixtures OOXML aprovadas no GitHub Actions, mas não constituem testes funcionais do CronoCheck. A publicação de documentos e a aprovação das duas decisões não comprovam funcionamento do software ou conclusão da Fase 00.
