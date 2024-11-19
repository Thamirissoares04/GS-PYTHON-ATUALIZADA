aparelhos = ["Geladeira", "Ar Condicionado", "Máquina de Lavar", "Televisão", "Computador", "Lâmpadas"]
consumo_diario = [1.2, 3.5, 0.8, 0.5, 0.6, 0.3]  
energia_solar = 4.0  
energia_eolica = 2.0  

def consumo_total(consumo):
    return sum(consumo)


def sugestoes_economia(consumo, aparelhos):
    sugestoes = []
    for i in range(len(consumo)):
        if consumo[i] > 1.0:  
            sugestoes.append(f"Tente reduzir o uso do {aparelhos[i]}, pois consome {consumo[i]:.1f} kWh diariamente.")
    return sugestoes


def verifica_energia_renovavel(consumo_total, energia_solar, energia_eolica):
    energia_total = energia_solar + energia_eolica
    if energia_total >= consumo_total:
        return "A energia gerada por fontes renováveis cobre o consumo total da casa."
    else:
        return "A energia gerada por fontes renováveis não é suficiente para cobrir o consumo total. Considere aumentar a capacidade ou reduzir o consumo."


def salvar_dados(consumo_total, sugestoes, analise_renovavel):
    with open("dados_consumo.txt", "w") as file:
        file.write(f"Consumo total diário: {consumo_total:.1f} kWh\n\n")
        file.write("Sugestões para reduzir o consumo de energia:\n")
        for sugestao in sugestoes:
            file.write(f"- {sugestao}\n")
        file.write("\nAnálise de energia renovável:\n")
        file.write(analise_renovavel + "\n")


total_consumo_diario = consumo_total(consumo_diario)


sugestoes = sugestoes_economia(consumo_diario, aparelhos)
analise_renovavel = verifica_energia_renovavel(total_consumo_diario, energia_solar, energia_eolica)


print(f"Consumo total diário: {total_consumo_diario:.1f} kWh")
print("\nSugestões para reduzir o consumo de energia:")
for sugestao in sugestoes:
    print("-", sugestao)

print("\nAnálise de energia renovável:")
print(analise_renovavel)


salvar_dados(total_consumo_diario, sugestoes, analise_renovavel)
print("\nOs dados foram salvos no arquivo 'dados_consumo.txt'.")
