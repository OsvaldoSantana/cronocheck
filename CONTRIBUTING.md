# Contribuição ao CronoCheck

O CronoCheck está na **Fase 00**. Nenhuma funcionalidade da aplicação foi implementada,
o PRD e as ADRs permanecem em revisão e o **Gate G0 não está aprovado**. Issues,
commits, PRs ou um merge **não** substituem aceite de produto, arquitetura ou gate.

## Antes de começar

Consulte o [blueprint](docs/CRONOCHECK_BLUEPRINT_V1.md),
[o estado do projeto](docs/PROJECT_STATE.md),
[a política de governança](docs/engineering/repository-governance.md)
e o [registro de decisões](docs/product/open-questions.md).

O repositório é **público**. Não envie cronogramas reais de clientes,
informações pessoais, credenciais, `.env`, backups nem relatórios confidenciais.
Use fixtures sintéticas. Suspeitas de vulnerabilidades seguem
[SECURITY.md](SECURITY.md), **não** issues públicas.

## Processo de trabalho e Git

1. Abra ou vincule uma issue existente; identifique `CRONO-xxx`, `FNN-ENN`,
   RF/RNF, CU e OQ/ADR afetadas. Não reutilize IDs existentes.
2. Crie branch curta a partir da `main`: `docs/`, `feat/`, `fix/`,
   `test/`, `ci/` ou `chore/` e um nome explicativo.
3. Faça commits pequenos no padrão Conventional Commits:
   `feat:`, `fix:`, `docs:`, `test:`, `ci:`, `refactor:`, `chore:`.
4. Abra PR com o template padrão. Documente o que realmente mudou,
   verificações executadas, limitações, riscos e evidências.
5. Verifique **Repository quality gate** no PR. Por ora valida documentação e
   fixtures XLSX, **não código C#/React**. Testes de aplicação serão
   obrigatórios quando forem implementados na Fase 01.
6. Faça revisão humana e registre aprovação **separada** de decisões OQ/ADR/PRD
   ou gates. Nunca declarar sucesso sem resultado de CI/ação correspondente.
7. Integre por merge somente com autorização e checks adequados. A visibilidade
   e proteções da `main` não devem ser alteradas sem a decisão GOV-01/GOV-02.

## Definition of Ready (DoR)

- Objetivo, contexto, dependências e não-objetivos claros.
- Etapa/issue e requisitos referenciados, com critérios verificáveis.
- Dados de teste apropriados e não confidenciais.
- Decisões bloqueantes identificadas, sem preencher lacunas silenciosamente.

## Definition of Done (DoD)

- Mudança rastreável e revisável; testes adequados **realmente executados**.
- Documentação, contratos, matriz e estado do projeto atualizados quando aplicável.
- CI pertinente com resultado registrado; falhas investigadas, não ignoradas.
- Segurança, autorização, auditabilidade e imutabilidade revisadas conforme impacto.
- Nenhum dado sigiloso no diff ou no histórico.
- Revisão humana/aceite de artefatos registrados conforme a fase.

## Arquitetura e revisão

ADRs vivem em `docs/architecture/adr/`. O estado `Proposto` significa que
a alternativa ainda **não foi adotada formalmente**. CODEOWNERS fornece
orientação de responsabilidade, mas não é aprovação independente automática.
Em projeto de mantenedor único, não ativar regra que exige revisão por outra
pessoa sem primeiro garantir um revisor disponível.

Proteção de branch e visibilidade estão documentadas como propostas
em `docs/engineering/repository-governance.md`; regras efetivas precisam de
verificação no GitHub e aprovação administrativa.
