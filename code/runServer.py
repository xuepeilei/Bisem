# -*- coding: utf-8 -*-
import web
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
        corr_centence=corr(sentence)
        return(render.show(corr_centence))



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


