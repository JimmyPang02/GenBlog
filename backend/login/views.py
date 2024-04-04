import json

from django.contrib import auth
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from get_jwt.views import get_jwt_token


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 验证用户名和密码是否正确
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # 验证成功，返回jwt令牌
        jwt = json.loads(get_jwt_token(request).content)
        access_token = jwt['access_token']
        refresh_token = jwt['refresh_token']
        #把当前登录时间写入数据库的last_login字段
        current_time=timezone.now()
        user.last_login=current_time
        user.save()
        return JsonResponse({'result': '登录成功，生成jwt令牌', 'access_token': access_token, 'refresh_token': refresh_token})
    else:
        # 验证失败，返回None
        return JsonResponse({'result': '登录失败，拒绝生成jwt令牌', 'access_token': None, 'refresh_token': None})
