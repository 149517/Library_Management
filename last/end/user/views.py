from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user.models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse

from rest_framework.authtoken.models import Token


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


def logout_view(request):
    logout(request)
    return JsonResponse({'code': 200, 'msg': '退出登录'})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def manage_view(request):
    if request.method == 'POST':
        user_id = request.user.id  # 从令牌中解析出user_id
        # 获取用户对象，如果不存在则返回404错误页面
        # print(user_id)
        try:
            user = UserInfo.objects.get(id=user_id)
        except UserInfo.DoesNotExist:
            return JsonResponse({'code': 404, "msg": "当前用户不存在"})

        # 检查用户是否具有管理权限
        if user.is_staff:
            # 如果用户具有管理权限，执行相应的操作
            # 例如，返回一个成功的响应或执行其他逻辑
            return JsonResponse({'code': 200, "msg": "用户具有管理权限"})
        else:
            # 如果用户没有管理权限，执行相应的操作
            # 例如，返回一个错误的响应或执行其他逻辑
            return JsonResponse({'code': 401, "msg": "用户权限不足"})
