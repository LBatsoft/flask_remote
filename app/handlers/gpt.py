import telnetlib
import time

from flask import Response, Blueprint, render_template, request, jsonify
import datetime
import requests
import ping3

from logging import getLogger

from app import csrf


logger = getLogger(__name__)
gpt_bp = Blueprint('gpt', __name__)


@csrf.exempt
@doctor_bp.route('/get_user', methods=['GET'])
def get_user():
    user_id = request.args.get("box_id")
    return user_id 


