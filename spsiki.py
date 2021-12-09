from module import*
from random import*
from time import*
Capitals=dict()
Capitals["Estonia"]="Tallinn"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Finland"]="Helsinki"
Capitals["France"]="Paris"
Capitals["Germany"]="Berlin"
Capitals["Sweden"]="Stockholm"
Capitals["Spain"]="Madrid"
Capitals["Serbia"]="Belgrade"
Capitals["Norway"]="Oslo"
Capitals["Moldova"]="Chisinau"
Capitals["Greece"]="Athens"
Capitals["Bulgaria"]="Sofia"
Capitals["Austria"]="Vienna"
Capitals["Switzerland"]="Bern"
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany","Sweden","Spain","Serbia","Norway","Moldova","Greece","Bulgaria","Austria","Switzerland"]
for country in Countries:
    country=input("Введите страну: ")
    if country in Capitals:
        print("Столица страны "+country+": " +Capitals[country])
    else:
        print("В базе данных нет страны с названием " +country)
        v=input("Хотите внести " +country+ " в базу данных?Да или Нет? ")
        if v=="Да":
            ca=input("Введите столицу страны " +country+": ")
            Capitals.update({country: ca})
            p=input("Возможно в базе данных ошибка, хотите исправить её? Да или Нет? ")
            if p=="Нет":
                print("Хорошо")
            if p=="Да":
                o=input("Введите правильно страну: ")
                l=input("Введите правильно столицу: ")
                Capitals.pop(country)
                Capitals.update({o: l})
        if v=="Нет":
            print("Хорошо")
    d=input("Хотите ли вы начать проговаривание слов для самостоятельного изучения? Да или Нет? ")
    if d=="Да":
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
        a=input()
    if d=="Нет":
        print("Хорошо")
    p=input("Хотите ли пройти тест на знания столиц Европы? Да или Нет? ")
    if p=="Да":
        Countries.sort()
        Countries.reverse()
        m=0
        for i in range(10):
            country=str(choice(Countries))
            print(country)
            st=input("Введите столицу: ")
            if st==Capitals[country]:
                print("Правильно!")
                m+=1
            else:
                print("Неправильно!")
        if m==0:
            print("0%")
        elif m==1:
            print("10%")
        elif m==2:
            print("20%")
        elif m==3:
            print("30%")
        elif m==4:
            print("40%")
        elif m==5:
            print("50%")
        elif m==6:
            print("60%")
        elif m==7:
            print("70%")
        elif m==8:
            print("80%")
        elif m==9:
            print("90%")
        elif m==10:
            print("100%")
    if p=="Нет":
        print("Всего доброго!")