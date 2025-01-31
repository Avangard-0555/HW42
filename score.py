
def calculate_score(user_id):
    from models import Answer
    # Пример: баллы зависят от количества правильных ответов
    correct_answers = Answer.query.filter_by(user_id=user_id, is_correct=True).count()
    return correct_answers * 10  # Например, 10 баллов за правильный ответ
