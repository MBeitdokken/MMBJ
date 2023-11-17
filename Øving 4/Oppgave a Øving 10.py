navnliste = []
stasjonIDliste = []
datoliste = []
snodybdeliste = []
nedborliste = []
middeltemp = []
gjennomsnittskydekke = []
hoyestmiddelvind = []


def jabba():
    with open("/Users/bjartelandrak/Documents/UIS/HØST 2023/DATA/SPIDER/snoedybder_vaer_en_stasjon_dogn.csv","r",encoding="UTF8") as fila:
        first_line = fila.readline()
        for linje in fila:
            ordene = linje.split(";")
            navnliste.append(ordene[0])
            stasjonIDliste.append(ordene[1])
            datoliste.append(ordene[2])
            try:
                snodybdeliste.append(int(ordene[3]))
            except ValueError:
                snodybdeliste.append(0)  
            nedborliste.append(ordene[4])
            middeltemp.append(ordene[5])
            gjennomsnittskydekke.append(ordene[6])
            hoyestmiddelvind.append(ordene[7])
jabba()
