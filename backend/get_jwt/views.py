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
        access_token = generate_access_token(username)
        refresh_token = generate_refresh_token(username)
        return JsonResponse({'access_token': access_token.decode(), 'refresh_token': refresh_token.decode()})
    else:
        # 验证失败，返回None
        return JsonResponse({'校验失败，拒绝生成jwt令牌'})


def generate_access_token(username):
    expiration = datetime.utcnow() + timedelta(minutes=300)
    payload = {
        'type': 'access',
        'username': username,
        'exp': expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def generate_refresh_token(username):
    expiration = datetime.utcnow() + timedelta(days=14)
    payload = {
        'type': 'refresh',
        'username': username,
        'exp': expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


@csrf_exempt
def validate_access_jwt(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return JsonResponse({'result': '缺少token'}, status=401)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        username = payload.get('username')
        type = payload.get('type')
    except jwt.ExpiredSignatureError:
        return JsonResponse({'result': 'expired'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'result': 'invalid'}, status=401)
    if type != 'access':
        return JsonResponse({'result': 'not a access type jwt'}, status=401)

    return JsonResponse({'result': 'success', 'username': username}, status=200)


@csrf_exempt
def validate_refresh_jwt(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return JsonResponse({'result': '缺少token'}, status=401)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        username = payload.get('username')
        type = payload.get('type')
    except jwt.ExpiredSignatureError:
        return JsonResponse({'result': 'expired'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'result': 'invalid'}, status=401)
    if type != 'refresh':
        return JsonResponse({'result': 'not a refresh type jwt'}, status=401)

    return JsonResponse({'result': 'success', 'username': username}, status=200)

