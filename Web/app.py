import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

#Titre de l'application et header
st.title("Data app")
st.header("DataSet sur les films ")

#lecture des dataset utilisé par la web app
dataMovies = pd.read_csv('movies.csv', encoding='latin1')
dataPokemons = pd.read_csv('pokemon.csv')


number = st.number_input("Selectionner un nombre de lignes")
st.dataframe(dataMovies.head(int(number)))
if st.checkbox("afficher les types des colonnes "):
    st.dataframe(dataMovies.dtypes)
if st.checkbox("afficher les shapes du dataset "):
    st.dataframe(dataMovies.shape)
if st.checkbox("afficher la description du dataset "):
    st.dataframe(dataMovies.describe())
if st.checkbox("afficher la Heatmap "):
    plt.title('Heatmap dataset Films ', fontsize=20)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write(sns.heatmap(dataMovies.corr().astype(float).corr(),vmax=1.0, annot=True))
    st.pyplot()
if st.checkbox("afficher le graph "):
    plt.xlabel('année ')
    plt.ylabel('budget')
    plt.title('histogramme')
    plt.hist(dataMovies['year'], bins=26)
    st.pyplot()


st.header("DataSet sur les pokemons ")
numberPokemon = st.number_input("Selectionner un nombre de lignesd")
st.dataframe(dataPokemons.head(int(numberPokemon)))
if st.checkbox("afficher les types des colonnes2 "):
    st.dataframe(dataPokemons.dtypes)
if st.checkbox("afficher les shapes du dataset 2"):
    st.dataframe(dataPokemons.shape)
if st.checkbox("afficher la description du dataset 2"):
    st.dataframe(dataPokemons.describe())
if st.checkbox("afficher la Heatmap 2"):
    plt.title('Heatmap dataset Pokemon ', fontsize=20)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write(sns.heatmap(dataPokemons.corr().astype(float).corr(),vmax=1.0, annot=True))
    st.pyplot()

if st.checkbox("afficher le graph 2"):
    plt.title('histogramme')
    plt.hist(dataPokemons['attack'])
    st.pyplot()

#st.title("Streamlit Crash course")
#st.header("Simple Header")
#st.subheader("Another sub header")
#st.sidebar.header("Example de Side Bar")
#st.sidebar.text("Hello")
#st.text("For a simple text")
#st.markdown("#### A Markdown ")
#st.success("Successful")
#st.info("This is an info alert ")
#st.warning("This is a warning ")
#st.error("This shows an error ")
#st.write("Text with write")
#st.write("Python Range with write",range(10))
#st.text("Display JSON")
#dico={'name':'hello','age':34}
#st.json(dico)