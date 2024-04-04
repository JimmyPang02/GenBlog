from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        # 检测用户名和密码是否为空
        if (request.POST.get('username') == '' or request.POST.get('password') == ''):
            return JsonResponse({'result': '用户名或密码为空，注册失败'})
        # 查找用户名是否存在
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'result': '用户名已存在，注册失败'})
        else:
            # 创建用户
            if (request.POST.get('password') != request.POST.get('password_confirm')):
                return JsonResponse({'result': '两次密码不一致，注册失败'})
            user = User.objects.create_user(username=username, password=request.POST.get('password'))
            user.save()
            return JsonResponse({'result': '注册成功'})
    else:
        return JsonResponse({'result': '仅支持POST调用，注册失败'})
