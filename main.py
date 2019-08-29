from flask import Flask, jsonify, request
from middleware.auth import AuthUser
from api.user import User
from api.rental import SendingInformation
from util.util import response_false, response_incomplete, verifyExist, verifyRequired
import time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
  if (request.method == 'GET'):
    response_fail = {
      'response' : 'Para usar este servicio lea la documentacion',
      'documentacion' : ''
    }
    return jsonify(response_fail), 200

@app.route('/createUser', methods = ['POST'])
def createUser():
  if (request.method == 'POST'):
    
    arg_param = request.get_json()
    
    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')
    _arg_password = verifyExist(arg_param, 'password')

    data_obligatorios = [
      _arg_email,
      _arg_password
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 401
    
    # Se llama la clase que tiene el metodo de creacion de usuario
    __user = User(_arg_email,_arg_password)
    r_create = __user.createUser()
    r_status = 200

    if (r_create == False):
      r_create = response_false
      r_status = 401

    return jsonify(r_create), r_status

@app.route('/forgotPassword', methods = ['POST'])
def fpassword():
  if (request.method == 'POST'):
    arg_param = request.get_json()
    
    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')

    data_obligatorios = [
      _arg_email
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 401

    __auth = AuthUser(_arg_email)
    r_fpassword = __auth.forgotPassword()
    r_status = 200

    if (r_fpassword == False):
      r_fpassword = response_false
      r_status = 401

    return jsonify(r_fpassword), r_status

@app.route('/alquilar', methods = ['POST'])
def addData():
  if (request.method == 'POST'):
    arg_param = request.get_json()

    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')
    _arg_password = verifyExist(arg_param, 'password')
    _arg_modelo = verifyExist(arg_param, 'modelo')
    _arg_marca = verifyExist(arg_param, 'marca')
    _arg_year = verifyExist(arg_param, 'year')
    _arg_color = verifyExist(arg_param, 'color')
    _arg_responsable = verifyExist(arg_param, 'responsable')

    data_obligatorios = [
      _arg_email,
      _arg_password,
      _arg_modelo,
      _arg_marca,
      _arg_year,
      _arg_color,
      _arg_responsable
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 400

    # Se llama la clase que tiene el metodo de autentificacion de usuario
    __auth = AuthUser(_arg_email,_arg_password)
    r_auth = __auth.auth_user()
    r_status = 200

    if (r_auth == False):
      r_auth = response_false
      r_status = 401

      return jsonify(r_auth), r_status
    
    data = {
      'uid': r_auth['localId'],
      'modelo': _arg_modelo,
      'color': _arg_color,
      'marca': _arg_marca,
      'year': _arg_year,
      'responsable': _arg_responsable,
      'dia': time.strftime("%d/%m/%y"),
      'status': 'pendiente'
    }

    # Se llama la clase que tiene el metodo de insercion de data
    __send = SendingInformation(u'rentals', data)
    s_add = __send.addData()
    s_status = 200

    if (s_add == False):
      s_add = response_false
      s_status = 401
    
    return jsonify(s_add), s_status

@app.route('/alquileres/user', methods = ['POST'])
def getdata_user():
  if (request.method == 'POST'):
    arg_param = request.get_json()

    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')
    _arg_password = verifyExist(arg_param, 'password')
    _arg_filter = verifyExist(arg_param, 'filtro')

    data_obligatorios = [
      _arg_email,
      _arg_password,
      _arg_filter
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 401

    if(_arg_filter != 'todo' and _arg_filter != 'pendiente' and _arg_filter != 'entregado'):
      return jsonify(response_false), 401

    # Se llama la clase que tiene el metodo de autentificacion de usuario
    __auth = AuthUser(_arg_email,_arg_password)
    r_auth = __auth.auth_user()

    if (r_auth == False):
      r_auth = response_false
      r_status = 401

      return jsonify(r_auth), r_status

    uid = r_auth['localId']

    __send = SendingInformation(u'rentals', _arg_filter, uid)
    s_get = __send.getDataxUser()
    s_status = 200

    if (s_get == False):
      s_get = response_false
      s_status = 401
    
    return jsonify(s_get), s_status

@app.route('/alquileres', methods = ['POST'])
def getdata_all():
  if (request.method == 'POST'):
    arg_param = request.get_json()

    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')
    _arg_password = verifyExist(arg_param, 'password')
    _arg_filter = verifyExist(arg_param, 'filtro')

    data_obligatorios = [
      _arg_email,
      _arg_password,
      _arg_filter
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 401

    if(_arg_filter != 'todo' and _arg_filter != 'pendiente' and _arg_filter != 'entregado'):
      return jsonify(response_false), 401

    # Se llama la clase que tiene el metodo de autentificacion de usuario
    __auth = AuthUser(_arg_email,_arg_password)
    r_auth = __auth.auth_user()

    if (r_auth == False):
      r_auth = response_false
      r_status = 401

      return jsonify(r_auth), r_status

    __send = SendingInformation(u'rentals', _arg_filter)
    s_get = __send.getData()
    s_status = 200

    if (s_get == False):
      s_get = response_false
      s_status = 401
    
    return jsonify(s_get), s_status

@app.route('/cerrarAlquiler', methods = ['POST'])
def closeData():
  if (request.method == 'POST'):
    arg_param = request.get_json()

    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')
    _arg_password = verifyExist(arg_param, 'password')
    _arg_document = verifyExist(arg_param, 'id')
    _arg_filter = verifyExist(arg_param, 'filtro')

    data_obligatorios = [
      _arg_email,
      _arg_password,
      _arg_document,
      _arg_filter
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 401

    if(_arg_filter != 'entregado'):
      return jsonify(response_false), 401

    # Se llama la clase que tiene el metodo de autentificacion de usuario
    __auth = AuthUser(_arg_email,_arg_password)
    r_auth = __auth.auth_user()

    if (r_auth == False):
      r_auth = response_false
      r_status = 401

      return jsonify(r_auth), r_status

    data = {
      'document': _arg_document,
      'filtro': _arg_filter
    }

    __send = SendingInformation(u'rentals', data)
    s_delete = __send.closeData()
    s_status = 200

    if (s_delete == False):
      s_delete = response_false
      s_status = 400
    
    return jsonify(s_delete), s_status

@app.route('/corregirDatos', methods = ['POST'])
def updateData():
  if (request.method == 'POST'):
    arg_param = request.get_json()

    # Se verifica si los parametros existen
    _arg_email = verifyExist(arg_param, 'email')
    _arg_password = verifyExist(arg_param, 'password')
    _arg_document = verifyExist(arg_param, 'id')

    _arg_color = verifyExist(arg_param, 'color')
    _arg_marca = verifyExist(arg_param, 'marca')
    _arg_year = verifyExist(arg_param, 'year')
    _arg_responsable = verifyExist(arg_param, 'responsable')
    _arg_modelo = verifyExist(arg_param, 'modelo')

    data_obligatorios = [
      _arg_email,
      _arg_password,
      _arg_document
    ]

    verify_obligatorios = verifyRequired(data_obligatorios)

    if (verify_obligatorios == False):
      return jsonify(response_incomplete), 401

    # Se llama la clase que tiene el metodo de autentificacion de usuario
    __auth = AuthUser(_arg_email,_arg_password)
    r_auth = __auth.auth_user()

    if (r_auth == False):
      r_auth = response_false
      r_status = 401

      return jsonify(r_auth), r_status

    udata_list = {}

    if (_arg_color != None):
      udata_list['color'] = _arg_color
    if (_arg_marca != None):
      udata_list['marca'] = _arg_marca
    if (_arg_year != None):
      udata_list['year'] = _arg_year
    if (_arg_responsable != None):
      udata_list['responsable'] = _arg_responsable
    if (_arg_modelo != None):
      udata_list['modelo'] = _arg_modelo

    data = {
      'document': _arg_document,
      'udata': udata_list
    }

    __send = SendingInformation(u'rentals', data)
    s_update = __send.updateData()
    s_status = 200

    if (s_update == False):
      s_update = response_false
      s_status = 401
    
    return jsonify(s_update), s_status

if __name__ == '__main__':
  app.run(debug=True)
