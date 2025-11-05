from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),

    # ---- メインアプリ設定 ----
    # トップページ → inputValueアプリを表示
    path('', include(('inputValue.urls', 'inputValue'), namespace='inputValue')),

    # ---- サブアプリ設定 ----
    # http://127.0.0.1:8000/studylog/
    path('studylog/', include(('studylog.urls', 'studylog'), namespace='studylog')),
]
