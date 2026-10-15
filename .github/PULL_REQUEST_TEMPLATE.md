## Objetivo e rastreabilidade

- **Issue:** #
- **EAP / CRONO:** 
- **RF/RNF/CU:** 
- **ADR/OQ relacionadas (estado aprovado ou pendente):**

Descreva o problema, a mudança e o motivo. Mudanças na arquitetura e em requisitos precisam de registro de decisão; **merge não equivale a aprovação de ADR, PRD ou Gate**.

## Escopo da mudança

**Arquivos / módulos / comportamento alterado:**  

**Fora de escopo:**  

**Riscos e possíveis regressões:**  

## Evidências e testes

| Verificação | Comando / link para run | Resultado real | Limitações |
|---|---|---|---|
| Checks automatizados relevantes | | Não executado | |
| Teste manual, se aplicável | | Não executado | |
| Testes de segurança/autorização, se aplicável | | Não executado | |

Não marcar como “passou” o que não foi executado. Testes documentais/fixtures não comprovam funcionamento de código da aplicação.

## Checklist de engenharia e segurança

- [ ] Escopo vinculado à issue e aos requisitos/etapa.
- [ ] Atualizei documentos, matriz e estado quando necessário.
- [ ] Registrei decisões e dúvidas sem converter proposta em aprovação.
- [ ] Confirmei que **não há** dados reais de clientes, pessoais, credenciais, tokens ou arquivos confidenciais.
- [ ] Mudanças de permissões, importações e exportações têm análise de autorização no backend, quando aplicável.
- [ ] Preservei imutabilidade, origem, evidências e trilha de auditoria, quando aplicável.
- [ ] Listei testes efetivamente executados e limitações.
- [ ] O resultado está pronto para revisão humana; **merge será decisão explícita**.

## Revisão, deploy e gate

- **Reviewer(s):** a designar.
- **Status da issue:** 
- **Gate G0/G1 (quando aplicável):** não aprovado, salvo registro específico.
- **Passos de rollback (se houver execução em produção):** não aplicável nesta Fase 00.
