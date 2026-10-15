# CronoCheck — Brief de decisões para encerramento da Fase 00

**Data:** 2026-10-15 · **Status:** recomendações **NÃO APROVADAS**.  
**Issue:** [F00-E05 #14](https://github.com/OsvaldoSantana/cronocheck/issues/14).  
**Referências:** `open-questions.md`, `decisions-2026-10-14.md`, PRD §§7–12, `xlsx-import-contract-v0.md`, `domain-invariants.md`, ADR-001/002 e `g0-readiness.md`.

## 1. O que já recebeu autorização

| ID | Escolha autorizada em 14/10/2026 | Limite |
|---|---|---|
| OQ-01 | Prosseguir com personas e jornadas **hipotéticas** | Não declarar entrevistas realizadas; validação antes dos marcos F03/F07 ainda necessária |
| OQ-02 | Desenvolver fixtures e contrato v0 com arquivos **integralmente sintéticos** | Não publicar nem utilizar arquivos reais de clientes sem nova autorização |

Nenhuma das escolhas abaixo foi aprovada por merge de PR. Este brief
**não altera `open-questions.md`** e não registra votos, assinaturas
ou datas fictícias.

## 2. Recomendações para OQ-03 a OQ-09

| ID | Decisão em debate | Alternativa recomendada para deliberação | Consequências e limite | Momento crítico |
|---|---|---|---|---|
| **OQ-03** | FS simples vs SS/FF/SF e lag complexo no MVP | **(a) FS simples** como nível inicial das regras auditáveis | Não converter outros tipos para FS silenciosamente; registrar não suportados e evidências; demais dependências podem ser mantidas como tokens brutos | Antes de fechar contrato e motor F04/F05 |
| **OQ-04** | Escolher stack/hosting/identidade já ou no desenho F01 | **(b) decisão final na F01-E01 via ADR** | ADR-001/002 seguem propostas; .NET/React são premissas do blueprint, mas Vite/Next, OIDC/BFF e hospedagem precisam de decisão explícita antes da implementação correspondente | Início F01-E01 |
| **OQ-05** | Tratar RNF-03/04/08 como SLAs ou metas calibráveis | **(b) provisórias, com experimentos** | Não prometer p95/tempo de importação/RPO/RTO como compromissos antes do benchmark/restauração; obrigações RNF permanecem no MVP | F05-E07/F08-E02/E03 |
| **OQ-06** | Ordem de RF-08..11 após regras e evidências | **Sequenciar UI de revisão depois de RF-06/07, mas fundar AuditEvent em F03-E04** | Todos RF-08..11 seguem obrigatórios no MVP; não adiar a base transacional de RNF-07 | F03-E04 |
| **OQ-07** | Priorizar CU-05 multiprojeto entre 3–5 cenários | **Incluir CU-05 como cenário proposto**, não validado | Dashboard já está no MVP; validação de necessidade real e autoridade entre projetos é obrigatória antes de afirmar priorização do usuário | F00-E01/F02-E05 |
| **OQ-08** | Datas textuais ISO, dias corridos inclusivos, fórmula como erro no perfil XLSX | **(a) somente como perfil de fixture v0**, revisável | Não impor `finish-start+1` a calendários profissionais; marcos de duração zero, datas/hora, serial Excel e jornadas requerem regras separadas; fórmula não executada | Antes de F04-E01 |
| **OQ-09** | Identidade interna e predecessora referindo ID duplicado | **Chave interna distinta de ID de origem**, preservar bruto + SourceLocator, classificar referências múltiplas como ambíguas | Não mesclar atividades por ID; definir política de igualdade/case/Unicode e pareamento entre versões em especificação adicional; exigir evidência antes de criar aresta de grafo | F04-E01/F05/F07 |

OQ-06 não cabe perfeitamente em uma leitura estritamente linear da tabela:
o **aceite proposto** deve registrar explicitamente que **AuditEvent nasce em
F03-E04**, mesmo que a experiência de consulta do histórico tenha entrega
posterior. Essa ressalva impede confundir ordem de UI com adiamento de requisito.

## 3. Recomendação de prioridade para deliberação

| Prioridade | Conjunto | Por quê |
|---|---|---|
| 1 — Antes do aceite de baseline G0 | Escopo PRD e linha de corte, OQ-07, declaração de limitações com usuários | Define **o que** o software deverá entregar e para quem |
| 2 — Antes de estabilizar contrato e implementar F04/F05 | OQ-03, OQ-08, OQ-09 | Semântica errada causa falsos achados que não se corrigem só na UI |
| 3 — Planejamento/qualidade do MVP | OQ-05, OQ-06 | Afeta cronograma, provas e arquitetura transacional |
| 4 — Escolha tecnológica ao entrar na F01 | OQ-04, ADR-001, ADR-002 e, futuramente, ADR-007 | Não selecionar hospedagem/provedor de identidade sem confirmar requisitos |
| Administrativa separada | GOV-01, GOV-02 | Visibilidade/proteção de branch não são alteração de escopo do produto |

Essas prioridades representam **ordem de decisão recomendada**, não classe
MoSCoW de requisitos. O registro RF-01..11/RNF-01..10 permanece intacto.

## 4. GOV-01 e GOV-02 — FORA das OQ de produto

| ID | Alternativas | Recomendação | Estado |
|---|---|---|---|
| GOV-01 — público/privado | Manter público; migrar a privado | Manter o estado existente **até decisão expressa**. O blueprint propõe privado, mas mudar acesso exige autorização separada e análise de colaboradores/links/CI. | Pendente |
| GOV-02 — proteção da `main` | Política documental; required PR + check; review obrigatório | Avaliar ruleset exigindo PR e **Repository quality gate**, sem impor revisor externo que não existe. A integração não pôde ler a proteção clássica (403); validar com admin no GitHub. | Pendente |

**Nada foi modificado nas configurações do repositório.** Não inferir que o
quality gate está configurado como obrigatório apenas porque executa com sucesso.

## 5. Solicitações de aprovação a registrar quando o responsável decidir

Para cada decisão:

```text
ID: OQ-__ / GOV-__
Alternativa escolhida: __
Justificativa e limites: __
Responsável por aprovar: __
Data: __
Evidência do aceite: link para comentário/PR/registro autorizado
Artefatos impactados: PRD, contrato XLSX, ADR, backlog, testes, UX
Dependências/ação antes de implementar: __
```

**Sem preenchimento antecipado.** Respostas parciais podem aprovar
uma decisão específica e deixar outras pendentes. O Gate G0 permanece
**não aprovado** até o responsável emitir decisão separada, indicando
restrições e riscos residuais.

## 6. Critérios para iniciar F01 futuramente

A Fase 01 exige aceite humano do Gate G0 com baseline PRD e limites
aceitos. Após G0, iniciar F01-E01 para ratificar arquitetura e OQ-04,
seguida do scaffold compilável em F01-E02 e demais etapas do blueprint.

Não criar stack operacional, CI de compilação `dotnet` ou banco de
produção como consequência automática deste documento.
