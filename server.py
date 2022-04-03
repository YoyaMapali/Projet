#./bin/bash
import socket
import time
import json
import database

#Fonction qui recupére les informations de connexion d'un client
def Connexion(client:socket,buffer:int):
    liste = list()
    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) #1
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre mot de passe svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Connexion(liste) == True:
        req = "Connexion reussie !!!"
        client.send(req.encode("utf-8")) #3
    else:
        req = "Echec de lors de la connexion !!!"
        client.send(req.encode("utf-8")) #3

#Fonction qui initialise une connexion client et d'interagir avec lui
def openServer(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((host,port))
    serveur.listen(5)

    client, infClient = serveur.accept()
    print("Client connecté. Adresse " + infClient[0])  

    while True:    
        
        reponse = " 1 se connecter, 2 pour quitter "
        client.send(reponse.encode("utf-8"))
        time.sleep(2)

        requete = client.recv(buffer)
        requete_decode = requete.decode("utf-8")

        if requete_decode == "1":
            Connexion(client,buffer)

        elif requete_decode == "2":         
            req = "by !!!"
            client.send(req.encode("utf-8")) 
            client.close()
            break

    serveur.close()
           
    


if __name__ == "__main__":
    
    openServer('localhost', 50000)
