from django.shortcuts import render
from nature.models import *
from requests import request, session

# Create your views here.
from django.http import HttpResponse



def langChanger(request, lang):
    request.session["language"]=lang
    return HttpResponse(lang)


def home(request):
    carusel_01 = Carusel.objects.filter(item='1').last()
    carusel_02 = Carusel.objects.filter(item='2').last()
    carusel_03 = Carusel.objects.filter(item='3').last()
    carusel_04 = Carusel.objects.filter(item='4').last()
    carusel_05 = Carusel.objects.filter(item='5').last()

    monumet_01 = HomePageMon.objects.filter(item='1').last()
    monumet_02 = HomePageMon.objects.filter(item='2').last()
    monumet_03 = HomePageMon.objects.filter(item='3').last()
    monumet_04 = HomePageMon.objects.filter(item='4').last()
    monumet_05 = HomePageMon.objects.filter(item='5').last()
    monumet_06 = HomePageMon.objects.filter(item='6').last()

    gallery_01 = HomePageGallery.objects.filter(item='1').last()
    gallery_02 = HomePageGallery.objects.filter(item='2').last()
    gallery_03 = HomePageGallery.objects.filter(item='3').last()
    gallery_04 = HomePageGallery.objects.filter(item='4').last()
    gallery_05 = HomePageGallery.objects.filter(item='5').last()
    gallery_06 = HomePageGallery.objects.filter(item='6').last()
    gallery_07 = HomePageGallery.objects.filter(item='8').last()
    gallery_08 = HomePageGallery.objects.filter(item='7').last()

    videos = HomePageVideo.objects.all()

    top = HomePageTop.objects.last()

    news = latest_news.objects.all().order_by('-id')
    return render(request, 'home.html', {
        "carusel_01": carusel_01,
        "carusel_02": carusel_02,
        "carusel_03": carusel_03,
        "carusel_04": carusel_04,
        "carusel_05": carusel_05,

        "news": news,

        "top": top,

        "monument_01": monumet_01,
        "monument_02": monumet_02,
        "monument_03": monumet_03,
        "monument_04": monumet_04,
        "monument_05": monumet_05,
        "monument_06": monumet_06,

        "gallery_01": gallery_01,
        "gallery_02": gallery_02,
        "gallery_03": gallery_03,
        "gallery_04": gallery_04,
        "gallery_05": gallery_05,
        "gallery_06": gallery_06,
        "gallery_07": gallery_07,
        "gallery_08": gallery_08,

        "videos": videos,

    })


def gallery(request):
    all_gall = GalleryPageGallery.objects.all().order_by('-id')
    return render(request, 'gallery.html', {
        "all_gall": all_gall
    })


def monuments(request, destrict):
    posts = AllPost.objects.filter(
        destrict=destrict, category='monument').order_by("-id")
    return render(request, 'monuments.html', {
        'posts': posts
    })


def reserves(request):
    posts = AllPost.objects.filter(category='reserve').order_by("-id")
    return render(request, 'reserves.html', {
        "posts": posts
    })


def single(request, id):
    post = AllPost.objects.filter(id=id).first()
    post.views += 1
    post.save()
    recomended_posts = AllPost.objects.filter(
        category=post.category, destrict=post.destrict).exclude(id=id).order_by('-id')[:15]
    # prit
    return render(request, 'single.html', {
        "post": post,
        "recommended_posts": recomended_posts
    })


def natural_res(request):
    posts = AllPost.objects.filter(category='resources').order_by("-id")
    return render(request, 'natural_res.html', {
        "posts": posts
    })


def contact(request):
    return render(request, 'contact.html')


def PostSearch(request):
    if request.method == "POST":
        keyword = request.POST['search']
        posts = AllPost.objects.filter(title__contains=keyword)
        return render(request, 'search.html', {
            'posts': posts
        })
