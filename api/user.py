from firebase_admin import auth
from firebase import Firebase
from config.config import config

firebase = Firebase(config)

authCliente = firebase.auth()

class User:
  def __init__(self, email, password = None):
    self.email = email
    self.password = password

  def createUser(self):
    try:
      # Se crea el nuevo usuario
      new_user = auth.create_user(
        email = self.email,
        password = self.password,
        email_verified = False
      )

      # Se verifica su creacion y se envia correo el usuario para la verificacion de email
      new_user_verify = authCliente.sign_in_with_email_and_password(self.email, self.password)
      authCliente.send_email_verification(new_user_verify['idToken'])

      verify = {
        'message' : 'Registro exitoso',
        'id' : new_user.uid,
        'alert': 'Verifique su correo antes de usar el servicio'
      }

      return verify
    except:
      return False

  def forgotPassword(self):
    try:
      authCliente.send_password_reset_email(self.email)

      arg_recovery = {
        'message': 'Correo de recuperacion exitoso',
        'alert' : 'Correo de recuperacion enviado a la direccion: '+self.email
      }

      return arg_recovery
    except:
      return False 