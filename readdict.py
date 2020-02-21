import pickle

dictresult = {}
try:
    file = open('moviesdict', 'rb')
    dictresult = pickle.load(file)
    file.close()
except FileNotFoundError:
    disctresult = {}

meses = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December')
lista_anos = (2020, 2019)
# dictresult{'2020': [ { }, { }, { } ], '2019': [ { }, { }, { } ] }
# { } = {'Data_Lanc': x, 'Filme': y ....Genero, Tipo, Receita
for ano in lista_anos:
    print(ano)
    del dictresult[f'{ano}'][0]
    data_tmp = ''
    dictnovo = {f'{ano}': []}
    for c, x in enumerate(dictresult[f'{ano}']):
        # cada x é um dict { }
        deletar = 'N'
        if str(x['Filme']) == 'nan':
            deletar = 'S'
        elif str(x['Data_Lanc']) == 'nan':
            x['Data_Lanc'] = data_tmp
        elif x['Data_Lanc'].replace(',', '').split()[0] not in meses:
            x['Data_Lanc'] = 'TBD'
            data_tmp = 'TBD'
        elif (x['Filme'].replace(',', '').split()[0] in meses) and (x['Filme'].replace(',', '').split()[1] == str(ano)):
            deletar = 'S'
        else:
            data_tmp = x['Data_Lanc']
        if deletar == 'N':
            registro = {'Data_Lanc': x['Data_Lanc'], 'Mes': str(x['Data_Lanc']).replace(',', '').split()[0],
                        'Ano': ano, 'Filme': x['Filme'], 'Genero': x['Genero'], 'Tipo': x['Tipo'],
                        'Receita': x['Receita'].replace(',', '').replace('$', '')}
            dictnovo[f'{ano}'].append(registro)
        if deletar == 'S':
            x['Del'] = 'S'
        else:
            x['Del'] = 'N'

    print(ano)
    for c, x in enumerate(dictnovo[f'{ano}']):
        print(f'{c:5,} - {x["Data_Lanc"]:<12} - {x["Mes"]:<10} - {x["Ano"]:<4} - {x["Filme"]:<40} - '
              f'{x["Genero"]:<18} - {x["Tipo"]:<10} - {x["Receita"]:<15}')
