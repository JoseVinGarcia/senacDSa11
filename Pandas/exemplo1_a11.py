import pandas as pd
import os

# EXEMPLO 1 - LISTAS
os.system("cls")

dados = {
    "cargos" : ["assistente", "auxiliar", "gerente", "auxiliar"],
    "salario" : [2500, 1800, 6000, 1700],
}

df = pd.DataFrame(dados)
print(df)
# print(f"{type(df)}\n")

# EXEMPLO 2 - SERIES

# serie_cargos = pd.Series(df["cargos"])

# print(serie_cargos)
# print(f"{type(serie_cargos)}\n")

# EXEMPLO 3 - Ver o intervalo dos valores
# print(serie_cargos.index)

# EXEMPLO 4 - Ver os valores do intervalo
# print(serie_cargos.values)

# EXEMPLO 5 - Acesso pelo indice numerico
# iloc - acessa pela posição

# print("\n", df)
# serie_linha = df.iloc[1]
# print(serie_linha)

# EXEMPLO 6 - ACESSANDO INDICE PELO ROTULO TEXTUAL

# ABORDAGEM 1
# serie_colunas = df.loc[:,"cargos"]
# print(serie_colunas)

# ABORDAGEM 2 - CRIANDO INDICES TEXTUAIS (trocando os numericos pelos textuais)
# df.index = ["a", "b", "c", "d"]
# series_colunas = df.loc["a"]
# print("\n", series_colunas)

# EXEMPLO 7 - ACESSANDO VALORES INDIVIDUAIS
# df_cargos = df.iloc[1]["cargos"]
# print("\n", df_cargos)

# EXEMPLO 8
# iloc para localizar por indices
# print("\n", serie_cargos.iloc[0])

#por posicao na serie
# print(serie_cargos[serie_cargos.index[0]])

#posicao no dataframe
# print(df.iloc[0])

# EXEMPLO 9 - FILTRANDO
print("\n", df[df["cargos"] == "auxiliar"])

salarios = df.loc[df["cargos"] == "auxiliar", "salario"].values[0]
print("\n", salarios)
