
import webapp2
import jinja2
import os

env = jinja2.Environment(loader = 
jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('view/index.html')
        self.response.out.write(template.render(var='variables'))

app = webapp2.WSGIApplication([('/', MainHandler)],
debug=True)
