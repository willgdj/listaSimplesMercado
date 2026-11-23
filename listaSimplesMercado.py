from datetime import datetime
import os
from pathlib import Path

import matplotlib.pyplot as plt


def obter_caminho_area_de_trabalho(nome_arquivo="lista.txt"):
    home = Path.home()
    for pasta in (home / "OneDrive" / "Desktop", home / "Desktop"):
        if pasta.exists():
            return pasta / nome_arquivo
    return home / "Desktop" / nome_arquivo


CAMINHO_ARQUIVO = obter_caminho_area_de_trabalho("lista.txt")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_inteiro_positivo(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if valor > 0:
                return valor
            print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros (ex: 3).")


def exibir_grafico(lista_mercado):
    if not lista_mercado:
        print("\nNenhum item na lista para gerar o gráfico.")
        return

    itens = list(lista_mercado.keys())
    quantidades = list(lista_mercado.values())

    plt.figure(figsize=(8, 4.5))
    barras = plt.bar(itens, quantidades, color="#2b7bba")
    plt.title("Quantidade de itens na lista de compras")
    plt.xlabel("Item")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=25, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    # Exibe o valor exato acima de cada barra
    for barra in barras:
        altura = barra.get_height()
        plt.annotate(
            f"{int(altura)}",
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

    plt.tight_layout()
    plt.show()


def mostrar_resumo_e_menu(lista_mercado):
    while True:
        limpar_tela()
        print("Lista gerada com sucesso! Confira ela abaixo:\n")
        for item, quantidade in lista_mercado.items():
            print(f"Item: {item} -> Quantidade: {quantidade}")

        print(f"\nTotal de unidades: {sum(lista_mercado.values())}")

        escolha = input(
            "\n[1] -> Salvar lista na Área de Trabalho\n"
            "[2] -> Exibir gráfico (matplotlib)\n"
            "[0] -> Sair\n"
            "[Qualquer outro botão] -> Gerar nova lista\n"
            "Escolha: "
        ).strip()

        if escolha == "1":
            CAMINHO_ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
            carimbo = datetime.now().strftime("%Y-%m-%d %H:%M")
            with open(CAMINHO_ARQUIVO, "a", encoding="utf-8") as arquivo:
                arquivo.write(f"\n--- Lista ({carimbo}) ---\n")
                for item, quantidade in lista_mercado.items():
                    arquivo.write(f"Item: {item} -> Quantidade: {quantidade}\n")

            print(f"\nLista salva com sucesso em:\n{CAMINHO_ARQUIVO}\n")
            return "sair"

        if escolha == "2":
            exibir_grafico(lista_mercado)
            input("\nPressione Enter para voltar ao menu...")

        elif escolha == "0":
            return "sair"

        else:
            return "nova_lista"


def main():
    while True:
        limpar_tela()
        print(" Lista de compras de mercado ".center(45, "="))

        qnt_itens = ler_inteiro_positivo(
            "\nDigite a quantidade de itens que deseja inserir na sua lista: "
        )
        lista_mercado = {}

        for i in range(qnt_itens):
            while True:
                nome_item = input(f"\nDigite o nome do {i + 1}º item: ").strip().capitalize()
                if nome_item:
                    break
                print("O nome do item não pode ficar vazio.")

            qnt_item = ler_inteiro_positivo(
                f"Digite a quantidade de {nome_item.lower()} (apenas números): "
            )

            lista_mercado[nome_item] = lista_mercado.get(nome_item, 0) + qnt_item

        acao = mostrar_resumo_e_menu(lista_mercado)
        if acao == "sair":
            break

    print(" Obrigado por usar o programa! ".center(47, "="))


if __name__ == "__main__":
    main()