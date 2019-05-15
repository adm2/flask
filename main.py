import pickle
from flask import Flask, request, Response

app = Flask(__name__)

user_list = []

def get_all_users():
  data = {}
  pickle_in = open('users.txt', 'rb')
  data = pickle.load(pickle_in)
  pickle_in.close()

  return Response(str(data), status=200, mimetype='application/text')

def create_user(user_id, name, age):
  data = []
  data_new = {}

  pickle_in = open('users.txt', 'rb')
  data = pickle.load(pickle_in)
  data_new['user_id'] = user_id
  data_new['name'] = name
  data_new['age'] = age
  pickle_in.close()
  data.append(data_new)

  data_new['user_id'] = user_id
  data_new['name'] = name
  data_new['age'] = age
  users_out = open("users.txt","wb")
  data.append(data_new)
  pickle.dump(data, users_out) 
  users_out.close()
  
  return Response('{"status": "ok"}', status=200, mimetype='application/json')

def update_user(arg):
  return Response('{"status": "ok PATCH"}', status=200, mimetype='application/text')

def delete_user(arg):
  return Response('{"status": "ok DELETE"}', status=200, mimetype='application/text')



@app.route('/users/', methods=['POST', 'PATCH', 'DELETE'])
def create():
  if request.method == 'POST':
    return create_user(user_id, request.form['name'],request.form['age'])

@app.route('/users/<user_id>', methods=['PATCH', 'DELETE'])
def users(user_id):
  if request.method == 'PATCH':
    return update_user(user_id)
  elif request.method == 'DELETE':
    return delete_user(user_id)
  else:
    pass

@app.route('/users/', methods=['GET'])
def lister():
  if request.method == 'GET':
     return get_all_users()


if __name__ == '__main__':
    app.run()

