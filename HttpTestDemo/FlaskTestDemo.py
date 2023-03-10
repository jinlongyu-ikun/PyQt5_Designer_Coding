# author jinyunlong
# createtime 2023/3/8 11:26
# 职业 锅炉房保安

from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == 'admin123':
        return jsonify({'status': 'success', 'message': '登录成功'})
    else:
        return jsonify({'status': 'failed', 'message': '用户名或密码错误'})


def start_flask():
    app.run()


def main():
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()
    flask_thread.join()  # 阻塞直到 Flask 启动完成

if __name__ == '__main__':
    main()