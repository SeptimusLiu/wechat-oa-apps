from conf import auth
from flask import request
import hashlib
from route import app


@app.route('/mp/auth/', methods=['GET'])
def index():
    res = ""
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')
    token = auth.TOKEN

    list = [token, timestamp, nonce]
    print(list)
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print "handle/GET func: hashcode, signature: ", hashcode, signature
    if hashcode == signature:
        res = echostr
    return res

