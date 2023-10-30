from db import connect,disconnect
import  role.role as role
from flask import  g
import logging

def getRoleFromId(role_id):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,name, label,created_at,updated_at from role where id='{role_id}'"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchone()
    g.db.commit()
    # disconnect(connection_pool, obj, mycursor)

    if data == None:
        return None
    return role.role(data[0] ,data[1] ,data[2] ,data[3] ,data[4])
