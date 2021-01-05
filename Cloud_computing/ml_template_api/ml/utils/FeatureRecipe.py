import pandas as pd
import numpy as np


class FeatureRecipe:

    def __init__(self, data):
        self.df = data
        self.categories = []
        self.floats = []
        self.int = []
        self.drop = []

    def dropNaNPourcentage(self, seuil):
        """
            drop la colonne suivant un seuil %( param)
        """
        for colonne in self.df:
            nbNaN = self.df[colonne].isna().sum()
            if (nbNaN / self.df.shape[0]) * 100 > seuil:
                del self.df[colonne]
                print('{} supprimée'.format(colonne))

    def dropUselessFeature(self):
        to_drop = [] # a remplir suivant les colonnes qui sont inutiles
        self.df.drop(columns=to_drop, inplace=True)
        for colonne in self.df:
            if self.df[colonne].nunique() <= 1:
                print('{} supprimée'.format(colonne))
                del self.df[colonne]

    def dropDuplicates(self):
        """
            drop des duplica de colonnes
        """
        i = 0
        for colonnes in self.df:
            i += 1
            y = 0
            for colonnesDuplicate in self.df:
                y += 1
                if i != y and (self.df[colonnes].equals(self.df[colonnesDuplicate])) == True:
                    del self.df[colonnesDuplicate]
                    print('colonne {} supprimée'.format(colonnesDuplicate))

    def separeteVariableTypes(self):
        print("separating columns")
        for colonne in self.df.columns:
            if self.df[colonne].dtypes == int:
                self.int.append(self.df[colonne])
            elif self.df[colonne].dtypes == float:
                self.floats.append(self.df[colonne])
            else:
                self.categories.append(self.df[colonne])
        print("nombre de colonnes : {} \n \
            number of discreet values : {} \n \
            number of continuous values : {} \n \
            number of others : {} \n  \
            taille total : {}".format(len(self.df.columns), len(self.int), \
                                      len(self.floats), len(self.categories),
                                      len(self.int) + len(self.floats) + len(self.categories)))

    def prepareData(self, seuil):
        self.dropUselessFeature()
        self.dropDuplicates()
        self.dropNaNPourcentage(seuil)
        self.separeteVariableTypes()