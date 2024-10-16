import pandas as pd

# EXEMPLO 2 - CARREGANDO CSV
try:
    df = pd.read_csv("ClassicDisco.csv", sep=",", encoding="utf-8")
    
    print(df) # Não mostra tudo
    print(df.to_string()) # Mostra tudo
    print(df.head()) # Mostra as primeiras (por padrao 5)
    print(df.tail()) # e ultimas (por padrao 5)
    print(df.info()) # exibe informações
    print(df.describe()) # descreve os dados presentes
    pd.set_option("display.min_rows",20) # imprimindo o numero minimo de linhas
    # pd.set_option("display.min_columns",20) # imprimindo o numero minimo de colunas
    
    # LENDO UMA COLUNA ESPECIFICA
    artistas = df["Track"]
    print(artistas)

    # FILTRANDO OS MAIS POPULARES
    populares = df[df["Popularity"] > 20] # cria um dataframe a partir do dataframe com uma condicao especifica
    print(populares)

    # IMPRIMINDO APENAS COLUNAS
    print(populares[["Track", "Popularity"]]) #passa o campo dentro de uma lista

    # FILTRANDO POR ALBUM
    mj = df[df["Artist"] == "Michael Jackson"]
    print(mj[["Album", "Artist"]])

    # SALVANDO UM CSV
    df.to_csv("ClassicDisco_Modificado.csv", index=False, sep=",", encoding="utf-8")

    # SALVANDO UM EXCEL (Precisa do openpyxl)
    df.to_excel("ClassicDisco_Excel.xls", index=False, engine="openpyxl")

except Exception as e:
    print(f"Erro {e}")
    exit()
