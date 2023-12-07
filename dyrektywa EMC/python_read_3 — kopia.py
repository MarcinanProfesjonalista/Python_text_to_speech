

import pyttsx3
import re #regexy
import threading


    

f = open("Python_czyta.txt", "r",encoding="utf8")
rep = {" EN ": "Europejska Norma",
       " itp. ": " i tym podobne ",
       "UWAGA 1":"UWAGA pierwsza,",
       "UWAGA 2":"UWAGA druga,",
       "UWAGA 3":"UWAGA trzecia,",
       "UWAGA 4":"UWAGA czwarta,",
       "UWAGA 5":"UWAGA piąta,",
       "UWAGA 6":"UWAGA szusta,",
       "UWAGA 7":"UWAGA siudma,",
       "UWAGA 8":"UWAGA ósma,",
       " IEC ":"normy",
       " V ":"Volt",
       " 1 s ":"jedna sekunda",
       "61000":"sześdziesiąt jeden tysięcy",
       #"§":"paragraf",
       " ust. ":" ustęp ",
       "Dz. U.":"dziennik ustaw",
       " poz. ":"pozycja",
       " nr ":" numer ",
       #" r. ":" roku ",
       " str. ":" strona ",
       "Dz. Urz. UE":"Dziennik urzędowy Unii Europejskiej",
       "1)":"punkt pierwszy",
       "2)":"punkt drugi",
       "3)":"punkt trzeci",
       "4)":"punkt czwarty",
       "5)":"punkt piąty",
       "6)":"punkt szusty",
       "7)":"punkt siudmy",
       "8)":"punkt ósmy",
       "Poz.":"Pozycja",
       " art.":" artykuł",
       " m2":" metrów kwadratowych",
       " m3":" metrów sześciennych",
       " r. ":" ",
       " .":""
       
       }

#to zamienia jednopunkotowe akapity 
regexy ={#r"\n\d\.\d\s": "", 
         #r"\n\d\.\d\.\d\s": "",
         #r"\n\d\.\d\.\d\.\d\s": "",
         #r",\s*\n":", ",
         #r"\n(?![§\d])":"",
         r"Dziennik Ustaw – \d – Poz. 1065":"",
         #r"\n[a-z]":"",
         r"\sCE\.":"CE,"
         #r"\d\.":" ",
         #r"\b\d{1}\b\)":" "
        }

#to splituje po rozdziałach
f =f.read()
for x,y in rep.items():
    f = f.replace(x, y)

for x,y in regexy.items():
    f = re.sub(x, y,f)

i=1
#lista_plikow = re.split("\n\d\s|\n\d\d\s",f)
#lista_plikow = re.split(r"ROZDZIAŁ",f)
lista_plikow = f.splitlines()
print(lista_plikow[0])

def read_text_and_save(text, name):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.save_to_file(text , name)
    engine.runAndWait()
    engine.stop()
    
    
def get_audio_length(file_path):
    # Wczytaj plik audio
    audio = AudioSegment.from_file(file_path)
    # Uzyskaj długość w milisekundach
    length_in_ms = len(audio)
    # Przekształć długość na bardziej czytelną formę
    length_in_sec = length_in_ms / 1000.0

    return length_in_sec

for x in (lista_plikow):
    nazwa_pliku = "("+str(i)+").mp3"
    read_text_and_save(x,nazwa_pliku)
    
    print(str(i)+"/"+str(len(lista_plikow)))
    i=i+1
    

    #



