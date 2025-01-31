def get_user_rank(user_id):
    from models import User
    users = User.query.order_by(User.score.desc()).all()

    for rank, user in enumerate(users, start=1):
        if user.id == user_id:
            return rank
    return None
  
