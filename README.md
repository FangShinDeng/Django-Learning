# 學習使用Django
    參考學習: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment
    參考學習: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## 最重要的兩個指令(
    參考學習: https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment
    1. django-admin startproject [mysite] 創建一個站點
    2. python manage.py runserver　運行伺服器
    
## 學習運用 manage.py 來創建app項目, 並產生index page
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

## 用數據庫API, 來使用創建的兩張表吧! 
    創建兩張表後，我們能用 py manage.py shell 來執行命令視窗
    執行以下內容: 
    from polls.models import Choice, Question
    Question.objects.all() -> 發現沒有資料
    q = Question(question_text="What's new?", pub_date=timezone.now()) -> 創建Question資料
    q.save() -> 儲存資料 (這樣資料就已經進到資料庫了)
    
    在來使用內建的API, Django提供了_set的方法, ex:
    q.choice_set.create(choice_text='Not much', votes=0) -> 透過foreign key指定的表去創立choice表的內容
    q.choice_set.all() -> 查看該question的內容
    q.choice_set.create(parameters = 'content') -> 創建資料

## 創建adminuser, 進入後台!
    首先透過指令來創建admin user
    python manage.py createsuperuser
    username: admin
    Email address: admin@example.com
    password: XXXXXXXX

    運行伺服器, 然後到/admin路徑並用admin帳號密碼登入!

## 後臺操作
    進入到後台後, 我們透過在polls/admin.py去新增Question, Choice, Answer模塊, 這些模塊我們能直接在後台做操作! 包含新建, 刪除, 查詢資料 及操作紀錄(log查詢)
    

## 小筆記
    1. 為何使用py manage.py 去執行指令, 不是用py執行呢?
        是因為manage.py會設置DJANGO_SETTINGS_MODULE環境變量，這個變量會讓Django根據mysite/settings.py文件來設置Python包的導入路徑。