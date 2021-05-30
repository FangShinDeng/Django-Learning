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
    1. python manage.py migrate 初始化資料庫, 同時進行資料庫版本控管
    2. polls/model.py 加入兩張表
    3. mysite/setting.py INSTALLED_APPS 加入 'polls.apps.PollsConfig'
    4. 運行 python manage.py makemigrations polls 指令, 產生版本的變更
    5. 運行 python manage.py sqlmigrate polls 0001, 就會看到自動生成的sql語法
    6. 運行 python manage.py migrate, 再次運行migrate命令，在數據庫裡創建新定義的模型的數據表
    執行完第6步驟後, 再去看一次db, 就會發現資料庫確實新增了兩張表了
    
    