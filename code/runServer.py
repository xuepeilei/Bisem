import web
from Patient.gps import *
from Patient.mark import *
from Cure.knn import *

web.config.debug = True

render = web.template.render('www/')


urls=('/', 'index',
      '/show', 'show')


class index:
    def GET(self):
        return(render.index())


class show:
    def POST(self):
        i = web.input()
        cure=i.get("cure")
        sentence=i.article
        cure_sentence=[]
        wrong_list=gps(sentence)
        mark_sentence=mark(sentence,wrong_list)
        if cure=="on":
            cure_sentence=knn(wrong_list)
        return(render.show(mark_sentence,cure_sentence,cure))



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


