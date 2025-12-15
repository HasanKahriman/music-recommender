import customtkinter as ctk
import pandas as pd
import os
from reccomender import MusicRecommender

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class MusicApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Muzik Öneri Motoru")
        self.geometry("700x550")
        self.resizable(False,False)
        
        current_dir=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(current_dir, "..","data","spotify_tracks.csv")
        
        try:
            print("🎵 Müzik öneri motoru başlatılıyor...")
            self.df=pd.read_csv(file_path)
            self.reccomender=MusicRecommender(self.df)
            print("Veri başarıyla yüklendi ve motor hazır.")
            self.data_ready=True
        except :
            self.data_ready=False
            print(f"❌ Hata: Veri dosyası bulunamadı.")

        self.create_widgets()

    def create_widgets(self):
        self.title_label=ctk.CTkLabel(self,text="🎵 Müzik Öneri Motoru",font=ctk.CTkFont(size=26,weight="bold"))
        self.title_label.pack(pady=20)
    
        self.subtitle_label=ctk.CTkLabel(self,text="114.000'den fazla şarkı arasından sevdiğin şarkıya benzer öneriler al!",font=ctk.CTkFont(size=14))
        self.subtitle_label.pack(pady=(0,20))

        self.input_frame=ctk.CTkFrame(self)
        self.input_frame.pack(pady=10,padx=30,fill="x")

        self.song_entry=ctk.CTkEntry(self.input_frame,placeholder_text="Örn: Blinding Lights",width=350)
        self.song_entry.pack(side="left",padx=(20,10),pady=20)

        self.search_button=ctk.CTkButton(self.input_frame,text="Önerileri Getir",command=self.run_recommendation)
        self.search_button.pack(side="left",padx=10)

        self.result_textbox=ctk.CTkTextbox(self,width=700,height=300,font=("Consolas", 12),wrap="none")
        self.result_textbox.pack(pady=20)

        self.result_textbox.insert("0.0","Yukarıya sevdiğin bir Türkçe şarkı adını gir ve butona tıkla.\n\n(Örnekler: Sicko Mode, Bohemian Rhapsody, Bad Guy ")
        self.result_textbox.configure(state="disabled")

    def run_recommendation(self):
        if not self.data_ready:
            self.show_result("❌ Hata: Veri yüklenemedi. Lütfen 'data' klasörünü kontrol et.")    
            return 

        user_song = self.song_entry.get()
        
        if user_song.strip() == "":
            self.show_result("⚠️ Lütfen geçerli bir şarkı adı girin.")
            return
        
        self.search_button.configure(state="disabled",text="Öneriler Getiriliyor...")
        self.update()

        try:
            result = self.reccomender.recommend(user_song)
            if isinstance(result, str):
                self.show_result(result)
            else:
                formatted_result = f"🎉 '{user_song}' için benzer şarkılar:\n\n"
                
                header = f"{'ŞARKI':<30} {'SANATÇI':<25} {'TÜR':<15} {'BPM':<5}"
                formatted_result += header + "\n"
                formatted_result += "-" * 80 + "\n" 

                for index, row in result.iterrows():
                    song_name = str(row['Şarkı'])
                    if len(song_name) > 28:
                        song_name = song_name[:28] + ".."
                    
                    artist_name = str(row['Sanatçı'])
                    if len(artist_name) > 22:
                        artist_name = artist_name[:22] + ".."
                    
                    try:
                        bpm_val = int(float(row['BPM']))
                    except:
                        bpm_val = str(row['BPM'])

                    line = f"{song_name:<30} {artist_name:<25} {str(row['Tür']):<15} {str(bpm_val):<5}"
                    formatted_result += line + "\n"

                self.show_result(formatted_result)
                
            
        except Exception as e:
            self.show_result(f"❌ Bir hata oluştu: {e}")
        finally:
            self.search_button.configure(state="normal",text="Önerileri Getir")
        
    def show_result(self, message):
        self.result_textbox.configure(state="normal")  # Kilidi aç
        self.result_textbox.delete("0.0", "end")       # Önceki metni sil
        self.result_textbox.insert("0.0", message)      # Yeni metni ekle
        self.result_textbox.configure(state="disabled") # Tekrar kilitle
    
if __name__ =="__main__":
    app=MusicApp()
    app.mainloop()