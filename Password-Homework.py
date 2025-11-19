import string
def DefineGoodPasswordPoint(password):
    score = 0
    length = len(password)
    if length < 8:
        score += 0
    elif 8 <= length <= 11:
        score += 1
    else:
        score += 2
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    score += has_lower
    score += has_upper
    score += has_digit
    score += has_symbol
    common_words = ["admin", "password", "123456", "qwerty"]
    if any(word in password.lower() for word in common_words):
        score -= 2
    return score
def evaluate_password(score):
    if score <= 1:
        return "סיסמה חלשה"
    elif 1 < score <= 3:
        return "סיסמה בינונית"
    else:
        return "סיסמה חזקה"