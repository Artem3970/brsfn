from django.test import TestCase
from django.urls import reverse

from .models import Project


class LandingPagesTests(TestCase):
	def test_home_page_renders_successfully(self):
		response = self.client.get(reverse('homeview'))
		self.assertEqual(response.status_code, 200)

	def test_public_routes_are_defined(self):
		for name in ('homeview', 'projects', 'about', 'join', 'project-unbreakable'):
			self.assertTrue(reverse(name).startswith('/'))

	def test_dynamic_project_route_is_buildable(self):
		project = Project.objects.create(
			title='Test Project',
			slug='test-project',
			short_description='A test project.',
		)
		self.assertEqual(
			reverse('project-detail', kwargs={'slug': project.slug}),
			'/projects/test-project/',
		)

	def test_project_card_and_detail_show_editorial_fields(self):
		project = Project.objects.create(
			title='Festival Project',
			slug='festival-project',
			short_description='A short card description.',
			date_label='11–12 September 2026',
			location='Linz, Austria',
			goal='Reach 50,000 people.',
			budget='€70,000',
			partners='Ars Electronica, SARAVÁ',
			participants='Svitlana Tereshchenko',
			website_text='A highlighted project note.',
			description='The complete project story.',
		)
		card_response = self.client.get(reverse('homeview'))
		detail_response = self.client.get(reverse('project-detail', kwargs={'slug': project.slug}))
		self.assertContains(card_response, '11–12 September 2026')
		self.assertContains(card_response, 'Linz, Austria')
		for text in ('Reach 50,000 people.', '€70,000', 'Ars Electronica, SARAVÁ', 'A highlighted project note.', 'The complete project story.'):
			self.assertContains(detail_response, text)
