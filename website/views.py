from django.shortcuts import render, get_object_or_404
from .models import WebsiteImage, MenuPost

def home(request):
    hero_image = WebsiteImage.objects.filter(category='hero').first()
    featured_dishes = WebsiteImage.objects.filter(category='featured_dish')
    testimonial_background = WebsiteImage.objects.filter(category='testimonial_background').first()

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

    # Debugging output
    print(f"History Image: {history_image}")
    print(f"Team Members: {team_members}")
    print(f"Gallery Images: {gallery_images}")

    context = {
        'history_image': history_image,
        'team_members': team_members,    
        'gallery_images': gallery_images,  
    }
    return render(request, 'website/about_us.html', context)

def contact_us(request):
    if request.method == 'POST':
        # Handle contact form submission logic here if needed.
        pass
    return render(request, 'website/contact_us.html')

def menu_list(request):
    posts = MenuPost.objects.all().order_by('-created_at')
    return render(request, 'website/menu_list.html', {'posts': posts})

def menu_detail(request, pk):
    post = get_object_or_404(MenuPost, pk=pk)
    return render(request, 'website/menu_detail.html', {'post': post})
