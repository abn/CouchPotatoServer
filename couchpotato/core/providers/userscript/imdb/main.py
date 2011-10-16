from couchpotato.core.event import fireEvent
from couchpotato.core.helpers.variable import getImdb
from couchpotato.core.providers.userscript.base import UserscriptBase


class IMDB(UserscriptBase):

    includes = ['http*://*.imdb.com/title/tt*', 'http*://imdb.com/title/tt*']

    def getMovie(self, url):
        return fireEvent('movie.info', identifier = getImdb(url), merge = True)
