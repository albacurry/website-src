AUTHOR = 'Alba Curry'
SITENAME = 'Alba Curry'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = './pelican-chunk'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['memes']


MENUITEMS = [
  #('Home', 'index.html'),
  ('Memes', 'incendium.html'),
('Projects', 'projects.html'),
  ('About', 'index.html'),
  #('Podcast', 'podcast.html'),
  
  #('', 'pages/support-the-podcast.html'),
  
]

DIRECT_TEMPLATES = ['index', 'incendium']
PAGINATED_DIRECT_TEMPLATES = ['incendium']



STATIC_PATHS = [
    'images',
    #'extra',  # this
]


# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
#PAGE_ORDER_BY = 'order'

# Blogroll
'''
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)
'''


# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/LetsChatEthics'),
          ('Instagram', 'https://www.instagram.com/lets.chat.ethics/'),
          ('LinkedIn', 'https://www.linkedin.com/company/letschatethics/'),
          ('youtube', 'https://www.youtube.com/channel/UCmNiaM-czvVCiDBNzxQbKOg'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True