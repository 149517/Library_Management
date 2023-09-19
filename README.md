#  图书管理系统



##  项目概览

####  登录注册

* 在一个页面中切换UI，使页面切换更流畅。

![image-20230919140639903](./assets/image-20230919140639903.png)

![image-20230919140658337](./assets/image-20230919140658337.png)

####  Home

![image-20230919140857132](./assets/image-20230919140857132.png)

#### 图书列表

![image-20230919140903845](./assets/image-20230919140903845.png)

####  记录查询

![image-20230919140911066](./assets/image-20230919140911066.png)


####  数据修改

![image-20230919140915498](./assets/image-20230919140915498.png)


###  项目介绍

通过 Vue.js + Django 搭建前后端分离的图书管理系统。

用于平时的制作与学习。

部分图书数据来自于微信读书和豆瓣阅读。



###  项目更新



* 2023-09-16

1. 实现登录注册功能，在可在客户端实现注册登录功能。
2. 实现图书数据的获取和刷新，书籍信息的分页展示
3. 实现图书的查询，用户书籍信息的添加（购买和借阅）
4. 个人用户书籍信息的查询（购买和借阅）



* 2023-09-19

1. 修改了登录注册时候验证token，无法请求的问题
2. 增加了部分数据
3. 添加了数据的修改和增加（管理用户）
4. 优化部分UI



#  制作



###  网站设计

网站链接：[HappyFunCorp, a NYC-based Product Engineering Firm](https://happyfuncorp.com/#home)

参考页面：

![image-20230904190556408](./assets/image-20230904190556408.png)



####  栏目设计和内容

######  前端

* 首页（不必登录）

* 用户登录注册（一页）

* 书目（书籍列表）

  

  

######   后端

* 用户系统（内建用户，继承内部抽象类进行拓展）
* 书籍
* 记录



####  项目大纲

![image-20230919135734670](./assets/image-20230919135734670.png)



##  后端程序

* Python，Django，MySQL



> django-admin startproject end



###  数据库配置

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library',
        'USER': 'root',
        'PASSWORD': '149517',
        'HOST': '127.0.0.1',
        'POST': '3306'
    }
}
```



* 由于跨域，Cookie等问题的影响，重新建立一个后端系统，last-end




###   跨越处理-Django

####  使用模块

> pip install django-cors-headers



####  settings.py 配置

* 只对修改了并且关于跨域的部分进行展示

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    ['http://127.0.0.1:*']
)

CORE_ALLOW_METHODS = ('DELETE', 'GET', 'POST', 'PUT')

CORS_ALLOWED_ORIGINS = [
    "http://10.218.39.118:5173",  # 允许跨域请求的前端应用的域名
]

CORS_ALLOW_HEADERS = (
    "content-type",
    'XMLHttpRequest',
    'x_FILENAME',
    'accept-encoding',
    'authorization',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma'
)

```



* 配置完成即可实现跨域



###  发送token

前后端分离的系统中，Django发送token也需要配置跨域

####  模块

> pip install djangorestframework 
>
> pip install djangorestframework-extensions

####  settings.py配置

* 保留对应的修改

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

```



####  在 views 中使用

```py
# dajngo 自己的用户表和内建的用户表
from django.contrib.auth.models import User
from user.models import UserInfo
# Django用户表的操作
from django.contrib.auth import authenticate, login

from django.http import JsonResponse
# token 
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login_view(request):
	# 接受 POST 请求
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')
		
        # 内置，比对用户名和密码
        user = authenticate(username=username, password=password)

        if user is not None:
            # 登录用户，login登录状态
            login(request, user)

            # 创建或获取 Token
            token, created = Token.objects.get_or_create(user=user)
            # 返回 Token 到客户端
            return JsonResponse({'code': 200, 'msg': '登录成功', 'token': token.key})
        else:
            # 身份验证失败，返回错误消息
            return JsonResponse({'code': 400, 'msg': '登录失败，用户名或密码错误'})


def register_view(request):

    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # 1. 密码保持一致
        if password != password2:
            return JsonResponse({"msg": '密码输入不一致', "success": False})

        # 检查用户名是否已经存在
        if UserInfo.objects.filter(username=username).exists():
            return JsonResponse({'code': 200, 'msg': '用户名已经存在'})
        else:
            # 创建用户
            UserInfo.objects.create_user(username=username, password=password)
            return JsonResponse({'code': 201, 'msg': '用户创建成功'})

