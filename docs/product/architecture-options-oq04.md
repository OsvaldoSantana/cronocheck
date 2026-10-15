# OQ-04 — Alternativas de stack, autenticação e hospedagem

**Status:** orientação técnica para decisão; **NENHUMA OPÇÃO APROVADA** em 15/10/2026.  
**Fontes internas:** [ADR-001](../architecture/adr/ADR-001-modular-monolith.md), [ADR-002](../architecture/adr/ADR-002-frontend-boundary.md), PRD, RF-01/RF-03/RF-08, RNF-06/09/10.  
**Contexto de produto:** SaaS privado de trabalho em projetos, com importação XLSX, auditoria determinística, filas/jobs, relatórios e papéis; não há requisito de SEO público medido.

## 1. A decisão é um conjunto, não uma tecnologia única

| Camada | Alternativas reais | Critério principal |
|---|---|---|
| Frontend | **React + TypeScript + Vite (SPA)**; **React + Next.js (SSR/BFF)**; Razor/Blazor como mudança maior do blueprint | Complexidade de autenticação, necessidade de servidor de UI, operação e UX |
| Backend | **ASP.NET Core .NET 10 monólito modular** (ADR-001 proposta), vários serviços (não recomendados sem evidência) | AuditEvent transacional, consistência, custo de implantação/observabilidade |
| Banco | **PostgreSQL gerenciado**; **PostgreSQL autogerido**; solução relacional alternativa mediante ADR | Operações, backups, migração, recuperação e isolamento por projeto |
| Identidade | **OIDC com Code + PKCE na SPA**; **BFF com cookie seguro/servidor**; provedor gerenciado ou auto-hospedado | Segurança de sessão, CSRF/XSS, administração de usuários e custos |
| Hospedagem | PaaS com web+API+worker+PostgreSQL/storage; containers orquestrados; VM gerenciada manualmente | Durabilidade de jobs, storage privado, logs, observabilidade e esforço de operação |
| Arquivos | Armazenamento de objeto privado com hashes; disco local ligado a uma máquina | Portabilidade e escalabilidade; não expor XLSX a URL pública |

Nenhuma das categorias deve ser decidida isoladamente: por exemplo,
Next.js permite BFF, mas **não o obriga**; Vite SPA pode conversar com
uma API de sessões seguras/BFF própria, com mais desenho. O provedor de
identidade não determina sozinho o runtime da API.

## 2. Comparação de frontend

| Critério | React/Vite SPA | React/Next.js com BFF | Razor/Blazor |
|---|---|---|---|
| Painéis e wizard interativos | Ótimo ajuste | Ótimo ajuste | Viável, mas difere do blueprint |
| SEO/renderização pública | Sem SSR automático; pouco relevante para app privada | SSR/SEO opcionais | Server rendering disponível |
| Autenticação | Requer escolher SPA PKCE ou API de sessão; cuidar do browser | BFF torna simples manter tokens no servidor; exige proteção CSRF | Pode centralizar sessão no servidor |
| Hosting/operabilidade | Web estática + API separada; menos runtime web | Processo Next + processo API; mais camadas e diagnósticos | Possível simplificar stacks, porém refatoração maior |
| Escalabilidade | CDN para estáticos; API escala separadamente | Escala SSR/BFF e API conforme carga | Depende da modalidade de hospedagem |
| Testes e evolução | Vitest/Playwright + OpenAPI | Semelhante, incluindo BFF/SSR | Ferramentas .NET e UI correspondentes |
| Recomendação contextual | **Base preferida**, sem necessidade comprovada de SSR/BFF | Preferir se a política de identidade exigir BFF ou dados SSR | Só mediante mudança expressa de arquitetura |

Um frontend Vite não é “menos escalável”: normalmente o gargalo desse produto
será parsing/auditoria, SQL e jobs, não o HTML estático. A comparação aqui
não é benchmark nem garantia de capacidade futura.

## 3. Identidade: SPA com PKCE ou BFF?

