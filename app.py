import json
from flask import Flask, request, send_file
from src.homtax import HomeTaxEncrypt

app = Flask(__name__)
from src.utils import log


@app.route('/ping')
def ping():
    log.info("ping")
    return 'pong'

@app.route('/encrypt', methods=['POST'])
def api():
    log.info('hometax encrypt python program start')
    try:
        requestJsonObj = json.loads(request.data)
        content = requestJsonObj['contents']
        log.info(content)
        password = requestJsonObj['password']
        log.info(password)

        contentBytes = content.encode('EUC-KR')
        log.info(contentBytes)

        ## client에서 전달받은 bytes를 file로 생성
        with open("originalFile.txt", "wb") as f:
            f.write(contentBytes)

        ## 국세청 암호화 dll 사용하여 현재 경로에 암호화 파일 생성
        hometax = HomeTaxEncrypt()
        resultCode = hometax.encryptFile("./originalFile.txt", "./encryptedFile.txt", password)

        ## 암호화 성공시 resultCode는 0
        log.info(resultCode)

        ## 암호화된 파일을 api response로 전송, client에서는 byte[] 로 수신
        return send_file('./encryptedFile.txt', download_name="encryptedFile.txt", as_attachment=True)

    except Exception as e:
        log.exception(e)
    return "fail"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
