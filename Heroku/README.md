#WorkFlow 

Heroku est une plateforme qui permet de construire, déployer et d'utiliser une application dans le could 

# Upload 

## projet 

1 - heroku create : aller dans le dossier de l'image et créer une app heroku 
2 - git push heroku main : un acces remote au git keroku est créer en meme temps que la creation de l'app 
3 - heroku ps:scale web=1 : créer le nombre d'instance de l'application 
4 - heroku open : ouvre l'application elle est mainteant accessible partout 

https://tranquil-lowlands-64761.herokuapp.com/

## images docker 

1 - heroku container:login : s'identifier 
2 - heroku create : aller dans le dossier de l'image et créer une app heroku 
3 - heroku container:push web --app <nomApplication> 
4 - heroku container:release web --app <nomApplication>
5 - heroku open --app <nomApplication>

https://enigmatic-fortress-38688.herokuapp.com/


### en cas d'erreur(s) 

$ heroku logs -tail 