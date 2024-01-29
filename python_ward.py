import requests
import pprint
import csv
from colorama import init, Fore

ascii_art = """
 __    _____  ____  ____     ____    __    ___  _   _  ____  _____    __    ____  ____  
(  )  (  _  )(  _ \(  _ \   (  _ \  /__\  / __)( )_( )(  _ \(  _  )  /__\  (  _ \(  _ \ 
 )(__  )(_)(  )   / )(_) )   )(_) )/(__)\ \__ \ ) _ (  ) _ < )(_)(  /(__)\  )   / )(_) )
(____)(_____)(_)\_)(____/   (____/(__)(__)(___/(_) (_)(____/(_____)(__)(__)(_)\_)(____/ 
                                                                                                                                                                 
"""
init(autoreset=True)
print(Fore.GREEN + ascii_art)
print(Fore.CYAN + "Welkom bij het python examen script!")

# Het script moet de user op een bepaalde manier welkom heten bij het starten van het programma
naam = input("Wat is je naam: ")
print(Fore.YELLOW + f"Yo, {naam}! We gaan wat JSON data van een saaie api afhalen.")
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# Controleer de responsecode
if response.status_code == 200:
    print(Fore.GREEN + f"Data succesvol opgehaald. responscode is: {response.status_code}")
    data = response.json()
    pprint.pprint(data)
    
    # Data nu naar een CSV-bestand
    with open('json_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

    print(Fore.BLUE + "Data is opgeslagen in 'json_data.csv'.")
else:
    #Gaat mis error
    print(Fore.RED + f"Dat ging mis: {response.status_code}")

print(Fore.CYAN + f"Bedankt voor het gebruiken van het dit script, {naam}!")
