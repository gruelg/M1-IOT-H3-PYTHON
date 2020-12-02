## Commandes : 

docker build : construit l'image d'un conteneur d'apres un fichier dockerfile 

docker run : lance un conteneur 

docker exec : execute une commande dans un conteneur 

docker images : liste la totalité des images dockers present sur la machine 

docker ps : list les container 

docker stop : arret un+ container 

docker rm : suppr de 1+ container

docker rmi : suppr de 1+ images

##build image du TP 

docker build tpdocker/ --tag tp
!!!! ne pas mettre de maj au dossier utilisé pour build l'image ni au tag 

##demarrage d'un container 

docker run --publish <n°portHote>:<n°portContainer> --name TPDocker tp 
docker run  --publish 127.0.0.1:5000:0.0.0.0:5000 --name tpdocker tp 
le param --publish permet d'autoriser la communication avec le port de l'hote et celui du container. 

le param --name attribut un nom a l'instance du container qui vient de démarrer 