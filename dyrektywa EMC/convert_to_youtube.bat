@echo off

setlocal enabledelayedexpansion

set "total_files=0"
for %%I in (*.mp3) do (
    set /a "total_files+=1"
)

set "i=0"

for %%I in (*.mp3) do (
    set /a "i+=1"
    
    set "output_file=Dyrektywa EMC %%~nI.mkv"

    rem Wywołanie FFmpeg dla konwersji (w tle)
    start "" ffmpeg -loop 1 -framerate 2 -i "Dyrektywa EMC.jpg" -i "%%I" -c:a libx264 -preset medium -tune stillimage -crf 18 -c:a copy -shortest -pix_fmt yuv420p "!output_file!"

    rem Obliczanie postępu i wyświetlanie paska
    set /a "progress=i * 100 / total_files"
    echo Progress: !progress!%%
)

echo Conversion complete!