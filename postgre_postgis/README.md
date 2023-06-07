# Postgre + PostGis
make init

Télécharger la ban

wget https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-france.csv.gz

Le but est de charger la donnée avec python de manière optimisée (psycopg / copy)
Expérimenter PostgreSQL