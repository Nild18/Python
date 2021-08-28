import random

#Genererar slumpade vokaler och konsonanter
def PermutationsFunktion(randomVocal,randomConsonant,randomVocal2,randomConsonaut2):

    randomVocal = (random.randint(1, 8))
    randomConsonant = (random.randint(1, 18)) 
    randomVocal2 = (random.randint(1, 8))
    randomConsonaut2 = (random.randint(1, 18))
    
    return(randomVocal,randomConsonant,randomVocal2,randomConsonaut2)

#Inmatning klartext och nyckel
def MessageKey():

    plaintext = input("Enter the message you want to encrypt: ")
    keyString = input("Enter the Key you want to use to encrypt the message? ")

    return(plaintext,keyString)

#Maskera längden av sjörövarspråket
def Hidelenght(cryptTemp):
    
    cryptedMsg = ((countVocal*3)+countConsonant+countNumber+countSign)
    messageLen = (len(cryptTemp))
    for i in range(cryptedMsg):
        if messageLen <= i:
            cryptTemp += Alfa[(random.randint(0,27))]

    return(cryptTemp)

#Omvandling till sjörövarspråk
def Pirat(plaintext,countConsonant,countVocal,countNumber,countSign): 

    cryptTemp = ""
    for i in range(len(plaintext)):
        if plaintext[i] in Vocal:
            cryptTemp += plaintext[i] 
            countVocal += 1
        elif plaintext[i] in Number:
            for j in range(len(Number)):
                if plaintext[i] == Number[j]:
                    cryptTemp += Conso[j]
                    cryptTemp += 'a'
                    cryptTemp += Conso[j]
                    countNumber += 3
        elif plaintext[i] in Sign:
            for h in range(len(Sign)):
                if plaintext[i] == Sign[h]:
                    cryptTemp += Conso[h]
                    cryptTemp += 'å'
                    cryptTemp += Conso[h]
                    countSign += 3
        elif plaintext[i] in Conso:
            cryptTemp += plaintext[i]
            cryptTemp += 'o'
            cryptTemp += plaintext[i]
            countConsonant += 3
    
    return(cryptTemp,countConsonant,countVocal,countNumber,countSign) 

#Cryptering baserat på index och vocal eller Konsonant
def PermKrypt(cryptTemp,temprandomVocal,temprandomConsonaut):

    cryptTemp2 = ""
    for i in range(len(cryptTemp)):
        if cryptTemp[i] in Vocal:
            for j in range(len(Vocal)):
                if cryptTemp[i] == Vocal[j]:
                    cryptTemp2 += Vocal[(j+i+temprandomVocal)%(len(Vocal))]
        else:
            for j in range(len(Conso)):
                if cryptTemp[i] == Conso[j]:
                    cryptTemp2 += Conso[(j+i+temprandomConsonaut)%(len(Conso))] 

    return(cryptTemp2)

#Omvandling nyckel till lista
def KeyList(keyString):
    
    KEY = []
    for i in keyString:
        KEY.append(i)

    return(KEY)

#Översätter de slumpade variablerna som används i PermKrypt samt byter ut de sista 
#bokstäverna i Kryptogrammet med dessa bokstäver
def AddRandomtoCrypt(cryptTemp2,randomVocal,randomConsonant,randomVocal2,randomConsonaut2):
   
    tempList = []
    for i in range(len(cryptTemp2)):
        tempList.append(cryptTemp2[i])
    
    if countVocal < 2:
        tempList[-2] = Vocal[randomVocal]
        tempList[-1] = Conso[randomConsonant]
    else:
        tempList[-2] = Vocal[randomVocal]
        tempList[-1] = Conso[randomConsonant]
        tempList[-4] = Vocal[randomVocal2]
        tempList[-3] = Conso[randomConsonaut2]

    cryptTemp2 = ""

    for i in range(len(tempList)):
        cryptTemp2 += tempList[i]

    return cryptTemp2

#Kryptering med Vigionere
def Vigionere(cryptTemp2,KEY):
    
    CRYPTOGRAM = ""

    for i in range(len(cryptTemp2)):
        for j in range(len(Alfa)):
            if cryptTemp2[i] == Alfa[j]:
                a = j
        
        for k in range(len(Alfa)):
            if KEY[i%(len(KEY))] == Alfa[k]:
                b = k

        CRYPTOGRAM += Alfa[((a+b)%len(Alfa))]
    
    return(CRYPTOGRAM)

#Huvudfunktion
def HaddockCrypt():
   
    global Vocal,Conso,Alfa,Number,Sign,countConsonant,countVocal,countNumber,countSign
    #Listor
    Vocal = ['a','o','u','å','e','i','y','ä','ö']
    Conso = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
    Alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','å','ä','ö']
    Number = ['0','1','2','3','4','5','6','7','8','9']
    Sign = [' ','.',',','=','(',')',':',';','"','@','&','-','_','*','^','!','?','+','/']

    #Countvariabler 
    countVocal = 0
    countConsonant = 0
    countNumber = 0
    countSign = 0

    #Randomvariabler
    randomVocal = 0
    randomConsonant = 0
    randomVocal2 = 0
    randomConsonaut2 = 0

    #Inmatning av meddelande och nyckel
    plaintext,keyString = MessageKey()

    #Omvandling nyckel till en lista
    KEY = KeyList(keyString)
    
    #Omvandling klartexten till sjörövarspråk
    cryptTemp,countConsonant,countVocal,countNumber,countSign = Pirat(plaintext,countConsonant,countVocal,countNumber,countSign) 

    #Maskera längden av CRYPTOGRAMMET
    cryptTemp = Hidelenght(cryptTemp)
    
    #Skapar de slumpvariabler som ska användas
    randomVocal,randomConsonant,randomVocal2,randomConsonaut2 = PermutationsFunktion(randomVocal,randomConsonant,randomVocal2,randomConsonaut2)
    
    #Sparar slumpade variable i en temp variable
    temprandomVocal = randomVocal
    temprandomConsonaut = randomConsonant

    #Kryptering baserat på index och vocal eller Konsonant
    cryptTemp2 = PermKrypt(cryptTemp,temprandomVocal,temprandomConsonaut) 

    if countVocal < 2:
        cryptTemp2 = AddRandomtoCrypt(cryptTemp2,randomVocal,randomConsonant,randomVocal2,randomConsonaut2)
        CRYPTOGRAM = Vigionere(cryptTemp2,KEY)
    else:
        cryptTemp = cryptTemp2
        cryptTemp2 = ""
        temprandomVocal = randomVocal2
        temprandomConsonaut = randomConsonaut2
        cryptTemp2 = PermKrypt(cryptTemp,temprandomVocal,temprandomConsonaut)
        cryptTemp2 = AddRandomtoCrypt(cryptTemp2,randomVocal,randomConsonant,randomVocal2,randomConsonaut2)
        CRYPTOGRAM = Vigionere(cryptTemp2,KEY)
    
    return(CRYPTOGRAM)
           
print(HaddockCrypt())