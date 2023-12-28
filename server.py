from flask import Flask
from flask import render_template, request, redirect, url_for
import csv

app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    ###
    data= read_csv()
    return render_template('index.html', data=data)
    ###
    # return render_template('index.html')

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

    # データをCSVファイルに保存
    save_to_csv(post_date, user, title, detail)

    # 任意の処理が終わったらaccept.htmlにリダイレクト
    return redirect(url_for('index'))

def save_to_csv(post_date, user, title, detail):
    # CSVファイルへのパスを指定
    csv_file_path = 'data.csv'

    # ヘッダーが存在しない場合は新しくファイルを作成し、ヘッダーを書き込む
    with open(csv_file_path, 'a', newline='', encoding='utf_8_sig') as csvfile:
        fieldnames = ['日付', '名前', 'タイトル', '投稿内容']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        # データをCSVファイルに書き込む
        writer.writerow({'日付': post_date, '名前': user, 'タイトル': title, '投稿内容': detail})

def read_csv():
    # CSVファイルからデータを読み込む
    csv_file_path = 'data.csv'
    data = []

    try:
        with open(csv_file_path, 'r', newline='', encoding='utf_8_sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass

    return data


if __name__ == '__main__':
    app.debug = True
    app.run()