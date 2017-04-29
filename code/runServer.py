# -*- coding: utf-8 -*-
import web
from Patient.gps import *
from Patient.mark import *

web.config.debug = False

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
        wrong_set=gps(sentence)
        mark_sentence=mark(sentence,wrong_set)
        return(render.show(mark_sentence))



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


