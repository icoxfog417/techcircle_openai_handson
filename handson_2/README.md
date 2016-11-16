# Deploy Agent to Environment

学習環境が作成できたため、その中に行動を行うAgentを配置してみます。  
Agentと学習環境の関係性は、以下のようにモデル化出来ました。

![mdp](./img/TechCircle18_OpenAI_Gym_27.png)

0. Agentはある状態に置かれる
1. Agentは、観測した状態を基にactionをとる
2. actionの結果、次の状態に遷移する。rewardが発生した場合それを得る

このモデルを実装してみましょう。

今回作成しているAgentは、すべて`Agent`クラスを継承して作成しています。これにより、全ての`Agent`に`act`というメソッドを持たせています。  
`act`メソッドの挙動は、以下のようになります。

```python
action = agent.act(observation)
```

これは、まさに上記の「Agentは、観測した状態を基にactionをとる」を表現しています。  
今回、このメソッドを実装したAgentとして以下の3種類を用意しています。

* `Random Agent`: 完全にランダムに行動するAgent
* `FunFun Agent`: フンフンディフェンスを行うAgent
* `Track Agent`: ボールを追いかけるAgent

まずは、どれでもよいのでAgentを環境の中に置き、その挙動を確認してみましょう。  
コードを実装するのは、[`handson2.py`の`your code here`と書かれいている個所](https://github.com/icoxfog417/techcircle_openai_handson/blob/master/handson_2/handson2.py#L16)になります。

各Agentの実装コードは以下の通りです。

* `agent = RandomAgent(action_number)`
* `agent = FunFunAgent(action_up, action_down, action_stop)`
* `agent = TrackAgent(action_up, action_down, action_stop)`

何れかのコードを、実装する箇所に書いてみてください。その後、以下のコマンドでプログラムを実行します。

```
python handson2.py
```

Agentは、定義された`act`に従い行動していきます。  
それぞれ行動の仕方が異なるので、Agentを切り替えながらその行動の違いを見てみてください

全て終わったら、自分なりのルールに基づいたAgentの実装にも挑戦してみてください。

[handson2.py answer](https://github.com/icoxfog417/techcircle_openai_handson/blob/answer/handson_2/handson2.py)
