# DESAFIO DIO PRO - FORMAÇÃO PYTHON DEVELOPER 

O código que foi apresentado é uma implementação em Python de um sistema bancário simplificado que permite realizar operações comuns como depósito, saque e extrato.

A classe "Banco" representa o objeto responsável por gerenciar as operações financeiras. Ela possui atributos como "saldo", "depositos" e "saques", que são utilizados para controlar o saldo atual da conta, armazenar os valores depositados e registrar os saques efetuados, respectivamente.

No processo de depósito, o método "deposito()" recebe um valor como entrada e verifica se é um número positivo. Caso seja, o valor é adicionado ao saldo da conta e registrado na lista de depósitos. Uma mensagem de confirmação é exibida para indicar que o depósito foi realizado com sucesso. Caso o valor não seja positivo, uma mensagem de erro é exibida para informar que o valor do depósito deve ser um número positivo.

Já na operação de saque, o método "saque()" recebe um valor como entrada e verifica se é possível realizar o saque com base em algumas condições: o saldo da conta deve ser suficiente para cobrir o valor solicitado, o valor do saque não pode ultrapassar R$ 500,00 e não é permitido exceder o limite de três saques diários. Se todas essas condições forem atendidas, o valor é subtraído do saldo da conta e registrado na lista de saques. Caso alguma das condições não seja satisfeita, uma mensagem de erro específica é exibida, informando o motivo pelo qual o saque não pode ser realizado.

Para obter o extrato da conta, é utilizada a operação "extrato()", que lista de forma formatada todos os depósitos e saques efetuados, além do saldo atual da conta. Os valores são exibidos seguindo o formato monetário "R$ xxx.xx".

A interação com o usuário é feita por meio da função "main()", que permite escolher entre as opções de depósito, saque, extrato e sair do programa. Dependendo da opção selecionada, o usuário é solicitado a fornecer os valores necessários para realizar a operação correspondente.

Além disso, o código inclui testes unitários implementados com a biblioteca "unittest" para verificar o comportamento correto das operações bancárias. Os testes cobrem casos de sucesso e também as condições de erro esperadas em cada operação.

Essa implementação fornece uma base sólida para um sistema bancário simplificado, permitindo que os usuários realizem operações financeiras básicas, como depósito e saque, e obtenham um extrato atualizado da conta.
