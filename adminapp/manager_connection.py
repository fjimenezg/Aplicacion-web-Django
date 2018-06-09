import psycopg2, psycopg2.extras
import pymysql
import cx_Oracle

class ManagerConnection():
    #Constructor
    def __init__(self, manager_db, user, passwd, port, host, dbname=None):
        
        self.manager_db = manager_db

        self.config_mysql = {
            'user': user,
            'password': passwd,
            'host': host,
            'port': int(port),                
        }

        if dbname is not None:
            self.config_mysql['db'] = dbname

        self.config_postgre = {
            'user': user,
            'password': passwd,
            'host': host,
            'port': port,
        }

        self.config_oracle = str(user+"/"+passwd+"@"+host)


    #Verifica si la connection es correcta
    def check_connection(self):
        if self.manager_db == 'mysql':
            try:
                conn = pymysql.connect(**self.config_mysql)
                conn.close()
                return True
            except:
                return False

        if self.manager_db == 'postgresql':
            try:
                conn = psycopg2.connect(**self.config_postgre)
                conn.close()
                return True
            except:
                return False

        if self.manager_db == 'oracle':
            try:                
                conn=cx_Oracle.connect(self.config_oracle)
                conn.close()
                return True
            except:
                return False
            
    #Consulta las bases de datos de un gestor  
    def list_db(self):
        if self.manager_db == 'mysql':
            if self.check_connection():
                conn = pymysql.connect(**self.config_mysql)          
                cursor = conn.cursor() 
                query = "show databases"
                cursor.execute(query)
                data = [row[0] for row in cursor.fetchall()]
                conn.close()
                return data
            return None

        if self.manager_db == 'postgresql':
            pass

        if self.manager_db == 'oracle':
            pass

    def managerSQL(self, query):
        if self.manager_db == 'mysql':
            if self.check_connection():
                self.config_mysql['dbname'] = self.dbname
                conn = pymysql.connect(**self.config_mysql)          
                cursor = conn.cursor() 
                query = "show databases"
                cursor.execute(query)
                data = [row[0] for row in cursor.fetchall()]
                conn.close()
                return data
            return None

        if self.manager_db == 'postgresql':
            pass

        if self.manager_db == 'oracle':
            pass