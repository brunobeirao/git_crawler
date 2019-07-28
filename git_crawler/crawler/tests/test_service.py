from git_crawler.crawler.services import CrawlerService


service = CrawlerService()


def test_service():
    service.teste()
    assert service is not None
