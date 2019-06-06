# exercicio 1
def verificar_ano(data):
    ano=(data[-2]+data[-1])
    ano=int(ano)
    return ano

with open('series.csv', 'r', encoding='utf-8') as file:
    Lista_nota10_nome=[]
    Lista_nota10_temp=[]
    Lista_nota10_epi=[]
    Lista_nota10_IMDB=[]
    Lista_nota10_Netflix=[]
    N_epi_até2009=0
    N_epi_2010até2019=0

    ep_Black=0
    ep_Breaking=0
    ep_Friends=0
    ep_TheBig=0
    n_black_I=0
    n_b_I=0
    n_f_I=0
    n_t_I=0
    n_black=0
    n_b=0
    n_f=0
    n_t=0
    
    
    for line in file.readlines():
        div = line.replace('\n','').split(',')
        V = verificar_ano(div[3])

        print(div)
        if div[-2]=='10' and div[-1]=='10':
            Lista_nota10_nome.append(div[0])
            Lista_nota10_temp.append(div[1])
            Lista_nota10_epi.append(div[2])
            Lista_nota10_IMDB.append(div[5])
            Lista_nota10_Netflix.append(div[6])
        elif V <= 9:
            N_epi_até2009 += 1

        elif V > 10 and V <= 19:
            N_epi_2010até2019 += 1

        elif div[0] =='Black Mirror':
            ep_Black+=1
            n_black_I+= int(div[-2])
            n_black+= int(div[-1])
        elif div[0] =='Breaking Bad':
            ep_Breaking+=1
            n_b_I+=int(div[-2])
            n_b+=int(div[-1])
        elif div[0] =='Friends':
            ep_Friends+=1
            n_f_I+=int(div[-2])
            n_f+=int(div[-1])
        elif div[0] =='The Big Bang Theory':
            ep_TheBig+=1
            n_t_I+=int(div[-2])
            n_t+=int(div[-1])
        
    # exercicio 2
    número= len(Lista_nota10_nome)
    for i in range(1,número):
        print('Série:', Lista_nota10_nome[i])
        print('Episódio: Temporada',Lista_nota10_temp[i],', Ep',Lista_nota10_epi[i])
        print('Nota IMDB:', Lista_nota10_IMDB[i])
        print('Nota Netflix:', Lista_nota10_Netflix[i])
        print('')

    #exercicio 3
    print('Número de episódios até 2009:',N_epi_até2009)
    print('Número de episódios entre 2010 e 2019:',N_epi_2010até2019)

    #exercicio 4
    M_Black_N = n_black/ep_Black
    M_Black_I= n_black_I/ep_Black
    M_b_N= n_b/ep_Breaking
    M_b_I= n_b_I/ep_Breaking
    M_f_N= n_f/ep_Friends
    M_f_I= n_f_I/ep_Friends
    M_big_N= n_b/ep_TheBig
    M_big_I= n_b_i/ep_TheBig
    
    print('Black Mirror:', M_Black_I,'(IMDB)', M_Black_N,'(Netflix)' )
    print('Breaking Bad:', M_b_I,'(IMDB)', M_b_N,'(Netflix)')
    print('Friends:', M_f_I,'(IMDB)', M_f_N,'(Netflix)')
    print('The Big Bang Theory:', M_Big_I,'(IMDB)', M_Big_N,'(Netflix)' )

    

    

