#!/usr/bin/env python3
import ast, os, textwrap
from datetime import datetime, date, timedelta
from time import sleep

versie = "0.78"
datum = "20231108"
plaats = "Pedara"

basismap = os.path.dirname(os.path.realpath(__file__))
os.chdir(basismap)

forc3 = "{:^3}".format
forr3 = "{:>3}".format
forl5 = "{:<5}".format
forr5 = "{:>5}".format
forl10 = "{:<10}".format

col0 = "\033[0m"
colmk = "\033[92m"
colls = "\033[93m"
colch = "\033[96m"
colrm = "\033[91m"
colfd = "\033[95m"
colStart = "\033[44m"+"\033[95m"
colOpen = "\033[103m"+"\033[94m"
colDicht = "\033[41m"+"\033[96m"


inputindent = "  : "
afsluitlijst = ["X","Q"]
statuslijst = ["Open","Actief","Dicht"]
statcollijst = [colStart,colOpen,colDicht]
lijstlijst = ["Datum","Functie","Bedrijf","Salaris","Gewijzigd","Status","Contact","Via","Weblink","Notitie"]
#              0       1         2         3         4           5        6         7     8         9
#  _    __  __   __
# / \\ / \\ ||   ||
#\\__ ||  ||||   ||
#   \\||  ||||   ||
#\\__/ \\_/ /\_/|/\_/| niet met me!
#
logo = """
  _    __  __   __  
 / \\\\ / \\\\ ||   ||  
\\\\__ ||  ||||   ||  
   \\\\||  ||||   ||  
\\\\__/ \\\\_/ /\_/|/\_/| niet met me!"""
print()
lenlijst = 0
try:
    while len(logo) > 0:
        for i in statcollijst:
            print(i, end = "")
            print(logo[statcollijst.index(i)+lenlijst], end = "", flush = True)
            logo = logo[0:]
            sleep(0.01)
        lenlijst += len(statcollijst)
except:
    print(col0)
print()

def lslijst():
    ls = os.listdir()
    if "lijst" in ls:
        with open("lijst","r") as l:
            lijst = ast.literal_eval(l.read())
    else:
        lijst = []
    return lijst

def mksoll():
    col = colmk
    lijst = lslijst()
    mkdat = True
    while mkdat == True:
        Mkdat = input("%s%s%s:\n%s" % (col,lijstlijst[0],col0,inputindent))
        if Mkdat.upper() in afsluitlijst:
            return lijst
        elif Mkdat == "":
            Mkdat = datetime.strftime(date.today(),"%Y%m%d")
        try:
            datetime.strptime(Mkdat,"%Y%m%d")
            mkdat = False
        except(Exception) as f:
            #print(f)
            pass
    functie = True
    while functie == True:
        Functie = input("%s%s%s:\n%s" % (col,lijstlijst[1],col0,inputindent))
        if Functie.upper() in afsluitlijst:
            return lijst
        else:
            functie = False
    bedrijf = True
    while bedrijf == True:
        Bedrijf = input("%s%s%s:\n%s" % (col,lijstlijst[2],col0,inputindent))
        if Bedrijf.upper() in afsluitlijst:
            return lijst
        else:
            bedrijf = False
    geld = True
    while geld == True:
        Geld =  input("%s%s%s:\n%s" % (col,lijstlijst[3],col0,inputindent))
        if Geld.upper() in afsluitlijst:
            return lijst
        else:
            if Geld == "":
                Geld = 0
            try:
                Geld = int(Geld)
                geld = False
            except(Exception) as f:
                #print(f)
                Geld = 0
                pass
    chdat = True
    while chdat == True:
        Chdat = input("%s%s%s:\n%s" % (col,lijstlijst[4],col0,inputindent))
        if Chdat.upper() in afsluitlijst:
            return lijst
        elif Chdat == "":
            Chdat = datetime.strftime(date.today(),"%Y%m%d")
        try:
            datetime.strptime(Chdat,"%Y%m%d")
            chdat = False
        except(Exception) as f:
            #print(f)
            pass
    status = True
    while status == True:
        for i in statuslijst:
            print("  "+str(statuslijst.index(i))+" : "+i)
        Status = input("%s%s%s:\n%s" % (col,lijstlijst[5],col0,inputindent))
        if Status.upper() in afsluitlijst:
            return lijst
        elif Status == "":
            Status = "0"
        try:
            ints = int(Status)
            if ints in range(len(statuslijst)):
                Status = statuslijst[ints]
                status = False
            else:
                pass
        except(Exception) as f:
            #print(f)
            pass
    contact = True
    while contact == True:
        Contact = input("%s%s%s:\n%s" % (col,lijstlijst[6],col0,inputindent))
        if Contact.upper() in afsluitlijst:
            return lijst
        else:
            contact = False
    kanaal = True
    while kanaal == True:
        Kanaal = input("%s%s%s:\n%s" % (col,lijstlijst[7],col0,inputindent))
        if Kanaal.upper() in afsluitlijst:
            return lijst
        else:
            kanaal = False
    link = True
    while link == True:
        Link = input("%s%s%s:\n%s" % (col,lijstlijst[8],col0,inputindent))
        if Link.upper() in afsluitlijst:
            return lijst
        else:
            link = False
    aant = True
    while aant == True:
        Aant = input("%s%s%s:\n%s" % (col,lijstlijst[9],col0,inputindent))
        if Aant.upper() in afsluitlijst:
            return lijst
        else:
            aant = False
    nwsoll = [Mkdat,Functie,Bedrijf,Geld,Chdat,Status,Contact,Kanaal,Link,Aant]
    lijst.append(nwsoll)
    with open("lijst","w") as l:
        print(lijst,end = "", file = l)
    print()
    col = col0
    return lijst

