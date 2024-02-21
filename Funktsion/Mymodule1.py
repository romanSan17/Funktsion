from re import X


def summa(arv1:int, arv2:int, arv3=0)->int:
    """ Funktsioon tagastab kolme arvu suuma
        Summa(arv1,arv2,arv3)

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    s=arv1+arv2+arv3
    return s
def IntKontroll(x):
    try:
        x = int(x)
        return "int"
    except:
        try:
            x=float(x)
            return "float"
        

def arithmetic (arv1,arv2,operatsioon)->any:
""" 

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    if operatsioon=="+":
        return arv1+arv2
    elif operatsioon=="-":
        return arv1-arv2
    elif operatsioon=="*":
        return arv1*arv2
    elif operatsioon=="/":
        if not(arv2==0):
            return arv1/arv2
        else:
            return "Nullga jagada ei saa"
    else:
        return "Tundmatu toiming"