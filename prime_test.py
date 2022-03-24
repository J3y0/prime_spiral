import random as rd
from math import floor, sqrt


########## Probabilistic primality test ############
def temoin_fermat(integer,a):
    """
    :param a est le potentiel témoin de n selon la propriété du petit théorème de Fermat
    :return booléen selon si a est un témoin ou non
    """
    if exponentiation_rapide_modulaire(integer-1,a,integer) != 1:
        return True
    else:
        return False

def exponentiation_rapide_modulaire(integer,a,mod):
    """
    Permet d'améliorer la vitesse de calcul
    :return: le résultat a**integer modulo mod
    """
    if integer == 1:
        return a%mod
    else:
        if integer%2 == 0:
            c = exponentiation_rapide_modulaire(integer//2, a,mod)
            return (c*c)%mod #On écrit pas deux fois explicitement c sinon on fait 2 fois le même calcul -> complexité plus importante
        else:
            return (a*exponentiation_rapide_modulaire(integer-1,a,mod))%mod


def is_prime_fermat(integer):
    for i in range(3):
        a = rd.randint(1, integer-1)
        if temoin_fermat(integer,a):
            return False
    return True

##################################################

########## Determinist primality test ############
def is_prime_div(n):
    """
    Méthode classique, on teste s'il existe un entier plus petit que sqrt(n) qui divise n
    :param l'entier dont on veut tester la primalité
    :return un booléen
    """
    if n<2:
        return False

    for d in range(2, floor(sqrt(n))):
        if n%d == 0:
            return False
    return True
##################################################


if __name__ == '__main__':
    print(is_prime_fermat(7))
    print(is_prime_fermat(70))
    print(is_prime_fermat(7152548))
