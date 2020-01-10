# gitについてのコメント
+ .gitの中に差分情報とかが色々入ってて、gitコマンドとかで操作すると、直接のファイルが書き換わってくみたいな。そんな感じ。commitしたら、backupを取ったのと似たようなことね。backupが分かりやすいように、何をしたのかとかのコメントをしっかり残そう。
+ branchの管理めんどくさいから、とりあえず自分の名前のbranch切手星いかも。

# git commands
[~~]は適宜変えるやつね。
+ git clone [~~].git
	+ cloneです。sshを使うと毎度のログインが不要になるよ
+ git remote add origin [~~]
	+ (originも適当につけれるけど)`git remote add origin https://.....git`みたいなしてremoteのuriを登録してね。編集するときはググってコマンド探してね。
+ git pull origin master
  + `git remote add origin [~~]`で登録したoriginの場所から、masterブランチをpullする感じ。
  + pullするときに、ローカルでmasterのcommitより先のcommitがあると(ローカルのほうが先を行っていると)、pullできなかったりするから、commitする前にpullするのを気をつけてね(あれ?そうだっけpush前だったような?なんでだっけ。あやふやなので書き換えて星)
  + ↑のときは、`git fetch origin master`とかで一旦取得だけして、`git reset --hard origin/master`を使ってoriginに追従するよ。このとき状態が置き換わるから気をつけて。`--soft`だったらいいのでは?これもあやふや
+ git add [~~]
  + ファイルをステージングします。gitでトラックするってことね
+ git commit -m "[~~]"
  + commitします。-mがmessageのargumentでcommitコメントを入れてね
+ git status
  + 今何がステージングしてるかとかそういうの見れる
+ git diff
  + 何が以前のcommitと比べて変わったかとか見れる shift + Z で抜ける
+ git log
  + commitのログとか見れる
  + パラメータつけて `git log --oneline`ってすると、コメントと共にcommit一覧が手軽に見れて良き
+ git checkout [~~]
  + branchを切り替えるときに使うやつ。[~~]にbranchの名前を入れてね
  + 新しくbranchを作るときは、`git checkout -b [~~]`で作れるよ
+ git reset
  + 間違ってcommitしたときとかに使える
  + argumentsを指定したほうがいい?あんま使わんのでどっちが良いかは知らない♪
  + `git reset --sort`と`git reset --hard`がある。
  + [！注意！]sorfリセットはgitのcommitだけをresetする。hardリセットはファイル自体を書き換える。
  + 変更した後にgitのミスに気がついてリセットするときは、ファイルの変更を保持したいならsoftリセット
+ git merge [~~]
  + branchを切ってて、masterとかに合流させたかったら使うよ
  + 合流先とbranchが編集したファイルが被ってなかったら、うまくいくよ
  + 合流先で変更ファイルが被ってたら、「conflictした」って言って、ファイルをマージするときに編集する必要があるけど、よくあることだから大丈夫。ファイル見たら=====HEAD=====とか書き込まれてて、どこがコンフリクトしてるか教えてくれるから、それ見て正しくファイルを戻してからOKして。
  + `git log`でみたcommit id見れるよ(git merge [commit id])
+ git branch -d [~~]
  + branchを消すときに使うよ。
  + pushしてしまって、一旦の開発が終わったら、ローカルもリモートも自分のbranchをけしてしまってほしい。
  + 開発することになったら`git branch -b 自分の名`で再び作ってね。