def lsls():
    col = colls
    lijn3 = forr3("+ +")
    lijn5 = forr5("-- +")
    lijn = lijn3+lijn5*10
    lijst = lslijst()
    print("Statusopties: %s %s %s" % (statcollijst[0]+statuslijst[0]+col0,statcollijst[1]+statuslijst[1]+col0,statcollijst[2]+statuslijst[2]+col0))
    print(col+lijn+col0)
    print(forc3("-"), end = "")
    for i in lijstlijst:
        print(forl5(i[:5]),end = "")
    print()
    print(col+lijn+col0)
    for i in range(len(lijst)):
        print(forc3(str(i)),end = "")
        for j in range(len(lijstlijst)):
            if j == 0 or j == 4:
                dat = str(lijst[i][j])[4:]
                print(forl5(dat),end = "")
            elif j == 3:
                if lijst[i][j] == 0:
                    lijst[i][j] = ""
                print(forl5(str(lijst[i][j])[:4]),end = "")
            elif j == 5:
                col = statcollijst[statuslijst.index(lijst[i][j])]
                print(col+forl5(str(lijst[i][j])[:4])+col0,end = "")
                col = colls
            else:
                print(forl5(str(lijst[i][j])[:4]),end = "")
        print()
    print(col+lijn+col0)
    col = col0
    return lijst

def rgsoll():
    lijst = lslijst()
    rgs = []
    Geef = "Geef de index op als geheel getal (\"#\"), inclusief bereik (\":#\", \"#:#\" of \"#:\") of lijst (\"#,#,#\")"
    twGeef = textwrap.wrap(Geef, width = 53)
    ix = 0
    while ix < len(twGeef)-1:
        print(twGeef[ix])
        ix += 1
    details = input(twGeef[-1]+inputindent)
    try:
        if ":" in details:
            if len(details) >1 and details[0] == ":":
                for i in range(len(lijst)):
                    if i <= int(details[1:]):
                        rgs.append(i)
            elif len(details) >1 and details[-1] == ":":
                for i in range(len(lijst)):
                    if i >= int(details[:-1]):
                        rgs.append(i)
            elif len(details) >=3:
                for i in range(len(lijst)):
                    if i >= int(details[:details.index(":")]) and i <= int(details[details.index(":")+1:]):
                        rgs.append(i)
        elif "," in details:
            rgsl = details.split(",")
            for i in rgsl:
                rgs.append(int(i))
        else:
            rgs.append(int(details))
    except(Exception) as f:
        #print(f)
        pass
    return rgs

