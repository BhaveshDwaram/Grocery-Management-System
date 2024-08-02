
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root',host='127.0.0.1', password='bhavesh@2003', database='grocery_store')

  return __cnx

