import web
import src.urls.myurls as myurls

render = web.template.render('views/')

if __name__ == "__main__":
    app = web.application(myurls.urls,globals())
    app.run()
