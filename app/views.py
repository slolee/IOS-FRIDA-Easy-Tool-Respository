from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from app.models import Post, Repository
import base64

# Create your views here.
def index(request):
    context = {"content1":"ch4njun"}
    return render(request, 'index.html', context=context)

def repositoryList(request):
    context = {}
    return render(request, 'repositoryList.html', context=context)

def repositorySearch(request):
    id = request.GET.get("id")

    if id == None or id == '':
        repositorys = Repository.objects.all()
    else:
        repositorys = Repository.objects.filter(repo_id=id)
    
    data = [ repository.to_dict_json() for repository in repositorys ]
    response = {'data': data}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def repositoryCheckName(request):
    repo_title = request.GET.get("repo_title")
    
    repositorys = Repository.objects.filter(repo_title=repo_title)
    data = [ repository.to_dict_json() for repository in repositorys ]
    response = {'data': data}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def createRepository(request):
    repo_title = request.GET.get("repo_title")
    repo_password = request.GET.get("repo_password")

    last_id = Repository.objects.raw('select repo_id from app_repository order by repo_id desc limit 1')
    if len(last_id) == 0:
        repo_id = 0
    else:
        repo_id = last_id[0].repo_id

    repository = Repository()
    repository.repo_id = repo_id + 1
    repository.repo_title = repo_title
    repository.repo_password = repo_password
    repository.repo_post_count = 0
    repository.save()
    
    response = {'data': ''}
    return JsonResponse(response, safe=False, content_type="application/json")

def deleteRepository(request):
    repo_id = request.GET.get("repo_id")
    repository = Repository.objects.get(repo_id=repo_id)
    repository.delete()

    response = {'data': ''}
    return JsonResponse(response, safe=False, content_type="application/json")

def scriptBoardList(request, id):
    context = {'id': id}
    return render(request, 'scriptBoard.html', context=context)

def scriptBoardSearch(request):
    start = request.GET.get("start")
    length = request.GET.get("length")
    search = request.GET.get("search[value]")
    
    id = request.GET.get("id")
    if search == None or search == '':
        posts = Post.objects.filter(repo_id=id)
    else:
        posts = Post.objects.filter(title__contains=search)
    
    data = [ post.to_dict_json() for post in posts ]
    response = {'data': data, 'recordsFiltered':len(data)}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def postCheckName(request):
    title = request.GET.get("title")
    repo_id = request.GET.get("repo_id")

    posts = Post.objects.raw('select * from app_post where title=\'' + title + '\' and repo_id=' + repo_id)
    data = [ post.to_dict_json() for post in posts ]

    response = {'data': data }
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def createPost(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    repo_id = request.GET.get("repo_id")

    last_id = Post.objects.raw('select post_id, repo_id from app_post order by post_id desc limit 1')
    if len(last_id) == 0:
        post_id = 0
    else:
        post_id = last_id[0].post_id

    repo_id = Repository.objects.raw('select repo_id from app_repository where repo_id=' + repo_id)

    posts = Post.objects.raw('select * from app_post where title=\'' + title + '\' and repo_id=' + str(repo_id[0].repo_id))
    if len(posts) > 0:
        print('----------------' + title)
        post = Post.objects.get(post_id=posts[0].post_id)
        post.content = base64.b64encode(content.encode('utf-8')).decode()
        post.save()
    else:
        post = Post()
        post.post_id = post_id + 1
        post.title = title
        post.content = base64.b64encode(content.encode('utf-8')).decode()
        import datetime
        post.pub_date = datetime.datetime.now()
        post.count = 0
        post.repo_id = repo_id[0]
        post.save()

        repository = Repository.objects.get(repo_id=repo_id[0].repo_id)
        repository.repo_post_count = repository.repo_post_count + 1
        repository.save()

    response = {'data': ''}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def getPost(requests):
    post_id = requests.GET.get("post_id")
    print(post_id)
    
    posts = Post.objects.filter(post_id=post_id)
    data = [ post.to_dict_json() for post in posts ]
    response = {'data': data, 'recordsFiltered':len(data)}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def getRepository(requests):
    repo_title = requests.GET.get("repo_title")
    
    repo_id = Repository.objects.raw('select repo_id from app_repository where repo_title=\'' + repo_title + '\'')
    if len(repo_id) > 0:
        repo_id = repo_id[0].repo_id
    else:
        response = {'data': -1}
        print(response)
        return JsonResponse(response, safe=False, content_type="application/json")
    
    posts = Post.objects.filter(repo_id=repo_id)
    data = [ post.to_dict_json() for post in posts ]
    response = {'data': data}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def getRepositoryId(requests):
    repo_title = requests.GET.get("repo_title")
    
    repo_id = Repository.objects.raw('select repo_id from app_repository where repo_title=\'' + repo_title + '\'')
    if len(repo_id) > 0:
        repo_id = repo_id[0].repo_id
    else:
        repo_id = -1
    response = {'data': repo_id}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def getRepositoryList(requests):
    repo_list = Repository.objects.all()
    data = [ repo.repo_title for repo in repo_list ]
    response = {'data': data}
    print(response)
    return JsonResponse(response, safe=False, content_type="application/json")

def deletePost(requests):
    pass