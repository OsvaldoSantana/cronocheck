# Fixtures sintéticas para o contrato de importação XLSX v0

**Fase:** F00-E04 / **ticket:** CRONO-002.  
**Status:** dados de teste criados; sem parser ou motor de auditoria implementados.  
**Referência:** `docs/product/xlsx-import-contract-v0.md` (proposta sujeita a OQ-03/OQ-08).  
**Resultados esperados:** `expected-results.json`.

Todos os arquivos são **inteiramente sintéticos**. Não contêm cronogramas de clientes, dados reais de
obras ou pessoas. Os exemplos usam uma aba `Activities`, cabeçalho na linha 1, datas civis ISO
(`YYYY-MM-DD`) como texto e duração em dias corridos inclusivos **apenas como hipótese da v0**.

| Arquivo | Atividades | Objetivo | Saída esperada proposta |
|---|---:|---|---|
| `basic-valid.xlsx` | 4 | Caminho de referência sem erros estruturais | Importável, zero achados estruturais |
| `duplicate-ids.xlsx` | 3 | Mesmo ID em duas linhas distintas | Importável; grupo de ID duplicado |
| `missing-predecessor.xlsx` | 2 | Predecessora `P999` inexistente | Importável; referência ausente |
| `dependency-cycle.xlsx` | 3 | Ciclo entre C001/C002/C003 | Importável; ciclo de precedências |
| `invalid-dates.xlsx` | 2 | Data civil impossível `2026-02-30` | Rejeição na prévia, sem versão |
| `inconsistent-dates.xlsx` | 2 | Fim anterior ao início | Importável; achado de cronologia |
| `formula-cells.xlsx` | 2 | Fórmula inocente `2+2` na célula B2 | Rejeição na prévia, sem execução |
| `large-5000-activities.xlsx` | 5.000 | Volume representativo de RNF-04 | Importável; **não comprova** meta de 60s |
| `multi-version-v1.xlsx` | 3 | Versão de origem para comparação | Importável |
| `multi-version-v2.xlsx` | 3 | Adição/remoção/modificação controlada | Importável; diff M004+/M002-/M003~ |

## Uso e validação

- O catálogo é **proposto**, não é resultado observado de um parser CronoCheck.
- As duas rejeições pertencem à importação; duplicatas, ciclos, referências ausentes e
  cronologia reversa são candidatos a **achados de auditoria após importação**.
- O resultado estrutural esperado define o **conjunto de categorias testadas**;
  novas regras temporais podem gerar achados adicionais, sempre por versão de regra.
- Não abrir/avaliar fórmulas automaticamente; a fórmula do caso de teste é `=2+2` e existe
  apenas para exercitar a rejeição da presença de fórmula em campo mapeado.
- O arquivo de 5.000 atividades ocupa mais espaço por usar entrada ZIP sem compressão
  (método `store`) para reprodutibilidade e portabilidade dos artefatos.
- A fixture `cross-project-permission` depende de autenticação e recursos implementados (F03).
- Casos de XLSX malicioso e de ZIP bomb devem ser criados apenas em laboratório controlado,
  após modelagem de ameaças; **não** são distribuídos no repositório público.

## Verificação estrutural dos arquivos

O script `validate_fixtures.py` usa somente a biblioteca padrão de Python
(`zipfile`, `xml.etree.ElementTree`) para verificar pacotes OOXML, cabeçalho, número de
linhas, semântica sintética e `expected-results.json`.

```bash
python tests/fixtures/validate_fixtures.py
```

Esta verificação **não** substitui testes do importador real nem prova comportamento
do Excel/MS Project. Uma vez implementado o motor, os testes de integração devem consumir
o mesmo JSON e comparar resultados efetivamente calculados.
