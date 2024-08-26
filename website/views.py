from django.shortcuts import render
from .models import WebsiteImage

# Create your views here.


def home(request):
    hero_image = WebsiteImage.objects.filter(category='hero').first()
    featured_dishes = WebsiteImage.objects.filter(category='featured_dish')
    testimonial_background = WebsiteImage.objects.filter(
        category='testimonial_background').first()

    context = {
        'hero_image': hero_image,
        'featured_dishes': featured_dishes,
        'testimonial_background': testimonial_background,
    }
    return render(request, 'website/home.html', context)


def menus(request):
    menu_images = WebsiteImage.objects.filter(category='menu')

    context = {
        'menu_images': menu_images,
    }
    return render(request, 'website/menus.html', context)


def about_us(request):
    history_image = WebsiteImage.objects.filter(
    category='history_background').first()
    team_members = WebsiteImage.objects.filter(category='team_member')
    gallery_images = WebsiteImage.objects.filter(category='gallery')

    context = {
        'history_image': history_image,
        'team_members': team_members,
        'gallery_images': gallery_images,
    }
    return render(request, 'website/about_us.html', context)


def contact_us(request):
    return render(request, 'website/contact_us.html')
