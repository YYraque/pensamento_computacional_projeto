'''
Isso é um bloco de Comentários.

'''

# isso é um Comentário em Linha, Finalmente quebramos a maldição
print("Olá, Mundo!")
while True:
    print('\n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\n')
    print('Bem-vindo ao projeto de desenvolvimento de um sistema de agendamento de horáros - Primus Motors')
    print('1 - Cadastrar veículo, por marcas')
    print('2 - Escolhendo a cor e modificações')
    print('3 - Escolhendo o horário')
    print('4 - Finalizar agendamento do horário')
    print('5 - Agendar test-drive')       
    print('6 - Finalizar agendamento do test-drive')
    print('7 - Encaminhar para um chat com um atendente')
    print('8 - Escolher loja física onde finalizar compra')
    print('9 - Enviar feedback/Enviar Reclamação')
    print('0 - sair')
    print('\n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰\n')

opcao = input('Digite a opção desejada:')

if opcao == '1': 
    print(' 1 - Cadastrar veículo, por marcas...')
if veiculo_1 == "":                  
    nome_veiculo = input('Digite o Nome do Veículo...')
    descricao_veiculo = input('Digite a Descrição do Produto...')
    marca_veiculo = input('Digite a Marca do Veículo...')
elif veiculo_2 == "":   
    nome_veiculo = input('Digite o Nome do Veículo...')
    descricao_veiculo = input('Digite a Descrição do Produto...')
    marca_veiculo = input('Digite a Marca do Veículo...')
elif veiculo_3 == "":  
    nome_veiculo = input('Digite o Nome do Veículo...')
    descricao_veiculo = input('Digite a Descrição do Produto...')
    marca_veiculo = input('Digite a Marca do Veículo...')
else:
    print('❌ Sistema cheio! Limite de 3 itens Atingido.')    

if opcao == '2':
    print(' 2 - Escolhendo cor e modificações...')
    cor_veiculo = input('Digite a Cor que Deseja...')
    modelo_aro_veiculo = input('Digite o Modelo do aro que Deseja...')
    aerofolio_veiculo = input('Digite o Modelo de Aerofólio que Deseja...')
    
elif opcao == '3':
    print(' 3 - Escolhendo Horário...')
    agendar_horario = int(input('Selecione o horario...'))

elif opcao == '4':
    print(' 4 - Finalizar agendamento do horário...')
    escolher_data = input('Digite o dia e o mês que Deseja Realizar a Compra...')

elif opcao == '5' :
    print(' 5 - Agendar Test-Drive...')
    agendar_horario = int(input('Selecione o horario...'))

elif opcao == '6' :
    print(' 6 - Finalizar Agendamento do Test-Drive...')
    escolher_data = input('Digite o dia e o mês que Deseja Realizar o Test-Drive...')

elif opcao == '7' :
    print(' 7 - Encaminhar para um chat com um atendente...')
    seu_nome = input('Digite seu nome...')
    seu_email = input('Digite seu email...')
    seu_numero = int(input('Digite seu Número de Telefone...'))

elif opcao == '8' :
    print('8 - Escolher loja física onde finalizar compra...')
    localizacao_lojafisica = input('Digite o Endereço da Loja Física...')

elif opcao == '9' :
    print('9 - Enviar feedback/Enviar Reclamação...')
    feed_back = input('Digite aqui sua experiencia...')
    reclame_aqui = input('Conte-nos o Porque sua Experiencia foi ruim...')

elif opcao == '0' :
    print('0 - sair')

else:
    print('Opção Inválida!')                


'''
>>Projeto Industria de Automóveis: Isaque e Gabriel

>PO (Como dono do negócio: Quero executar um sistema de agendamento) de horários pra venda de carros,
 simples, prático e funcional) 

 >QA (Como cliente: Quero um sistema de agendamento de horários que facilite a compra do meu carro dos sonhos)

 >Tech (Como programador: Quero um trabalho simples e fácil de executar e organizado)

 >Dev (Como programador: Quero fazer um sistema de chat autonomo
   pra facilitar o agendamento de horários dos meus clientes)

>UX (Como designer de experiência do usuário: Quero um sistema acessível,
 otimizado e responsivo com cores chamativas e relembraveis)

>IA (Como analista de dados: Quero uma analise inteligente e autonôma
 para que eu possa identificar padrões de vendas)

'''