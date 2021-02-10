import time
import pickle
titulo = "\033[1;36mCIGANA VIRTUAL\033[m"
print(titulo.center(70))
print("\033[1;34m*"*70)
print("- Ola, tudo bem?")
time.sleep(1.5)
print("Me chamo Pytricia, sua cigana virtual.")
time.sleep(1.5)
print("A seguir faça o cadastro, e baseda nas informações ")
time.sleep(1.5)
print("lhe direi as suas previsões para 2021.")
print("*"*70)
time.sleep(1.5)

cliente = {}
try:
  arqCliente = open("Clientes.dat","rb")
  cliente = pickle.load(arqCliente)
  arqCliente.close()
except IOError:
  print("Erro ao abrir o arquivo")
  print("Base de dados está vazia!")

resp = "6"
while resp.lower() != "5":
  print("\033[1;32mCarregando...\033[m")
  time.sleep(1.5)
  print()
  print("# 1 - CADASTRAMENTO     # ")
  print("# 2 - PREVISÕES         #")
  print("# 3 - EXIBIÇÃO DE DADOS #")
  print("# 4 - EXCLUIR DADOS     #")
  print("# 5 - SAIR              #")
  print()
  resp = input("Informe a opção desejada: ")
  print()


  if resp == "1":
      print("\033[1;32mMODULO DE CADASTRAMENTO\033[m")
      print()
      nome = input("Nome: ").capitalize()
     
      while True:
        sexo = input("Sexo [M/F]: ")
        sexo = sexo.upper()
        if sexo.upper() !="F" and sexo.upper()!= "M":
          print("\033[1;34mDigite 'M' ou 'F'!\033[m")
        else:
          break


      while True:
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        if dia <= 0 or dia > 31 and mes < 0 or mes > 12:
          print()
          print("\033[1;34mDigite um dia e mês válidos!\033[m")
          print()
        else:
          if dia == 31 and mes != 1 and mes != 3 and mes != 5 and mes != 6 and mes!= 7 and mes != 8 and mes != 10 and mes!= 12:
            print()
            print("\033[1;34mDigite um dia válido dentro do mês informado!\033[m")
            print()
          elif dia == 29 or dia == 30 and mes == 2:
            print()
            print("Data inválida,pois 2021 não é ano bissexto!")
            print()
          else:
            break

      while True:
        ano = int(input("Ano: "))
        
        if ano < 1900 or ano >= 2020:
          print()
          print("\033[1;34mInforme um ano válido!\033[m")
          print()
        else:
          break
      signo = input ("Signo: ")
      signo = signo.upper()
      if dia >= 18 and mes == 12:
        idade = (2020 - ano) - 1
      else:
         idade = (2020 - ano) 

      cliente[nome] = [sexo, dia, mes, ano, signo, idade] 
     
      print()
      print("Cadastramento feito!")

  elif resp == "2":
    print("\033[1;33mMODULO DAS PREVISÕES\033[m")
    print()
    busca = input("Digite o seu nome: ").capitalize()
    if nome.startswith(busca):
      print()
      if nome in cliente:
        print("INFORMAÇÕES:")
        print()
        print("#"*70)
        print("Nome:",nome)
        print("Sexo: ",cliente[nome][0])
        print("Data de Nascimento:",cliente[nome][1], "/", cliente[nome] [2],"/", cliente[nome] [3] )
        print("Idade: ",cliente[nome][5])
        print("Signo:",cliente[nome][4])
        print("#"*70)
        print()
        if cliente[nome][4] == "ARIES" or cliente[nome][4] == "ÁRIES" :
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nOs movimentos de Urano podem proporcionar às arianas e aos arianos mudança na maneira de lidar com as finanças. A energia flui e você poderá atrair mais dinheiro sem se tornar refém dele.\033[m")
          print()
          print("\033[1;34mAMOR:\nNo segundo semestre, a vida afetiva de pessoas de Áries tende a ficar mais movimentada. No fim de junho, Marte vai entrar em Leão e este é um momento excelente de conquista para quem não está namorando. Pode ser ótimo para tomar a iniciativa, conquistar alguém que você queira, começar um romance e desfrutar mais, inclusive, de sexo.\033[m")
          print()
          print("CARREIRA E DINHEIRO:\nO trânsito de Júpiter em Aquário pode ser interessante aos negócios de quem é de Áries, em 2021. Já Saturno em Aquário pode ajudar a garantir e a estruturar melhor essas oportunidades, evitando que a energia ariana seja fogo de palha.")
          print()
        elif cliente[nome][4] == "TOURO":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nQuem é de Touro está vivendo trânsitos muito importantes em 2021. Esses trânsitos astrológicos indicam necessidade de você se colocar mais, principalmente no nível social, dentro de um contexto mais público e amplo. É preciso sair do familiar, do confortável e tomar alguns riscos.\033[m")
          print()
          print("AMOR:\nCom Urano passando pelo setor da identidade de taurinas e taurinos, todas as áreas da vida podem ser tocadas pelo planeta. Isso inclui a maneira como você se relaciona com seu próprio mundo e com as outras pessoas.")
          print()
          print("CARREIRA E DINHEIRO:\nOs taurinos vão passar por eclipses em 2021 que podem mexer com a questão do dinheiro na sua vida. Por isso, é um ano para tomar mais consciência do modo como vêm administrando suas finanças.")
          print()
        elif cliente[nome][4] == "GEMEOS" or cliente[nome][4] == "GÊMEOS":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS PARA GÊMEOS EM 2021:\nQuem é de Gêmeos provavelmente vai passar por um ano com algumas instabilidades. Embora não seja um grande problema para geminianas e geminianos, o trânsito de Urano em Touro pode trazer muitas mudanças repentinas em compromissos, atividades e na rotina. Essa versatilidade geralmente interessa a você.\033[m")
          print()
          print("\033[1;34mAMOR:\nTanto Júpiter quanto Saturno estarão no signo de Aquário e, para quem é de Gêmeos, esses trânsitos podem trazer uma visão mais a longo prazo de vida. Assim, quem está num relacionamento sério poderá se ver olhando mais para frente.\033[m")
          print()
          print("\033[1;34mCARREIRA E DINHEIRO:\nOs movimentos de Plutão podem fazer com que geminianas e geminianos tenham de ter atenção às finanças variáveis e relacionadas às outras pessoas assim como o dinheiro que você ganha com o seu trabalho. A dica aqui é ter atenção ao seu controle financeiro, empréstimos e dívidas.\033[m")
          print()
        elif cliente[nome][4] == "CANCER" or cliente[nome][4] == "CÂNCER":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nA tendência para cancerianas e cancerianos é de profundas mudanças, por conta dos movimentos que Júpiter e Saturno em Aquário vão fazer para quem é de Câncer. Para passar por essas transformações, será fundamental confiar na sua capacidade inventiva e trazer à tona talentos e habilidades que podem estar inconscientes.\033[m")
          print()
          print("\033[1;34mAMOR:\nAs mudanças do ano também podem envolver o amor. Embora no início no ano possam aparecer mais oportunidades, com o passar dos meses pode ficar mais difícil para cancerianas e cancerianos.")
          print()
          print("CARREIRA E DINHEIRO:\nPode haver boas oportunidades de ganhos e entrada de dinheiro, principalmente no primeiro semestre do ano. Mas como Saturno está quadrando Urano, pode causar instabilidade na área econômica, principalmente em fevereiro, junho e dezembro. Lembre-se de que o contexto coletivo tende a instabilidades nessa área.\033[m")
          print()
        elif cliente[nome][4] == "LEAO" or cliente[nome][4] == "LEÃO":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nCom Júpiter passando sobre seus relacionamentos e parcerias, é bom você ter em mente que é importante a questão da reciprocidade. Você pode ter mais retorno se oferecer mais, porque Júpiter é um planeta generoso e relações de mão única não funcionam com ele.")
          print("AMOR:\nPara quem está em um relacionamento, Júpiter pode tanto ser benéfico para quem está com você, o que vai ser bom para você indiretamente, quanto pode indicar um momento expansivo da relação.")
          print()
          print("CARREIRA E DINHEIRO:\nLeoninas e leoninos vêm passando por alterações externas, que têm demandado adaptabilidade a novas ferramentas de trabalho e maneiras de se comportar. Tudo isso pode levar a troca de emprego e até a mudanças radicais de carreira. Se for seu caso, esse é o momento apropriado para isso.\033[m")
          print()
        elif cliente[nome][4] == "VIRGEM":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nNesse processo de aprimoramento pessoal, técnico e profissional que o trânsito de Urano pode destacar, um dos grandes desafios para quem é de Virgem pode ser o de buscar conhecimentos novos,  que não sejam tão convencionais e que ampliem sua área de atuação ou de estudos.")
          print()
          print("AMOR:\nO trânsito de Netuno pode destacar questões sobre relacionamentos para quem é de Virgem. Por isso, é preciso cuidar para não endeusar demais a outra pessoa e achar que a relação está perfeita. Se possível, baixe um pouco as expectativas.")
          print()
          print("CARREIRA E DINHEIRO:\nO trânsito de Júpiter em Aquário, durante quase todo o ano, pode destacar aumento de projetos que podem ser destinados a quem é de Virgem. A tendência é de que você abrace tudo. Mas é preciso ter noção da sua capacidade de assumir tarefas dentro do seu trabalho. Por isso, é muito importante aprender a delegar.\033[m")
          print()
        elif cliente[nome][4] == "LIBRA":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nAs reformas e as crises internas que vocêm vem passando devem seguir acontecendo na vida de quem é de Libra, principalmente por causa de Plutão.")
          print()
          print("AMOR:\nEm geral, quem é de Libra nasceu para ser par, e não ímpar, certo? Pois 2021 pode ser um ano de transformação na sua vida amorosa, de paixões avassaladoras a pedidos de casamento.")
          print()
          print("CARREIRA E DINHEIRO:\nVocê, antes de tudo, tem de acreditar em si, na sua maneira de fazer as coisas, no seu diferencial. Isso pode gerar muitas oportunidades de negócios, de trabalho, de mudanças que tenham mais a ver com seu próprio prazer. Essa autoconfiança pode repercutir na sua carreira e finanças.\033[m")
          print()
        elif cliente[nome][4] == "ESCORPIÃO" or cliente[nome][4] == "ESCORPIAO":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nQuanto mais escorpianas e escorpianos puderem se voltar para dentro de si em 2021 e reestruturarem a maneira de lidar com pais, filhos e pessoas com as quais têm laço mais íntimo, melhor. Mas um laço de intimidade que respeite a liberdade e a autonomia das outras pessoas.")
          print()
          print("AMOR:\nO trânsito de Urano em Touro (que vai até 2026) pode contribuir para que pessoas de Escorpião passem por mudanças importantes nos relacionamentos. Não só com quem você se relaciona, mas que tipo de relacionamento você quer.")
          print()
          print("CARREIRA E DINHEIRO:\nO trânsito de Saturno em Aquário para quem é de Escorpião pode ser um indicativo de trabalho remoto ou de esvaziamento do foco em questões de carreira, profissão e projeção social por conta de responsabilidades maiores que poderão surgir dentro do ambiente doméstico.\033[m")
          print()
        elif cliente[nome][4] == "SARGITARIO" or cliente[nome][4] == "SARGITÁRIO":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nSaturno vem junto com Júpiter na vida de quem é de Sagitário. A energia saturniana pode ajudar você a se questionar sobre quais oportunidades realmente podem ser aplicadas para consolidação da sua carreira e no seu progresso material.")
          print()
          print("AMOR:\nÉ muito importante que você diversifique, mude de ambientes, se socialize (o que pode ser feito pela internet também), mas será fundamental para trazer oportunidades mais interessantes para o amor. Os eclipses podem provocar confronto entre passado e futuro em relação aos relacionamentos, inclusive trazer ex parcerias, mas é importante olhar para frente.")
          print()
          print("CARREIRA E DINHEIRO:\nO trânsito de Plutão pode ter ativado questões sobre suas finanças há algum tempo. Enquanto 2020 foi um ano de reavaliação sobre valores e como você se valoriza, em 2021 Plutão pode mudar o foco. Agora é um momento de aplicar o que você aprendeu, de valorizar o seu talento e aplicar de maneira inovadora, mais tecnológica e avançada.\033[m")
          print()
        elif cliente[nome][4] == "CAPRICORNIO" or cliente[nome][4] == "CAPRICÓRNIO":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nCom Júpiter e Saturno em Aquário, quem é de Capricórnio precisará dar atenção ao seu próprio corpo, sua saúde e também as questões práticas, materiais e financeiras. O desafio vai ser não exagerar (algo jupiteriano) no trabalho e em querer ganhar muito dinheiro, porque você pode acabar esquecendo das necessidades corporais. Aí é que Saturno pede disciplina, comprometimento e consistência para cuidar da saúde.")
          print()
          print("AMOR:\nNessa reformulação da relação com si, com as pessoas mais próximas e com seus prazeres, a capricorniana solteira ou o capricorniano solteiro pode encontrar um amor.Esse alguém pode chegar de maneira inesperada e contribuir para esse processo de redescobrimento de si.")
          print()
          print("CARREIRA E DINHEIRO:\nPara quem é de Capricórnio, 2021 pode ser um ano ótimo para administrar as finanças e trabalhar melhor o seu tempo. A capricorniana e o capricorniano têm mania de pegar muita tarefa para si, mas você pode aproveitar 2021 para aprender a delegar e, com isso, gerir melhor seu tempo, seu dinheiro e seu trabalho.\033[m")
          print()
        elif cliente[nome][4] == "AQUARIO" or cliente[nome][4] == "AQUÁRIO":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nSaturno também está forte em Aquário em 2021. É como se Júpiter abrisse as portas, e Saturno filtrasse as opções. Por isso, se possível, escolha aquela oportunidade que você sabe onde pode se dar bem. Tenha sabedoria saturnina para sustentar as oportunidades jupiterianas.")
          print()
          print("AMOR:\nO eclipse do dia 10/6 será no signo de Gêmeos pode trazer questões afetivas para pessoas de Aquário. Para quem não estão se relacionando, pode perceber mais oportunidades no amor. Inclusive, duas ao mesmo tempo. Será preciso escolher essa pessoa baseada no prazer, na afinidade intelectual, no prazer da troca de ideias que aquarianas e aquarianos amam.")
          print()
          print("CARREIRA E DINHEIRO:\nSe tem alguém que tem condições de colocar no bolso essa crise agravada pela pandemia são as pessoas de Aquário. O fato de Júpiter e Saturno estarem juntos em Aquário em 2021 aponta para um momento de expansão profissional, mas que vai demandar mais comprometimento, mais responsabilidade, mais pé no chão.\033[m")
          print()
        elif cliente[nome][4] == "PEIXES":
          print("PREVISÃO PARA {} EM 2021:".format(cliente[nome][4]))
          print()
          print("\033[1;34mDESAFIOS EM 2021:\nO planeta convida você a enfrentar seus próprios medos, principalmente para entender o que está te limitando até agora. A tendência é de que 2021 seja um período mais de conclusão do que de início para piscianas e piscianos. Fechar ciclos, resolver pendências e finalizar etapas são as principais previsões para Peixes em 2021. Possivelmente, tudo isso envolverá muitos sacrifícios pessoais.")
          print()
          print("AMOR:\nComo você provavelmente estará fazendo uma reforma interna em 2021, a tendência é que isso impacte em tudo, inclusive no amor. O ano traz a oportunidade de você reconstruir relações que fazem mais sentido neste novo momento de vida. Se estiver em um relacionamento, é provável que tenha de fazer sacrifícios maiores em prol da pessoa parceira e vice-versa. Cumplicidade e companheirismo serão fundamentais. Piscianas e piscianos deverão refletir no quanto a pessoa parceira aceita (ou não) sua individualidade, suas amizades e seu jeito de ser.")
          print()
          print("CARREIRA E DINHEIRO:\nRevisão é o tom para Peixes em 2021. Os movimentos de Júpiter e Saturno trazem a oportunidade de você buscar o que você quer para a sua vida profissional para que, quando 2022 chegar, você possa estar pronto crescer na sua carreira. É muito importante que piscianas e piscianos olhem para seus valores pessoais. Quanto você acha que vale? Essa resposta pode ser determinante, porque aquilo que você ganha estará diretamente relacionado ao que você pensa sobre si\033[m.")
          print()
        else:
          print("\033[1;34mDigite um nome de signo válido!\033[m")
      else:
        print("{} não está cadastrado!".format(busca))
   
    else:
      print("{} não está cadastrado!".format(busca))
  


  elif resp == "3":
    print("\033[1;31mMODULO EXIBIÇÃO DE DADOS\033[m")

    print()
    for nome in cliente:
      print("Nome:",nome)
      print("Sexo: ",cliente[nome][0])
      print("Data de Nascimento:",cliente[nome][1], "/", cliente[nome] [2],"/", cliente[nome] [3] )
      print("Idade: ",cliente[nome][5])
      print("Signo:",cliente[nome][4])
      print()
  elif resp == "4":
     busca = input("Digite o seu nome: ").capitalize()
     if nome.startswith(busca):
      print()
      if nome in cliente:
        print("INFORMAÇÕES:")
        print()
        print("#"*70)
        print("Nome:",nome)
        print("Sexo: ",cliente[nome][0])
        print("Data de Nascimento:",cliente[nome][1], "/", cliente[nome] [2],"/", cliente[nome] [3] )
        print("Idade: ",cliente[nome][5])
        print("Signo:",cliente[nome][4])
        print("#"*70)
        print()
        perg = input("Tem certeza que quer excluir? ")
        if perg == "s":
          del cliente[nome]
          print("\033[1;34mExcluido com sucesso!\033[m")
        else:
          print("\033[1;34mDados não excluidos\033[m")

     
  elif resp == "5":
    print("\033[1;34mEspero que tenha gostado da sua previsão para 2021!")
print()

print("Obrigado por usar o programa!\033[m")
print()
print("Programa  Cigana-Virtual by: Renildo Rabi Vale Dos Santos.")
arqCliente = open("Clientes.dat", "wb")
pickle.dump(cliente, arqCliente)
arqCliente.close()

   
      