```





###  用户系统

* 通过 Django 内置的用户系统作为网站的用户系统
  * 处理方便，添加和删除等操作都有对应的指令完成
  * 对于密码等自动进行处理无需手动加密
  * 但是内置用户字段固定



####  继承抽象类进行创建

步骤

> 1. 添加新应用 -    `py manage.py startapp user`
> 2. 定义模型类，继承 AbstractUser
> 3. settings 中，指明` AUTH_USER_MODEL = ‘应用名.类名’`

**注意，此操作一定要在第一次 Migrate 之前**

```Python
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    career = models.CharField(max_length=24,default="")
```

* 在Django内置的字段基础上，添加了一个 career （职业）



####  数据迁移

> py manage.py makemigrations
>
> py manage.py migrate







####  用户添加

* user/views.py 
* 注册模块

```Python
def register_view(request):
    """
    :param request:
    :return: msg
    """
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # 1. 密码保持一致
        if password != password2:
            return JsonResponse({"msg": '密码输入不一致', "success": False})

        # 检查用户名是否已经存在
        if UserInfo.objects.filter(username=username).exists():
            return JsonResponse({'code': 200, 'msg': '用户名已经存在'})
        else:
            # 创建用户
            UserInfo.objects.create_user(username=username, password=password)
            return JsonResponse({'code': 201, 'msg': '用户创建成功'})
```





###  应用创建及数据模型

####  应用

> py manage.py startapp books;

* books,record

####  图书数据模型

```py
from django.db import models


class Book(models.Model):
    bookname = models.CharField('书名', max_length=64)
    author = models.CharField("作者", max_length=64)
    isbn = models.CharField('ISBN', unique=True, max_length=20)
    Listing_time = models.DateField("出版时间")
    updated_time = models.DateTimeField("添加时间", auto_now_add=True)
    type = models.CharField("类型", max_length=32)
    lang = models.CharField("语言", max_length=32)
    publisher = models.CharField("出版社", max_length=32)
    price = models.DecimalField("定价", max_digits=8, decimal_places=2)
    intro = models.CharField("描述", default="", max_length=512)
    pic = models.CharField("封面", default='',max_length=64)
```



####  记录数据模型

```py
class Record(models.Model):
    user = models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    # 使用ForeignKey关联User模型中的id字段
    type = models.CharField("记录类型", max_length=12)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    status = models.BooleanField("状态", default=True)
    addTime = models.DateTimeField("添加时间", auto_now_add=True)

```




###  分页查询

####  模块

> from django.core.paginator import Paginator
> from django.core import serializers
> import json

* Paginator，Django自带的分页查询工具
* serializeres，json，用于QuerySet对象的序列化，因为是前后端分离项目，返回JsonResponse对象时候需要进行序列化

####  分页

```py
def all_view(request):
    # 数据获取
    books = Book.objects.all()
    # 分页，分页的数组，每页的数量
    paginator = Paginator(books, 4)

    # 获取 url 地址中的page，传递的第几页，如果没有page，则默认为1
    page_number = request.GET.get('page', 1)
   	# 获取 第 page 页内容
    page_obj = paginator.get_page(page_number)

    # 将QuerySet序列化为JSON格式
    serialized_data = serializers.serialize('json', page_obj)

    # 转换为Python数据结构
    data = json.loads(serialized_data)

    # 构建包含分页信息的字典
    pagination_info = {
        # 总数
        # 当前页
        # 是否有下一页
        # 是否有上一页
        "total_pages": paginator.num_pages,
        "current_page": page_obj.number,
        "has_next": page_obj.has_next(),
        "has_previous": page_obj.has_previous(),
    }

    return JsonResponse({"data": data, "pagination_info": pagination_info}, safe=False)
```



####  

##  前端程序

* Vite，Vue.js



> npm create vite@latest front -- --template vue



####  路由配置

######  main 

```js
import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/router.js";


const app = createApp(App)
app.use(router)

app.mount('#app')

```



######  router 路由

```js
import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "../components/Home.vue";


const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {path: '/', component: Home},
    ],
})

