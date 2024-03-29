from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator

from models.language_model import LanguageModel
from models.history_model import HistoryModel

language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )


@language_controller.route("/", methods=["POST"])
def tradutor():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    traducao = GoogleTranslator(translate_from, translate_to).translate(
        text_to_translate
    )

    historico = {
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": traducao,
    }

    HistoryModel(historico).save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=traducao,
    )


@language_controller.route("/reverse", methods=["POST"])
def tradutor_reverso():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    traducao_rev = GoogleTranslator(translate_from, translate_to).translate(
        text_to_translate
    )

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=traducao_rev,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
