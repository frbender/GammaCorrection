def mM(x):
    if x < 0:
        return 0
    if x > bits-1:
        return bits-1
    return int(round(x))

def generateGammaCorrectionTable(a,b):
    myOutput = "{"
    for i in range(bits):
        myOutput += str(mM(pow(float(i) / float(bits-1),a)*float(b)*float(bits-1)))
        if(i != bits-1):
            myOutput += ", "
    myOutput += "}"
    return myOutput

bits = 4096
print(generateGammaCorrectionTable(2,1))
