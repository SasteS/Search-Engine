from parser_method import Parser
# os import *
import os
from adjacent_list import Graph
from sort import quick_sort


def pravi_putanju(graph):
    try:
        graph.vertices = {}
        unos = input("Unesite direktorijum koji zelite da pretrazite: ")

        putanja = os.path.abspath(unos)
  
        graph = parser.napravi_graf(putanja)
    except:
        print("Ne postoji direktorijum!")
        pravi_putanju(graph)
    pretraga(graph)


def pretraga(graph):
    #UNOS
    print("Opcija 1, 2? (1 - Obicna pretraga; 2 - AND, OR, NOT)\n")
    opcija = input("Opcija: ")
    while opcija != "1" and opcija != "2":
        print("Pogresno unet zahtev!")
        print("Opcija 1, 2? (1 - Obicna pretraga; 2 - AND, OR, NOT)\n")
        opcija = input("Opcija: ")

    if opcija == "1":
        search = input("  Search..  :   ").split(" ")
        if len(search) > 1:
            if search[1] == "AND" or search[1] == "OR" or search[1] == "NOT":
                print("Pogresan unos!")
                pretraga(graph)

        #OPCIJA DEFAULT
        rezultati = []
        broj_nadjenih_reci = 0
        for key in graph.vertices.keys():
            temp = graph.vertices[key]
            ukupan_broj_ponavljanja = 0
            broj_nadjenih_reci = 0
            for item in search:          
                temp_lista = temp.dict_ponavljanja.keys() #VECINSKI POPRAVLJENO
                if item in temp_lista:
                    broj_nadjenih_reci += 1
                    ukupan_broj_ponavljanja += temp.dict_ponavljanja[item]
            if broj_nadjenih_reci > 0:
                rezultati.append({key: [ukupan_broj_ponavljanja, len(temp.neighbors)]})
        if len(rezultati) != 0: #ZAKLJUCAK JE DA DOBRO RADI OVO PRAVLJENJE
            lista_quick_sorted = quick_sort(rezultati)
        else:
            print("Ne postoji zadata rec/fraza!")
            ponovna_pretraga(graph)


        broj_rezultata = input("Unesite broj rezuktata za prikaz(\"all\" za sve): ") 

    
        index = 1
        #ovde moze da se ubaci prikaz broja rezultata
        for item in lista_quick_sorted:
            for key in item:
                print(str(index) + ".) " + str(key))
                if index == 1:
                    reader = open(key, 'r')#O_RDONLY)
                    read_file = []
                    for line in reader.readlines():
                        temp = line.split(" ")
                        for word in temp:
                            read_file.append(word) #RADI
                    for word in read_file:
                        nasao = False
                        for stvar in search:
                            for letter in word:
                                if stvar.lower() == letter.lower() or stvar.lower() == word.lower():       
                                    nasao = True
                                    string = ""
                                    for i in range(read_file.index(word), read_file.index(word) + 10):
                                        string += read_file[i] + " "                                        
                                    print("------------------------------------------------------")
                                    print(string)
                                    print("------------------------------------------------------")
                                if nasao == True: break
                        if nasao == True: break
                    reader.close()
            if str(index) == broj_rezultata: break
            index += 1
    else:
        search = input("  Search..  :   ").split(" ")
        while len(search) < 3 or len(search) > 3:
            print("Pogresan unos!")
            search = input("  Search..  :   ").split(" ")

        if search[1] != "AND" and search[1] != "OR" and search[1] != "NOT":
            print("Pogresan unos!")
            pretraga(graph)

        #OPCIJA AND OR NOT
        if search[1] == "AND":
            rezultati = []
            search.remove("AND")
            broj_nadjenih_reci = 0
            for key in graph.vertices.keys():
                temp = graph.vertices[key]
                ukupan_broj_ponavljanja = 0
                #print(temp.dict_ponavljanja)
                broj_nadjenih_reci = 0
                for item in search:            
                    temp_lista = temp.dict_ponavljanja.keys() #VECINSKI POPRAVLJENO
                    if item in temp_lista:
                        broj_nadjenih_reci += 1
                        ukupan_broj_ponavljanja += temp.dict_ponavljanja[item]
                if broj_nadjenih_reci == 2:
                    rezultati.append({key: [ukupan_broj_ponavljanja, len(temp.neighbors)]})
            if len(rezultati) != 0: #ZAKLJUCAK JE DA DOBRO RADI OVO PRAVLJENJE
                lista_quick_sorted = quick_sort(rezultati)
            else:
                print("Ne postoji zadata kombinacija!")
                ponovna_pretraga(graph)

        elif search[1] == "OR":
            rezultati = []
            search.remove("OR")
            broj_nadjenih_reci = 0
            for key in graph.vertices.keys():
                temp = graph.vertices[key]
                ukupan_broj_ponavljanja = 0
                broj_nadjenih_reci = 0
                for item in search:           
                    temp_lista = temp.dict_ponavljanja.keys() #VECINSKI POPRAVLJENO
                    if item in temp_lista:
                        broj_nadjenih_reci += 1
                        ukupan_broj_ponavljanja += temp.dict_ponavljanja[item]
                if broj_nadjenih_reci > 0:
                    rezultati.append({key: [ukupan_broj_ponavljanja, len(temp.neighbors)]})
            if len(rezultati) != 0: #ZAKLJUCAK JE DA DOBRO RADI OVO PRAVLJENJE
                lista_quick_sorted = quick_sort(rezultati)
            else:
                print("Ne postoji zadata kombinacija!")
                ponovna_pretraga(graph)

        elif search[1] == "NOT":
            rezultati = []
            search.remove("NOT")
            broj_nadjenih_reci = 0
            for key in graph.vertices.keys():
                temp = graph.vertices[key]
                ukupan_broj_ponavljanja = 0
                prva_nadjena = False
                druga_nadjena = False       
                temp_lista = temp.dict_ponavljanja.keys() #VECINSKI POPRAVLJENO
                if search[0] in temp_lista:
                    prva_nadjena = True
                    ukupan_broj_ponavljanja += temp.dict_ponavljanja[search[0]]
                if search[1] in temp_lista:
                    druga_nadjena = True
                if prva_nadjena == True and druga_nadjena == False:
                    rezultati.append({key: [ukupan_broj_ponavljanja, len(temp.neighbors)]})
            if len(rezultati) != 0: #ZAKLJUCAK JE DA DOBRO RADI OVO PRAVLJENJE
                lista_quick_sorted = quick_sort(rezultati)        
            else:
                print("Ne postoji zadata kombinacija!")
                ponovna_pretraga(graph)

        broj_rezultata = input("Unesite broj rezuktata za prikaz(\"all\" za sve): ") 

    
        index = 1
        #ovde moze da se ubaci prikaz broja rezultata
        for item in lista_quick_sorted:
            for key in item:
                print(str(index) + ".) " + str(key))
                if index == 1:
                    reader = open(key, 'r')#O_RDONLY)
                    read_file = []
                    for line in reader.readlines():
                        temp = line.split(" ")
                        for word in temp:
                            read_file.append(word) #RADI                    
                    for word in read_file:
                        nasao = False
                        for stvar in search:
                            for letter in word:
                                if stvar.lower() == letter.lower() or stvar.lower() == word.lower():       
                                    nasao = True
                                    string = ""                                    
                                    for i in range(read_file.index(word), read_file.index(word) + 10):
                                        string += read_file[i] + " "
                                    print("------------------------------------------------------")
                                    print(string)
                                    print("------------------------------------------------------")
                                if nasao == True: break
                        if nasao == True: break
                    reader.close()
            if str(index) == broj_rezultata: break
            index += 1

    #pozivanje upita da li zeli da se nastavi pretraga ili je kraj
    ponovna_pretraga(graph)


def ponovna_pretraga(graph):
    ponovna_pretraga = input("Pretrazuj sledece? (da/ne)\n")
    while ponovna_pretraga != "da" and ponovna_pretraga != "ne":
        print("Greska pri unosu!")
        ponovna_pretraga = input("Pretrazuj sledece? (da/ne)\n")
        
    if ponovna_pretraga == "da":
        unos = input("Promeni direktorijum? (da/ne) ")
        while unos != "da" and unos != "ne":
            print("Greska pri unosu!")
            unos = input("Promeni direktorijum? (da/ne)\n")
        if unos == "da":
            pravi_putanju(graph)
        elif unos == "ne":
            pretraga(graph)
    elif ponovna_pretraga == "ne":
        exit()

parser = Parser()
graph = Graph()
pravi_putanju(graph)