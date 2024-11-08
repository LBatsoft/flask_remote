import telnetlib
import time

from flask import Response, Blueprint, render_template, request, jsonify
import datetime
import requests
import ping3

from logging import getLogger

from app import csrf

logger = getLogger(__name__)
doctor_bp = Blueprint('doctor', __name__)


def valid_mail_server(mail_server: str, mail_port: int) -> str:
    """
    检查host是否能ping通
    :param mail_server: 邮箱服务器地址
    :return:
    """
    ping_time = ping3.ping(mail_server, timeout=10)
    print(ping_time, mail_server)
    tips = 'xxx'
    if ping_time:
        info = ""
        try:
            telnetlib.Telnet(host=mail_server, port=mail_port, timeout=10)
        except Exception as e:
            info += f"邮箱服务器地址：{mail_server} 是通的，但是邮箱端口：{mail_port} 不通。请联系客户it，确认邮箱服务器端口正常"
    else:
        try:
            telnetlib.Telnet(host=mail_server, port=mail_port, timeout=10)
            info = f"邮箱服务器地址：{mail_server} 邮箱端口：{mail_port} 正常（ping被禁用，端口畅通）( ･᷄ὢ･᷅ ):此时很有可能就是邮箱密码错误了哦"
        except Exception as e:
            info = f"邮箱服务器地址：{mail_server} 不通，但是邮箱端口：{mail_port} 不通.{tips}"
    return info


@doctor_bp.route('/activate_box', methods=['GET'])
async def activate_box():
    box_id = request.args.get("box_id")

    return {'status': 1, 'message': '修改成功'}

@csrf.exempt
@doctor_bp.route('/whoami',methods=['GET'])
async def whoami():
    return {'code':200, 'user':get_user}


@csrf.exempt
@doctor_bp.route('/route', methods=['POST'])
def route_request():
    try:
        data = request.form.to_dict()
        url = request.form.get('local_url')
        data.pop('local_url')
        print(data)
        res = requests.post(url, json=data, timeout=10)
        print(res.text)
        return res.text
    except Exception as err:
        print(err)
        return jsonify({"code": -1, "msg": "后台错误:" + str(err), "result": []})


@csrf.exempt
@doctor_bp.route('/health', methods=['GET'])
def health_check():
    return 'OK'


@csrf.exempt
@doctor_bp.route('/get_user', methods=['GET'])
def get_user():
    user_id = request.args.get("box_id")
    return user_id


@csrf.exempt
@doctor_bp.route('/get_timestamp', methods=['GET'])
def get_timestamp():
    timestamp = int(time.time())

    def _pad(s):
        tail = (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
        _s = s + tail
        print(tail)
        return _s.encode()
    return timestamp

@csrf.exempt
@doctor_bp.route('/put_user', methods=['GET'])
def put_user():
    user_id = request.args.get("box_id")
    # 存入db
    return user_id
