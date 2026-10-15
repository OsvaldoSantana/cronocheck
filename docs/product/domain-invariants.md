# CronoCheck — Invariantes, estados e critérios do domínio v0.1

> **Nota de 15/10/2026:** OQ-03 e OQ-09 aprovaram diretrizes de extensibilidade e identidade; OQ-08 aprovou apenas convenções de fixtures. As regras profissionais de calendário e normalização permanecem pendentes de detalhamento. Ver `decisions-2026-10-15.md`.

**Referências:** CRONO-003 ([Issue #4](https://github.com/OsvaldoSantana/cronocheck/issues/4)), [glossário](domain-glossary.md), blueprint C.5–C.7, PRD, contrato XLSX v0 e `tests/fixtures/expected-results.json`.  
**Estado:** análise conceitual para revisão humana. Não cria classes C#, migrações ou código da aplicação.

## 1. Classes de regras

- **INV (invariante estrutural obrigatória):** proteção do estado do sistema prevista no
  blueprint, como não sobrescrever versões ou não autorizar acesso cruzado.
- **VAL (pré-condição de importação proposta):** validação de formato/tipo antes de criar
  versão, dependente do contrato XLSX v0.
- **AUD (condição a ser auditada):** inconsistência de cronograma **preservada** como
  dado e examinada por regra posterior; nunca corrigida silenciosamente.
- **DEC (decisão aberta):** convenção do domínio ainda não homologada;
  não deve ser imposta como requisito final de produção.

## 2. Invariantes transacionais e de segurança

| ID | Tipo | Regra | Falha que previne | Evidência necessária em implementação |
|---|---|---|---|---|
| INV-001 | INV | `ProjectId` delimita autorização em toda operação e consulta de origem, versão, auditoria, achado e exportação. | Leitura/edição entre projetos | Testes de acesso positivo/negativo RF-01/RF-02, inclusive IDs adivinháveis |
| INV-002 | INV | Uma tentativa de upload/prévia não cria `ScheduleVersion` sem confirmação explícita. | Versionamento implícito e perda de controle | Contagem de versões antes/depois da prévia (RF-04) |
| INV-003 | INV | Confirmar nova versão não sobrescreve os bytes originais, mapeamento e snapshot de qualquer versão histórica. | Auditoria não reproduzível | Teste de integridade e consulta às duas versões (RF-05) |
| INV-004 | INV | Reprocessar a mesma operação com chave de idempotência apropriada não duplica versões ou achados; intenção distinta não é automaticamente suprimida só por ter arquivo igual. | Duplicação ou descarte indevido de importações | Testes de retry e concorrência (RNF-05) |
| INV-005 | INV | A cada versão pertencem arquivo original, hash SHA-256, origem das linhas e política de mapeamento usada. | Perda de procedência | Reconstrução da versão a partir de evidência e SHA (RF-05) |
| INV-006 | INV | Um `AuditRun` deve registrar `ScheduleVersionId`, `RuleSetVersion`, estado e contexto de execução; reexecução não altera resultados passados. | Mudança retroativa de achados | Reexecução e comparação de duas auditorias (RF-06) |
| INV-007 | INV | Um `Finding` preserva regra, versão, entradas, evidências e origens; uma `FindingReview` não edita retroativamente o achado. | Decisão humana falsificando resultado do motor | Consulta histórica de achado antes/depois de revisão (RF-07/RF-08) |
| INV-008 | INV | Toda mutação de negócio declarada crítica deve produzir `AuditEvent` na mesma transação; rollback não deixa evento órfão. | Trilha incompleta ou falsa | Teste transacional e casos de falha induzida (RNF-07) |
| INV-009 | INV | Tempos de eventos operacionais são instantes UTC; datas planejadas sem horário são preservadas como datas civis quando a origem assim o determina. | Deslocamento de datas por timezone | Testes de horário de verão/fuso e serialização de datas |
| INV-010 | INV | Um vínculo cujo ID de origem é inválido/ambíguo não pode ser silenciosamente resolvido para outra atividade. | Grafo incorreto e falsos achados | Fixtures de predecessora ausente ou duplicada (RF-06; OQ-09) |
| INV-011 | INV | Exportação, consulta e decisões respeitam autorização do recurso no backend; ocultação de UI não é autorização. | Exposição indevida | Testes 401/403/404 e exportação RF-10 |
| INV-012 | INV | Código não executa fórmulas, macros, links ou consultas incorporadas em XLSX; o arquivo é entrada não confiável. | Execução de código ou abuso de recursos | Testes de upload malformado, ZIP anômalo, fórmula e recursos |
| INV-013 | INV | Regras versionadas + snapshots idênticos produzem as mesmas **categorias e evidências determinísticas**; timestamps de execução/IDs técnicos são metadados fora da comparação. | Resultados de auditoria inconsistentes | Golden datasets + comparação projetada das saídas (RF-06) |
| INV-014 | INV | IDs internos e associações entre versões não podem ser presumidos pelo número da linha ou nome visível da atividade. | Pareamento incorreto em VersionDiff | Casos de reordenação, renomeação e IDs duplicados (RF-09; OQ-09) |

As invariantes descrevem expectativas; **nenhum teste de produto foi implementado ainda**.

## 3. Validações do perfil XLSX de referência

| ID | Tipo | Pré-condição e resultado propostos | Fixture |
|---|---|---|---|
| VAL-001 | VAL | Pacote OOXML seguro e legível, aba/colunas mapeáveis; caso contrário, erro impeditivo sem criar versão. | Caso inválido OOXML ainda não criado |
| VAL-002 | VAL | Data `YYYY-MM-DD` textual impossível/ilegível → `IMP_INVALID_DATE`, preservando localização da célula; não converte automaticamente. | `invalid-dates.xlsx` (C2) |
| VAL-003 | VAL | Fórmula em coluna mapeada → `IMP_FORMULA_IN_MAPPED_CELL`; não executa nem confia no cache. | `formula-cells.xlsx` (B2) |
| VAL-004 | VAL | Duração não parseável como inteiro positivo no perfil v0 → validação impeditiva; isso não é regra universal de calendários profissionais. | Fixture específica ainda não criada |
| VAL-005 | VAL | Cabeçalho/colunas de origem são mapeados pelo usuário; falta de mapeamento obrigatório é erro de prévia. | Teste de UI e contrato pendente |
| AUD-001 | AUD | IDs de origem repetidos **permanecem como registros distintos**; uma categoria de auditoria aponta todas as linhas relevantes. | `duplicate-ids.xlsx` |
| AUD-002 | AUD | Predecessora inexistente **não é removida**; referência fica rastreável e gera achado. | `missing-predecessor.xlsx` |
| AUD-003 | AUD | Ciclo de precedências **não é corrigido**; é relatado como achado. | `dependency-cycle.xlsx` |
| AUD-004 | AUD | Data final anterior à inicial, porém legível, **não é bloqueada pela importação v0**; gera achado posterior. | `inconsistent-dates.xlsx` |
| AUD-005 | AUD/DEC | Duração divergente das datas civis inclusivas pode ser candidata a achado **somente no perfil proposto** e após decisão OQ-08. | Fixture ainda não criada |

**Diferença importante:** VAL-002 rejeita uma data impossível, enquanto AUD-004 preserva uma
data civil legível que contraria uma regra de cronologia. Essa distinção permite auditar
cronogramas problemáticos sem apagar a evidência de origem.

## 4. Regras de resolução de referência (proposta, ainda não aprovada)

Dado um token bruto `P001` na célula de predecessoras de uma atividade:

1. Preservar token, aba, linha, célula, versão e forma normalizada adotada.
2. Aplicar *apenas* a política de igualdade de IDs aprovada.
3. Se nenhuma atividade for encontrada, classificar como `unresolved_missing`.
4. Se uma atividade for encontrada, classificar como `resolved`.
5. Se múltiplas atividades coincidirem, classificar como `unresolved_ambiguous`.
6. Se vínculo usar tipo ou defasagem não suportados, classificar como
   `unsupported`/aviso, sem convertê-lo para FS silenciosamente.
7. Nunca criar aresta de grafo para `unresolved_missing` ou
   `unresolved_ambiguous` como se existisse correspondência única.

Uma política de comparação **case-sensitive/case-insensitive**, escopo hierárquico,
normalização Unicode, espaçamento e conflito de IDs exige decisão OQ-09.
O exemplo `dependency-cycle.xlsx` contém IDs únicos e três referências inequívocas.

## 5. Caso de versionamento — exemplo sintético

| Fonte | Registro | Esperado |
|---|---|---|
| `multi-version-v1.xlsx` | `M001`, `M002`, `M003` | Três atividades na versão base |
| `multi-version-v2.xlsx` | `M001`, `M003`, `M004` | Três atividades na versão nova |
| Diff planejado | ID `M002` | Removida |
| Diff planejado | ID `M004` | Adicionada |
| Diff planejado | ID `M003` | Modificada |
| Diff planejado | ID `M001` | Inalterada |

Essa comparação é inequívoca **somente porque os IDs são únicos e estáveis nas duas
fixtures**. Mudança de identificadores, duplicação ou importação de outro projeto requer
uma política explícita de pareamento, não heurística silenciosa.

## 6. Modelagem de datas, duração e calendários

### Perfil experimental das fixtures (OQ-08 pendente)

- `CivilDate`: dia ISO, sem timezone e sem horário.
- `CalendarDayDuration`: inteiro positivo, contagem inclusiva (`finish - start + 1`)
  proposta **somente** no contrato sintético v0.
- `WorkingDuration`: ainda sem unidade/regra; não converter automaticamente.
- `Calendar`: entidade conceitual prevista para trabalho e exceções; ainda não
  definida em nível de precisão de jornada, feriados, turnos ou hora-base.
- `Dependency`: representa predecessor/sucessor e registra tipo, defasagem e
  procedência. Vínculos FS simples são usados **nos exemplos**; OQ-03 pendente.

### Casos que bloqueiam adoção ingênua dessa regra

- Atividade de turno noturno que atravessa uma data civil.
- Atividade com duração 0 em projeto, como marco (milestone), se admitida na produção.
- Calendários diferentes para predecessora e sucessora.
- Lag negativo (lead) ou defasagem em horas.
- Datas com timezone/offset, ou datas nativas numéricas Excel.
- Resumos/WBS que não são executáveis e podem ter datas derivadas.

**Decisão necessária:** não promover a equação de duração inclusiva nem a proibição
universal de duração zero a regra normativa para cronogramas reais sem OQ-08.

## 7. Critérios verificáveis para F04/F05/F07

| Caso | Entrada | Comportamento futuro a testar | Evidência esperada |
|---|---|---|---|
| T-DOM-01 | Dois registros com mesmo ID, linhas diferentes | Duas entidades e um grupo de duplicidade | IDs internos distintos + SourceLocator |
| T-DOM-02 | Predecessora não presente | Referência preservada, aviso/achado | Origem e identificador ausente |
| T-DOM-03 | Referência a ID repetido | Nenhuma resolução arbitrária | Estado ambíguo + linhas candidatas |
| T-DOM-04 | `finish < start` com datas válidas | Importação aceita e achado posterior | Uma versão e achado versionado |
| T-DOM-05 | Data impossível | Bloqueio na prévia | Nenhuma nova versão |
| T-DOM-06 | Fórmula na célula mapeada | Bloqueio, sem execução | Célula e código de erro |
| T-DOM-07 | Reexecutar auditoria idêntica | Nova execução, evidências iguais | Dois AuditRuns e resultados comparáveis |
| T-DOM-08 | Repetir confirmação com mesma chave | Sem versão duplicada | Contagem de versões |
| T-DOM-09 | Alterar ordem das linhas sem alterar IDs | Sem inferir mudanças por posições | Diff consistente |
| T-DOM-10 | Consultar outro projeto | Negado sem vazar dados | Testes de autorização |
| T-DOM-11 | Planejamento com duração zero/marco | **Especificar após OQ-08** | Regra documentada, fixture adicional |
| T-DOM-12 | Relacionamento FS com calendário útil | **Especificar após OQ-03/OQ-08** | Regra temporal e dataset aprovados |

Os identificadores `T-DOM-xx` são **cenários propostos**, não IDs de testes
automatizados implementados e nem compromissos de resultado para decisões pendentes.

## 8. Critérios para aceite documental

- [x] Invariantes de projeto, importação, versionamento, auditoria e eventos documentadas.
- [x] Semântica de erro impeditivo separada de achado de auditoria.
- [x] Casos de ID duplicado, referência ambígua e diferenças entre versões descritos.
- [x] Requisitos RF-03/04/05/06/09 e RNF-05/07 relacionados a cenários verificáveis.
- [ ] Revisão humana das invariantes e prioridade de regras.
- [ ] Deliberação OQ-03, OQ-08, OQ-09 antes das respectivas implementações.
- [ ] Exemplos de borda incorporados às fixtures quando necessários.
- [ ] Gate G0 aprovado formalmente após todas as exigências da Fase 00.

**Não confundir documentação rastreável com implementação e teste de domínio.**
