# -*- coding:utf-8 -*-

from conf import server
from route import app

#
# @app.route('/mp/msg', methods=['POST'])
# def msg_handle():
#     print request.data
#     return '''
#          <xml>
#         <ToUserName><![CDATA[粉丝号]]></ToUserName>
#         <FromUserName><![CDATA[公众号]]></FromUserName>
#         <CreateTime>1460541339</CreateTime>
#         <MsgType><![CDATA[text]]></MsgType>
#         <Content><![CDATA[test]]></Content>
#         </xml>
#     '''

if __name__ == '__main__':
    app.run(host=server.IP, port=server.PORT, debug=True, threaded=True)
