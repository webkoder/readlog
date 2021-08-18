USE nobeta;

CREATE TABLE estatistica(
id int auto_increment not null,
bloco varchar(80) null ,
categorias varchar (80) null,
device text null ,
browser text null ,
response varchar(255) null  ,
status varchar(255) null ,
avgsize float null ,
sumsize float null,
latencymobile float null,
latencydesktop float null,
referer text null ,
data date null,
primary key (id));


select * from estatistica;

CREATE TABLE acesso(
id int auto_increment not null,
bloco varchar(80) null ,
referer varchar(255) null ,
contagem int null, 
mes int null,
ano int null, 
primary key (id));

select * from acesso;