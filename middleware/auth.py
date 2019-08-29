from firebase_admin import auth
from firebase import Firebase
from config.config import config

firebase = Firebase(config)

authCliente = firebase.auth()

class AuthUser:
  def __init__(self, email, password = None):
    self.email = email
    self.password = password

  def auth_user(self):
      try:
        # Se inicia session y se verifica la informacion
        user = authCliente.sign_in_with_email_and_password(self.email, self.password)      
        info_user = self.getInformation(user['idToken'])

        # Se verifica si el email esta en estatus "Verificado"
        if (info_user['users'][0]['emailVerified'] == False):
          verified = {
            'code': '401',
            'response': {
              'message' : 'Debe validar su correo para poder hacer uso de esta cuenta',
              'reason' : 'not-verified'
            }            
          }
          return verified
        else:
          # Se verifica si el token es correcto y autentico
          decoded_token = auth.verify_id_token(user['idToken'])
          uid = decoded_token['uid']

          if (uid != user['localId']):
            verified = {
              'code': '401',
              'response': {
                'message' : 'El token es incorrecto.',
                'reason' : 'incorrect-token'
              }              
            }
            return verified

          return user
      except:
        return False

  def getInformation(self, idToken):    
    return authCliente.get_account_info(idToken)
  