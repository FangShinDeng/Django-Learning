# 學習使用Django
    參考學習: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment
    參考學習: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## 最重要的兩個指令(
    參考學習: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment
    1. django-admin startproject [mysite] 創建一個站點
    2. python manage.py runserver　運行伺服器
    
## 學習運用manage.py 來創建app項目, 並產生index page
    參考學習: https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial01/
    1. 創建app指令: python manage.py startapp `polls`
    2. 創建 polls/urls.py 路由器, 設定polls的跟目錄到index function
    3. 在polls/views.py 定義index函式
    4. 最後記得要在主要設定的路由器上加入polls的路由 mysite/urls.py -> urlspatterns 加入polls的路徑

## 使用指令初始化資料表, 創建新的資料表
    參考學習: https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial02/
    python manage.py migrate

    