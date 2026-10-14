# CronoCheck — Governança Git/GitHub (CRONO-007)

**Data:** 2026-10-14 • **Estado:** política proposta, em revisão humana.  
**Issue:** [CRONO-007](https://github.com/OsvaldoSantana/cronocheck/issues/12).  
**Fonte:** blueprint C.4, F01-E04, seção L e checklist de gates; CONTRIBUTING; PRD e estado do projeto.  
**Gate G0:** não aprovado; **F01:** não iniciada; **produto:** não implementado.

## 1. Estado factual constatado

| Item | Evidência/estado |
|---|---|
| GitHub | `OsvaldoSantana/cronocheck`, branch padrão `main` |
| Visibilidade | **Público**; não foi alterada nesta entrega |
| Rulesets | `GET /repos/OsvaldoSantana/cronocheck/rulesets` retornou lista vazia em 14/10/2026 |
| Proteção clássica da `main` | **Não verificável**: consulta retornou 403 “Resource not accessible by integration”; não concluir que está desprotegida |
| Templates | Issues (defeito, funcionalidade, tarefa), PR e `CODEOWNERS` nesta branch |
| CI de qualidade | Novo check único para **todos os PRs** (valida documentos e fixtures); não substitui builds/testes futuros |
| Revisões | Aprovação de PRD/ADR/gate requer registro separado; publicar/merge não concede aceite automaticamente |

O blueprint menciona criar repositório **privado**, mas este projeto já existe
como **público**. A decisão de mudar a visibilidade está aberta (GOV-01);
nenhuma migração, exclusão ou alteração de permissão foi executada.

## 2. Branches e alterações

- `main`: branch principal de integração; não desenvolver novas funcionalidades diretamente nela.
- `docs/<tema>`: documentação; `feat/<tema>`: nova função; `fix/<tema>`: correção;
  `test/<tema>`: testes; `chore/<tema>`: manutenção; `ci/<tema>`: pipelines.
- Associar cada branch/PR a issue e etapa EAP (`CRONO-xxx` ou `FNN-ENN`).
- Preferir mudanças pequenas, revisáveis e com retorno simples; não misturar
  refatoração transversal, arquitetura e feature sem justificativa.
- Commits no padrão Conventional Commits, escopo opcional.
- Sincronizar documentação de decisão e rastreabilidade; `docs/PROJECT_STATE.md`
  deve registrar o estado efetivo de integração, não um estado futuro presumido.
- Fechar issues só após critérios satisfeitos e evidências verificáveis.
- Escolher merge/squash/rebase explicitamente no PR; não reescrever histórico
  público da `main` sem plano formal.

## 3. Revisão e evidências

Cada PR utiliza `.github/PULL_REQUEST_TEMPLATE.md`, descrevendo problema,
escopo, requisitos/decisões, verificações **realmente realizadas**, riscos,
artefatos e rollback se aplicável. Não marcar ADR pendente como `Accepted` por
abrir/mesclar PR. `CODEOWNERS` identifica o proprietário do código, mas **não**
é, sozinho, uma política de aprovações obrigatórias.

**Repositório de mantenedor único:** o autor não pode aprovar o próprio PR como
revisor independente. Portanto, exigir 1 aprovação alheia ou aprovação
obrigatória de CODEOWNERS sem segundo revisor efetivo pode bloquear o
desenvolvimento. Usar revisão técnica própria documentada **não é equivalente**
a revisão independente. Considere adicionar colaborador revisor antes de
ativar enforcement de aprovações externas.

## 4. Verificações automáticas

**`.github/workflows/repository-quality-gate.yml`** executa em **todo PR**
(não apenas quando alguns caminhos são alterados), em push à `main` e sob
demanda. Roda os validadores já existentes:

- `tests/documentation/validate_requirements.py`
- `tests/documentation/validate_ux_flows.py`
- `tests/documentation/validate_architecture.py`
- `tests/fixtures/validate_fixtures.py`
- `tests/documentation/validate_governance.py`

Ele usa apenas Python da imagem GitHub Actions, sem segredos, em evento
`pull_request` (não `pull_request_target`), com permissão `contents: read`.
O nome do check a selecionar como obrigatório, **após execução verificada**,
é o job “Repository quality gate / Documentation and synthetic XLSX” ou
o nome equivalente exibido pelo GitHub. Não configurar checks com filtro de
caminho como obrigatórios sem garantir que sejam executados em todo PR.

Essa suíte valida **a documentação e as fixtures**, não o software CronoCheck.
Ao iniciar F01, ampliar gates com `dotnet build/test`, analyzers, scan de
dependências, frontend lint/test/build e contratos OpenAPI; não deixar o
check documental como único gate de código.

## 5. Configuração de rulesets sugerida (NÃO APLICADA)

Somente após GOV-02 aprovado e verificação das opções disponíveis na conta:

1. Abrir **Settings → Rules → Rulesets**, criar ruleset para o branch padrão `main`.
2. Exigir PR antes da integração e bloquear force-push/deleção, considerando
   recuperação e administradores explicitamente.
3. Exigir check unificado que rode em **todos os PRs**, selecionando pelo
   nome real após o primeiro CI verde.
4. Definir política de reviews para mantenedor único: inicialmente **não**
   exigir aprovação externa indisponível; quando houver revisor independente,
   decidir número de aprovações e CODEOWNERS.
5. Avaliar regras para squash/merge, branch up-to-date, resolução de comentários
   e bypass administrativo. Ativar apenas depois de validar que PRs normais
   continuam integráveis.
6. Testar com PR de controle e registrar evidências. Configurações podem
   variar por plano, repositório e nível de permissão.

**Não afirmar que a `main` está protegida antes de consultar a configuração
efetiva e comprovar o comportamento em PR.** Esta entrega apenas documenta.

## 6. Segurança, confidencialidade e visibilidade

- `SECURITY.md` define divulgação responsável; não usar Issues públicas
  para vulnerabilidades sensíveis.
- `.gitignore` exclui padrões comuns, mas **não** substitui secret scanning
  nem revisão de diff/histórico. Evitar dados corporativos reais no Git.
- CRONO-002 usa somente fixtures sintéticas autorizadas (OQ-02).
- `CODEOWNERS` não substitui RBAC e permissões por projeto da aplicação.
- Se a opção GOV-01 for **privado**, confirmar previamente implicações de
  acesso de colaboradores, links públicos, Actions e eventuais integrações.
  Fazer alteração de visibilidade **somente após autorização explícita**.

## 7. Registro de decisões de governança pendentes

| ID | Decisão | Alternativas | Recomendação inicial | Estado |
|---|---|---|---|---|
| GOV-01 | Visibilidade do repositório | Manter público / tornar privado | Manter como está enquanto se decide o acesso; nenhuma mudança tácita | **Pendente** |
| GOV-02 | Enforcement em `main` | Apenas política documental / ruleset exigindo PR + CI / revisores externos | Preparar check único e escolher enforcement após testar; evitar bloqueio de mantenedor único | **Pendente** |

**Não acrescentar essas decisões como OQ-10/11 do produto sem deliberação**;
são decisões administrativas de repositório, separadas das OQ-03..09.

## 8. Critérios de aceite CRONO-007

- [x] Templates para bug, funcionalidade, tarefa, PR e CODEOWNERS escritos.
- [x] CONTRIBUTING e SECURITY com política de dados sintéticos e segredos.
- [x] Proposta de rulesets e privacidade documentada sem alterar configurações.
- [ ] Validação documental CI aprovada e evidência do run registrada.
- [ ] Revisão humana de termos, permissões e decisões GOV-01/GOV-02.
- [ ] Policies efetivas de ruleset aplicadas (se autorizadas) e comportamento testado.
- [ ] Gate G0 formalmente aprovado (atividade separada; não é pré-requisito para publicar esta proposta).

A publicação e o merge dos arquivos **não aprovam** GOV-01/GOV-02, ADRs,
Fase 01, ou Gate G0.
