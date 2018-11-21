stack = []
codigoEJECUTAR = []
SALTOS = {}

lineaEjecutada = -1

lineaAsaltar = 0

CE = 0
weota = 0

AX = 0x0;
BX = 0x0;
CX = 0x0;
DX = 0x0;
BP = 0x0;

carryFlag = False
parityFlag = False
auxCarryFlag = False
zeroFlag = False
overflowFlag = False
traceFlag = False
interruptFlag = False
DirectionFlag = False
signFlag = False

JEF = False
JZF = False



#STACK
def MOV (register, dataMov):
    global AX
    global BX
    global CX
    global DX
    global BP
    '''
    if (type(dataMov) == int):
        dataMov = int(dataMov, 16)
    elif (type(dataMov)== hex):
        dataMov = int(dataMov,16)
    '''
    if (register == "AX,"):
        AX = dataMov
    elif (register == "BX,"):
        BX = dataMov
    elif(register == "CX,"):
        CX = dataMov
    elif(register == "DX,"):
        DX = dataMov
    elif(register == "BP,"):
        BP = dataMov

    printEstatus()

def POP (register):
    global AX
    global BX
    global CX
    global DX
    global BP
    if (register == "AX"):
        AX  = stack.pop()
    elif (register == "BX"):
        BX= stack.pop()
    elif (register == "CX"):
        CX  = stack.pop()
    elif (register == "DX"):
        DX  = stack.pop()
    elif (register == "BP,"):
        BP = stack.pop()
    printEstatus()

def PUSH(register):
    global AX
    global BX
    global CX
    global DX

    if (register == "AX"):
        stack.append(AX)
    elif (register == "BX"):
        stack.append(BX)
    elif (register == "CX"):
        stack.append(CX)
    elif (register == "DX"):
        stack.append(DX)
    elif (register == "BP"):
        stack.append(BX)
    else:
        stack.append(register)

    printEstatus()

#MAtematicas

def INC(register):
    global AX
    global BX
    global CX
    global DX
    global BP

    if (register == "AX"):
        AX = AX + 1
    if (register == "BX"):
        BX = BX + 1
    if (register == "CX"):
        CX = CX + 1
    if (register == "DX"):
        DX = DX + 1
    if (register == "BP"):
        BP = BP + 1

    printEstatus()


def DEC(register):
    global AX
    global BX
    global CX
    global DX
    global BP

    if (register == "AX"):
        AX -= 1
    elif (register == "BX"):
        BX -= 1
    elif (register == "CX"):
        CX -= 1
    elif (register == "DX"):
        DX -= 1
    elif (register == "BP"):
        BP -= 1
    printEstatus()


def ADD(register, num):
    global AX
    global BX
    global CX
    global DX
    global BP

    if num in ["AX", "BX", "CX","DX","BP"]:
        num = globals()[num]
    else:
        num = int(num, 16)

    #AX = AX + num

    if (register == "AX"):
        AX += num
    elif (register == "BX"):
        BX += num
    elif (register == "CX"):
        CX += num
    elif (register == "DX"):
        DX += num
    elif (register == "BP"):
        BP += num

    printEstatus()

def SUB(register, num):
    global AX
    global BX
    global CX
    global DX
    global BP

    if num in ["AX", "BX", "CX","DX","BP"]:
        num = globals()[num]
    else:
        num = int(num, 16)

    #AX = AX - num

    if (register == "AX"):
        AX -= num
    elif (register == "BX"):
        BX -= num
    elif (register == "CX"):
        CX -= num
    elif (register == "DX"):
        DX -= num
    elif (REGISTER == "BP"):
        BP -= num

    printEstatus()

def MUL(register):
    global AX
    global BX
    global CX
    global DX
    global BP
    register = int(register, 16)

    if (register == "AX"):
        AX = AX*AX
    elif (register == "BX"):
        AX = AX*BX
    elif (register == "CX"):
        AX = AX*CX
    elif (register == "DX"):
        AX = AX*DX
    elif (register == "BP"):
        BP = AX * BP
    printEstatus()

