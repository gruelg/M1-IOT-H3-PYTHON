#a mettre dans le fichier /home/<user>/.bashrc

function gitacp () 
{
  echo git status
  echo Continuer ? [Y\/N]
  read varClavier
  if [[ $varClavier == "Y" ]]; 
  then
    git add * 
	  git commit -m "$@" 
	  git push -u origin master 
  else 
    exit 
  fi 
}