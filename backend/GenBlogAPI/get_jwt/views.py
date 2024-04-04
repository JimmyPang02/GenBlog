import datetime
import jwt
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

from GenBlogAPI.settings import SECRET_KEY


@csrf_exempt
def get_jwt_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 验证用户名和密码是否正确
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # 验证成功，返回jwt令牌
        access_token = generate_access_token()
        refresh_token = generate_refresh_token()
        return JsonResponse({'access_token': access_token.decode(), 'refresh_token': refresh_token.decode()})
    else:
        # 验证失败，返回None
        return JsonResponse({'校验失败，拒绝生成jwt令牌'})


def generate_access_token():
    # 设置token的有效期为5分钟
    expiration = datetime.utcnow() + timedelta(minutes=5)
    # payload中包含用户相关信息和token的过期时间
    payload = {
        'uid': 1,
        'exp': expiration
    }
    # 使用SECRET_KEY进行签名,生成token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def generate_refresh_token():
    # 设置token的有效期为14天
    expiration = datetime.utcnow() + timedelta(days=14)
    # payload中包含用户相关信息和token的过期时间
    payload = {
        'uid': 1,
        'exp': expiration
    }
    # 使用SECRET_KEY进行签名,生成token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


@csrf_exempt
def validate_jwt(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return JsonResponse({'0': '缺少token'}, status=401)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse({'0': 'token已过期'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'0': '无效token'}, status=401)

    return JsonResponse({'1': '验证通过'}, status=200)
