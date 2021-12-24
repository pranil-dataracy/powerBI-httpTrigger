import requests

re=requests.get('https://powerbi-refresh-api.azurewebsites.net/api/powerBI-refresh?code=uSmyuvYUp9EOPJuAhlFAFPpvay/dZiChztp9KfOTAHz1a5438mW01A==')
print(re.text)