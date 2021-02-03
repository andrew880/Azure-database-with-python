upload crt.pem file onto azure portal for ssl_cert
#make sure the path to crt.pem file is correct

run following code
connect to server
```
mysql --host retailing-test2.mysql.database.azure.com \
--user retailing880@retailing-test2 \
--ssl_ca /home/polastrijeff/BaltimoreCyberTrustRoot.crt.pem -p
```
create database
```
CREATE DATABASE test;
USE test;
```

mysql --host retailing-test2.mysql.database.azure.com \
--database test \
--user retailing880@retailing-test2 \
--ssl_ca /home/polastrijeff/BaltimoreCyberTrustRoot.crt.pem -p

https://hackmd.io/8VAFnSL1Tzmu9maoneDcFA