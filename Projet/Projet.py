import psutil
import subprocess

def lister_partitions():
    partitions = psutil.disk_partitions(all=True)
    for partition in partitions:
        print("Device:", partition.device)
        print("Mountpoint:", partition.mountpoint)
        print("Fstype:", partition.fstype)
        print("Opts:", partition.opts)
        print("")

def creer_partition():
    print("Attention: La création de partition est une opération potentiellement dangereuse.")
    device = input("Veuillez entrer le chemin du périphérique à partitionner (ex: 'C:') : ")
    confirm = input(f"Êtes-vous sûr de vouloir créer une partition sur {device} ? (oui/non) : ")
    if confirm.lower() == "oui":
        try:
            with open("create_partition.txt", "w") as f:
                f.write(f"select volume {device}\ncreate partition primary\nexit")
            subprocess.run(["diskpart", "/s", "create_partition.txt"], check=True)
            print("Partition créée avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la création de la partition : {e}")
        finally:
            subprocess.run(["del", "create_partition.txt"], shell=True)
    else:
        print("Opération annulée.")

def supprimer_partition():
    print("Attention: La suppression de partition est une opération potentiellement dangereuse.")
    device = input("Veuillez entrer le chemin du périphérique à supprimer (ex: 'C:') : ")
    confirm = input(f"Êtes-vous sûr de vouloir supprimer la partition {device} ? (oui/non) : ")
    if confirm.lower() == "oui":
        try:
            with open("delete_partition.txt", "w") as f:
                f.write(f"select volume {device}\ndelete volume\nexit")
            subprocess.run(["diskpart", "/s", "delete_partition.txt"], check=True)
            print("Partition supprimée avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la suppression de la partition : {e}")
        finally:
            
            subprocess.run(["del", "delete_partition.txt"], shell=True)
    else:
        print("Opération annulée.")

def afficher_menu():
    print("1. Lister les partitions disponibles")
    print("2. Créer une partition")
    print("3. Supprimer une partition")
    print("4. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            lister_partitions()
        elif choix == "2":
            creer_partition()
        elif choix == "3":
            supprimer_partition()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()