def DIV(register):
    global AX
    global BX
    global CX
    global DX
    global BP

    if (register == "AX"):
        DX = AX % AX
        AX = AX // AX
    elif (register == "BX"):
        DX = BX % AX
        AX = BX // AX
    elif (register == "CX"):
        DX = CX % AX
        AX = CX // AX
    elif (register == "DX"):
        DX = DX % AX
        AX = DX // AX
    elif (register == "BP"):
        DX = BP % AX
        AX = BP // AX
#LOGICOS
    printEstatus()

def AND(register, Op2):
    global AX
    global BX
    global CX
    global DX
    global BP

    if Op2 in ["AX", "BX", "CX","DX","BP"]:
        Op2 = globals()[Op2]
    else:
        Op2 = int(Op2, 16)
    y =globals()[register[:2]]
    Op1 = int(bin(y),2)
    Op2 = int(bin(Op2), 2)
    if (register == "AX"):
        AX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "BX"):
        BX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "CX"):
        CX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "DX"):
        DX = int(hex(Op1.__and__(Op2)), 16)
    elif (register == "BP"):
        BP = int(hex(Op1.__and__(Op2)), 16)
    printEstatus()

def OR(register, Op2):
    global AX
    global BX
    global CX
    global DX
    global BP

    if Op2 in ["AX", "BX", "CX", "DX","BP"]:
        Op2 = globals()[Op2]
    else:
        Op2 = int(Op2, 16)
    y = globals()[register[:2]]
    Op1 = int(bin(y), 2)
    Op2 = int(bin(Op2), 2)
    if (register == "AX"):
        AX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "BX"):
        BX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "CX"):
        CX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "DX"):
        DX = int(hex(Op1.__or__(Op2)), 16)
    elif (register == "BP"):
        BP = int(hex(Op1.__or__(Op2)), 16)

    printEstatus()

def XOR(register, Op2):
    global AX
    global BX
    global CX
    global DX
    global BP

    if Op2 in ["AX", "BX", "CX", "DX"]:
        Op2 = globals()[Op2]
    else:
        Op2 = int(Op2, 16)
    y = globals()[register[:2]]
    Op1 = int(bin(y), 2)
    Op2 = int(bin(Op2), 2)
    if (register == "AX"):
        AX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "BX"):
        BX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "CX"):
        CX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "DX"):
        DX = int(hex(Op1.__xor__(Op2)), 16)
    elif (register == "BP"):
        BP = int(hex(Op1.__xor__(Op2)), 16)
    printEstatus()

def NOT(register):
    global AX
    global BX
    global CX
    global DX
    global BP

    if register in ["AX", "BX", "CX", "DX"]:
        Op1 = globals()[register[:2]]
    Op1 = int(bin(Op1),2)
    exp = Op1.bit_length()
    xor = 2**exp-1
    if (register == "AX"):
        AX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "BX"):
        BX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "CX"):
        CX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "DX"):
        DX = int(hex(Op1.__xor__(xor)), 16)
    elif (register == "BP"):
        BP = int(hex(Op1.__xor__(xor)), 16)

    printEstatus()

def CMP(OP1, OP2):
    global JEF
    global JZF

    global AX
    global BX
    global CX
    global DX
    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag


    if (OP1 == OP2):
        zeroFlag = True
        JEF = True
    else:
        JEF = False

    printEstatus()
    ####JUMPS###
def JE(label):
    global JEF
    global JZF

    global lineaAsaltar
    global lineaEjecutada
    global CE
    global weota

    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    printEstatus()
    if (JEF):
        #main(int(lugar) - 1)
        pass
    printEstatus()

def JNE(lugar):
    global JEF
    global JZF
    global CE

    global lineaAsaltar
    global lineaEjecutada
    global weaRara
    global weota

    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    printEstatus()
    if (not JEF):
        #main(int(lugar) - 1)
        pass
    printEstatus()

def JZ(lugar):
    global JEF
    global JZF
    global CE

    global lineaAsaltar
    global lineaEjecutada
    global weaRara
    global weota

    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    printEstatus()
    if (JZF):
        #main(int(lugar) - 1)
        pass
    printEstatus()

def JNZ(label):
    global JEF
    global JZF
    global CE

    global lineaAsaltar
    global lineaEjecutada
    global weaRara
    global weota

    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    printEstatus()
    if (not JZF):
        pass
    printEstatus()

