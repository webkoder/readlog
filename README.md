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
- Configurar o arquivo db.py com a seguinte estrutura
```
import mysql.connector

con = mysql.connector.connect(host='localhost',database='<dbname>',user='<username>',password='<yourpassword>')
cursor = con.cursor()
```

## Instalação
- Atender os requisitos
- Instalar as dependências
```
pip install -r requirements.txt
```
- Se necessário alterar a query do BigQuery para atender a sua demanda

## Como usar
O comando usado para executar é 
```
python main.py
```

Você pode usar a data que deseja processar, no formato padrão do MySQL Ex.
```
python main.py 2021-08-05
```