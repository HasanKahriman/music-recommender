import pandas as pd
import os
from reccomender import MusicRecommender

current_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(current_dir, "..","data","songs.csv")

def load_data():
    try:
        df=pd.read_csv(file_path)
        print("Data loaded successfully")
        

        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    
if __name__ == "__main__":
    print("🎵Müzik öneri motoru başlatılıyor...")
    df=load_data()
    if df is not None:
        print(f"Toplam {len(df)} şarkı yüklendi.")

        print("\n--- Örnek Şarkılar: Blinding Lights, Bohemian Rhapsody, Sicko Mode ---")
        user_song=input("Hangi şarkıyı seviyorsun : ")
        print(f"\n🎧 '{user_song}' şarkısını sevenler şunları da seviyor...\n")
        my_recommender = MusicRecommender(df) 
        result = my_recommender.recommend(user_song)

        print(result)
else :
    print("Veri yüklenemedi...")

