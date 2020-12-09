import pandas as pd


class DataHandler:
    """
        recuperer les data du GCP bucket
    """
    def __inti__(self):
        self.df_listings_final = None
        self.df_price_availability = None
        self.df_merged = None

    def get_data(self):
        """
            charge les datasets des csv
        """
        self.df_listings_final = pd.read_csv('listings_final.csv', delimiter=";", index_col=0)
        self.df_price_availability = pd.read_csv('price_availability.csv', delimiter=';')
        # self.df_listings_final = pd.read_csv('https://storage.googleapis.com/h3-data/listings_final.csv', delimiter=";",index_col = 0)
        # self.df_price_availability = pd.read_csv('phttps://storage.googleapis.com/h3-data/price_availability.csv', delimiter=';')
        print("Datasets chargés ")

    def group_data(self):
        """
            merge les 2 dataset sur la colonne listing_id
        """
        resultMeans = self.df_price_availability.groupby('listing_id').mean()
        resultMeans['listing_id'] = self.df_price_availability['listing_id'].unique()
        self.df_merged = pd.merge(self.df_listings_final, resultMeans[['available', 'local_price', 'min_nights']],
                                  on='listing_id')
        print("dataset merged")

    def get_process_data(self):
        """
            get_data() + group_data()
        """
        self.get_data()
        self.group_data()

