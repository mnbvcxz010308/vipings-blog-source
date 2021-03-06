from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

SITEURL = 'https://vipings.com'
# SITEURL = 'http://danielfrg.github.io'
AUTHOR = u'Vipin G S'
SITENAME = u'VipinGS Notes'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

MARKUP = ('md', 'ipynb')

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 150
DEFAULT_PAGINATION = 10

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']

THEME = 'theme'
STATIC_PATHS = ['images']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = PAGE_SAVE_AS

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Paths are relative to `content`
STATIC_PATHS = ['images', 'favicon.ico', '404.html', 'robots.txt', 'CNAME']

# THEME SETTINGS
DEFAULT_HEADER_BG = '/images/station1.jpg'
ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'mnbvcxz'
GITHUB_USERNAME = 'mnbvcxz010308'
SHOW_ARCHIVES = True
SHOW_FEED = True
#
GOOGLE_ANALYTICS_CODE = 'UA-108813279-1'
GOOGLE_ANALYTICS_DOMAIN = 'vipings.com'

# PLUGINS SETTINGS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'ipynb.markup', 'ipynb.liquid', 'liquid_tags.youtube', 'liquid_tags.b64img']

SITEMAP = {
    'format': 'xml'
}

IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('ol', None), ('ul', None)]
