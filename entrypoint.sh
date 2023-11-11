cp /etc/production.ini /etc/production.ini.tmp
envsubst \$DB_CONNECTION_STRING < /etc/production.ini.tmp > /etc/production.ini
rm /etc/production.ini.tmp
pserve /etc/production.ini
