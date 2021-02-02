#Installation d'un container mysql 

`docker pull mysql:<version>`

`docker run --name M1-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:5.6`

`docker exec -i M1-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < C:\Users\gruel\Downloads\bdd.sql`

mysql  --user=root --password my-secret-pw

#Créer un utilisateur et afficher ses autorisations 

`CREATE USER 'ggul'@'localhost' IDENTIFIED BY 'hitema';`

## autorisations 

`GRANT ALL PRIVILEGES ON * . * TO 'ggul'@'localhost';`

### afficher les utilisateurs

`select user,host from mysql.user;`

###afficher les droits d'un utilisateur 

`show grants for "ggul"@"localhost";`