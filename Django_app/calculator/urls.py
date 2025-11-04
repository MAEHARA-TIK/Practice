from django.urls import path
from . import views

# calculator アプリのルーティング設定
urlpatterns = [
    # トップページ（電卓本体）
    # GET: フォームを表示、POST: 計算を実行して結果を表示
    path('', views.index, name='index'),

    # result/ は index の中で処理しているので不要
    # path('result/', views.result, name='result'),
]
