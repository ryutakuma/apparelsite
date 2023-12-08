from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

def rakutenApi(url, params):
    keyword = request.POST.get('keyword', '')
    app_id = os.getenv('RAKUTEN_API_KEY')
    params = {
        'format': 'json',
        'keyword': keyword,
        'applicationId': app_id,

    }
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

def result(request):
  if request.method == 'POST':
    keyword = request.POST.get('keyword', '')#ユーザーが書き込みするときはデータを受け取るから書く
    api_url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch'
    app_id = os.getenv('YAHOO_API_KEY')
    params = {
      'format': 'json',
      'keyword': keyword,
      'applicationId': app_id,
    }
    response = requests.get(api_url, params=params)
    search_data = response.json()

    items = search_data['Items']
  else:
    items = []
    keyword = ""
  return render(request, 'top.html', {'items': items, 'keyword': keyword}) 

def index(request):
  ## ここからーーーーー
  keyword = request.POST.get('keyword', '')//ユーザーが書き込みするときはデータを受け取るから書く
  api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
  app_id = os.getenv('RAKUTEN_API_KEY')
  params = {
    'format': 'json',
    'keyword': keyword,
    'applicationId': app_id,
    'keyword': '',
  }
  response = requests.get(api_url, params=params)
  search_data = response.json()
  ## ここまでーーーーー 

  return render(request, 'top.html')

def rakutenApi(url, params):
    Ranking = request.POST.get('Ranking', '')
    app_id = os.getenv('RAKUTEN_API_KEY')
    params = {
        'format': 'json',
        'Ranking': Ranking,
        'applicationId': app_id,
        
    }
    response = requests.get(url, params=params)
    search_data = response.json()
    return Ranking_data

 

def index(request):
  ## ここからーーーーー
  Ranking = request.POST.get('Ranking', '')//ユーザーが書き込みするときはデータを受け取るから書く
  api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20220601?'
  app_id = os.getenv('RAKUTEN_API_KEY')
  params = {
    'format': 'json',
    'keyword': Ranking,
    'applicationId': app_id,
  }
  response = requests.get(api_url, params=params)
  Ranking_data = response.json()
  ## ここまでーーーーー 

  return render(request, 'top.html')