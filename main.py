from random import randint, choice
import random
strich=("------------------------------------")
monsters={}
class Charakter:
    def __init__(self):
        self.name = ""
        self.leben = 1
        self.max_leben = 1
        self.monsters=monsters



 
 
    def angriff_durchfuehren(self, gegner):

        
        schaden = randint(spieler.max_leben//7, spieler.max_leben//3)
 
        if schaden == 0:
            print(f"{gegner.name} weicht dem Angriff von {self.name} aus.")
        else:
            print(f"{self.name} greift {gegner.name} an und verursacht {schaden} Schaden.")
            gegner.leben -= schaden
            if spieler.name==self.name:
                spieler.schaden+=schaden
            else:
                spieler.schadn_erlitten+=schaden

 

class Gegner(Charakter):
    def __init__(self, spieler):
        super().__init__()
        self.name = monsters[f"mob{welt.px}{welt.py}"]
        if spieler.leben <= 0:
            welt.spiel_aktive = False
            self.leben = 1
        else:
            maximum = spieler.max_leben*2 // spieler.schwer // 2
            minimum = maximum//3>1
            if minimum==0:
                minimum=1

            if maximum < minimum:
                maximum = minimum

            self.leben = randint(minimum, maximum)
                
        self.name = gegen[f"mob{welt.px}{welt.py}"]
        if isinstance(self.name, list):
            self.name = self.name[0]
 
 
class Spieler(Charakter):
    def __init__(self, leben, schwirigkeit):
        super().__init__()
        self.leben = leben
        self.max_leben = leben
        self.name = input("Gib den Namen des Spielers ein: ")
        self.key_have=False
        self.kills=0
        self.regenerrirt=0
        self.schaden=0
        self.schadn_erlitten=0
        self.schwer=schwirigkeit
        
 
    def ausruhen(self):
        
        if self.leben >= self.max_leben:
            self.leben = self.max_leben
        else:
            reg=randint(1, self.max_leben//10)
            self.leben += reg
            self.regenerrirt+=reg
        print(f"{self.name} ruht sich aus. Leben: {self.leben}/{self.max_leben}")
    
    def monster_name(self):
        monstername = gegen[f"mob{welt.px}{welt.py}"]
        if isinstance(monstername, list):
            monstername = monstername[0]

        print(f"{spieler.name} ist auf einen {gegner.name} gestoßen")
 
    def kaempfen(self):
        if gegner.name ==0:
            kampf=False
            print ("hier ist kein Monster.")
        else:
            monstername = gegen[f"mob{welt.px}{welt.py}"]
            if isinstance(monstername, list):
                monstername = monstername[0]

            print(f"{spieler.name} ist auf einen {monstername} gestoßen")


            kampf = True
        while kampf:
            
            print(f"Leben des Spielers: {self.leben}")
            print(f"Leben von {monstername}: {gegner.leben}")
            aktion = input("Aktion (1:angreifen, 2:fliehen): ")
 
            if aktion == "1":
                self.angriff_durchfuehren(gegner)
                
                if gegner.leben <= 0:
                    print(f"{self.name} besiegt {monstername}")
                    if monstername=="Keykeeper":
                        self.key_have=True
                    self.kills+=1
                    gegen[f"mob{welt.px}{welt.py}"]=0
                    return True
                gegner.angriff_durchfuehren(self)
                if self.leben<0:
                    self.leben=0
                
                print(strich)
            elif aktion == "2":
                print(f"{self.name} flieht")
                gegner.angriff_durchfuehren(self)
                if self.leben<0:
                    self.leben=0
                kampf = False
                print(strich)
            else:
                print("Unbekannte Aktion. Bitte berichtigen")
 
            if self.leben <= 0:
                print(f"{self.name} ist gestorben")
                print(strich)
                
                return False
        return True

    def ereignis(self, biom):
        print(strich)
        if biom == "Portal":
            if spieler.key_have:
                welt.win_not = False  
                print("Du hast das Portal geöffnet und gewonnen!")
            else:
                print("Das Portal ist verschlossen. Du brauchst den Schlüssel.")

        if biom=="Tempel":
            n_leben=self.max_leben//5
            self.max_leben+=n_leben
            print(f"Du hast plus {n_leben} Maximaleben bekommen. Deine Leben{self.leben}/{self.max_leben}")
            welt_karte[f"biom{welt.px}{welt.py}"] =("tempel")
            
        elif biom=="Lagerfeuer":
            n_leben=self.max_leben//5
            self.leben+=n_leben
            if self.leben>self.max_leben:
                self.leben=self.max_leben
            print(f"Du hast plus {n_leben} Leben bekommen. Deine Leben{self.leben}/{self.max_leben}")
            welt_karte[f"biom{welt.px}{welt.py}"] =("lagerfeuer")
            
        elif biom=="Ruine":
            self.leben-=self.max_leben//5
            if self.leben<0:
                    self.leben=0
            print(f"Du bist in eine Falle getreten sie hat {self.leben} Schaden verursacht. Deine Leben{self.leben}/{self.max_leben}")
            welt_karte[f"biom{welt.px}{welt.py}"] =("Ruine")
            
        elif biom=="Ruine":
            print("diese Ruinee ist inaktiv")
        elif biom=="tempel":
            print("dieser Tempel ist inaktiv")
        elif biom=="lagerfeuer":
            print("dieses Lagerfeuer ist inaktiv")
        
        


        return welt_karte
    
    def stats(self):
        print (f"Name: {spieler.name}")
        print(f"HP: {self.leben}/{self.max_leben}")
        print (f"Schlüssel: {self.key_have}")
    
    def end_stats(self):

        
        print(f"Die Expedition {welt.name_expo} endet bei den Koordinaten {welt.px}/{welt.py} ")
        print(f"auf einer Weltgröße von {welt.width}x{welt.height}. ")
        print(f"Das letzte erreichte Biom war {welt.speicherung[f"biom{welt.px}{welt.py}"]}. ")
        print(f"Spieler {spieler.name} legte insgesamt {welt.schritte} Schritte zurück. ")
        print(f"Mit {self.leben}/{self.max_leben} HP, {self.kills} besiegte Gegner, ")
        print(f"{self.schadn_erlitten} erlittener Schaden, {self.schaden} verursachter Schaden ")
        print(f"und {self.regenerrirt} Punkten Regeneration endet diese Reise.")
        

        

    
class Map:
    def __init__(self, width, height, px,py , ex_name):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.px = px
        self.py = py
        self.spiel_aktive=True
        self.lacs=""
        self.speicherung={}
        self.mobs=""
        self.monseters=monsters
        self.win_not=True
        self.schritte=0
        self.treffer=""
        self.treffer1=""
        self.name_expo=ex_name

    def kords(self):
        pos=self.speicherung[f"biom{self.px}{self.py}"]
        return pos

    def movement(self):
        move = input("Wohin gehst du? (w, a, d, s) ")

        if move == "s":
            if self.py==0:
                
                spieler.leben=0
                welt.spiel_aktive=False
                return welt.spiel_aktive 
            else:
                self.py -= 1
                self.schritte+=1
        elif move == "d":
            self.px += 1
            self.schritte+=1
        elif move == "a":
            if self.px==0:
                welt.spiel_aktive = False
                return welt.spiel_aktive
            else:
                self.px -= 1
                self.schritte+=1
        elif move == "w":
            self.py += 1
            self.schritte+=1
        else:
            print("Unbekannte Eingabe. Bitte berichtigen")

        if self.px >= self.width or self.py >= self.height or self.px <= 0 or self.py <= 0:
            print("Du bist von der Welt gefallen.")
            spieler.leben=0
            return False
        


        
        return welt.spiel_aktive
    
    def save_map(self):
        self.x=0
        self.x=0
        for self.x in range(self.width +1):
            for self.y in range(self.height +1):
                bio=random.randint(1, 10)
                if bio==1:
                    self.lacs="Wald"
                elif bio==2:
                    self.lacs="Sumpf"
                elif bio==3:
                    self.lacs="Berge"
                elif bio==4:
                    self.lacs="Dorf"
                elif bio==5:
                    self.lacs="Fluss"
                elif bio==6:
                    self.lacs="Feld"
                elif bio==7:
                    self.lacs="Lager"
                elif bio==8:
                    self.lacs="Tempel"
                elif bio==9:
                    self.lacs="Lagerfeuer"
                else:
                    self.lacs="Ruine"
                    
                self.speicherung[f"biom{self.x}{self.y}"] =(self.lacs)
        self.speicherung[f"biom{random.randint(1, self.width-1)}{random.randint(1, self.height-1)}"] ="Portal"
        ziel = {"Portal"}

        self.treffer1 = [
        k for k, v in self.speicherung.items()
        if (v[0] if isinstance(v, list) else v) in ziel
        ]
        
        self.treffer1 = self.treffer1[0]
        

        # print(self.speicherung)
        return self.speicherung

    def monster_map(self):
        self.x=0
        self.x=0
        self.mobs="<!=>"
        wald_monster=["Zombie","Skelett","Wolf"]
        sumpf_monster=["Zombie","Ertrunknen","Moorleiche"]
        berg_monster=["Skelett","Wanderer","Jety"]
        dorf_monster=["Zombie","Werwolf","Hexe"]
        fluss_monster=["All","Ertrunknen","Fischer"]
        feld_monster=["Vogelscheuche","Grueffelo","Zombie"]
        lager_monster=["Goblin","Oger","Skelette"]
        key="Keykeeper"
        for self.x in range(self.width +1):
            for self.y in range(self.height +1):
                if self.speicherung[f"biom{self.x}{self.y}"]=="Wald":
                   self.monseters[f"mob{self.x}{self.y}"] =random.choices(wald_monster)
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Sumpf":
                    self.monseters[f"mob{self.x}{self.y}"] =random.choices(sumpf_monster)
                
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Berge":
                    self.monseters[f"mob{self.x}{self.y}"] =random.choices(berg_monster)
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Dorf":
                    self.monseters[f"mob{self.x}{self.y}"] =random.choices(dorf_monster)
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Fluss":
                    self.monseters[f"mob{self.x}{self.y}"] =random.choices(fluss_monster)
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Feld":
                    self.monseters[f"mob{self.x}{self.y}"] =random.choices(feld_monster)
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Lager":
                    self.monseters[f"mob{self.x}{self.y}"] =random.choices(lager_monster)
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Tempel":
                    self.monseters[f"mob{self.x}{self.y}"] =0
                elif self.speicherung[f"biom{self.x}{self.y}"]=="Lagerfeuer":
                    self.monseters[f"mob{self.x}{self.y}"] =0
                else:
                    self.monseters[f"mob{self.x}{self.y}"] =0
        self.monseters[f"mob{random.randint(1, self.width-1)}{random.randint(1, self.height-1)}"] =key
        
        ziel = {"Keykeeper"}

        self.treffer = [
        k for k, v in monsters.items()
        if (v[0] if isinstance(v, list) else v) in ziel
        ]
        
        self.treffer = self.treffer[0]
        



                
        return self.monseters
    
    def stats(self):
        print(f"Koordinaten: {self.px}/{self.width}, {self.py}/{self.height}")
        print(f"Biom: {self.speicherung[f"biom{self.px}{self.py}"]}")
        print(f"Schritt: {self.schritte}")

game=True
while game:
    print ("Willkommen beim Gigathon 2026 von Leon Schoeneich")
    ex_name=input("Bitte gib deinem Abenteuer einen Namen: ")
    leben=int(input("Wie viele Leben soll dein Charakter haben?  "))
    schwe=int(input("Welchen Schwierigkeitsgrad soll das Spiel haben?(1:hart, 2:normal, 3:einfach)  "))
    spieler = Spieler(leben, schwe)
    print("Wo sollen die Ränder deiner Welt sein?")
    x=int(input("x: "))
    y=int(input("y: "))
    print("Wo möchtest du starten? (ich empfehle die Mitte.)")
    stx=int(input("x: "))
    sty=int(input("y: "))
    if stx>=x:
        print("dann erweitern wir die Karte bis da.")
        x=stx+1
    if stx>=y:
        print("dann erweirten wir die Karte bis da.")
        y=sty+1
    welt = Map(x, y,stx ,sty, ex_name )
    welt_karte=welt.save_map()
    gegen=welt.monster_map()

    print(f"Du bist in einer Fantasy-Welt gefangen und es lauern haufenweise Monster und Gefahren.")
    print(f"Dein Ziel ist es aus dieser Welt zu entkommen. Doch leider ist das Ausgangs-Portal verschlossen und der Schlüssel wird von einem Wächter bewacht der besiegt werden muss um die Welt zu verlassen.")
    print(F" Er befindet sich bei {welt.treffer}. Das portal findest du {welt.treffer1}")
    # print(type(welt_karte))
    while welt.spiel_aktive and welt.win_not:
        if spieler.leben<=0:
            welt.spiel_aktive=False
        print(strich)
        spieler.stats()
        welt.stats()
        print(strich)
        


        aktion = input("Aktion (1:erkunden, 2:ausruhen): ")
    
        if aktion == "1":
            welt.spiel_aktive=welt.movement()

            if welt.px >= welt.width or welt.py >= welt.height or welt.px <= 0 or welt.py <= 0:
                print("Du bist von der Welt gefallen.")
                welt.spiel_aktive==False
                break

            biom =welt.kords()
            if biom in ("Tempel", "Lagerfeuer", "Ruine", "Portal"):
                welt_karte=spieler.ereignis(biom)
            gegner = Gegner(spieler)
            welt.spiel_aktive = spieler.kaempfen()
            
        elif aktion == "2":
            spieler.ausruhen()
        else:
            print("Unbekannte Aktion. Bitte berichtigen.")
            
        
        if welt.spiel_aktive==False:
            break

    if not welt.spiel_aktive:
        print("Game Over!")
        spieler.end_stats()
        print()
        print(strich)
    elif not welt.win_not:
        print(strich)
        print("")
        spieler.end_stats()
        print()
        print(strich)
    g=input("Nochmal spielen?(JA, NEIN)")
    if g=="JA":
        pass
    elif g =="NEIN":
        game=False
        break
    else:
        print("Ich glaub das soll das ein JA sein!")






