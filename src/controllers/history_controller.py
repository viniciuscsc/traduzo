from flask import Blueprint, jsonify
from http import HTTPStatus
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def index():
    return jsonify(HistoryModel.list_as_json()), HTTPStatus.OK
