import os
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import google.generativeai as genai
from pathlib import Path
import time

def save_load(videoname=""):
    file = (open("Genral_Infos/Uploaded_Videos.txt", "r").read()).split("\n")
    forwrite = open("Genral_Infos/Uploaded_Videos.txt", "a")
    if videoname != "":
        if videoname in file:
            return False
        else:
            forwrite.write(f"{videoname}\n")
            return True
    return file

def TookAllVideos():
    videos = os.listdir("Videos")
    paths = []
    for path_for in videos:
        pather = str(Path(f"Videos/{path_for}").resolve().as_posix())
        paths.append(pather)

    return (videos , paths)


Uploaded_Files = save_load()

class AI:
    def __init__(self,API):
        self.api = API
 

    def Ask(self,promt):
        genai.configure(api_key=self.api)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(promt)
        return (response.text)



class Youtube_Upload:
    def __init__(self):
        self.youtube = self.get_authenticated_service()


    def get_authenticated_service(self):
        CLIENT_SECRETS_FILE = "client_secrets.json"  # OAuth 2.0 istemci kimliği dosyası
        SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

        # OAuth akışını başlat
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, SCOPES
        )
        
        # Tarayıcıda yerel bir sunucu açarak kullanıcıyı yetkilendir
        credentials = flow.run_local_server(port=8080)  
        return build("youtube", "v3", credentials=credentials)

    def upload_video(self,file_path, title, description,video_tags="", category_id="22", privacy_status="public"):
        if save_load(title):
            

            # Yüklenecek video dosyasını belirtin
            media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

            # Video meta verilerini belirleyin
            request_body = {
                "snippet": {
                    "title": title,
                    "description": description,
                    "categoryId": category_id,
                    "tags": video_tags
                },
                "status": {
                    "privacyStatus": privacy_status,  # "public", "private" veya "unlisted"
                },
                "madeForKids": False
            }

            # Video yükleme isteği gönder
            request = self.youtube.videos().insert(
                part="snippet,status",
                body=request_body,
                media_body=media,
            )
            response = request.execute()  # İsteği çalıştır
            print(f"Video başarıyla yüklendi: https://www.youtube.com/watch?v={response['id']}")
            save_load(title)
        else:
            print(f"Already Uploded : {title}")

    


Video_Names , Video_Paths = TookAllVideos()
ai = AI(API="AIzaSyAEmfhYB--XuyPAlZDtBbRz9Skou4BdhRU")
yt = Youtube_Upload()
Delay = 300


for video_name , vide_pths in zip(Video_Names,Video_Paths):
    #print(video_name,vide_pths)
    time.sleep(Delay)
    video_dcp_ai = (ai.Ask(f"{video_name} isimli youtube short videom için etkileşim arttırıcı bir açıklama yazar mısın ? Sadece açıkama olsun lütfen"))
    yt.upload_video(file_path=vide_pths,description=video_dcp_ai,title=video_name[:-9])
    