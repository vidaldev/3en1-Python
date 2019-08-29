import re

expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

response_false = {
  'message' : 'Ha ocurrido un problema, verifique la informacion suministrada. Si el error persiste comuniquese con el administrador del servicio',
  'email' : 'xtrate@protonmail.com',
  'reason' : 'invalid'
}

response_incomplete = {
    'message': 'Los parametros estan incompletos, revise la informacion suministrada antes de enviar nuevamente.',
    'reason':'missing parameters'
}

def checkKey(dict, key): 
  if key in dict.keys(): 
      return True 
  else: 
      return False 

def verifyExist(arg_param, key):
  __param = arg_param[key] if (checkKey(arg_param, key)) else None

  if(key == 'email' and __param != None):
    if (re.match(expresion_regular, __param) == None):
      __param = None

  return __param

def verifyRequired(arg_data):
  for data in arg_data:
    if (data == None):
      return False
  return True