def JMP(lugar):
    global JEF
    global JZF
    global CE

    global lineaAsaltar
    global lineaEjecutada
    global weaRara
    global weota

    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    CE = 1
    printEstatus()

###########PRINTESTATUS###############

def printEstatus():
    global carryFlag
    global parityFlag
    global auxCarryFlag
    global zeroFlag
    global overflowFlag
    global traceFlag
    global interruptFlag
    global DirectionFlag
    global signFlag

    print("STACK")
    for x in range(len(stack)):
        print(stack[x])
    print("                                 ")
    print("AX =     ", AX)
    print("BX =     ", BX)
    print("CX =     ", CX)
    print("DX =     ", DX)
    print("BP =     ", BP)
    print("                      ")
    print("FLAGS    CF      PF      ACF     ZF      OF      TF      IF      DF      SF")
    print("        ", carryFlag ," ", parityFlag ," ", auxCarryFlag ," ", zeroFlag ," ", overflowFlag ," ", traceFlag ," ", interruptFlag ," ", DirectionFlag ," ", signFlag)
    #print(codigoEJECUTAR)
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////// \n")

def leer(linea):
    global lineaAsaltar
    global lineaEjecutada
    global weaRara
    #DATA
    if "MOV" in linea:
        MOV(linea[1], linea[-1]) #Ragistro, Variable

    elif "POP" in linea:
        POP(linea[1]) # Registro

    elif "PUSH" in linea:
        PUSH(linea[-1]) # Variable

    #ARITMETICA
    elif "INC" in linea:
        INC(linea[-1]) #registro

    elif "DEC" in linea:
        DEC(linea[-1]) #registro

    elif "ADD" in linea:
        ADD(linea[1], linea[-1]) #registro, numero

    elif "SUB" in linea:
        SUB(linea[1], linea[-1]) #registro, numero

    elif "MUL" in linea:
        MUL(linea[-1]) #Registro

    elif "DIV" in linea:
        DIV(linea[-1]) #Registro

    #Logico
    elif "CMP" in linea:
        CMP(linea[1], linea[-1]) #Operador 1, Operador 2 (Generalmente el Op1 es registro)

    elif "AND" in linea:
        AND(linea[1], linea[-1]) #IDEM

    elif "OR" in linea:
        OR(linea[1], linea[-1]) # IDEM

    elif "XOR" in linea:
        XOR(linea[1], linea[-1]) # IDEM

    elif "NOT" in linea:
        NOT(linea[-1]) # Operador 1

    elif "JE" in linea:
        JE(linea[1])
    elif "JNE" in linea:
        JNE(linea[1])
    elif "JZ" in linea:
        JZ(linea[1])
    elif "JNZ" in linea:
        JNZ(linea[1])
    elif "JMP" in linea:
        JMP(linea[1])
    #JUMPS
    '''
    else:
        SALTOS[weaRara] = linea[1]
        print(SALTOS)

    elif ":" in linea:
        lineaAsaltar = lineaEjecutada #ES UNA ETIQUETA...
        print (lineaAsaltar)
    '''
def main():
    global lineaAsaltar
    global lineaEjecutada
    global CE
    global weota
    global codigoEJECUTAR


    Asb = open("test2.txt", "r")
    Asb.readline()
    for line in Asb:
        #print (line)
        lineaEjecutada = lineaEjecutada + 1
        #print("LINEA:   ",lineaEjecutada)
        line = line.upper()
        listLinea = line.split()
        #print(listLinea)
        codigoEJECUTAR.append(listLinea)
        #print (codigoEJECUTAR)
    print(codigoEJECUTAR)
    Asb.close()
    for CE in range(0, len(codigoEJECUTAR)):
        print(CE)
        print(codigoEJECUTAR[CE])
        leer(codigoEJECUTAR[CE])
        CE = 1

'''
//DATAs
MOV
POP
PUSH
//ARITMETICA
INC
DEC
ADD
SUB
MULN
DIV
//LOGICAL
CMP
AND
OR
XOR
NOT
//BRANCHES
JE
JNE
JZ
JNZ
JMP
'''

main()
