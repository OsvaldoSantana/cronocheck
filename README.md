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

## Priorização e rastreabilidade (CRONO-004)

- [Matriz de prioridades MoSCoW](docs/product/requirements-prioritization.md): lançamento MVP, sequência técnica e metas de RNF provisórias são eixos distintos.
- [Registro de requisitos](docs/product/requirements-register.json): estrutura legível por máquinas para 11 RF e 10 RNF.
- [Matriz de rastreabilidade](docs/product/traceability-matrix.md): fases, cenários, critérios do PRD e fixtures sintéticas.
- [Validador documental](tests/documentation/validate_requirements.py): verificações de integridade das especificações, **não** testes da aplicação.
- [Issue CRONO-004](https://github.com/OsvaldoSantana/cronocheck/issues/6): pendências e aceite humano.

As prioridades são propostas para revisão; nenhum RF/RNF foi implementado ou homologado, o PRD permanece pendente e o Gate G0 ainda não foi aprovado.

## Experiência de usuário — CRONO-005

- [Fluxos de navegação e jornadas](docs/ux/flows.md) — FL-01..FL-05, sitemap, contexto de projeto, importação e revisão de achados.
- [Wireframes de baixa fidelidade](docs/ux/wireframes.md) — W-01..W-11, estados desktop/mobile e casos de erro.
- [Plano de revisão de usabilidade](docs/ux/usability-review.md) — tarefas UXT-01..10 **não executadas**.
- [Issue CRONO-005](https://github.com/OsvaldoSantana/cronocheck/issues/8) — escopo, revisão e decisões abertas.

Os diagramas e wireframes são documentação proposta, **não uma interface navegável**.
Testes com usuários, protótipos clicáveis, F02 e Gate G0 continuam pendentes.

## Arquitetura proposta — CRONO-006

- [ADR-001: monólito modular](docs/architecture/adr/ADR-001-modular-monolith.md) — alternativas, módulos, invariantes transacionais e critérios de verificação.
- [ADR-002: fronteira frontend/API](docs/architecture/adr/ADR-002-frontend-boundary.md) — React/TypeScript, comparação Vite/Next.js e segurança OIDC/BFF.
- [Contexto e contêineres C4 L1/L2](docs/architecture/context-and-containers.md) — fronteiras de confiança e responsabilidades.
- [Issue CRONO-006](https://github.com/OsvaldoSantana/cronocheck/issues/10) — revisão, evidências e próximos passos.

**Status:** ADRs propostas, sem aceite humano; OQ-04, Gate G0 e F01 permanecem pendentes.
