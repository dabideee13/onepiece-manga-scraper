BOT_NAME = 'onepiece'

SPIDER_MODULES = ['onepiece_manga_scraper.spiders']
NEWSPIDER_MODULE = 'onepiece_manga_scraper.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
AUTOTHROTTLE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

HTTPCACHE_ENABLED = True

ITEM_PIPELINES = {'onepiece_manga_scraper.pipelines.OnepieceMangaScraperPipeline': 1}
IMAGES_STORE = 'local_folder'
