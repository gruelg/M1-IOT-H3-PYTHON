for F in $(ls)
do
    if [[ -f $F ]]
    then
    if [[ -s $F ]]
    then
        echo "Fichier ; " $F
        echo "Ligne(s) :" `wc -l < $F`
        echo "Mot(s) :" `wc -w < $F`
        echo ""
    fi
    fi
done