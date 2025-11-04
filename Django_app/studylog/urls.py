from django.urls import path
from . import views

# このファイルは studylog アプリ（学習ログ）のURL設定をまとめる場所
# calc_project/urls.py から include() で呼び出される

app_name = "studylog"  # ← テンプレート内で {% url 'studylog:～' %} として使うための名前空間

urlpatterns = [
    # ---- トップページ（学習科目の一覧）----
    # 例: http://127.0.0.1:8000/studylog/
    # → views.subject_list() が実行される
    path("", views.subject_list, name="subject_list"),

]
