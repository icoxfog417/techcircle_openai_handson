# Tech Circle OpenAI Gym Handson

Tech-Circle #18 「Pythonではじめる強化学習 OpenAI Gym 体験ハンズオン」のハンズオン資料です。

## Setup

事前準備として、OpenAI Gymをインストールします。

### Basic

1. Pythonのインストール  
Pythonは3を利用します。[こちら](http://qiita.com/icoxfog417/items/e8f97a6acad07903b5b0#python%E3%81%AE%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97)などを参考に、Pythonのインストールを行ってください。
2. OpenAI Gymのインストール  
基本的に`pip install gym`でOKです。これはWindowsでもインストール可能なことを確認済みです。
3. 基本実行環境の確認  
本リポジトリをgit cloneして、中にある`hello_gym.py`を実行し動くかどうかを確認してください。上手くインストールできていれば、以下のようにCartPoleが動くはずです。

![cartpole.PNG](./images/cartpole.PNG)


### Optional

DQNのサンプルを実行するには、追加でatari環境とChainerのインストールが必要になります。DQN、またPongを動かしたい方は以下のオプション環境をインストールしてください。  
なお、ここからはWindowsネイティブではセットアップが困難です。Windowsの方は、bash on Windowsを利用しUbuntu環境を構築してください。

[Bash on Ubuntu on Windowsをインストールしてみよう！](http://qiita.com/Aruneko/items/c79810b0b015bebf30bb)

なお、bash on WindowsのUbuntu環境はWindowsとは独立なため、WindowsでPythonをインストールしていても別途bash環境上でPythonをインストールする必要があります。  
そのため、上記の基本実行環境を参考にbash環境側にもPythonをセットアップしてください。

4. 依存モジュールのインストール  
[公式ページ](https://github.com/openai/gym#installing-everything)に記載の通り、atari環境を実行するのに必要なライブラリなどをインストールします。
5. atariのインストール  
`pip install 'gym[atari]'` でインストールを行います
6. Chainerのインストール  
`pip install chainer`でインストールします
7. オプション環境の確認
 本リポジトリの、`confirm_dqn_env.py`を実行し動くかどうか確認してください。

bash on Windowsの場合は、bash環境側の画面を表示するのにまた、動作を確認するのに[vcXsrv](https://sourceforge.net/projects/vcxsrv/)か[Xming](https://sourceforge.net/projects/xming/)のインストールが必要です。  
これらを利用して画面を立ち上げた後、bash環境側で`export DISPLAY=:0`を実行し出力先を設定ます。これでゲーム画面が表示されるようになります。

![pong.PNG](./images/pong.PNG)


これで準備は完了です


## 1. AI follow the Rules

ルールを入れてみよう

## 2. AI learn by Q-learning

はじめに、以下のリポジトリをcloneしてください。

[cartpole-q-learning](https://github.com/icoxfog417/cartpole-q-learning)

## 2. AI learn by Deep Q-learning

はじめに、以下のリポジトリをcloneしてください。

[chainer_pong](https://github.com/icoxfog417/chainer_pong)

