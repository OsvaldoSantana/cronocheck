# CronoCheck — Matriz de rastreabilidade (CRONO-004 / revisão 1.3)

**Status:** proposta documental, aguardando validação técnica e aceite humano.  
**Escopo:** requisitos do MVP, sem implementação C# concluída.  
**Registro auditável:** [`requirements-register.json`](requirements-register.json) • [MoSCoW e priorização](requirements-prioritization.md) • [PRD e critérios de aceite](prd.md) • [Blueprint](../CRONOCHECK_BLUEPRINT_V1.md).

Esta matriz é uma **visão humana** derivada do registro de requisitos. A coluna `Must*`
indica a **proposta de obrigatoriedade para lançamento** conforme o escopo do blueprint/PRD,
**não** prova aprovação do PRD, nem validação da funcionalidade. Ordem de execução
e natureza de meta provisória estão detalhadas no registro e no documento MoSCoW.

| ID | Cenário CU | MoSCoW | Etapas EAP | Dependências propostas | Critério de aceite | Fixture existente (preparatória) | T-DOM planejado | Implementação / validação |
|---|---|---|---|---|---|---|---|---|
| RF-01 | `CU-01`, `CU-02`, `CU-03`, `CU-04`, `CU-05` | Must* | F03-E01, F03-E05 | — | prd.md §8 (RF-01) | — | `T-DOM-10` | Não implementado / Não validado |
| RF-02 | `CU-01`, `CU-05` | Must* | F03-E02, F03-E03 | `RF-01` | prd.md §8 (RF-02) | — | — | Não implementado / Não validado |
| RF-03 | `CU-01` | Must* | F04-E02, F04-E06 | `RF-01`, `RF-02` | prd.md §8 (RF-03) | `basic-valid.xlsx`, `invalid-dates.xlsx`, `formula-cells.xlsx` | — | Não implementado / Não validado |
| RF-04 | `CU-01` | Must* | F04-E03 | `RF-03` | prd.md §8 (RF-04) | — | `T-DOM-05`, `T-DOM-06` | Não implementado / Não validado |
| RF-05 | `CU-01`, `CU-02` | Must* | F04-E04 | `RF-03`, `RF-04` | prd.md §8 (RF-05) | `multi-version-v1.xlsx`, `multi-version-v2.xlsx` | `T-DOM-08` | Não implementado / Não validado |
| RF-06 | `CU-01` | Must* | F05-E01..F05-E05 | `RF-05` | prd.md §8 (RF-06) | `duplicate-ids.xlsx`, `missing-predecessor.xlsx`, `dependency-cycle.xlsx`, `inconsistent-dates.xlsx` | — | Não implementado / Não validado |
| RF-07 | `CU-01`, `CU-03` | Must* | F05-E06 | `RF-06` | prd.md §8 (RF-07) | — | — | Não implementado / Não validado |
| RF-08 | `CU-03`, `CU-05` | Must* | F06-E01, F06-E02, F06-E04 | `RF-07` | prd.md §8 (RF-08) | — | — | Não implementado / Não validado |
| RF-09 | `CU-02` | Must* | F07-E03 | `RF-05` | prd.md §8 (RF-09) | `multi-version-v1.xlsx`, `multi-version-v2.xlsx` | — | Não implementado / Não validado |
| RF-10 | `CU-04` | Must* | F07-E04 | `RF-07` | prd.md §8 (RF-10) | — | — | Não implementado / Não validado |
| RF-11 | `CU-03`, `CU-04` | Must* | F03-E04, F06-E04, F07 | `RF-01` | prd.md §8 (RF-11) | — | — | Não implementado / Não validado |
| RNF-01 | `CU-01`, `CU-02`, `CU-03`, `CU-04`, `CU-05` | Must* | F02-E05, F07-E05 | — | prd.md §9 (RNF-01) | — | — | Não implementado / Não validado |
| RNF-02 | `CU-01`, `CU-02`, `CU-03`, `CU-04`, `CU-05` | Must* | F02-E06, F08-E04 | — | prd.md §9 (RNF-02) | — | — | Não implementado / Não validado |
| RNF-03 | `CU-05` | Must* | F08-E02 | — | prd.md §9 (RNF-03) | — | — | Não implementado / Não validado |
| RNF-04 | `CU-01` | Must* | F05-E07, F08-E02 | — | prd.md §9 (RNF-04) | `large-5000-activities.xlsx` | — | Não implementado / Não validado |
| RNF-05 | `CU-01` | Must* | F04-E05 | `RF-05` | prd.md §9 (RNF-05) | — | `T-DOM-08` | Não implementado / Não validado |
| RNF-06 | `CU-01`, `CU-04` | Must* | F04-E06, F08-E01 | — | prd.md §9 (RNF-06) | — | — | Não implementado / Não validado |
| RNF-07 | `CU-03` | Must* | F03-E04 | `RF-11` | prd.md §9 (RNF-07) | — | — | Não implementado / Não validado |
| RNF-08 | — | Must* | F08-E03 | — | prd.md §9 (RNF-08) | — | — | Não implementado / Não validado |
| RNF-09 | — | Must* | F01-E06 | — | prd.md §9 (RNF-09) | — | — | Não implementado / Não validado |
| RNF-10 | — | Must* | F01-E05 | — | prd.md §9 (RNF-10) | — | — | Não implementado / Não validado |

## Observações de auditoria e evidência

- **21/21 requisitos ligados a etapas EAP**: RF-01..RF-11 e RNF-01..RNF-10.
- **RNF-08/09/10** são operacionais; ausência de cenário CU específico não os torna órfãos.
- **RNF-03/04/08** exigem calibração de metas numéricas, ainda provisórias; consultar OQ-05.
- **RF-11** tem infraestrutura de AuditEvent prevista em F03-E04 e consulta/UX nas fases seguintes (OQ-06 pendente).
- **F00-E04 já preparou** dez arquivos de fixture OOXML e manifestos em `tests/fixtures/`. O workflow
  [Fixture contract checks](../../.github/workflows/fixtures-validation.yml) passou com 10 arquivos
  e uma comparação sintética no PR #3; sua função é verificar o conjunto de testes, **não**
  validar importação, regras, autorização, desempenho ou backup do produto.
- **T-DOM-xx** referenciam cenários do documento `domain-invariants.md`; não são nomes
  de testes automatizados implementados. Os IDs de testes reais serão registrados quando existirem.
- **Decisões atualizadas em 15/10/2026:** OQ-01/02 e OQ-06..09 aprovadas; OQ-03 com diretriz de domínio profissional extensível aprovada e detalhamento pendente. OQ-04/05 abertas; o PRD v1.2 ainda exige emenda para OQ-03 e aprovação formal. Ver `decisions-2026-10-15.md` e `requirements-register.json`.
- **Gate G0** e PRD permanecem sem aceite formal.

## Atualização futura e critérios de conformidade

Após uma implementação real, cada requisito deverá ganhar: issue, commit/PR, suíte de testes,
logs/artefatos do pipeline, resultado de validação humana, release e exceções documentadas.
Não marcar `implemented`/ `validated` sem referências verificáveis.

O registro estruturado e esta matriz devem permanecer **sincronizados**. A checagem automatizada
no PR cobre IDs, prioridades, documentos e referências; não examina a qualidade semântica
dos critérios de aceite nem substitui revisão por profissional.
