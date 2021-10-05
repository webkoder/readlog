from mysqldata import MySQLData
from Monthly import Monthly

mes = 9
ano = 2021
tipo = 'script'

data = MySQLData()
mes = data.getMonthData( mes, ano, tipo )

sites = {}
c = 0

for dia in mes:
    if dia['bloco'] not in sites:
        sites[ dia['bloco'] ] = Monthly( dia['bloco'] )
    
    sites[ dia['bloco'] ].add( dia )
    c += 1
    print(  sites[ dia['bloco'] ] )

print( str(c) )