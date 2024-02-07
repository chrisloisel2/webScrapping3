## Importer librairies multiThreading
import threading
import time


def fonctiona():
    print("Fonction a")
    time.sleep(20)
    print("Fonction a terminée")

def fonctionb():
    print("Fonction b")
    time.sleep(2)
    print("Fonction b terminée")

## Creer les threads

# t1 = threading.Thread(target=fonctiona)
# t2 = threading.Thread(target=fonctionb)

# ## Lancer les threads
# t1.start()
# t2.start()


## Dictionnaire de threads

threads = {
	"t1": threading.Thread(target=fonctionb),
	"t2": threading.Thread(target=fonctiona)
}

threads["t1"].start()
threads["t2"].start()

## Attendre la fin des threads

threads["t1"].join()
print("Thread 1 terminé")


Faire une fonction qui permet de lancer le programme que vous vener de faire.

lancer cette fonction dans trois threads differents
 