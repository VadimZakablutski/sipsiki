
#def pealinn():
#    for country in Countries:
#        country=input("Введите страну: ")
#        if country in Capitals:
#            print("Столица страны "+country+": " +Capitals[country])
#            p=input("Возможно в базе данных ошибка, хотите исправить её? ")
#            if p=="Да":
#                o=input("Введите правильно страну: ")
#                l=input("Введите правильно столицу: ")
#                Capitals.pop(country)
#                Capitals.update({o: l})
#            elif p=="Нет":
#                print("Всего доброго!")
#        else:
#            print("В базе данных не страны с названием " +country)
#            v=input("Хотите внести " +country+ " в базу данных?: ")
#            if v=="Да":
#                ca=input("Введите столицу страны "+country)
#                Capitals.update({country: ca})
#            elif v=="Нет":
#                print("Всего доброго!")
#        p=input("Хотите ли пройти тест на знания столиц Европы? Да или Нет? ")
#        if p=="Да":
#            Countries.sort()
#            Countries.reverse()
#            m=0
#            for i in range(10):
#                print(choices(Countries))
#                st=input("Введите столицу: ")
#                if st in Capitals:
#                        print("Правильно!")
#                        m+=1
#                else:
#                    print("Неправильно!")
#            if m==0:
#                print("0%")
#            elif m==1:
#                print("10%")
#            elif m==2:
#                print("20%")
#            elif m==3:
#                print("30%")
#            elif m==4:
#                print("40%")
#            elif m==5:
#                print("50%")
#            elif m==6:
#                print("60%")
#            elif m==7:
#                print("70%")
#            elif m==8:
#                print("80%")
#            elif m==9:
#                print("90%")
#            elif m==10:
#                print("100%")
#        if p=="Нет":
#            print("Всего доброго!")
