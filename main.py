#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from models import Pedido
from models import UsuarioEstabelecimento
import json


class MainHandler(webapp2.RequestHandler):
  def get(self):
    #u = UsuarioEstabelecimento()
    #u.email = "kenta"
    #u.idEstalebecimento = [40]
    #u.password = "asd"
    #u.put()
    p = Pedido()
    p.idEstabelecimento = 100
    p.itens="{nada}"
    p.rua = "Mesa 10"
    p.status = "Waiting"
    p.put()
    lista = Pedido.all()
    count = 0
    for p in lista:
      print "a"
    lista2 = UsuarioEstabelecimento.all()
    count = 0
    #for u in lista2:
    #  #u.id_est = u.idEstalebecimentoList[0]
    #  #u.put()
    #  self.response.out.write("parser do id do Estabelecimento %d" %u.idEstabelecimentoList.pop())
    #  
class UserHandler(webapp2.RequestHandler):
  def get(self):
    login = self.request.get('login')
    password = self.request.get('password')
    u = UsuarioEstabelecimento.all()
    user = u.filter('email =' , login).get()
    if user:
      if user.password == password:
        self.response.out.write("{'authentication':'true','idStore':%d}" %user.idEstabelecimentoList.pop())
      else:
        self.response.out.write("{'authentication':false,'error':1,'msg':'Password Incorreto'}")
    else:
      self.response.out.write("{'authentication':false,'error':0,'msg':'Usuario nao existe'}")
     
class PedidoHandler(webapp2.RequestHandler):
  def get(self,est_id):
    lista = Pedido.all()
    lista.filter('idEstabelecimento =', long(est_id))
    count = 0
    for p in lista.run():
     count+=1
    #  count+=1
    self.response.out.write("{'qtd':%d}" %count)

app = webapp2.WSGIApplication([
    (r'/pedidos/(\d+)', PedidoHandler)
    ,(r'/user', UserHandler)
    ,('/', MainHandler)], debug=True)
