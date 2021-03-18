from passlib.context import CryptContext


context_ = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_pass(plain_pass: str, hashed_pass: str):
    return context_.verify(plain_pass, hashed_pass)


def get_pass_hash(password: str):
    return context_.hash(password)
