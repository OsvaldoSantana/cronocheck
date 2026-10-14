# Contribuição ao CronoCheck

## Estado e escopo
O projeto está na Fase 00 (descoberta). A baseline documental ainda requer revisão humana e o Gate G0 não está aprovado. Não antecipe funcionalidades ou decisões de arquitetura em PRs documentais.

## Processo
1. Crie uma issue ou vincule sua alteração a uma tarefa da EAP (`FNN-ENN`, `CRONO-NNN`).
2. Crie uma branch curta a partir da `main` (ex.: `docs/f00-product-charter`, `feat/import-validation`, `fix/schedule-parser`).
3. Separe mudanças por responsabilidade e use Conventional Commits (`docs:`, `feat:`, `fix:`, `test:`, `refactor:`, `chore:`, `ci:`).
4. Abra PR com objetivo, motivação, arquivos afetados, requisitos, riscos, evidências, validações e pendências.
5. Não marque como concluído o que não foi executado ou aprovado. Não faça merge sem revisão humana.

## Definition of Ready (DoR)
- Escopo e dependências claros; referência à EAP/requisito; critérios de aceite verificáveis.
- Dados de exemplo apropriados, sem conteúdo corporativo sensível; dúvidas bloqueantes identificadas.

## Definition of Done (DoD)
- Mudanças dentro do escopo e rastreáveis a requisitos e decisões.
- Testes pertinentes executados com resultados registrados (ou impedimentos declarados).
- Documentação, contratos, estados da interface e riscos atualizados quando aplicáveis.
- Revisão humana e verificações de CI realizadas quando disponíveis.
- Nenhuma credencial ou dado sigiloso no repositório.

## ADR e governança
Decisões de arquitetura com impacto significativo exigem ADR em `docs/architecture/adr/`. Propostas pendentes não são decisões aprovadas. Os arquivos de `docs/product/` e o `docs/CRONOCHECK_BLUEPRINT_V1.md` são documentos de planejamento sujeitos a validação.

## Segurança e privacidade
Repositório público: não envie arquivos reais de clientes/obras, CPF, documentos pessoais, credenciais, tokens, backups nem logs sensíveis. Use fixtures sintéticas e revisadas.
