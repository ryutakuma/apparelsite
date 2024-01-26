from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

def rakutenApi(url, params):
  ## ApplicationIDを取得するためのコード
  load_dotenv()

  app_id = os.getenv('RAKUTEN_API_KEY')
  params['applicationId'] = app_id
  response = requests.get(url, params=params)
  search_data = response.json()
  return search_data

def yahooApi(url, params):
  ## ApplicationIDを取得するためのコード
  load_dotenv()

  app_id = os.getenv('YAHOO_API_KEY')
  params['applicationId'] = app_id
  response = requests.get(url, params=params)
  search_data = response.json()
  return search_data


# Create your views here.
def result(request):
  ## HTMLに渡す変数群
  viewDatas = {}

  ## ここからーーーーー
  Ranking = request.POST.get('Ranking', '') #ユーザーが書き込みするときはデータを受け取るから書く
  # Ranking_data = response.json()
  Ranking_data = rakutenApi('https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20220601?', {
    'format': 'json',
    'keyword': Ranking,
  })
  viewDatas['Ranking_data'] = Ranking_data['Items']
  ## ここまでーーーーー 

  ## ここからーーーーー
  keyword = request.GET.get('keyword', '') #ユーザーが書き込みするときはデータを受け取るから書く
  if len(keyword) != 0:
    result = rakutenApi('https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?', {
      'format': 'json',
      'keyword': keyword,
    })
    viewDatas['result'] = result['Items']
    print(result['Items'][0])
  ## ここまでーーーーー 

  return render(request, 'top.html', viewDatas)


def index(request):
  ## ここからーーーーー
  Ranking = request.POST.get('Ranking', '') #ユーザーが書き込みするときはデータを受け取るから書く
  # Ranking_data = response.json()
  Ranking_data = rakutenApi('https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20220601?', {
    'format': 'json',
    'keyword': Ranking,
  })
  ## ここまでーーーーー 

  return render(request, 'top.html', {
    'Ranking_data': Ranking_data['Items']
  })