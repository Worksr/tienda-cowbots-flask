Aqui Usamos una app web muy simple con Flask y PostgreSQL para hacer el backend de una tienda en linean de los Cowboys

Usamos: 
Python
Flask
PostgreSQL (AWS RDS) Docker 
EC2 de AWS con el AMI Amazon Linux 2
DBeaver
Postman pero la pagina web
Github, evidentemente.

Para usar, installamos dependencias sin Docker con estos comandos:
pip install -r requirements.txt
python3 app.py

Luego pegamos esto para ejecutar con Docker:
docker build -t tienda-cowboys-app .
docker run -d -p 5000:5000 tienda-cowboys-app

Tenemos los endpoints:
GET/items
POST/items

Para el post seria el formato:
{
  "name": "X cosa",
  "price": X precio 
}

En el EC2 abrimos los puertos 22, 80, 443, y 5000, vamos a ocupar la clave PEM y solamente se aceptaran conexiones desde la EC2
