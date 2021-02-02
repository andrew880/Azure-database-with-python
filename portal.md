upload crt.pem file onto azure portal for ssl_cert
#make sure the path to crt.pem file is correct

mysql --host retailing-test1.mysql.database.azure.com \
--database test \
--user retailing880@retailing-test1 \
--ssl_ca /home/polastrijeff/BaltimoreCyberTrustRoot.crt.pem -p