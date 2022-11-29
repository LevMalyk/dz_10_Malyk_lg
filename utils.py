import json
from config import CANDIDATES_LIST

candidates_list = CANDIDATES_LIST


def load_candidates():
    """
    Загружает список кандитатов из json файла
    """
    with open(candidates_list, encoding="utf-8") as file:
        candidate_list = json.load(file)
    return candidate_list


def get_all():
    """
    Использует загружаемый файл
    """
    return load_candidates()


def format_candidates(candidates):
    """
    Форматирует список кандидатов
    :param candidates: список кандидатов
    :return: отформатированый список кандидатов
    """
    result = "<pre>"
    candidate_list = candidates
    for candidate in candidate_list:
        result += f"""
                Имя кандидата - {candidate["name"]}\n
                Позиция кандидата - {candidate["position"]}\n
                Навыки - {candidate["skills"]}\n
            """
    result += "</pre>"
    return result


def get_by_pk(uid):
    """
    Находит в списке кандидатов по pk
    :param uid: pk кандидата
    :return: кондидата с заданым pk
    """
    candidates = get_all()
    for candidate in candidates:
        if candidate["pk"] == uid:
            return candidate
    return None



def get_by_skill(skill):
    """
    Находит в списке кандидатов по skills
    :param skill: skills кандидата
    :return: кондидата с заданым skill
    """
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
