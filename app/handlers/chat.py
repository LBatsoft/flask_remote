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
    # ignore
    return {'status':1, 'message':"test"}