| | OIDC Code + PKCE (SPA como cliente público) | BFF (servidor com sessão/cookie) |
|---|---|---|
| Tokens de acesso | Em contexto do browser, conforme SDK/política; riscos de exposição por XSS | No servidor; browser recebe cookie de sessão |
| Riscos centrais | XSS, persistência insegura, expiração e renovação de sessão | CSRF, cookies, estado de sessão, escala/alta disponibilidade do BFF |
| Complexidade inicial | Menos componentes de servidor, mas fluxos OIDC e CORS exigem rigor | Componente de sessão e proxy; operação adicional |
| Proteção obrigatória | PKCE, CSP, rotas seguras, logout/renovação corretos, sem credenciais em localStorage por padrão | Cookies HttpOnly/Secure/SameSite, CSRF token/Origin, CSP, sessão e logout |
| Recomendação | Viável se políticas e testes de segurança forem bem tratados | **Preferência prudente para sistema corporativo com dados sensíveis**, caso haja operação suportável |

**BFF não significa necessariamente Next.js** e não torna a aplicação imune a
XSS/CSRF. Não afirmar que tokens em memória são automaticamente seguros ou
que um cookie HttpOnly basta sem proteção CSRF.

## 4. Hospedagem, banco e jobs

### A — Plataforma gerenciada (recomendação inicial)

Web estática/CDN + API ASP.NET Core + executor de jobs duráveis + PostgreSQL gerenciado +
object storage privado. Benefícios: menos esforço de manutenção, backups gerenciáveis,
escalabilidade incremental e logs centralizados. Custos: mensalidade,
limites de serviços, dependência operacional de fornecedor. **Verificar capacidade
de jobs de longa duração, networking privado, backups e restore antes de escolher.**

### B — Containers em cluster/orquestrador

Mais controle de runtime, autoscaling e deploy complexo. Exige políticas
de rede, segredos, migração/rollback, observabilidade, operadores e segurança
de cluster. Justificável após métricas/carga reais; não assumir vantagem
econômica imediata.

### C — VM única/servidor autogerenciado

Possivelmente menor custo direto para protótipos, porém manutenção de OS,
backups/restore, failover, jobs e storage ficam com o time. Mais risco
operacional na produção sem equipe de infraestrutura.

### Banco e storage

- **PostgreSQL gerenciado** é a proposta inicial. PostgreSQL autogerido é
  tecnicamente válido, mas exige backup, restore e atualização pelo mantenedor.
- Arquivos XLSX originais devem ficar em **object storage privado**
  com hash e verificação de permissão; não confiar em diretório efêmero do
  serviço web.
- Estado dos jobs, retries/idempotência e filas devem ser persistentes.
  O processo concreto de worker depende da ADR-006, ainda não aceita.

## 5. Recomendações condicionais para decisão

1. **Backend:** manter a proposta de monólito modular ASP.NET Core .NET 10 e
   PostgreSQL, submetidos a ADR/benchmark, por reduzir complexidade distribuída.
2. **Frontend:** iniciar com React + TypeScript/Vite se a necessidade for
   aplicação privada e interativa sem SEO/SSR. Escolher Next.js quando houver
   necessidade concreta de BFF integrado, SSR ou regras corporativas de sessão.
3. **Autenticação:** comparar OIDC SPA PKCE com BFF com preferência por sessão
   segura no servidor quando houver dados sensíveis de obras/clientes.
4. **Hospedagem:** preferir plataforma gerenciada com PostgreSQL e storage
   privados, jobs duráveis e restauração verificável; provedor e região
   ainda requerem requisitos e orçamento.
5. **Critérios para assinatura:** custos mensal/por uso, limites de
   upload, concorrência, localização/retensão dos dados, privacidade,
   RPO/RTO, prova de backup/restore, logs e migração de fornecedor.

**Questões ainda não respondidas pelo responsável:** haverá clientes externos
com requisitos de residência dos dados? Quantos usuários/obras simultâneos?
O deployment precisa ser gratuito no desenvolvimento? Qual orçamento
operacional mensal e nível de suporte? Existe exigência de usar fornecedor
específico ou conta corporativa já contratada?

**A decisão registrada em OQ-04 permanece: PENDENTE.**
