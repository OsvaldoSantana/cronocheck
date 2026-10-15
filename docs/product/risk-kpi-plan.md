# CronoCheck — Plano de riscos e KPIs (F00-E05)

**Revisão:** 0.1 · **Data:** 2026-10-15 · **Situação:** plano proposto, **não aprovado**.  
**Fonte normativa:** PRD §§11–12 e blueprint §K (R-01..R-09).  
**Issue:** [F00-E05 #14](https://github.com/OsvaldoSantana/cronocheck/issues/14).  
**Não existem:** dados reais de utilização, benchmarks do importador C#, amostras de entrevistas, SLA de produção, medição de recuperação ou aprovação de risco residual.

## 1. Registro operacional de riscos

Probabilidade/impacto são as **classificações herdadas do blueprint/PRD**, não resultados de
estatística medida. "Responsável sugerido" é função, não indivíduo aceitando formalmente risco.
Cada risco permanece **aberto / a validar**.

| Risco | Prob. | Impacto | Prevenção e resposta proposta | Sinal verificável de exposição | Dono sugerido | Quando validar |
|---|---|---|---|---|---|---|
| **R-01** Excel heterogêneo | Alta | Alto | Wizard de mapeamento; preservar origem; ampliar fixtures com layouts reais apenas mediante nova autorização | taxa de falha de mapeamento; divergência bruto/normalizado | Produto/Importação | F00-E04, F04 |
| **R-02** Calendários e defasagens | Alta | Alto | Limitar regras temporais suportadas; não converter SS/FF/SF para FS sem aviso; golden datasets com resultado independente | achados temporais contestados como falsos | Domínio | OQ-03/08, F05 |
| **R-03** Excesso de arquitetura | Média | Alto | ADRs, monólito modular proposto, prova de necessidade para novos componentes e serviços | dependências ou serviços sem critério/benefício documentado | Arquitetura | F01 contínua |
| **R-04** UI sem fluxo utilizável | Média | Alto | Prototipar tarefas, revisão heurística, testes com usuários autorizados; registrar falhas | taxa de conclusão de tarefas e bloqueios por tarefa | UX/Produto | F02-E05, F07 |
| **R-05** Auditoria não confiável | Média | Alto | AuditEvent transacional, imutabilidade, testes de concorrência, backup e restauração | eventos faltantes, histórico editável, falhas de restore | Dados/Segurança | F03-E04, F08 |
| **R-06** Upload adversarial | Média | Alto | Inspeção de OOXML, limites de ZIP/CPU/memória, não executar conteúdo incorporado; isolamento e testes negativos | uploads perigosos aceitos, exaustão de recursos | Segurança | F04-E06 |
| **R-07** Escopo cresce para Project/MPP | Alta | Médio | Manter .mpp e integrações online pós-MVP, backlog separado e decisão de produto por mudança | solicitações de MPP aceitas sem alteração formal do escopo | Produto | F09 / controle contínuo |
| **R-08** CI/dívida de testes | Média | Alto | Gate de documentação já existente; adicionar build/test/safety gates quando F01 iniciar; verificação obrigatória de compatibilidade | regressões, falhas de pipeline ignoradas, PR sem teste | Engenharia | F01-E04 contínua |
| **R-09** Falta de usuários reais | Média | Alto | Registrar personas hipotéticas; definir roteiro/recrutamento; proibir declarações de validação sem sessão real | número de hipóteses sem evidência e tarefas não testadas | Produto/UX | Antes de F03/F07, conforme OQ-01 |

**Ações recomendadas antes do aceite G0:** revisar R-01/R-02/R-09, atribuir responsáveis
nominais, decidir se suas condições residuais são aceitáveis e documentar
restrições à implementação. A existência dos documentos não reduz automaticamente
probabilidade ou impacto de qualquer risco.

### Atualização proposta do registro em futuras revisões

```text
RiskId: R-__
Classificação original: probabilidade / impacto
Nova classificação (se houver): __ + justificativa, data e fonte
Gatilho/indicador: __
Ação e evidência observada: __
Responsável nominal: __
Prazo/marco: __
Risco residual e aceite: __
Status: aberto / mitigando / aceito / fechado (mediante evidência)
```

## 2. Dicionário de KPIs de produto (propostas, sem baseline)

O PRD §11 propõe três métricas centrais. As definições abaixo **detalham a operacionalização
futura**, não alegam que eventos, telemetria ou dashboards já existem.

| ID | Indicador | Definição operacional proposta | Denominador / coorte | Evento/dado futuro | Exclusões / cautelas |
|---|---|---|---|---|---|
| KPI-01 | Taxa de importação concluída na primeira tentativa | 100 × número de tentativas lógicas cuja primeira confirmação válida gerou versão ÷ tentativas lógicas elegíveis iniciadas | Tentativas com usuário autorizado, projeto e arquivo elegíveis no período | `ImportAttemptStarted`, `ImportValidationFailed`, `ScheduleVersionConfirmed`, `idempotency_key` | Retries técnicos da mesma tentativa **não são novas tentativas**; rejeição por ausência de permissão deve ser reportada à parte; distinguir arquivo inválido de erro de sistema |
| KPI-02 | Tempo da importação até primeira decisão de achado | Mediana e p90 de `first_decision_at - version_confirmed_at` por versão auditada que recebeu decisão, em horas | Versões confirmadas com pelo menos uma decisão no período | `ScheduleVersionConfirmed`, `FindingReviewCommitted`, `AuditRun` | Reportar **também** proporção sem decisão e censura por janela; não excluir silenciosamente versões que aguardam análise |
| KPI-03 | Achados resolvidos com justificativa | 100 × achados cujo estado chegou a resolução com justificativa obrigatória preenchida ÷ total de achados resolvidos na coorte | Achados resolvidos segundo máquina de estados de F06 | `FindingReviewCommitted`, `justification`, `finding_id`, `actor` | Política de justificativa ainda depende do desenho F06; não contar `Finding` de nova execução como decisão humana anterior |

**Fórmulas de agregação** requerem definições de janela, unidade e estado
temporal pelo domínio. Todas as contas são propostas para instrumentação futura.
Nenhum valor numérico, amostra de usuários ou meta foi calculado aqui.

### Regras mínimas de qualidade de métrica

- Cada resultado deve identificar janela temporal, número de observações `n`,
  número de projetos/organizações autorizadas, versão do contrato de eventos e
  motivo das exclusões.
- Para denominador zero, exibir **N/A / sem dados**, nunca 0% nem 100%.
- Segmentar por perfil de upload (tamanho/linhas/tipo), versão de produto, projeto
  apenas no painel autorizado, sem logar arquivo real de cliente.
- Privacidade: evitar PII e valores de planilha brutos em logs/telemetria; o
  acesso a indicadores por projeto precisa de autorização no backend.
- Distinguir **medição realizada**, **meta proposta** e **meta formalmente aprovada**.
- Estabelecer baseline real após implementar e observar o fluxo com consentimento
  e controles de acesso; validações de fixture estrutural não são essa baseline.

## 3. RNFs quantitativas — metas provisórias

| RNF | Referência textual do PRD | O que falta para calibrar | Evidência necessária | Estado |
|---|---|---|---|---|
| RNF-03 | p95 inferior a 500 ms para consultas usuais em cenário de referência | Definir hardware, concorrência, volume, rotas, caches e critérios de amostragem | Benchmark reprodutível e percentis com amostra/report de ambiente | **Provisória** (OQ-05) |
| RNF-04 | Referência de XLSX com 5.000 atividades em até 60 s | Implementar parser + normalização real, validar limites de entrada e hardware; repetir medições | Teste de carga com fixture e perfil completo de ambiente | **Provisória** (OQ-05) |
| RNF-08 | RPO 24h e RTO 4h | Definir estratégia de backup/retenção, ambiente e ensaio de restauração isolado | Runbook executado e medições de perda/tempo | **Provisória** (OQ-05) |

O fato de `large-5000-activities.xlsx` passar na verificação XML/OOXML
**não prova** processamento de 5.000 atividades pelo CronoCheck em 60 segundos.

## 4. Indicadores de risco para futuras revisões

| Risco | Medida candidata | Interpretação / ação de acompanhamento |
|---|---|---|
| R-01 | importações que exigem correção do mapeamento / tentativas com prévia | medir sem confundir falha de layout com falha de parser |
| R-02 | achados temporais contestados / achados temporais revisados | investigar falso positivo por calendário/unidade |
| R-04 | tarefas completas sem assistência / tarefas tentadas, por cenário | usar observação real, não inferir da existência de wireframes |
| R-05 | mutações críticas sem AuditEvent / mutações críticas executadas | expectativa zero somente depois de definir lista e testar |
| R-06 | uploads adversariais bloqueados / cenários adversariais testados | executar apenas em ambiente controlado; não publicar amostras perigosas |
| R-08 | PRs com CI obrigatório verde / PRs submetidos | distinguir PR sem check por filtro de caminho |
| R-09 | hipóteses confirmadas/refutadas com evidência / hipóteses registradas | evitar marcar "confirmada" com base apenas em inferência do time |

## 5. Aceite e evidências pendentes (F00-E05)

- [x] Nove riscos R-01..R-09 documentados com classificação original preservada.
- [x] Três métricas do PRD detalhadas com eventos, cálculo e ressalvas.
- [x] Metas RNF-03/04/08 assinaladas como provisórias, sem SLA inventado.
- [ ] Revisão humana das definições e indicação de responsáveis efetivos.
- [ ] Plano de entrevistas/validação e aceite explícito das limitações.
- [ ] Decisões OQ-03..09 deliberadas ou formalmente diferidas com condições.
- [ ] Aprovação separada do PRD e do Gate G0.

**Status:** produto ainda não instrumentado; **nenhuma medição foi realizada**.
