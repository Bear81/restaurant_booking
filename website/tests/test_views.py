from django.test import TestCase
from django.urls import reverse
from website.models import WebsiteImage, MenuPost


class WebsiteViewsTest(TestCase):

    def setUp(self):
        self.hero_image = WebsiteImage.objects.create(
            name='Hero Image',
            category='hero',
            image_url='https://example.com/hero.jpg'
        )
        self.featured_dish = WebsiteImage.objects.create(
            name='Featured Dish',
            category='featured_dish',
            image_url='https://example.com/featured_dish.jpg'
        )
        self.testimonial_background = WebsiteImage.objects.create(
            name='Testimonial Background',
            category='testimonial_background',
            image_url='https://example.com/testimonial.jpg'
        )
        self.menu_post = MenuPost.objects.create(
            title='Test Menu Post',
            content='This is a test menu post.',
            image=self.featured_dish
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')
        self.assertIn('hero_image', response.context)
        self.assertIn('featured_dishes', response.context)
        self.assertIn('testimonial_background', response.context)

    def test_menus_view(self):
        response = self.client.get(reverse('menus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/menus.html')
        self.assertIn('menu_images', response.context)

    def test_about_us_view(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/about_us.html')
        self.assertIn('history_image', response.context)
        self.assertIn('team_members', response.context)
        self.assertIn('gallery_images', response.context)

    def test_contact_us_view_get(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/contact_us.html')

    def test_menu_list_view(self):
        response = self.client.get(reverse('menu_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/menu_list.html')
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), 1)

    def test_menu_detail_view(self):
        response = self.client.get(
            reverse('menu_detail', args=[self.menu_post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/menu_detail.html')
        self.assertIn('post', response.context)
        self.assertEqual(response.context['post'], self.menu_post)
