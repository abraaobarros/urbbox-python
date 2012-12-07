import webapp2
import jinja2
import os
from google.appengine.ext import db

class Estabelecimento(db.Model):
    nome = db.StringProperty()
    descricao = db.StringProperty()
    logoURL = db.StringProperty()


env = jinja2.Environment(loader = 
jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        inserir()  # para fazer funcionar tem que inserir alguma coisa no banco
    	estabelecimentos = Estabelecimento.all()
    	template = env.get_template('view/index.html')
        self.response.out.write(template.render(var=estabelecimentos))

def inserir():
	for i in range(10):	
		estab = Estabelecimento()
		estab.nome = "teste"+str(i)
		estab.descricao = "teste"+str(i)
		estab.logoURL = "teste"+str(i)
		estab.put() 

app = webapp2.WSGIApplication([('/', MainHandler) ],
debug=True)