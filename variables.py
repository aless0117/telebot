import requests
import sys

id = "@pruebadelcanal"

token = "366674849:AAH2xDCGrXohH3RaWAMfzeoVggJceNbPFTA"

url = "https://api.telegram.org/bot" + token + "/sendMessage"
params = {
'chat_id': id,

'text' : "Esto lo estoy enviando desde python"
}

requests.post(url, params=params)
