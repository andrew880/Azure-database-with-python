import mysql.connector
from mysql.connector import errorcode
try:
    conn = mysql.connector.connect(user='retailing880@retailing-test1',
                                   password='retailing@admin0',
                                   database='cs110032000cd8f2a75',
                                   host='retailing-test1.mysql.database.azure.com',
                                   ssl_ca='BaltimoreCyberTrustRoot.crt.pem')
except mysql.connector.Error as err:
    print(err)


    # --user=retailing880@retailing-test1
    #                                --password=retailing@admin0
    #                                --host=retailing-test1.mysql.database.azure.com
    #                                --ssl_caBaltimoreCyberTrustRoot.crt.pem