import xml.etree.ElementTree as ET


class MsgFactory(object):
    def __init__(self, xml_str):
        if not xml_str:
            raise Exception("Empty string")
        xml_data = ET.fromstring(xml_str)
        self.to_user = ET.find('ToUserName').text
        self.from_user = ET.find('FromUserName').text
        self.content = ET.find('Content').text
        self.msg_id = ET.find('MsgId').text
        self.msg_type = ET.find('MsgType').text
        # if (msg_type == '')
