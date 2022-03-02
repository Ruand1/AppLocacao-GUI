25/02/22 - Levantamento Inicial
App para locação em geral - 

Criar padrão para locação - Será criado no KivyMD

Criar com arquivo .json - posterior fazer com acesso a SQL

Novo Cadastro - Padrão - Nome - Foto - Descriçao

Ver Cadastro - Padrão - Listar todos os cadastros

26/02/22 - Finalizando videos KivyMD

- Criando Tela de Login - OK
	- Colocando datetime - mostrar Bom dia, Boa Tarde, Boa Noite - OK
		- criar variavel que receba a hora do dispositivo, se for até - OK
		meio dia (Bom Dia), até as 18 (Boa Tarde), depois (Boa Noite)

- Continuando Video -
	- Acrescentado text field do email - OK
	- Acrescentado text field de senha (mostrando/escondendo) senha - OK

- Tela de Login - OK

- Foi acrescentado botões para chavear entre dark/light theme - OK
	- Verificar possibilidade de chavear com apenas um botão - PENDENTE
		- Não esta funcionando se o icone é movimentado na posição y

27/02/22 e 28/02/22 -  
- Fazer tela do novo cadastro - 
	- cadastrar em json - OK
		variaveis ja estão recebendo os valores cadastrados - OK
		cadastrar em arquivo e puxar cadastros - OK
			- ERRO - QUANDO USUARIO ENTRA NO CADASTRO - MOSTRA DUAS VEZES
			- ERRO - POPUP ESTA SENDO MOSTRADO 2 VEZES

	- usar json para validar cadastro - OK
	- montar popup de cadastro correto - OK

01/03/22 e 02/03/22- 
- Tela de cadastro - OK
	- Grava cadastro único - OK
	- PopUps aparecendo duas vezes - Verificar erro posteriormente
		- Quando aperta o botão cadastrar, aparentemente o programa faz um loop duas vezes

- Tela Entrar - Inicial - 
	- montar popup para aviso de não cadastrado - OK
	- validar email e senha do cadastro - OK
	- verificar mandar email de confirmação - PENDENTE
	
	- Montar desenho da tela inicial -
		- Cadastrar objetos(Padrão) - OK
		- Fazer botão de menu superior lado direito - PENDENTE
		
		- Colocar saudação, puxando o nome do cadastro - FALTA PUXAR NOME - NÃO COLOCAR

		- Criar telas   - Novo Cadastro
					- Widgets - OK
					- Inteligência - OK
					- Escolher Imagem - OK
						- Verificar se é possivel fazer um filechooser em um Mddialog, para não precisar criar outra tela - Não foi preciso, um botão ja gera a tela de filechooser - OK


03/03/22 - 
		- Ver Cadastros - Fazer tela ver cadastros - gerando um MDCard para cada widget no cadastro

		- Fazer as movimentações das telas "Animações" - root.manager.transition.direction = 'left'
			VER SITE https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
