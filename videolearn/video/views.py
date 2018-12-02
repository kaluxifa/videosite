from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def index(request):
        # 获取视频分类作为菜单数据
        menu_list = Cate.objects.all()
        # 返回最新的3条数据
        new_list = Video.objects.all().order_by('-create_time')[:3]
        # 返回最热的4条数据
        hot_list = Video.objects.all().order_by('-views')[:4]
        # 返回Python基础的最新8条数据
        python_list = Video.objects.filter(cate=Cate.objects.get(name='Python基础')).order_by('-create_time')[:8]
        # 返回数据分析的最新4条数据
        analysis_list_1 = Video.objects.filter(cate=Cate.objects.get(name='数据分析')).order_by('-create_time')[:4]
        # 返回数据分析的最新4条数据
        analysis_list_2 = Video.objects.filter(cate=Cate.objects.get(name='数据分析')).order_by('-create_time')[4:8]
        # 返回数据分析的最新4条数据
        analysis_list_3 = Video.objects.filter(cate=Cate.objects.get(name='数据分析')).order_by('-create_time')[8:12]
        # 返回GUI开发的最新4条数据
        gui_list = Video.objects.filter(cate=Cate.objects.get(name='GUI编程')).order_by('-create_time')[:4]
        # 返回Web开发的最新4条数据
        web_list = Video.objects.filter(cate=Cate.objects.get(name='Web开发')).order_by('-create_time')[:4]
        return render(request, 'index.html', locals())

# 视频详情页
def videoDetail(request,vid):
    # 获取视频分类作为菜单数据
    menu_list = Cate.objects.all()
    # 获取视频数据
    id = int(vid)
    video = Video.objects.get(id=vid)
    print(video.name)
    # 获取视频专辑
    try:
        set_name = Set.objects.get(video=id).name
        video_set = Set.objects.filter(name = set_name)
    except:
        random_video = Video.objects.order_by('?')[:5]
    # 增加访问人数
    try:
        video.views += 1
        video.save()
    except Exception as e:
        print(e)
    return render(request,'single.html',locals())

# 观看历史页
def viewHistory(request):
    return HttpResponse("这是观看历史页")

# 视频分类页
def videoCate(request,cateid):
    return HttpResponse("这是{0}分类".format(cateid))

# 登录页面
def logIn(request):
    return HttpResponse("这是登录页")

# 注册页面
def register(request):
    return HttpResponse("这是注册页")

