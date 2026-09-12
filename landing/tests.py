from django.test import TestCase
from django.urls import reverse

from .models import Project


class LandingPagesTests(TestCase):
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
