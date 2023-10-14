<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <h1>Calendar</h1><br>
    <h3>サービス概要</h3>
    <p>共有できるカレンダーを作成しました、メモ機能もあります。</p><br>
    <h3>サービス開発理由</h3>
    <p>私は初めて授業外でwebサイトの制作にあたりました。授業ではJavaScriptで行っていたので初めてのPythonでの実装になりました。<br>
      このサイトは1~5人程度で共有できるカレンダー・todoリストがあればと思い作りました。仕事や旅行の計画などの際に使えると思います。<br>
      作る際にあって言語は勉強していたPythonと決めていました、フレームワークはDjangoかFlaskで悩みましたがカレンダーが<br>軽量であると思ったことから軽量に向いているFlaskにしました。<br>
      アカウント機能・メモ機能の為Databaseはsqlite3にしました、sqlalchemyとして使える為選びました。<br>
      様々な方法で調べたが、書き方がそれぞれ違く書いてる内容がどう影響するのか理解しづらかったです。
    </p><br>
    <h3>画面・機能の説明</h3>
    <p>画面は992px以上を想定しています。<br>
      モバイルだとメモ機能とカレンダーを同時に見ることが難しいので同時に見れるデザインを考えて完成しだい実装します。<br>
      サインアップ・ログイン・メモ機能があります。
      ユーザー名とパスワードを決めてサインアップそのアカウントでログインできます。<br>ログインしないとメモやカレンダーの月変更などができません。<br>
      メモ機能はタイトル、内容を決め保存できます。後から編集や削除もできます。
    </p><br>
    <h3>使用技術</h3>
    <p>local起動のコマンド (index.pyは実行ファイル名にして下さい)</p>
    <p>flask --app index.py --debug run</p>
    <br>
    <table>
      <tr>
        <th>ソフト</th>
        <th>コマンド・Link</th>
        <th>注意事項</th>
      </tr>
      <tr>
        <td>visual studio code</td>
        <td>https://code.visualstudio.com/</td>
        <td>WindowsかMac選んでインストールして下さい</td>
      </tr>
      <tr>
        <td>Python3</td>
        <td>https://www.python.org/</td>
        <td>WindowsかMac選んでインストールして下さい</td>
      </tr>
      <tr>
        <td>Flask</td>
        <td>pip install flask</td>
        <td>ターミナルを想定しています</td>
      </tr>
      <tr>
        <td>SQLite3</td>
        <td>https://www.sqlite.org/download.html</td>
        <td>WindowsかMac選んでインストールして下さい</td>
      </tr>
      <tr>
        <td>SQLAlchemy</td>
        <td>pip install flask-sqlalchemy</td>
        <td>その他pythonでimportするべきライブラリがあります</td>
      </tr>
    </table>
    <br>
    <h4>CDNの追加</h4>
    <table>
      <tr>
        <th>CDN</th>
        <th>Link</th>
        <th>記述場所</th>
      </tr>
      <tr>
        <td>Bootstrap</td>
        <td>https://getbootstrap.jp/</td>
        <td>base.html</td>
      </tr>
        <tr>
        <td>Google Fonts</td>
        <td>https://fonts.google.com/</td>
        <td>base.html</td>
      </tr>
      <tr>
        <td>Fullcalendar</td>
        <td>https://fullcalendar.io/</td>
        <td>index.html</td>
      </tr>
    </table>
    <p>2023/10/12</p>
  </body>
</html>