def lssoll():
    lijst = lslijst()
    rgs = rgsoll()
    try:
        for i in rgs:
            if i in range(len(lijst)):
                col = colls
                lijn = "-"*2+"+"+"-"*9+"+"+"-"*10+" -   -"
                lijst = lslijst()
                print(str(i)+":")
                print(col+lijn+col0)
                col = col0
                for j in range(len(lijstlijst)):
                    if j in [1,2,6,7,9]:
                        if len(lijst[i][j]) > 40:
                            w = textwrap.wrap(lijst[i][j], width = 40)
                            for k in w:
                                if k == w[0]:
                                    print(forc3(j)+forl10(lijstlijst[j])+k)
                                else:
                                    print(" "*13+k)
                        else:
                            print(forc3(j)+forl10(lijstlijst[j])+str(lijst[i][j]))
                    elif j == 8:
                        if len(lijst[i][j]) > 40:
                            w = lijst[i][j].split("/")
                            for k in w:
                                if k == w[0]:
                                    print(forc3(j)+forl10(lijstlijst[j])+k+"/")
                                elif len(k) > 40:
                                    l = textwrap.wrap(k, width = 40)
                                    for m in l:
                                        print(" "*13+m)
                                    print(" "*13+"/")
                                else:
                                    print(" "*13+k+"/")
                        else:
                            print(forc3(j)+forl10(lijstlijst[j])+str(lijst[i][j]))
                    else:
                        if j == 5:
                            col = statcollijst[statuslijst.index(lijst[i][j])]
                            print(forc3(j)+forl10(lijstlijst[j])+col+str(lijst[i][j])+col0)
                            col = col0
                        elif j == 3:
                            if lijst[i][j] == 0:
                                lijst[i][j] = ""
                            print(forc3(j)+forl10(lijstlijst[j])+col+str(lijst[i][j])+col0)
                        else:
                            print(forc3(j)+forl10(lijstlijst[j])+col+str(lijst[i][j])+col0)
                col = colls
                print(col+lijn+col0)
        print()
    except(Exception) as f:
        #print(f)
        pass
    return lijst

