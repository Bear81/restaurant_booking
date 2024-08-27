from django.test import TestCase
from django.utils import timezone
from website.models import RestaurantInfo, WebsiteImage, MenuPost


class RestaurantInfoModelTest(TestCase):

    def test_restaurant_info_creation(self):
        restaurant = RestaurantInfo.objects.create(
            name='The Great Restaurant',
            address='123 Food Street, Gourmet City',
            contact_details='Phone: 123-456-7890',
            opening_hours='Mon-Fri: 9am - 9pm',
            description='A fine dining experience.',
            about_us='We have been serving delicious food since 1980.'
        )
        self.assertEqual(str(restaurant), 'The Great Restaurant')
        self.assertTrue(isinstance(restaurant, RestaurantInfo))


class WebsiteImageModelTest(TestCase):

    def test_website_image_creation(self):
        image = WebsiteImage.objects.create(
            name='Hero Image 1',
            category='hero',
            image_url='https://example.com/hero-image.jpg'
        )
        self.assertEqual(str(image), 'Hero Image 1')
        self.assertTrue(isinstance(image, WebsiteImage))

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            WebsiteImage.objects.create(
                name='Invalid Image',
                category='invalid_category',  # This should raise an error
                image_url='https://example.com/invalid-image.jpg'
            )


class MenuPostModelTest(TestCase):

    def setUp(self):
        self.image = WebsiteImage.objects.create(
            name='Menu Image 1',
            category='menu',
            image_url='https://example.com/menu-image.jpg'
        )

    def test_menu_post_creation(self):
        menu_post = MenuPost.objects.create(
            title='Delicious Pasta',
            blurb='Try our new pasta dish!',
            content='<p>This is a great pasta dish.</p>',
            image=self.image,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        self.assertEqual(str(menu_post), 'Delicious Pasta')
        self.assertTrue(isinstance(menu_post, MenuPost))
        self.assertEqual(menu_post.image, self.image)
