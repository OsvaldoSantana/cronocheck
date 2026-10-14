# CronoCheck

Plataforma em planejamento para auditoria e governança de cronogramas de obras e projetos, com regras determinísticas, evidências rastreáveis e revisão humana.

> **Estado:** Fase 00 — Descoberta, escopo e requisitos. Nenhuma funcionalidade foi implementada ou homologada. O Gate G0 ainda não foi aprovado.

## Documentação

- [`docs/CRONOCHECK_BLUEPRINT_V1.md`](docs/CRONOCHECK_BLUEPRINT_V1.md) — plano diretor e arquitetura proposta.
- [`docs/product/prd.md`](docs/product/prd.md) — requisitos e escopo do MVP (rascunho).
- [`docs/product/personas-jtbd.md`](docs/product/personas-jtbd.md) — personas e cenários hipotéticos.
- [`docs/product/open-questions.md`](docs/product/open-questions.md) — decisões pendentes.
- [`docs/product/f00-backlog.md`](docs/product/f00-backlog.md) — etapas e entregáveis da fase 00.
- [`docs/product/traceability-matrix.md`](docs/product/traceability-matrix.md) — requisitos, evidências e marcos.
- [`docs/PROJECT_STATE.md`](docs/PROJECT_STATE.md) — situação operacional do projeto.

## Colaboração

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de propor alterações. O conteúdo documental é preliminar e depende de revisão humana. Não envie cronogramas reais de clientes, credenciais nem outros dados sensíveis para este repositório público.

## Avanço da Fase 00

- [Registro de decisões da Fase 00](docs/product/decisions-2026-10-14.md): OQ-01 e OQ-02 aprovadas; outras pendentes.
- [Jornadas AS-IS / TO-BE](docs/product/journey-as-is-to-be.md): rascunho hipotético da F00-E02, ainda sem validação empírica ou aceite humano.
- A autorização para **dados sintéticos** não autoriza publicar arquivos reais de clientes; o PRD e o Gate G0 continuam pendentes de aprovação.

## Contrato XLSX v0 (Fase 00)

- [Contrato de importação v0](docs/product/xlsx-import-contract-v0.md) — proposta sintética a revisar, não parser implementado.
- [Catálogo de fixtures XLSX](tests/fixtures/README.md) — dez arquivos sintéticos e resultados esperados versionados.
- [Validação estrutural](tests/fixtures/validate_fixtures.py) — verificações OOXML e categorias de teste, independentes do futuro produto.
- **Pendente:** OQ-08 (calendário e semântica de duração, entre outras decisões), análise do PRD e Gate G0.

## Modelo conceitual de domínio (CRONO-003)

- [Glossário de domínio](docs/product/domain-glossary.md) — conceitos de Activity, Dependency, Calendar, Duration, ScheduleVersion, AuditRun e rastreabilidade.
- [Invariantes de domínio](docs/product/domain-invariants.md) — regras de integridade, separação entre importação e auditoria e cenários de teste propostos.
- [Issue CRONO-003](https://github.com/OsvaldoSantana/cronocheck/issues/4) — entregáveis, critérios de aceite e pendências.
- **Decisões abertas:** OQ-03 (precedências), OQ-08 (semântica temporal/XLSX) e OQ-09 (identidade interna e ambiguidade de IDs); **não** são regras de produção aprovadas.
