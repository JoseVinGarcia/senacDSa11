import pandas as pd
import os

# ATIVIDADE 1
os.system("cls")

filmes = {
    "nome do filme" : ["Alien: Romulus", "Transformers: One", "Sonic 2"],
    "ano de lançamento" : [2024, 2024, 2022],
    "genero" : ["ficção científica", "animação", "animação"]
}

df_filmes = pd.DataFrame(filmes)

print("DATA FRAME:")
print(df_filmes)

# filtrando por genero
print("\nFILTRANDO POR GENERO:")
print(df_filmes[df_filmes["genero"] == "animação"])

print("\n FILTRANDO POR INDICE 0:")
print(df_filmes.iloc[0])
