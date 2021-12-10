from gtts import gTTS
import os
import webbrowser
def sonastik():
        sonastik={}
        countries=[]
        capitals=[]
        file=open("countries-.txt","r")
        for line in file:
            k, v=line.strip().split("-")
            sonastik[k.strip()]=v.strip()
            countries.append(k)
            capitals.append(sonastik[k.strip()])
        file.close()
        print(sonastik)
        print("Countries: ")
        print(countries)
        print("Capitals:")
        print(capitals)
        s=gTTS(text=capitals[6],lang="en",slow=True).save("countries.mp3")
        os.system("countries.mp3")
        a=input()