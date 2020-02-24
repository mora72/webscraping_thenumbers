import pickle
try:
    file = open('moviesdictclean', 'rb')
    dictnovo = pickle.load(file)
    file.close()
except FileNotFoundError:
    dictnovo = {}

for ano, filmes in dictnovo.items():
    for c, x in enumerate(filmes):
        if int(x['Receita']) > 2000000000:
            print(f'{c:5,} - {x["Data_Lanc"]:<12} - {x["Mes"]:<10} - {x["Ano"]:<4} - {x["Filme"]:<40} - '
                  f'{x["Genero"]:<18} - {x["Tipo"]:<10} - {x["Receita"]:<15}')

for ano, filmes in dictnovo.items():
    print(ano, len(filmes))
