import dsd

# Definição dos parâmetros de busca
Classe = "ADI"
NumeroInicial = 5000
NumeroFinal = 5500
diretorio_para_gravacao = 'ADIhtml'

# Iteração para gerar os urls
for n in range (NumeroFinal-NumeroInicial+1):
    
    # Definição do url a ser buscado
    NumProcesso = str(NumeroFinal-n)
    url = ('http://www.stf.jus.br/portal/peticaoInicial/verPeticaoInicial.asp?base='
           + Classe 
           + '&documento=&s1=1&numProcesso=' 
           + NumProcesso)
      
    # Busca dos dados na página
    html = dsd.get(url)
    
    # Redução do texto às variáveis
    inicio = html.find('processo/verProcessoAndamento.asp?')
    html = html[inicio:]

    # Gravação dos dados no arquivo
    arquivo_a_gravar = f'{diretorio_para_gravacao}\\{Classe}{str(0)*(4-len(NumProcesso))}{NumProcesso}.txt'
    dsd.gravar_dados_no_arquivo_nome(arquivo_a_gravar, html)

    print (f'Gravado arquivo {arquivo_a_gravar}')