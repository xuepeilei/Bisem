# -*- coding: utf-8 -*-
import web
web.config.debug = False
from Proofread.corr import *

render = web.template.render('www/')


urls=('/', 'index',
      '/show', 'show')


class index:
    def GET(self):
        return(render.index())


class show:
    def POST(self):
        i = web.input()
        sentence=i.article
        corr_sentence=corr(sentence)
        return(render.show(corr_sentence))



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


