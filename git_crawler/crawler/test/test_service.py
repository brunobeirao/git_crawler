from git_crawler.crawler.services import CrawlerService
from django.test import TestCase
from django.conf import settings

settings.configure()
service = CrawlerService()


class TestService(TestCase):

    def test_service(self):
        service.get_commits()
        assert service is not None
