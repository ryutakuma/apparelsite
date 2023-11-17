from django.shortcuts import render

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

# Create your views here.
def index(request):
    from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

# Create your views here.
def index(request):
    ## ランキングここからーーーーー
    search_data = rakutenApi('rankingのURL',{})
    ## ランキングここからーーーーー
    return render(request, 'top.html', {'keyword': ""})

def result(request):
  if request.method == 'POST':
    load_dotenv()

    ## ここからーーーーー
    keyword = request.POST.get('keyword', '')
    api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    app_id = os.getenv('RAKUTEN_API_KEY')
    params = {
      'format': 'json',
      'keyword': keyword,
      'applicationId': app_id,
    }
    response = requests.get(api_url, params=params)
    search_data = response.json()
    ## ここまでーーーーー

    ## ここからーーーーー
    keyword = request.POST.get('keyword1', '')
    api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    app_id = os.getenv('YAHOO_API_KEY')
    params = {
      'format': 'json',
      'keyword': keyword,
      'applicationId': app_id,
    }
    response = requests.get(api_url, params=params)
    yahoo_data = response.json()
    ## ここまでーーーーー

    items = data['Items']
  else:
    items = []
    keyword = ""
  return render(request, 'top.html', {'items': items, 'keyword': keyword})










    return render(request, "top.html")