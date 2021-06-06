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

## 透過views.py，創建從資料庫抓資料出來的頁面
    1. polls/views.py, 新增3個function,並用argument來處理各種頁面
    - detail 詳細頁
    - result 結果頁
    - vote 投票頁
    2. 在polls/urls.py去新增三個路由
    補充: 在每個路由中可以去指定name, 在前端templates可以方便套用
    3. 將.models內的資料表引進(Question), 在頁面的function去讀取資料表內容, 並return結果
    4. 若要回傳對應的templates html檔案, 則可以用render的方式
    return HttpResponse(template.render(context, request)), 或是用shortcut的方式
    return render(request, 'polls/index.html', context)
    5. 有時, 我們會需要從資料庫請求特定資料, 有的時候, 沒有的時候回傳404, Django提供了一種快速的函式, get_object_or_404()來使用, 記得要先導入才可以

    6. 若有多個app時, 要如何知道是哪個app的路徑呢?
    在polls/urls.py去新增 app_name, 並在templates動態變數中加入app_name:function
    ex: 
        polls/views.py, app_name = polls
        templates/polls/detail.html, {% url 'polls:detail' %}
    
## chapter4, 表單應用完成投票功能
    參考文獻: https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial04/
    1. 先在detail.html裡面去加上form的表單內容, 完成前端
    2. 接著在views.py裡面去處理detail function的返回內容, 完成後端
    3. 投票後, 我們將返回results的頁面, 頁面中去顯示該問題的每一個choice投票結果
    
    extra: 通用視圖(ListView)
    在views.py裡面, 透過一種class的特定寫法, 使用特定的變數命名
    就能達成一樣的結果, 並使代碼更簡潔有規則性
    例如: 要用通用視圖修改 index頁面
    1. polls/urls.py 將index的路徑改成 path('', views.IndexView.as_view(), name='index')
    2. views.py 建立 indexView的class(generic.ListView)去處理
    
    extra: 通用視圖(DetailView)
    例如: 要用通用視圖修改 detail頁面
    1. polls/urls.py 將index的路徑改成 path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    2. views.py 建立 DetailView的class(generic.DetailView)去處理
    

## 小筆記
    1. 為何使用py manage.py 去執行指令, 不是用py執行呢?
        是因為manage.py會設置DJANGO_SETTINGS_MODULE環境變量，這個變量會讓Django根據mysite/settings.py文件來設置Python包的導入路徑。