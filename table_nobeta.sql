USE nobeta;

CREATE TABLE estatistica(
id int auto_increment not null,
bloco varchar(80) null ,
device varchar(255) null ,
browser varchar(255) null ,
response varchar(255) null  ,
status varchar(255) null ,
avgsize float null ,
sumsize float null,
latency float null,
referer text null ,
data date null,
primary key (id));


select * from estatistica;