from django.shortcuts import render

# Create your views here.
def index(request):
    # 入力内容での検索をする
    return render(request, "top.html")

def category(request):
    # カテゴリでの検索をする
    return render(request, "top.html")