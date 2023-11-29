import pyttsx3
import re #regexy
import threading

def read_text_and_save(text,name):
    #engine = pyttsx3.init()
    #engine.setProperty('rate', 140)
    #engine.save_to_file(text , name)
    #engine.runAndWait()
    print("finito")
    

f = open("Python_czyta.txt", "r",encoding="utf8")
rep = {"EN": "Europejska Norma",
       "itp.": "i tym podobne",
       "UWAGA 1":"UWAGA pierwsza,",
       "UWAGA 2":"UWAGA druga,",
       "UWAGA 3":"UWAGA trzecia,",
       "UWAGA 4":"UWAGA czwarta,",
       "UWAGA 5":"UWAGA piąta,",
       "UWAGA 6":"UWAGA szusta,",
       "UWAGA 7":"UWAGA siudma,",
       "UWAGA 8":"UWAGA ósma,",
       "IEC":"normy",
       "V":"Volt",
       "1 s":"jedna sekunda",
       "61000":"sześdziesiąt jeden tysięcy"
       }

#to zamienia jednopunkotowe akapity 
regexy ={r"\n\d\.\d\s": "", 
         r"\n\d\.\d\.\d\s": "",
         r"\n\d\.\d\.\d\.\d\s": "",
    
           }

#to splituje po rozdziałach


f =f.read()
for x,y in rep.items():
    f = f.replace(x, y)

for x,y in regexy.items():
    f = re.sub(x, y,f)

i=0
lista_plikow = re.split("\n\d\s|\n\d\d\s",f)
#print(lista_plikow)

for x in (lista_plikow):
    nazwa_pliku = "rozdzial"+str(i)+".mp3"
    #a_thread = threading.Thread(target=read_text_and_save, args=[x,nazwa_pliku])
    #a_thread.start()
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.save_to_file(x , nazwa_pliku)
    engine.runAndWait()
    print(str(i)+"/"+str(len(lista_plikow)-1))
    i=i+1
    

    #