def chsoll():
    col = colch
    lijst = lsls()
    details = input("Welke sollicitatie wil je %sWIJZIGEN%s:\n%s" % (col,col0,inputindent))
    if details.upper() in afsluitlijst:
        return lijst
    ch = True
    while ch == True:
        try:
            intd = int(details)
            if intd in range(len(lijst)):
                lijn = "-"*2+"+"+"-"*9+"+"+"-"*10+" -   -"
                lijst = lslijst()
                print(col+lijn+col0)
                col = col0
                for j in range(len(lijstlijst)):
                    if j in [1,2,6,7,9]:
                        if len(lijst[intd][j]) > 40:
                            w = textwrap.wrap(lijst[intd][j], width = 40)
                            for k in w:
                                if k == w[0]:
                                    print(forc3(j)+forl10(lijstlijst[j])+k)
                                else:
                                    print(" "*13+k)
                        else:
                            print(forc3(j)+forl10(lijstlijst[j])+str(lijst[intd][j]))
                    elif j == 8:
                        if len(lijst[intd][j]) > 40:
                            w = lijst[intd][j].split("/")
                            for k in w:
                                if k == w[0]:
                                    print(forc3(j)+forl10(lijstlijst[j])+k+"/")
                                elif len(k) > 40:
                                    l = textwrap.wrap(k, width = 40)
                                    for m in l:
                                        print(" "*13+m)
                                    print(" "*13+"/")
                                else:
                                    print(" "*13+k+"/")
                        else:
                            print(forc3(j)+forl10(lijstlijst[j])+str(lijst[intd][j]))
                    else:
                        if j == 5:
                            col = statcollijst[statuslijst.index(lijst[intd][j])]
                            print(forc3(j)+forl10(lijstlijst[j])+col+str(lijst[intd][j])+col0)
                            col = col0
                        elif j == 3:
                            if lijst[intd][j] == 0:
                                lijst[intd][j] = ""
                            print(forc3(j)+forl10(lijstlijst[j])+col+str(lijst[intd][j])+col0)
                        else:
                            print(forc3(j)+forl10(lijstlijst[j])+col+str(lijst[intd][j])+col0)
                col = colch
                print(col+lijn+col0)
            if intd in range(len(lijst)):
                anders = input("Welk veld wil je %sWIJZIGEN%s:\n%s" % (col,col0,inputindent))
                if anders.upper() in afsluitlijst:
                    return lijst
                try:
                    inta = int(anders)
                    if inta in range(len(lijstlijst)):
                        if inta == 5:
                            for i in statuslijst:
                                print("  "+str(statuslijst.index(i))+" : "+i)
                            Status = input("%s:\n%s" % (lijstlijst[5],inputindent))
                            if Status.upper() in afsluitlijst:
                                return lijst
                            try:
                                if int(Status) in range(len(statuslijst)):
                                    wijz = statuslijst[int(Status)]
                                else:
                                    pass
                            except:
                                pass
                        else:
                            wijz = input()
                            if inta == 0 or inta == 4:
                                if wijz == "":
                                    wijz = datetime.strftime(date.today(),"%Y%m%d")
                                Dat = datetime.strptime(wijz,"%Y%m%d")
                            if inta == 3:
                                Sal = int(wijz)
                        lijst[intd][inta] = wijz
                        with open("lijst","w") as l:
                            print(lijst,end = "", file = l)
                except(Exception) as f:
                    #print(f)
                    pass
        except(Exception) as f:
            print(f)
            ch = False
            pass
    col = col0
    print()
    return lijst

def rmsoll():
    col = colrm
    lijst = lsls()
    rm = input("Welke sollicitatie wil je %sVERWIJDEREN%s:\n%s" % (col,col0,inputindent))
    try:
        intr = int(rm)
        if intr in range(len(lijst)):
            lijst.remove(lijst[intr])
            with open("lijst","w") as l:
                print(lijst,end = "", file = l)
    except(Exception) as f:
        #print(f)
        pass
    col = col0
    print()
    return lijst

def fdsoll():
    col = colfd
    lijst = lslijst()
    fd = input("Geef de %sZOEKREEKS%s op:\n%s" % (col,col0,inputindent))
    if fd.upper() in afsluitlijst:
        return lijst
    elif fd == "":
        pass
    else:
        for i in lijst:
            for j in i:
                if fd.lower() in str(j).lower():
                    ifd = lijst.index(i)
                    jfd = i.index(j)
                    veld = str(lijstlijst[jfd])
                    print(" >> %s is gevonden in soll %s:\n%s: %s" % (col+fd+col0, col+str(ifd)+col0, col+veld+col0, j))
    col = col0
    print()
    return lijst

soll = True
while soll == True:
    kies = input("  1 : %sMaak%s\n  2 : %sVind%s\n >3 : %sToon%s\n  4 : %sWijzig%s\n  5 : %sVerwijder%s\n%s" % (colmk,col0,colfd,col0,colls,col0,colch,col0,colrm,col0,inputindent))
    if kies.upper() in afsluitlijst:
        exit()
    elif kies == "0":
        print()
        print("Versie: "+versie)
        print("Datum : "+datum)
        print("Plaats: "+plaats)
        print()
    elif kies == "1":
        print()
        lijst = mksoll()
    elif kies == "2":
        print()
        lijst = fdsoll()
    elif kies == "4":
        print()
        lijst = chsoll()
    elif kies == "5":
        print()
        lijst = rmsoll()
    else: # 3 : Toon
        print()
        lijst = lsls()
        lijst = lssoll()
