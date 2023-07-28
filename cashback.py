print('1 - Cadastrar Empresa\n2 - Cadastrar Usuário\n3 - Registrar Compra de um Usuário\n4 - Mostrar Saldo de um Usuário\n5 - Resgatar Saldo de um Usuário\n6 - Excluir Empresa\n0 - Sair')


valorinicialsaldo=0
saldos=[]
usuarios=[]
empresas=['ALB','MM','CZB']
descontos=[10,8,5]


menu=int(input('opção menu (0 - encerra programa):'))
while menu!=0:


 if menu == 1:
    strart=input('quer iniciar cadastros de empresas (sim/não):').upper()
    while strart == 'SIM':
      empresa=input('empresa:').upper()
      while empresa in empresas:
        print('empresa já cadastrada!\ndigite novamente!')
        empresa=input('empresa:').upper()
      empresas.append(empresa)
      descont=int(input('desconto:'))
      descontos.append(descont)
      strart=input('quer cadastrar mais empresas (sim/não):').upper()
    
    print(empresas,'\n',descontos)
    

 elif menu ==2:
    strart2=input('quer iniciar cadastros de usuarios (sim/não):').upper()
    

    while strart2 == 'SIM':
     cliente=input('client:').upper()
     while cliente in usuarios:
      print('usuario ja cadrastrado')
      cliente=input('client:').upper()

     usuarios.append(cliente)
     saldos.append(valorinicialsaldo)
     strart2=input('quer cadastrar mais usuarios (sim/não):').upper()
    
    print('usuarios:{}\nempresas:{}\ndescontos{}'.format(usuarios,empresas,descontos))



 elif menu == 3:
   start3=input('quer registar as compras (sim/não):').upper()
   


   while start3 == 'SIM':
    idusuario=input('cliente:').upper()
    while idusuario not in usuarios:
       print('usuario não cadastrado')
       idusuario=input('cliente:').upper()
    x=usuarios.index(idusuario)
    valordacompra=int(input('valor compra:'))
    posempresa=input('local:').upper()
    pos=empresas.index(posempresa)
    valorcomdesc = valordacompra*(descontos[pos]/100)
    saldos.insert(x,valorcomdesc)
    start3=input('quer registar mais compras (sim/não):').upper()
   


 elif menu == 4:
        start4 = input('Quer conferir o saldo (sim/não):').upper()
        
        while start4 == 'SIM':
            alusuario = input('Cliente: ').upper()
            
            if alusuario in usuarios:
                pos = usuarios.index(alusuario)
                valorsaldo = saldos[pos]
                print('Saldo:', valorsaldo)
            else:
                print('Usuário não cadastrado')
            
            start4 = input('Quer conferir o saldo de outro usuário (sim/não): ').upper()
        
        

 elif menu ==5:
   start5=input('quer resgatar saldo (sim/não):').upper()



   while start5 == 'SIM':
     pesquisa=input('client:').upper()

     if pesquisa in usuarios:
       pospesquisa=usuarios.index(pesquisa)
       valorsaldo2=saldos[pospesquisa]
       print('saldo de {} resgatado'.format(valorsaldo2))
     else:
      print('usuario não cadastrado')
     start5=input('quer resgatar saldo de outro usuari (sim/não):')
   


 elif menu == 6:
  mensagemaviso=input('tem certeza que deseja escluir uma empresa (sim/não):').upper()
  if mensagemaviso == 'SIM':
    empresaexcluida=input('qual empresa excluir:').upper()
    
    if empresaexcluida in empresas:
        empresas.remove(empresaexcluida)
        
        print('Empresa', empresaexcluida, 'foi excluída com sucesso.')
    else:
        print('Empresa não encontrada.')

 print('1 - Cadastrar Empresa\n2 - Cadastrar Usuário\n3 - Registrar Compra de um Usuário\n4 - Mostrar Saldo de um Usuário\n5 - Resgatar Saldo de um Usuário\n6 - Excluir Empresa\n0 - Sair')

 menu=int(input('opção menu (0 - encerra programa):'))

print('empresas: {}\ndescontos:{}\nusuarios:{}\nsaldos:{}'.format(empresas,descontos,usuarios,saldos))
   
 
 