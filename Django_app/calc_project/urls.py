"""
URL configuration for calc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 管理画面用URL（Django標準）
    path('admin/', admin.site.urls),

    # ---- メインアプリ設定 ----
    # トップページ（http://127.0.0.1:8000/inputValue）で開くアプリを指定
    # ここでは「calculator」アプリをメインとして設定
    path('inputValue', include(('inputValue.urls', 'inputValue'), namespace='calculator')),

    # ---- サブアプリ設定 ----
    # 学習ログアプリへのルーティング
    # http://127.0.0.1:8000/studylog/ でアクセスできるようになる
    path('studylog/', include(('studylog.urls', 'studylog'), namespace='studylog')),
]



