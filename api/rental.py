from firebase_admin import firestore
from config.config import config
import json

db = firestore.client()

# Clase que maneja metodos para agregar, editar, eliminar informacion del usuario
class SendingInformation:
  def __init__(self, colection, data = None, uid = None, where = None, orderby = None):
    self.colection = colection
    self.data = data
    self.uid = uid
    self.where = where
    self.orderby = orderby

  def addData(self):
    try:
      db.collection(self.colection).document().set(self.data)
      
      add_true = {
        'message' : 'El alquiler del vehiculo se ha insertado correctamente',
        'reason': 'sucess'
      }

      return add_true
    except:
      return False

  def getDataxUser(self):
    try:
      if (self.data == 'todo'):
        docs = db.collection(self.colection).where(u'uid', u'==', self.uid).get()
      
      if (self.data == 'pendiente' or self.data == 'entregado'):
        docs = db.collection(self.colection).where(u'uid', u'==', self.uid).where(u'status', u'==', self.data).get()

      new_list = {}
      for doc in docs:
        arg = doc.to_dict()
        if 'uid' in arg: del arg['uid']
        new_list[doc.id] = arg
      
      return new_list
    except:
      return False

  def getData(self):
    try:
      if (self.data == 'todo'):
        docs = db.collection(self.colection).get()
      
      if (self.data == 'pendiente' or self.data == 'entregado'):
        docs = db.collection(self.colection).where(u'status', u'==', self.data).get()

      new_list = {}
      i = 0
      for doc in docs:
        arg = doc.to_dict()
        if 'uid' in arg: del arg['uid']
        new_list[i] = arg
        i+=1
      return new_list
    except:
      return False

  def closeData(self):
    if (self.data['filtro'] == 'entregado'):
      try:
        db.collection(self.colection).document(self.data['document']).set({
          "status": self.data['filtro']
        },merge=True)

        return {
          'message' : 'El status del alquiler del vehiculo ha sido modificado a entregado',
          'reason': 'success'
        }

      except:
        return False

  def updateData(self):
    try:
      db.collection(self.colection).document(self.data['document']).set(self.data['udata'],merge=True)

      return {
        'message' : 'La data ha sido actualizada correctamente',
        'reason': 'successful update'
      }
    except:
      return False