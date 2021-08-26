# Read Log
Faz a leitura do serviço de logging da GCP através do Big Query acessando via API em Python, com saída para o MySQL.

O script faz um processamento dos dados para pegar estatística diário e para cada bloco (bloco no nosso sistema significa site parceiro) para os campos:
- Tipo de device (desktop, mobile e bot)
- Latência média para cada device
- Contagem de status HTTP
- Média e total do tamanho do arquivo
- Contagem de páginas referer
- Contagem de resposta do servidor

## Requisitos

- Criar o dataset no serviço BigQuery na GCP
- Criar um sink dos dados que você deseja no serviço de Logging na GCP, com a saída para o dataset criado anteriormente
- Criar um acesso de api para o BigQuery na sua conta GCP
- Ter acesso ao servidor de banco de dados
**A instrução abaixo só é válido para o Cloud Functions, atualmente o parametro *unix_socket* não é usado**
- Configurar uma váriável de sistema com o nome de *MYSQLPY* com o seguinte valor
```
{"user":"[user]","password":"[password]","host":"[host]","database":"[database]", socket="[path to socket]"}
```
Onde os valores em colchetes deve ser trocado pelo respectivo valor de acesso ao banco. O valor de **"path to socket"** é obtido na tela da instancia dentro do console da GCP, identificado como **Connection name** e deve ser adicionado no inicio o texto **/cloudsql/**
no final o valor deverá ser parecido com este:
```
/cloudsql/projeto:regiao:instancename
```

## Instalação
- Atender os requisitos
- Instalar as dependências
```
pip install -r requirements.txt
```
- Se necessário alterar a query do BigQuery para atender a sua demanda

## Deploy no Google Cloud Functions

O deploy pode ser feito via Github / Source Repositories e usando como fonte, A função no Cloud Functions deve conter uma váriável de ambiente (Runtime environment variables) como descrito na seção **Requisitos** com o nome *MYSQLPY* e o valor json com os dados de conexão e socket do banco de dados MySQL hospedado no serviço Cloud SQL.

O campo Entry Point deve ser o valor "principal" e para o valor de Runtime, foi testado as versões Python 3.8 e 3.9

Ainda é possível testar a função usando o comando **functions-framework** simulando uma requisição pelo navegador no ambiente local, para instalar, execute o comando:
```
pip install functions-framework
```

E para rodar, o comando é:
```
functions_framework --target=principal
```
 após o serviço estiver rodando, basta entrar no endereço no navegador
```
http://192.168.0.106:8080
```
Ou para passar a data do processamento:
```
http://192.168.0.106:8080/?data=2021-08-23
```
## Deploy na instância do Google Compute Engine
-Fazer o clone do projeto
-Criar um ambiente virtual
-Copiar o arquivo de autenticação
-Ativar ambiente virtual
-Baixar as dependencias
```
python chamador.py
```
ou
```
python chamador.py 2021-08-23
```
