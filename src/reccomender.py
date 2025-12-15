import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

class MusicRecommender:
    def __init__(self, df: pd.DataFrame):
        self.df=df.copy()
        self.df=self.df.dropna()
        self.df=self.df.drop_duplicates(subset=['song_name'])
        self.df.reset_index(drop=True,inplace=True)
        self.df['track_name_lower']=self.df['track_name'].str.lower()
        self.feature_clos=['Danceability','energy','tempo','popularity','valence']
        scaler=MinMaxScaler()
        self.feature_matrix=scaler.fit_transform(self.df[self.feature_cols])
    def recommend(self,song_name: str,top_n : int=5):
        song_name=song_name.lower().strip()
        matches=self.df[self.df['track_name_lower'==song_name]]
        if matches.empty:
            return f"⚠️ Uyarı: '{song_name}' adlı şarkı veri setinde bulunamadı."
        target_index=matches.index[0]
        target_vector=self.feature_matrix[target_index].reshape(1.-1)
        sim_scores=cosine_similarity(target_vector,self.feature_matrix).flatten()
        sorted_indices=sim_scores.argsort()[::-1]
        top_indices=sorted_indices[1:top_n+1]
        recommendations=self.df.iloc[top_indices][['track_name','artist','track_genre','tempo']]
        recommendations.columns=['Şarkı','Sanatçı','Tür','BPM']
        return recommendations
    

    

        