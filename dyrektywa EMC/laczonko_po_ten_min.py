from pydub import AudioSegment
#from pydub.generators import AudioSegmentGenerator
import os
import re

def group_files_by_price(files_info, target_sum):
    grouped_files = []
    current_group = []
    current_sum = 0

    for file_info in files_info:
        file_name, file_price = file_info

        # Sprawdź, czy dodanie pliku nie przekroczy docelowej sumy
        if current_sum + file_price <= target_sum:
            current_group.append(file_name)
            current_sum += file_price
        else:
            # Jeśli dodanie pliku przekroczyłby docelową sumę, rozpocznij nową grupę
            grouped_files.append(current_group)
            current_group = [file_name]
            current_sum = file_price

    # Dodaj ostatnią grupę, jeśli istnieje
    if current_group:
        grouped_files.append(current_group)

    return grouped_files

def concatenate_audio(files_list, output_file, spacer_file=None):
    # Inicjalizacja pustego segmentu, który będzie wynikiem połączenia
    result = AudioSegment.silent(duration=0)

    # Iteracja przez listę plików audio
    for file_path in files_list:
        # Wczytanie pliku audio
        audio = AudioSegment.from_file(file_path)

        # Dodanie pliku audio do wynikowego segmentu
        result += audio

        # Jeśli istnieje plik spacerowy i file_path nie jest ostatni w liście, dodaj go
        if spacer_file and file_path != files_list[-1]:
            spacer = AudioSegment.from_file(spacer_file)
            result += spacer

    # Zapisz wynikowe połączenie do pliku
    result.export(output_file, format="mp3")

def get_audio_durations_in_folder(input_folder):
    audio_durations = []
    i=0

    # Iteracja przez pliki w folderze
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            print(i)
            i=i+1
            file_path = os.path.join(input_folder, filename)

            # Wczytanie pliku audio
            audio = AudioSegment.from_file(file_path)

            # Długość pliku w sekundach
            duration_in_seconds = len(audio) / 1000.0

            # Dodanie krotki do listy
            audio_durations.append((file_path, duration_in_seconds))

    return audio_durations

def get_mp3_files(folder_path):
    #mp3_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]
    #return mp3_files
    # Pobierz listę plików w folderze
    files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]

    # Użyj funkcji sortującej z własnym kluczem
    sorted_files = sorted(files, key=lambda x: int(re.search(r'\((\d+)\)', x).group(1)) if re.search(r'\((\d+)\)', x) else float('inf'))
    

    return sorted_files

def get_mp3_duration(mp3_file_path):
    # Wczytaj plik mp3
    audio = AudioSegment.from_file(mp3_file_path)

    # Oblicz długość w sekundach
    duration_in_seconds = len(audio) / 1000.0

    return duration_in_seconds


spacer_file_path = "1sec_silence.mp3"
folder_path = os.path.dirname(os.path.abspath(__file__))
tablica_nazw_audio = get_mp3_files(folder_path)
tablica_nazw_i_dlugosci = []
for item in tablica_nazw_audio:
    print(f"Plik: {item}")

for x in tablica_nazw_audio:
    tablica_nazw_i_dlugosci.append([x,get_mp3_duration(x)])

for item in tablica_nazw_i_dlugosci:
    print(f"Plik: {item[0]}, Długość: {item[1]:.2f} sekundy")



target_sum = 670
grouped_files = group_files_by_price(tablica_nazw_i_dlugosci, target_sum)
print("Zgrupowane pliki:")
j=1
for group in grouped_files:
    nazwa_pliku = "part "+str(j)+".mp3"
    concatenate_audio(group,nazwa_pliku)
    print(str(j)+"/"+str(len(grouped_files)))
    j=j+1

