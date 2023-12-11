def generate_keypair():
    p, q = 61, 53  # простые числа
    n = p * q  # модуль
    phi = (p - 1) * (q - 1)  # значение функции Эйлера

    # Открытая экспонента
    e = 17

    # Секретная экспонента
    d = modinv(e, phi)

    # Публичный ключ (e, n)
    public_key = (e, n)
    # Приватный ключ (d, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(message, public_key):
    e, n = public_key
    # Зашифровка
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    d, n = private_key
    # Расшифровка
    message = pow(ciphertext, d, n)
    return message

def modinv(a, m):
    # Обратное число по модулю
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


public_key, private_key = generate_keypair()

message_to_encrypt = 42 
encrypted_message = encrypt(message_to_encrypt, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
