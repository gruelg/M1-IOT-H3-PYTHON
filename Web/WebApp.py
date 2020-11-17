import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

@st.cache
def load_data(name, pEncoding=''):
    if pEncoding != '':
        return pd.read_csv(str(name), encoding=str(pEncoding))
    else:
        return pd.read_csv(str(name))
def genGraph(dataframe, colonne,):
    plt.hist(dataframe[colonne])
    st.pyplot()

#Titre de l'application et header
st.title("Data app")
data = [load_data('movies.csv', 'latin1')]
data.append(load_data('pokemon.csv'))
nomData = ['Films','Pokemon']

for i in range(len(data)):
    st.sidebar.header("DataSet sur les {}".format(nomData[i]))
##affichage du contenu du csv si checkbox cochée et nb de ligne fourni
    if st.sidebar.checkbox("afficher le dataframe {}".format(nomData[i])):
        st.header("DataSet sur les {}".format(nomData[i]))
        number = st.number_input("Selectionner un nombre de lignes")
        st.dataframe(data[i].head(int(number)))
        #affichage du nom de toutes les colonnes en cliquant sur le bouton
        if st.button("Noms des colonnes"):
            st.write(data[i].columns.tolist())
    #afichage du type des colonnes
    if st.sidebar.checkbox("afficher les types des colonnes {}".format(nomData[i])):
        st.dataframe(data[i].dtypes)
    #affichage du shape du csv
    if st.sidebar.checkbox("afficher les shapes du dataset {}".format(nomData[i])):
        st.dataframe(data[i].shape)
    #descirption du csv
    if st.sidebar.checkbox("afficher la description du dataset {}".format(nomData[i])):
        st.dataframe(data[i].describe())
    #affichage de la heatmap
    if st.sidebar.checkbox("afficher la Heatmap {}".format(nomData[i])):
        plt.title('Heatmap dataset {}'.format(nomData[i]), fontsize=20)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.write(sns.heatmap(data[i].corr().astype(float).corr(),vmax=1.0, annot=True))
        st.pyplot()
    #affichage graph
    if st.sidebar.checkbox("afficher le graph {}".format(nomData[i])):
        plt.title('histogramme')
        if i == 0:
            plt.hist(data[i]['year'], bins=26)
        else:
            plt.hist(data[i]['attack'])
        st.pyplot()
    if st.sidebar.checkbox("generer un graphique {}".format(nomData[i])):
        listeBouton = data[i].columns.tolist()
        for i in range(len(listeBouton)):
            if st.button(listeBouton[i]):
                genGraph(data[i], listeBouton[i])


