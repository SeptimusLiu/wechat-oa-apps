from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/wx_service', methods=['GET'])
def index():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')

    echostr = request.args.get('echostr') or ''
    return echostr

@app.route('/wx_service', methods=['POST'])
def msg_handle():
    print request.data
    return '''
         <xml>
        <ToUserName><![CDATA[粉丝号]]></ToUserName>
        <FromUserName><![CDATA[公众号]]></FromUserName>
        <CreateTime>1460541339</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[test]]></Content>
        </xml>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
