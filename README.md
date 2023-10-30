### To run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Tests:

```bash
coverage run -m pytest
```

```bash
coverage report
```

```bash
coverage html
```

### Fixtures
- Fixtures são uma característica fundamental do framework de teste pytest em Python. Elas são funções definidas pelo usuário que fornecem dados de configuração, objetos ou recursos para os testes. Fixtures são usadas para configurar o ambiente de teste, preparar dados de teste, inicializar objetos e realizar tarefas de configuração necessárias antes da execução dos testes

#### Convenção de nomeação:
- Fixtures são identificadas por seu nome e são reconhecidas por pytest quando começam com o prefixo @pytest.fixture. A convenção de nomeação recomenda que os nomes das fixtures sejam descritivos e representativos da finalidade que servem.

#### Escopo: 
- Fixtures podem ter diferentes escopos, como função, classe, módulo ou sessão, para determinar quanto tempo uma instância da fixture é mantida em memória. Por padrão, as fixtures têm escopo de função, o que significa que uma nova instância da fixture é criada para cada função de teste.

#### Uso em testes:
- As fixtures são injetadas nos testes como argumentos de função. Quando você deseja usar uma fixture em um teste, basta adicionar o nome da fixture como um argumento para a função de teste, e o pytest cuidará de executar a fixture e passar os resultados para o teste.


### Vantagens sobre o uso de fixtures:
#### Reutilização de código:
- Fixtures permitem reutilizar código de configuração e inicialização comum entre vários testes. Isso evita a duplicação de código e facilita a manutenção.

#### Isolamento de testes:
- As fixtures ajudam a isolar testes, garantindo que os recursos sejam criados e limpos adequadamente antes e depois da execução de cada teste. Isso evita efeitos colaterais entre testes.

#### Gerenciamento de recursos:
- Fixtures são ideais para gerenciar recursos externos, como bancos de dados de teste, servidores, conexões de rede, arquivos, etc. Elas garantem que os recursos sejam inicializados e liberados corretamente.


### Context Manager:

#### Gerenciamento de recursos:

- Os context managers permitem que você gerencie recursos, como arquivos, conexões de banco de dados, sockets, etc., de forma mais eficaz. Eles garantem que os recursos sejam adequadamente inicializados e liberados quando não são mais necessários, evitando vazamentos de recursos.

#### Código mais limpo e legível:
- Os context managers ajudam a tornar seu código mais limpo e legível, pois encapsulam a lógica de inicialização e liberação de recursos em um bloco de código delimitado. Isso torna mais fácil entender o que está acontecendo com o recurso e quando ele está sendo usado.

#### Gestão de exceções:
- Os context managers tratam automaticamente exceções, garantindo que os recursos sejam liberados mesmo se ocorrerem exceções no bloco de código. Isso ajuda a evitar vazamentos de recursos e garante que o código seja robusto em relação a erros.

#### Prevenção de erros comuns:
- O uso de context managers ajuda a prevenir erros comuns, como esquecer de fechar um arquivo ou uma conexão de banco de dados, o que poderia levar a problemas de desempenho e segurança.

#### Reutilização de código:
- Os context managers podem encapsular a lógica de inicialização e liberação de recursos, tornando-a reutilizável em diferentes partes do código. Isso promove a modularidade e a reutilização de código.

#### Melhoria de desempenho:
- Os context managers podem melhorar o desempenho, uma vez que podem ser projetados para inicializar recursos apenas quando necessário e liberá-los imediatamente após o uso, em vez de mantê-los abertos por mais tempo do que o necessário.


### SETUP e TEARDOWN

**__As funções de setup e teardown são usadas em testes para configurar o ambiente de teste antes de executar os testes e limpar qualquer estado após a execução dos testes. Elas são frequentemente utilizadas em frameworks de teste, como o Pytest, para garantir que os testes sejam executados em um ambiente previsível e consistente.__**

#### Setup (Configuração):

- A função de setup é usada para configurar o ambiente de teste antes da execução dos testes. Isso pode incluir a criação de dados de teste, a inicialização de recursos, a configuração de variáveis de ambiente, a preparação de conexões de banco de dados, entre outras tarefas.
- Essa configuração é comum a muitos testes e é executada uma vez antes de cada teste individual.
- No Pytest, as funções de setup geralmente seguem a convenção de nomenclatura setup_ + nome do teste. Por exemplo, para um teste chamado test_example, a função de setup correspondente seria setup_test_example.

#### Teardown (Limpeza):
- A função de teardown é usada para limpar ou restaurar o ambiente após a execução dos testes. Isso é importante para garantir que os testes sejam independentes uns dos outros e não deixem resíduos que possam interferir em testes subsequentes.
- A limpeza pode incluir a remoção de dados de teste, a liberação de recursos, o fechamento de conexões de banco de dados e a reversão de quaisquer alterações feitas durante a execução dos testes.
- Assim como a função de setup, as funções de teardown seguem a convenção de nomenclatura teardown_ + nome do teste no Pytest. Por exemplo, para o teste test_example, a função de teardown correspondente seria teardown_test_example.