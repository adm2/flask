import pickle
from flask import Flask, request, Response

app = Flask(__name__)


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