export default router;
```



###  homePage

####  Nav

![image-20230906114341913](./assets/image-20230906114341913.png)

* 在链接处，添加鼠标经过底部横线滑入和滑出事件
* 在 `Sign in`处，添加一个鼠标经过颜色块填充的效果，同样是滑入滑出效果



####  效果实现

初步实现是通过`:hover`事件，但是还添加了动画 `aniamtion:leftIn .3s linear`

1. 在执行中，只添加了了一个进入动画，结束直接消失没有动画。

2. 所以打算使用反向的动画，但是只能是通过css只能添加进入效果

3. 添加 JS 动画，但是没有执行效果。

4. 在后续实践中，无法使用。事件无法触发

5. 故而采用，width和transition的方式实现动画





####  logo

![logo2](./assets/logo2.png)



###  login & register

* 最初是制作为两个不同的组件通过跳转的方式进行打开

* 但是出于对页面UI，页面动画效果的呈现

**使用的是将两个页面放在一起，通过页面中变量的切换实现不同额页面样式的展示**

1. 在register页面，midBox 会比 Login 页面高
2. 同时 form 内部同样变高
3. 而内部还多出一个密码输入框

####  页面

![image-20230910225833091](./assets/image-20230910225833091.png)



####  实现

1. 在点击右上角登录或者注册时候修改 this.login 的值，进行页面样式的修改
2. 输入框内容发生改变时候，触发watch，监听数据的长度，这里只是进行了长度的检查
3. 点击登录时候，取消了默认的提交操作
   * 取而代之的是对于内容的检查，此处只是设置了是否为空的检查
   * 不为空则会执行this.submitForm()
   * 接收参数，如果是login，则请求login接口
4. 在用户登录后，会接收到来自服务器的token，然后将其存储到浏览器中





####  代码

```vue
<script>
import {mapState} from "vuex";
import axios, {formToJSON, toFormData} from "axios";
export default {
  computed: {
    ...mapState(['baseUrl'])
  },
  data() {
    return {
      // 是否是登录页面
      login: true,
      uname: '',
      password: "",
      password2: "",
      // 输入提示
      unameTip: "",
      passwordTip: "",
      password2Tip: "",
      // 控制密码可见
      psV: true,
      ps2V: true,
    }
  },
  methods: {
    Jump() {
      this.login = !this.login;
      let mid = document.querySelector('.mid');
      let btn = document.querySelectorAll('label')[2];

      if (!this.login) {
        mid.classList.add('res_mid')
      } else {
        mid.classList.remove('res_mid')
      }
    },
    submitForm(type) {
      let url = this.baseUrl + '/user/'
      let formData = new FormData();
      formData.append('uname', this.uname);
      formData.append('password', this.password);
      if (type === 'login') {
        url = url + 'login/';
        this.axiosLogin(url, formData)
      }
      if (type === 'register') {
        url = url + 'register/';
        formData.append('password2', this.password2);
        this.axiosRegister(url, formData)
      }
    },
    axiosLogin(url, formData) {
      axios
          .post(url,formData)
          .then(res => {
            console.log(res.data)
            if (res.data.code === 200) {
              localStorage.setItem('token', res.data.token);
              localStorage.setItem('pic', res.data.pic)
              this.$store.commit('setName', this.uname)
              this.$store.commit('setPicUrl', res.data.pic)
              this.$router.push('/')
            } else {
              alert(res.data.msg)
            }
          })
          .catch(err => {
            console.log("数据提交失败" + err)
          })
    },
    </div>
  </div>
</template>

```



###  书目



####  分页数据展示

> 现存问题，因为数据量较少，没有考虑数据过多时候的按钮切换效果

* 通过按钮点击传递数据
* 通过`disabled`控制按钮是否能够点击



#####  整体实现

* 通过data数据，监听page的修改，修改后就发送一次请求，获取当页的数据





##  数据库

* Mysql



> create database library charset=utf8;



###  书籍信息添加（手动）

**使用的是 Django的admin后台管理系统**

####  超级用户的创建

`py manage.py createsuperuser`

* 添加超级用户后才能进行书籍信息的修改，需要权限



####  书籍数据导入

* 通过在MySQL中创建 'library' 数据库
* 继承用户抽象类
* 在Python中进行数据迁移后
* 然后添加`books_book.sql`



####  后台管理界面查看数据

**注册步骤**

1. 在应用 app 中的 `admin.py` 中导入注册要管理的models类，如 `from .models import Book`
2. 调用 `admin.site.register` 方法进行注册，如 `admin.site.register` (自定义模型类)

```py
from django.contrib import admin

from .models import Book


admin.site.register(Book)
```

