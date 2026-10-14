# CronoCheck — Matriz de rastreabilidade — v1.2
Status: Redigido, aguardando validação técnica. Persistência: baseline v1.2 versionada na `main` pelo PR #1 em 14/10/2026. Nenhum requisito foi implementado, testado ou aprovado por esse fato.
Existem **fixtures OOXML sintéticas** e um validador estrutural em desenvolvimento (F00-E04). Não existe teste do importador ou do motor CronoCheck: nenhum RF/RNF foi implementado ou validado. IDs de testes de integração só serão registrados quando forem criados. A coluna "ID de teste" permanece "—" até a criação real do teste.

| Requisito | Cenário relacionado | Critério de aceite | Etapa da EAP | Evidência futura | ID de teste | Implementação | Validação |
|---|---|---|---|---|---|---|---|
| RF-01 | Todos (pré-condição) | PRD §8 RF-01 | F03-E01, F03-E05 | Teste automatizado + evidência no PR | — (teste de autorização futuro; não existe) | Não implementado | Não validado |
| RF-02 | Todos (pré-condição) | PRD §8 RF-02 | F03-E02, F03-E03 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RF-03 | CU-01 | PRD §8 RF-03 | F04-E02, F04-E06 | Teste automatizado + evidência no PR | — (Fixtures planejadas no blueprint H.2: basic-valid.xlsx, invalid-dates.xlsx (inexistentes)) | Não implementado | Não validado |
| RF-04 | CU-01 | PRD §8 RF-04 | F04-E03 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RF-05 | CU-01, CU-02 | PRD §8 RF-05 | F04-E04 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RF-06 | CU-01 | PRD §8 RF-06 | F05-E01 a F05-E05 | Teste automatizado + evidência no PR | — (Fixtures planejadas: duplicate-ids.xlsx, missing-predecessor.xlsx, dependency-cycle.xlsx (inexistentes)) | Não implementado | Não validado |
| RF-07 | CU-01, CU-03 | PRD §8 RF-07 | F05-E06 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RF-08 | CU-03, CU-05 | PRD §8 RF-08 | F06-E01, F06-E02, F06-E04 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RF-09 | CU-02 | PRD §8 RF-09 | F07-E03 | Teste automatizado + evidência no PR | — (Fixture planejada: multi-version-change (gerado; validação CI pendente)) | Não implementado | Não validado |
| RF-10 | CU-04 | PRD §8 RF-10 | F07-E04 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RF-11 | CU-03, CU-04 | PRD §8 RF-11 | F03-E04, F06-E02 | Teste automatizado + evidência no PR | — | Não implementado | Não validado |
| RNF-01 | CU-01 a CU-05 | PRD §9 RNF-01 | F02-E05, F07-E05 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-02 | CU-01 a CU-05 | PRD §9 RNF-02 | F02-E06, F08-E04 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-03 | CU-05 | PRD §9 RNF-03 (provisória) | F08-E02 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-04 | CU-01 | PRD §9 RNF-04 (provisória) | F05-E07, F08-E02 | Relatório de verificação + evidência no PR | — (Fixture planejada: large-5000-activities.xlsx (gerado; validação CI pendente)) | Não implementado | Não validado |
| RNF-05 | CU-01 | PRD §9 RNF-05 | F04-E05 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-06 | CU-01, CU-04 | PRD §9 RNF-06 | F04-E06, F08-E01 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-07 | CU-03 | PRD §9 RNF-07 | F03-E04 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-08 | N/A — requisito operacional | PRD §9 RNF-08 (provisória) | F08-E03 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-09 | N/A — requisito operacional | PRD §9 RNF-09 | F01-E06 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |
| RNF-10 | N/A — requisito operacional | PRD §9 RNF-10 | F01-E05 | Relatório de verificação + evidência no PR | — | Não implementado | Não validado |

Requisitos sem cenário de usuário (RNF-08, RNF-09, RNF-10) são operacionais e estão rastreados a
etapas da EAP — não são órfãos.

## Uso no controle de mudanças
Ao criar issue, teste ou PR reais, preencher "ID de teste" e atualizar as colunas de estado com
link verificável. Qualquer mudança de critério deve referenciar decisão registrada em
open-questions.md.
## Evidências preparatórias F00-E04 (não são testes da aplicação)

- `docs/product/xlsx-import-contract-v0.md`: proposta do contrato, ainda pendente de OQ-03/OQ-08.
- `tests/fixtures/expected-results.json`: resultados estruturais esperados, ainda não produzidos pelo motor do produto.
- `tests/fixtures/validate_fixtures.py`: validação estática dos arquivos OOXML e das hipóteses de teste.
- `.github/workflows/fixtures-validation.yml`: execução automatizada proposta; consultar estado do PR antes de classificar como aprovada.

Os resultados futuros do parser C# não podem ser declarados aprovados somente porque os arquivos sintéticos passam na verificação estrutural.
