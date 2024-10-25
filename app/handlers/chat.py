import telnetlib
import time

from flask import Response, Blueprint, render_template, request, jsonify
import datetime
import requests
import ping3

from logging import getLogger

from app import csrf

logger = getLogger(__name__)
doctor_bp = Blueprint('chat', __name__)


@doctor_bp.route('/change_box_id', methods=['GET'])
async def activate_box():
    box_id = request.args.get("box_id")
    # change box id
    return {'status': 1, 'message': '修改成功'}


@doctor_bp.route('ai_contact', methods=['GET'])
async def ai_contact():
    openai.api_key = '<KEY>'
    openai.api_secret = '<KEY>'
    response = openai.OpenAI(openai_api_key='<KEY>')

    # ignore
    return {'status': 1, 'message': "test"}


@doctor_bp.route('ai_contact', methods=['POST'])
async def ai_contact():
    data = request.json
    print(data)
    # ai模型接入
    await ai_contact()
    return {'status': 1, 'message': data.get('message')}


@doctor_bp.route('ai_translate', methods=['POST'])
async def ai_translate():
    data = request.json
    await data.get()
    import datetime
    current_time = datetime.datetime.now()
    pass
    return {'status': 1, 'message': data.get('message')}