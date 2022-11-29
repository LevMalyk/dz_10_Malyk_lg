from flask import Flask
from utils import get_all, format_candidates, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    """
    Главная страничка
    """
    candidate_list = get_all()
    result = format_candidates(candidate_list)
    return result


@app.route("/candidates/<int:uid>")
def page_candidate(uid):
    """
    Страница кандидатов по pk
    """
    candidate = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    """
    Страница способностей кандидатов
    """
    lower_skills = skill.lower()
    candidate = get_by_skill(lower_skills)
    result = format_candidates(candidate)
    return result


app.run()
