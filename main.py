from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'9',
  'limit':'1'
  }
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f9bf8f9d-1c75-4ffe-8a9a-759d2d5ddaf7',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)