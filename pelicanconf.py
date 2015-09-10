#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brook Jensen'
SITENAME = u'University of Waterloo Game Dev Club'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['pages/']

MAIN_CATEGORY = 'main'
DIRECTIONS_PAGE = 'directions'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'themes/gdc'

GOOGLE_CALENDER = 'https://www.google.com/calendar/embed?showTitle=0&amp;showNav=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;height=600&amp;wkst=1&amp;bgcolor=%23ffffff&amp;src=80ar36dhg37vskmhd4gjb2els4%40group.calendar.google.com&amp;color=%23691426&amp;ctz=America%2FToronto'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Games Institute', 'https://uwaterloo.ca/games-institute/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/groups/298486077021523/'),
          ('Twitter', 'https://twitter.com/uwgamedev'),
          ('Reddit', 'https://www.reddit.com/r/kwgamedev/'),)
          
# Contact widget
CONTACT = (('uw.gamedevclub@gmail.com', 'mailto:uw.gamedevclub@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
