"""
Paulo Werneck
03/04/2019

Classe para conexão ao teradata

IN: Host, usuario e senha do teradata
OUT: Conexão estabelecida
"""

import teradatasql
from time import sleep


class Connection:

    def __init__(self):
        self.url = 'XXX'
        self.user = 'XXX'
        self.password = 'XXX'

    def connection_gpa(self):
        try:
            print('Estabelecendo conexão ao teradata . . .')
            sleep(2)
            c = teradatasql.connect(None, host=self.url, user=self.user, password=self.password)
            print('Conexão realizada com sucesso!')
            exe = 'Seu banco padrão, conectado é: {0} \n'.format(c.cursor().execute('select database').fetchall())
            print(exe.replace('[', '').replace(']', ''))
            return c
        except teradatasql.DatabaseError:
            print('Falha na conexão ao teradata...')


if __name__ == '__main__':

    conn = Connection()
    conn.connection_gpa()
