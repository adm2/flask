import pickle
from flask import Flask, request, Response

app = Flask(__name__)
def get_all_users():
  return Response('{"status": "ok GET"}', status=200, mimetype='application/json')
def create_user():
  return Response('{"status": "ok POST"}', status=200, mimetype='application/json')
def update_user():
  return Response('{"status": "ok PATCH"}', status=200, mimetype='application/json')
def delete_user():
  return Response('{"status": "ok DELETE"}', status=200, mimetype='application/json')




@app.route('/users/', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def users():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        return create_user()
    elif request.method == 'PATCH':
        return update_user()
    elif request.method == 'DELETE':
        return delete_user()
    else:
        pass

if __name__ == '__main__':
    app.run()

