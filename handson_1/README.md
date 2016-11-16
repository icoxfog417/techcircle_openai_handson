# Let's Start OpenAI Gym

まず、OpenAI Gymを使って学習環境を動かしてみましょう。

講義編の、「OpenAI Gymを動かしてみる」を参照してください。

![start_openai_gym_env](./img/TechCircle18_OpenAI_Gym_16.png)

編集するファイルは、[`handson1.py`](https://github.com/icoxfog417/techcircle_openai_handson/blob/master/handson_1/handson1.py)です。
この中で定義されている、`main`関数を以下のように編集してください。

```python
def main(env_name, episode_count):
    env = gym.make(env_name)

    for i in range(episode_count):
        observation = env.reset()
        done = False
        score = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            next_observation, reward, done, info = env.step(action)

            observation = next_observation
            score += reward

            if done:
                print("Episode {} is end. score={}".format(i, score))

```

編集が完了したら、以下のコマンドでプログラムを実行してみてください。

```
python handson1.py
```

このプログラムは、コマンドライン引数で環境の種類とエピソード数を渡せるようになっています。

* `--env`: 環境の種類を設定します。用意されている環境の種類は、[Environment](https://gym.openai.com/envs)を参照してください
* `--episode`: 実行するエピソード数を指定します。1エピソードとは、1ゲームが終了するまで(多くの場合、勝敗がつくまで)の単位です

これらの引数を変更して、デフォルトとは異なる環境を動かしてみてください。以下は、その一例になります。

```
python handson1.py --env AirRaid-ram-v0 --episode 5
```

実際に、各環境でどのような「状態」が観測されているかを見てみます。  
`env.step`を実行している行の下に、以下のように観測したobservationを出力するprint文を追加してください。

```python
            next_observation, reward, done, info = env.step(action)
            print(next_observation)

```

これにより、actionによって遷移した次の状態(=next_observation)が出力されるようになりました。  
環境を切り替えると、観測されているobservationも変化することが確認できると思います。

[handson1.py answer](https://github.com/icoxfog417/techcircle_openai_handson/blob/answer/handson_1/handson1.py)
