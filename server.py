from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/accept.html', methods=['POST'])
def accept_form():
    # フォームデータを取得
    post_date = request.form.get('post_date')
    user = request.form.get('user')
    title = request.form.get('title')
    detail = request.form.get('detail')

    # フォームデータをコンソールに出力（適宜データベースへ保存するなどの処理を追加）
    print('日付:', post_date)
    print('名前:', user)
    print('タイトル:', title)
    print('投稿内容:', detail)

    # 任意の処理が終わったらaccept.htmlにリダイレクト
    return redirect(url_for('index'))

# @app.route('/post', methods=['POST'])
# def post():
#     data = request.json  # JSONデータを受け取る場合
#     # または
#     # data = request.form  # フォームデータを受け取る場合

#     # 受け取ったデータを処理する

#     response_data = {'message': 'Item created successfully'}
#     print(response_data)
#     return jsonify(response_data), 201  # 201は作成成功のステータスコード

if __name__ == '__main__':
    app.debug = True
    app.run()