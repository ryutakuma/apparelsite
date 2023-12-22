from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

def rakutenApi(url, params):
    app_id = os.getenv('RAKUTEN_API_KEY')
    params['applicationId'] = app_id
    response = requests.get(url, params=params)
    search_data = response.json()
    return search_data

def yahooApi(url, params):
    keyword = request.POST.get('keyword', '')
    app_id = os.getenv('YAHOO_API_KEY')
    params = {
        'format': 'json',
        'keyword': keyword,
        'applicationId': app_id,
    }
    response = requests.get(url, params=params)
    search_data = response.json()
    return search_data

# Create your views here.
def index(request):
  ## ここからーーーーー
  keyword = request.POST.get('keyword', '')//ユーザーが書き込みするときはデータを受け取るから書く
  api_url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch'
  app_id = os.getenv('YAHOO_API_KEY')
  params = {
    'format': 'json',
    'keyword': keyword,
    'applicationId': app_id,
  }
  response = requests.get(api_url, params=params)
  search_data = response.json()
  ## ここまでーーーーー 

  return render(request, 'top.html')

# def result(request):
#   if request.method == 'POST':
#     keyword = request.POST.get('keyword', '')#ユーザーが書き込みするときはデータを受け取るから書く
#     api_url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch'
#     app_id = os.getenv('YAHOO_API_KEY')
#     params = {
#       'format': 'json',
#       'keyword': keyword,
#       'applicationId': app_id,
#     }
#     response = requests.get(api_url, params=params)
#     search_data = response.json()

#     items = search_data['Items']
#   else:
#     items = []
#     keyword = ""
#   return render(request, 'top.html', {'items': items, 'keyword': keyword}) 

# def index(request):
#   ## ここからーーーーー
#   keyword = request.POST.get('keyword', '')//ユーザーが書き込みするときはデータを受け取るから書く
#   api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
#   app_id = os.getenv('RAKUTEN_API_KEY')
#   params = {
#     'format': 'json',
#     'keyword': keyword,
#     'applicationId': app_id,
#     'keyword': '',
#   }
#   response = requests.get(api_url, params=params)
#   search_data = response.json()
#   ## ここまでーーーーー 

#   return render(request, 'top.html')
 

def index(request):
  ## ここからーーーーー
  Ranking = request.POST.get('Ranking', '') #ユーザーが書き込みするときはデータを受け取るから書く
  # Ranking_data = response.json()
  Ranking_data = rakutenApi('https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20220601?', {
    'format': 'json',
    'keyword': Ranking,
  })
  ## ここまでーーーーー 
  print(Ranking_data)

  return render(request, 'top.html', {'Ranking_data': Ranking_data})

  def index(request):
  ## ここからーーーーー
  janru = request.POST.get('janru', '') #ユーザーが書き込みするときはデータを受け取るから書く
  # Ranking_data = response.json()
  janru_data = rakutenApi('https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222?', {
    'format': 'json',
    'genreId': janru,
  })
  ## ここまでーーーーー 
  print(janru['brothers'])

  return render(request, 'top.html', {'janruList': janru_data})