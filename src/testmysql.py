from db import  cursor, con 

def test():

    sites = ''
    cursor.execute("select * from site limit 5")
    
    myresult = cursor.fetchall()

    for x in myresult:
        sites +=  x[1] + ', '

    con.close()

    return sites