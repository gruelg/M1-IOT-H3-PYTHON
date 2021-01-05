import pandas as pd


class DataHandler:
    """
        chargement du dataset dans une classe
    """
    def __inti__(self):
        self.df_vgsales

    def get_data(self):
        """
            charge les datasets des csv
        """
        self.df_vgsales = pd.read_csv('vgsales.csv', delimiter=",", index_col=0)
        print("Dataset chargés ")

