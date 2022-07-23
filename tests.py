from dotenv import dotenv_values, load_dotenv
import os

key = dotenv_values(".env")
load_dotenv('.env')

print(os.getenv('APIKEY'))
print(key['APIKEY'])