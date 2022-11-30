# brojevi=[9,2,5,6,7,]
# # brojevi.sort()
# brojevi.reverse()

# # print(brojevi)

# brojevi=[9,2,5,6,7,1,3,4,8]
# while True:
# #     izvrsena_zamena=False
# #     for i in range(1,len(brojevi)):
# #     # print(brojevi[i],"poredim sa",brojevi[i-1])
# #         if brojevi[i]<brojevi[i-1]:
# #             privremena=brojevi[i]
# #             brojevi[i]=brojevi[i-1]
# #             brojevi[i-1]=privremena
# #             izvrsena_zamena=True
# #     if izvrsena_zamena==False:
# #         break
# # print(brojevi)


# # proizvodi=["automobil","tv","laptop"]
# # cena=[100,200,300]

# # for i in range(len(proizvodi)):
# #     print(proizvodi[i],cena[i])


# # automobili=["audi","bmw","ford","kia"]

# # for i in range(len(automobili)):
# #     if i==3:
# #         print (automobili[i])


# proizvodi=[
#     ["ajfon 11","samsug s21","xaomix3"],
#     ["acer","dell","mecbook"],
#     ["iped","samsung tab","xaomi tablet"]

# ]



# telefoni=["ajfon 11","samsug s21","xaomix3"]

# laptop=["acer","dell","mecbook"]

# tableti=["iped","samsung tab","xaomi tablet"]

# # # proizvodi=[telefoni,laptop,tableti]
# # print(proizvodi[0][0])
# # print(proizvodi[1][1])


# # for kategorija in proizvodi:
# #     for stavka in kategorija:

# #         print(kategorija)

#     # print(kategorija[0])
#     # print(kategorija[1])
#     # print(kategorija[2])


# for i in range(len(proizvodi)):
#     print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])



# hrana=[        
#          ["cokolade","bombone","[a;acinke"],
#          ["sarma","pljeskavica","pasulj"],
#          ["salata","paprika","kupus"]
#         ]
# for kategorija in hrana:
#     for jela in kategorija:
#         print("naziv:",jela)


biblioteka = [

]

while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige, preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        #ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")




