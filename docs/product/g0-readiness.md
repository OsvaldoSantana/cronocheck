# CronoCheck — Dossiê de prontidão do Gate G0 (F00-E05)

**Revisão:** 0.1 · **Data:** 2026-10-15 · **Estado:** análise de prontidão, **SEM APROVAÇÃO**.  
**Issue:** [F00-E05 — #14](https://github.com/OsvaldoSantana/cronocheck/issues/14).  
**Autoridade:** blueprint v1.0, seção E/FASE 00, seção L/checklist de gates, PRD v1.2, decisões em `open-questions.md`.  
**Objetivo do G0:** confirmar uma baseline testável de produto e seus limites, reconhecer riscos e pendências e registrar aceite humano para ingressar na preparação F01. **Merge de documentos ou CI verde não constituem Gate G0 aprovado.**

## 1. Diagnóstico executivo

**Situação recomendada nesta revisão:** **HOLD / AGUARDAR DECISÃO**, não GO.  
Existe conteúdo documental substancial e fixtures sintéticas verificadas por CI, mas faltam **aprovação explícita do PRD**, deliberação de OQ relevantes, revisão humana dos cenários e uma decisão formal sobre limitações de validação com usuários. O produto C#/React e suas integrações **não existem**; nada deve ser descrito como operacional.

A autorização anterior **OQ-01** permite continuar com hipóteses e documentar limites, mas mantém a necessidade de entrevistas antes de F03/F07. A autorização **OQ-02** permite apenas fixtures **integralmente sintéticas**, não arquivos reais de clientes. Isso possibilita preparar G0 **sem forjar entrevistas**, não aprová-lo automaticamente.

## 2. Critérios de saída Fase 00 (espelho do blueprint)

| Etapa | Aceite definido pelo blueprint | Evidência já existente | Lacuna e ação antes de fechar | Estado |
|---|---|---|---|---|
| F00-E01 | 3–5 cenários priorizados e validados, **ou limitações explicitadas** | `docs/product/personas-jtbd.md` com CU-01..05 e hipóteses declaradas | Registrar decisão humana sobre aceitar limitações para G0; entrevistar usuários reais antes dos marcos restringidos pela OQ-01 | Parcial — sem validação empírica |
| F00-E02 | Jornada primária completa, hipóteses registradas | `docs/product/journey-as-is-to-be.md` e `docs/ux/flows.md` | Revisão humana dos handoffs, personas e exceções; não tratar AS-IS como processo observado | Redigida, aceite pendente |
| F00-E03 | PRD, RF/RNF e backlog inicial **aprovados** | `docs/product/prd.md`, `requirements-register.json`, `traceability-matrix.md`, `requirements-prioritization.md` | Revisar RF-01..11 e RNF-01..10, aprovar formalmente a baseline e registrar responsável/data | **Bloqueado por aprovação do PRD** |
| F00-E04 | Formato XLSX de referência, calendário/regras; fixtures representativas e extremos catalogados | `xlsx-import-contract-v0.md`, 10 XLSX sintéticos, `expected-results.json` e CI OOXML | Deliberar OQ-03/08/09 ou formalizar o caráter limitado/provisório do contrato antes de comprometer implementação | Parcial — sem semântica definitiva |
| F00-E05 | Riscos, prioridades e definição de sucesso; **Gate G0 aprovado; nenhuma decisão crítica implícita** | PRD §11–12, `risk-kpi-plan.md`, `decision-brief-f00.md`, este dossiê | Registrar responsáveis reais, critérios/risco residual, decisões e aceite humano G0 | **Não aprovado** |

### Gate G0 do blueprint, de forma literal quanto ao significado

- PRD baseline: documento existente, **sem aprovação**.
- Dados de teste anonimizados: em vez de dados reais, foram produzidos dados **inteiramente sintéticos**, com autorização OQ-02. Não há dados reais anonimizados; indicar a diferença.
- Histórias prioritárias: CU-01..04 propostos; CU-05 adicional ainda sujeito à OQ-07 e validação.
- Decisões abertas catalogadas: OQ-03..09 e GOV-01/02 (administrativas, fora da decisão de produto), todas pendentes.
- Nenhuma decisão crítica pode ser tomada implicitamente por merge de documentação.

## 3. Checklist operacional de gate com evidências

| Item do checklist do blueprint | Evidência disponível | Verificação restante | Estado |
|---|---|---|---|
| Entregáveis publicados/versionados | PRs #1, #2, #3, #5, #7, #9, #11, #13 integrados à `main` | Revisar pertinência/versões vigentes dos documentos | Satisfeito quanto à publicação |
| Critérios de aceite demonstrados | PRD §§8–9 com critérios testáveis; fixtures estruturais verificadas | Demonstração funcional não se aplica à F00, mas **critérios documentais/aceite humano** pendentes | Parcial |
| RF/RNF ligados a testes | `traceability-matrix.md`, cenários T-DOM e fixtures planejadas | Testes de aplicação reais não existem; distinguir planejamento de evidência executada | Rastreabilidade documental, não verificação de produto |
| Segurança, UX, auditabilidade revisadas | SECURITY, UX flows, domain-invariants, ADRs propostos | Revisão formal de riscos e estados, sem declarar auditoria de segurança/usabilidade executada | Parcial |
| Migrações/contratos documentados, se houver | XLSX v0 documentado; sem migração/DDL porque não há banco criado | Especificar o que fica para F01/F04; não inventar migração | Condicional / aplicabilidade delimitada |
| Riscos e decisões atualizados | PRD R-01..09, OQ-01..09, GOV-01/02, risk-kpi-plan | Proprietários efetivos e critérios de risco residual; deliberação das OQ críticas | Pendente |
| CI verde e PRs integrados | Workflow `Repository quality gate` e validadores documentais/OOXML no GitHub | Conferir o último workflow da `main` e o do PR deste dossiê; CI não executa software | Parcial até verificação da revisão |
| Aprovação registrada com responsável, data e evidência | Aprovações OQ-01/02 de 14/10 | Aprovação de PRD, F00-E02/F00-E04, riscos/KPIs e **G0** separadamente | **Não satisfeito** |

O número de um pull request **não é prova de revisão independente**. A existência
de `CODEOWNERS` também não garante enforcement de aprovações na `main`.

## 4. Bloqueios e ordem de deliberação proposta

| Grupo | Decisões | Relevância para G0 | Recomendação do preparador |
|---|---|---|---|
| Escopo do MVP e linha de corte | PRD, RF-01..11, RNF-01..10, CU-05/OQ-07 | Alta | Aprovação expressa da baseline, com CU-05 marcada hipotética até validação |
| Semântica inicial do dado | OQ-03, OQ-08, OQ-09 | Alta para contrato v0; crítica antes de F04/F05 | Aceitar **limites sintéticos explícitos**, sem promover regras de cronograma profissional |
| Priorização e metas | OQ-05, OQ-06 | Alta para compromissos/planejamento | Metas provisórias calibradas depois; AuditEvent base em F03 |
| Arquitetura e ambiente | OQ-04, ADR-001/002 | Pode ser encaminhada a F01-E01 **com registro expresso** | Aprovar somente a sequência decisória, não antecipar hosting/OIDC |
| Validação de usuários | OQ-01 aprovada com ressalvas; revisão dos cenários | Alta | Registrar o limite atual e plano concreto de validação antes de F03/F07 |
| Administração GitHub | GOV-01/02 | Não são aceite funcional G0, mas afetam governança e confidencialidade | Deliberar fora do gate sem mudar configurações automaticamente |

Para alternativas, impacto e texto de deliberação, ver `decision-brief-f00.md`.

## 5. Proposta de decisão formal do responsável — NÃO PREENCHIDA

```text
Gate: G0 — Descoberta, escopo e requisitos
Baseline examinada (PRD versão/commit): [PENDENTE]
Artefatos verificados (links): [PENDENTE]
Decisões OQ aprovadas / adiadas: [PENDENTE]
Limitações aceitas, especialmente entrevistas: [PENDENTE]
Responsável: [PENDENTE]
Data: [PENDENTE]
Resultado: [ ] APROVADO  [ ] APROVADO COM CONDIÇÕES  [ ] NÃO APROVADO
Condições e prazos, se aplicável: [PENDENTE]
Riscos residuais e responsáveis: [PENDENTE]
Autorização expressa para iniciar F01: [PENDENTE]
Evidência inequívoca da decisão: [PENDENTE]
```

**Não escolher nenhuma das opções no lugar do responsável pelo produto.**
Até que a decisão seja registrada, `docs/PROJECT_STATE.md` deve conservar
`**Gate G0:** **não aprovado**` e `**Fase 01:** não iniciada`.

## 6. O que um G0 aprovado não comprovaria

- Não torna verdadeiras hipóteses de usuários sem entrevistas.
- Não substitui aprovação de ADR-001/002, escolha do IdP OIDC, hospedagem ou regras
  de proteção GitHub (GOV-01/02).
- Não garante precisão de auditoria temporal, desempenho RNF-03/04, RPO/RTO RNF-08,
  segurança, acessibilidade ou confiabilidade do código — inexistente nesta fase.
- Não autoriza importar ou publicar dados corporativos reais, nem adicionar funcionalidades pós-MVP.

## 7. Resultado desta revisão

**Preparo documental:** em andamento, com múltiplos artefatos existentes.  
**Evidências empíricas:** não realizadas.  
**Gate G0:** **não aprovado**.  
**Recomendação atual:** HOLD até decisão explícita sobre baseline PRD, pendências
prioritárias, limitações de validação e riscos.

**Próxima revisão:** responsável pelo produto avalia este dossiê e
`decision-brief-f00.md`; as decisões aceitas devem atualizar `open-questions.md`,
PRD e este gate **em uma revisão posterior, com evidência nominal**.
