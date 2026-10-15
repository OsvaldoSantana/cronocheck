# CronoCheck — Registro de decisões e diretrizes, 15/10/2026

**Origem:** manifestação expressa do responsável pelo produto nesta conversa, após merge do PR #15.  
**Evidência operacional:** [issue #16](https://github.com/OsvaldoSantana/cronocheck/issues/16), criada para rastrear esta rodada.  
**Estado:** decisões expressas registradas abaixo; itens incompletos permanecem abertos.  
**Limites:** não houve aprovação do PRD v1.2, das ADR-001/002, da Fase 01, do Gate G0, de hospedagem, identidade, preço/SLA ou de configurações administrativas.

## OQ-03 — DIRETRIZ APROVADA: rejeitar limitação a FS simples

Manifestação do responsável pelo produto: **“Não deve ser nada simples, uma das
diretrizes que guia esse projeto é que ele deve ser robusto e escalável portanto
todos seus campos devem sempre atender a todos contextos e soluções.”**

Decisão rastreável:
1. **Rejeitar** OQ-03(a) (restringir o **domínio** do cronograma a relações FS simples).
2. Adotar como requisito de arquitetura um **modelo canônico extensível e sem
   perda de informações** de cronogramas profissionais. Prever representações
   explícitas para FS, SS, FF, SF; defasagens/antecipações com sinal, unidade
   e calendário; múltiplas predecessoras; marcos/duração zero; hierarquia/WBS;
   datas e horas, calendários e exceções, quando presentes no dado de origem.
3. Relações desconhecidas ou não interpretáveis devem ter o **valor de origem
   preservado, procedência, tipo de suporte e diagnóstico claro**. Nunca
   converter silenciosamente SS/FF/SF em FS, descartar lag ou “corrigir”
   calendário para dias corridos.
4. Os esquemas XLSX sintéticos existentes com `predecessors_fs` continuam
   sendo **apenas fixtures elementares compatíveis para testes de regressão**,
   não a representação canônica alvo nem teto de funcionalidades.

**Não foi decidido**: catálogo universal de softwares/formats, suporte efetivo a
todas as convenções existentes, as regras temporais exatas, conversão entre
calendários, precisão de timestamps, capacidade por volume, nem quais
interpretações estarão completas na primeira release. Isso requer especificação
e testes orientados a casos de negócio. Um modelo extensível não garante
que “todo contexto possível” seja entendido corretamente; a aplicação deverá
distinguir representação preservada de semântica suportada.

**Impacto no escopo:** a antiga alternativa FS-only do blueprint/PRD perde
autoridade como limite de **modelagem do domínio**. O PRD v1.2 precisa
de **emenda formal**, estimativa e aceite antes de fechar G0, sem declarar que
a ampliação foi automaticamente incorporada à baseline aprovada.

## OQ-06 — APROVADA

Sequenciar a **UI** de revisão/histórico após o motor de auditoria, sem remover
RF-08..RF-11 do MVP. Implementar a **infraestrutura transacional AuditEvent
em F03-E04**, conforme blueprint, antes das telas de revisão. Nenhuma versão
do cronograma ou resultado de regra poderá ser modificada silenciosamente
por uma decisão humana. Não constitui aprovação de detalhes de storage/DDL.

## OQ-07 — APROVADA

Incluir **CU-05 — visão/priorização multiprojeto** entre os cenários prioritários
do MVP, com autorização por projeto. O cenário continua **hipotético quanto ao
uso real** até entrevistas e testes; aprovação de prioridade não é
evidência de validação empírica.

## OQ-08 — APROVADA COM LIMITE DE ESCOPO

O perfil `Activities` da fixture sintética v0 pode utilizar datas civis ISO
em texto, dias corridos inclusivos e rejeição de fórmula em campo mapeado como
**convenção do conjunto de testes atual**. Não aprova essas convenções como
semântica universal de produção nem valida calendário profissional. As
múltiplas modalidades de dependência/duração devem ser atendidas pelo futuro
modelo canônico extensível (OQ-03).

## OQ-09 — APROVADA COM ESPECIFICAÇÃO PENDENTE

Identidade interna única por atividade e versão deve ser separada do
identificador bruto proveniente do cronograma. Preservar `SourceLocator`,
IDs duplicados, e vínculos ambíguos **sem selecionar correspondência
arbitrária**. Ainda é preciso escolher a política exata de case/Unicode,
espaços, identidades entre versões e concorrência antes de F04/F07.

## OQ-04 — NÃO DECIDIDA

O responsável solicitou explicação das alternativas de interface, identidade,
infraestrutura e hospedagem, com impactos. Nenhuma opção recebeu autorização
final nesta rodada; ver `architecture-options-oq04.md`.

## OQ-05 — NÃO DECIDIDA

O responsável solicitou contexto sobre RNF-03/04/08 e alternativas de metas
contratuais, metas provisórias e metas calibradas por ensaio. Nenhuma alternativa
foi aprovada nesta rodada; ver `performance-options-oq05.md`.

## Aprovações anteriores mantidas

- **OQ-01:** hipóteses de usuário permitidas para descoberta; entrevistas não realizadas.
- **OQ-02:** dados exclusivamente sintéticos para fixtures; nenhum uso de dados reais autorizado.

**Gate G0 = NÃO APROVADO. F01 = NÃO INICIADA. PRD v1.2 = NÃO APROVADO.**
