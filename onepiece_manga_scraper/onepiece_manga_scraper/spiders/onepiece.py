import scrapy

from ..items import OnepieceMangaScraperItem


class OnepieceSpider(scrapy.Spider):
    name = 'onepiece'
    start_urls = ['https://myonepiecemanga.com/']

    def parse(self, response):
        chapters = response.xpath("//h3[@class='elementor-post__title']/a/@href").extract()

        for chapter_url in chapters[:2]:
            yield response.follow(chapter_url, callback=self.parse_chapter)

    def parse_chapter(self, response):
        images = response.css(".entry-content img::attr(src)").getall()
        clean_images = [response.urljoin(image) for image in images]

        yield {"image_urls": clean_images}
