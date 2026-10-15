# Política de segurança — CronoCheck

**Estado do produto:** Fase 00, sem software publicado nem release estável.
O repositório é **público** na data desta política. Consulte `docs/PROJECT_STATE.md`
para a situação operacional e as decisões pendentes.

## Divulgação responsável

Não publique detalhes de vulnerabilidades exploráveis em Issues, Pull Requests,
Discussions, comentários ou anexos públicos.

1. Se o repositório oferecer **GitHub Private Vulnerability Reporting**, use
   **Security → Report a vulnerability** para encaminhar o relatório privadamente.
2. Se esse recurso **não estiver habilitado**, procure o mantenedor por um canal
   privado já acordado. Solicite um canal seguro de reporte **sem publicar o
   exploit ou dados sensíveis no GitHub**.
3. Forneça no canal privado descrição, contexto, impacto, passos mínimos de
   reprodução e evidências sanitizadas, sem incluir dados reais de clientes.

Esta política **não afirma** que o recurso de reporte privado esteja habilitado,
nem estabelece SLA de resposta que não foi acordado.

## Regras de dados e credenciais

- Nunca publicar planilhas reais de obras/clientes, informações pessoais, chaves
  de API, `.env`, tokens, senhas, backups, certificados privados ou logs sigilosos.
- Usar **fixtures integralmente sintéticas** conforme OQ-02 e contrato de XLSX v0;
  dados reais anonimizados exigem autorização específica.
- Tratar todo XLSX como entrada não confiável: não executar macros, fórmulas,
  links ou conteúdo ativo. Limites de arquivo, decompressão e acessos serão
  definidos/validados quando o importador existir.
- No futuro, aplicar autorização por projeto no backend, redigir logs sem dados
  sensíveis, proteger storage e testar exportações CSV/PDF contra vazamentos.
- Se uma credencial for publicada, revogá-la/rotacioná-la imediatamente. Remover
  um commit do branch não torna um segredo seguro novamente.

## Atualizações e responsabilidades

O responsável pelo repositório decide mitigação, divulgação e versionamento
após receber o relatório. A criação de uma issue de segurança pública não é
um canal adequado para vulnerabilidades não corrigidas.

Nenhum teste de segurança da aplicação foi executado; a política é preparatória
e não equivale a certificação de segurança.
