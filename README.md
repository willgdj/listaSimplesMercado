# Lista de Compras de Mercado (CLI)

Aplicação em **Python** para linha de comandos (CLI) que permite criar listas de compras de forma rápida, validar quantidades, somar itens repetidos automaticamente, visualizar um gráfico de barras diretamente no terminal e guardar o histórico num ficheiro `lista.txt`.

## Funcionalidades

* **Validação de entradas numéricas:** impede quantidades inválidas, letras ou valores menores ou iguais a zero.
* **Agrupamento de itens repetidos:** se o mesmo item for digitado mais de uma vez, as quantidades são somadas automaticamente.
* **Gráfico de barras no terminal:** exibe barras proporcionais com a quantidade de cada item sem depender de bibliotecas externas.
* **Exportação para `.txt`:** grava a lista com data e hora em `lista.txt` na Área de Trabalho (com suporte a pastas `Desktop` e `OneDrive\Desktop`).
* **Fluxo interativo:** permite consultar o gráfico, guardar, gerar uma nova lista ou sair.

## Tecnologias utilizadas

* **Python 3** (bibliotecas padrão: `os`, `pathlib`, `datetime`)
* **Git e GitHub** para controlo de versão

## Como executar

1. Clone ou descarregue este repositório para o seu computador:
   ```bash
   git clone git@github.com:willgdj/listaSimplesMercado.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd listaSimplesMercado
   ```
3. Execute o script Python:
   ```bash
   python lista_compras.py
   ```

## Exemplo de uso no terminal

```text
--- Gráfico de quantidade por item ---

Arroz     | ######### (3)
Feijao    | ###### (2)
Bananas   | ######################### (8)
```
