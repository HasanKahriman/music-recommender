import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class MusicRecommender:
    def __init__(self, df):
        self.df=df
    def recommend(self,song_name,top_n=5):
        df_lower=self.df.copy()
        df_lower['song_name_lower']=df_lower['song_name'].str.lower()
        song_name=song_name.lower()

        if song_name not in df_lower['song_name_lower'].values:
            return f"❌ Hata: '{song_name}' listede bulunamadı!"
        song_index=df_lower[df_lower['song_name_lower']==song_name].index[0]
        features=self.df[['bpm','energy','danceability','popularity']]   
        similarity_matrix=cosine_similarity(features)
        song_scores=similarity_matrix[song_index]
        sorted_indices=song_scores.argsort()[::-1][1:top_n+1]

        recommendations=self.df.iloc[sorted_indices][['song_name', 'genre', 'bpm']]
        return recommendations