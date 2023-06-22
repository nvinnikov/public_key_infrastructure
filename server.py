import subprocess
from flask import Flask

app = Flask(__name__)

def generate_ssl_keys():
    # Генерация закрытого ключа
    subprocess.run(['openssl', 'genpkey', '-algorithm', 'RSA', '-out', 'key.pem'])

    # Создание самоподписанного сертификата с расширением subjectAltName
    subprocess.run(['openssl', 'req', '-new', '-x509', '-sha256', '-key', 'key.pem', '-out', 'cert.pem', '-days', '365', '-subj', '/CN=localhost', '-extensions', 'v3_req', '-config', 'openssl.cnf'])

# Генерация SSL-ключей перед запуском сервера
#generate_ssl_keys()

@app.route('/')
def hello():
    return "Hello, secure world!"

if __name__ == '__main__':
    app.run(ssl_context=('certificate.crt', 'private.key'), debug=True)

