from googleapiclient.discovery import build

search_term = input("Ingrese el nombre de la persona a la cual quiere buscar los resultados de las redes sociales")

my_api_key = "AIzaSyBMPvN0YUaPStv_pNEn5cKarwYYYnaaCQo" #The API_KEY you acquired
my_cse_id = "9b274256375f7c4a1" #The search-engine-ID you created

def google_search(search_term, api_key, cse_id):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id).execute()
    return res['items']


results = google_search(search_term, my_api_key, my_cse_id)
for result in results:
    print(result)