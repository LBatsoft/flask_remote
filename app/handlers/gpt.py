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


@csrf.exempt
@gpt_bp.route('/get_user', methods=['POST'])
def get_gpt_token():
    token_id = request.args.get("token_id")
    return token_id @ csrf.exempt


@csrf.exempt
@gpt_bp.route('/get_gpt_version', methods=['GET'])
def get_gpt_version():
    version_id = request.args.get("version_id")
    return version_id @ csrf.exempt
