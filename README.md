# Sistema de Gerenciamento de Contas e Geração de Gráficos

Este repositório contém um sistema de gerenciamento de contas de usuários e geração de gráficos estatísticos. O projeto foi desenvolvido por:

- Henrique Parra Benitez (RM551973) - [GitHub](https://github.com/rickparra)
- Roberto Oliveira Azzalin Navas (RM551460) - [GitHub](https://github.com/Robertooan07)
- Tony Willian da Silva Segalin (RM550667) - [GitHub](https://github.com/TonyWillianFIAP)
- Julia Amorim Bezerra (RM99609) - [GitHub](https://github.com/juamori)

## Funcionalidades Principais

O código desenvolvido inclui as seguintes funcionalidades:

1. **Leitura e gravação de dados em arquivo JSON**: As funções `carregar_contas()` e `salvar_contas()` interagem com o arquivo `contas.json` para persistir os dados.

2. **Cadastro e login de usuários**: As funções `criar_conta()` e `fazer_login()` permitem o cadastro de novos usuários com nome e senha, além de validar as credenciais durante o login.

3. **Menus de navegação**: As funções `menu()` e `segundo_menu()` contêm loops com opções para que os usuários possam navegar pelo sistema de forma intuitiva.

4. **Geração de gráficos**: As funções `clusterizar()`, `criar_densidade()` e `tempo_density()` realizam análises de dados utilizando a biblioteca Pandas e geram gráficos interativos com Plotly.

5. **Resumo de operações**: A função `feedback()` exibe um resumo das operações realizadas, incluindo contas criadas e gráficos gerados, ao final da execução.

6. **Tratamento de exceções**: O código é robusto e inclui tratamento de exceções para evitar erros inesperados.

7. **Utilização de funções**: O programa é estruturado em funções bem definidas, com parâmetros e retornos, seguindo boas práticas de programação para facilitar a manutenção e expansão do sistema.

Dessa forma, este código atende aos requisitos solicitados, permitindo o gerenciamento de contas de usuário, análise de dados externos e geração de saídas gráficas. As boas práticas de programação e o tratamento de erros foram aplicados para garantir a robustez do sistema.
