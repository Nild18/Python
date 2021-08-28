#Dekrypteringsfunktion för att dekryptera Vigenére
def DecryptVigionere(CRYPTOGRAM,KEY,ctemp):

    for i in range(len(CRYPTOGRAM)):
        for j in range(len(Alfa)):
            if CRYPTOGRAM[i] == Alfa[j]:
                a = j

        for k in range(len(Alfa)):
            if KEY[i%(len(KEY))] == Alfa[k]:
                b = k

        ctemp += Alfa[((a-b)%(len(Alfa)))]

    return(ctemp)

#Vokalräknare
def VocolsCounter(ctemp):

    VCounter = 0
    i = 0
    Counter = len(ctemp)
    while i < Counter:
        if ctemp[i] in Vocal: 
            VCounter += 1
            Counter -= 2
            i += 1
        elif ctemp[i] in Conso and ctemp[i+1] in Vocal:
            i += 3
        
    return VCounter

#Hämta de slumpade vikalerna ur kryptogrammet
def ReturnRandomValue(ctemp,rV,rC,rV2,rC2):

    #Om klartexten innehöll färre en 2 vokaler hämtas bara 2 slumpade värden
    if VCounter < 2:
        for i in range(len(Vocal)): 
            if ctemp[((len(ctemp))-2)] == Vocal[i]:
                rV = i

        for i in range(len(Conso)): 
            if ctemp[((len(ctemp))-1)] == Conso[i]:
                rC = i

        return(rV,rC)

    #Om klartexten innehöll 2 vokaler eller fler hämtas 4 slumpade värden
    else:
        for i in range(len(Vocal)): 
            if ctemp[((len(ctemp))-2)] == Vocal[i]:
                rV = i

        for i in range(len(Conso)): 
            if ctemp[((len(ctemp))-1)] == Conso[i]:
                rC = i

        for i in range(len(Vocal)): 
            if ctemp[((len(ctemp))-4)] == Vocal[i]:
                rV2 = i

        for i in range(len(Conso)): 
            if ctemp[(len(ctemp)-3)] == Conso[i]:
                rC2 = i

        return(rV,rC,rV2,rC2)

#Denna funktion revischerar vi substitutionen som gjordes i Permcrypt
def DecryptVoC(ctemp,temprV,temprC,ctemp2): 

    for i in range(len(ctemp)):
        if ctemp[i] in Vocal:
            for j in range(len(Vocal)):
                if ctemp[i] == Vocal[j]:
                    ctemp2 += Vocal[(j-i-temprV)%(len(Vocal))]
        else:
            for j in range(len(Conso)):
                if ctemp[i] == Conso[j]:
                    ctemp2 += Conso[(j-i-temprC)%(len(Conso))]  

    return(ctemp2)

#Denna funktion översätts sjörövarspråket tillbaka till klartext
def PiratToPlain(ctemp2,message):
    
    i = 0
    while i < (len(ctemp2)-(VCounter*2)):
        if ctemp2[i] in Vocal:
            message += ctemp2[i]
        elif (i+1 < (len(ctemp2))) and ctemp2[i] in Conso :
            if ctemp2[(i+1)] == 'a':
                for j in range(len(Number)):
                    if ctemp2[i] == Conso[j]:    
                        message += Number[j] 
                        i += 2 
            elif ctemp2[(i+1)] == 'å':
                for j in range(len(Sign)):
                    if ctemp2[i] == Conso[j]:    
                        message += Sign[j] 
                        i += 2 
            else:
                message += ctemp2[i]
                i += 2
        i+=1

    return(message) 

#Huvud dekrypteringsfunktionen
def HaddockDecrypt():

    global Vocal,Conso,Alfa,Number,Sign,VCounter

    CRYPTOGRAM = input("Enter the CRYPTOGRAM you want to decrypt: ")
    keyString = input("Enter the Key you want to use to decrypt the CRYPTOGRAM? ")

    #omvandling till lista
    KEY = []
    for i in keyString:
        KEY.append(i)

    #Tempvariabler
    ctemp = ""
    ctemp2 = ""
    message = ""

    #Slumpvariabler
    rV = 0
    rC = 0
    rV2 = 0
    rC2 = 0

    #Vokalräknare
    VCounter = 0

    #Listor som används
    Vocal = ['a','o','u','å','e','i','y','ä','ö']
    Conso = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
    Alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','å','ä','ö']
    Number = ['0','1','2','3','4','5','6','7','8','9']
    Sign = [' ','.',',','=','(',')',':',';','"','@','&','-','_','*','^','!','?','+','/']

    #Dekryptering av Vigenére
    ctemp = DecryptVigionere(CRYPTOGRAM,KEY,ctemp) 
    
    #Räknar antalet vokaler
    VCounter = VocolsCounter(ctemp)

    if VCounter < 2:
        #Hämtar ut de slumpade variablerna
        rV,rC = ReturnRandomValue(ctemp,rV,rC,rV2,rC2)

        #Sparar slumpvariablerna i temporärar varibler
        temprV = rV 
        temprC = rC

        #Här revischerar vi substitutionen som gjordes i Permcrypt
        ctemp2 = DecryptVoC(ctemp,temprV,temprC,ctemp2)

        #Här översätts sjörövarspråket tillbaka till klartexten
        message = PiratToPlain(ctemp2,message)

        return(message) 

    else:
        #Hämtar ut de slumpade variablerna
        rV,rC,rV2,rC2 = ReturnRandomValue(ctemp,rV,rC,rV2,rC2)

        #Sparar slumpvariablerna i temporärar varibler
        temprV = rV2 
        temprC = rC2

        #Här revischerar vi substitutionen som gjordes i Permcrypt första gången
        ctemp2 = DecryptVoC(ctemp,temprV,temprC,ctemp2)
        #Flyttar tillbaka Kryptogrammet till ctemp
        ctemp = ctemp2
        
        ctemp2 = ""
        #Sparar slumpvariablerna i temporärar varibler
        temprV = rV 
        temprC = rC

        #Här revischerar vi substitutionen som gjordes i Permcrypt för andra gången
        ctemp2 = DecryptVoC(ctemp,temprV,temprC,ctemp2) 

        #Här översätts sjörövarspråket tillbaka till klartexten
        message = PiratToPlain(ctemp2,message)

    return(message)

print(HaddockDecrypt())