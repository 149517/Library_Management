from django.contrib.auth.models import User
from user.models import UserInfo
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view


@api_view(['POST'])
def login_view(request):
    """

    :param request:
    :return: login_status token
    """
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # 登录用户
            login(request, user)
            # 获取与当前用户关联的UserInfo对象

            # 获取与当前用户关联的UserInfo对象
            try:
                userinfo = UserInfo.objects.get(username=username)
                pic = userinfo.pic
            except UserInfo.DoesNotExist:
                userinfo = None
                pic = None
                print(pic)
            # 创建或获取 Token
            token, created = Token.objects.get_or_create(user=user)
            # 返回 Token 到客户端
            return JsonResponse({'code': 200, 'msg': '登录成功', 'token': token.key, "pic": pic})
        else:
            # 身份验证失败，返回错误消息
            return JsonResponse({'code': 400, 'msg': '登录失败，用户名或密码错误'})


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
