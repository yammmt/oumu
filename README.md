# oumu

喋ったことをオウム返しで喋らせようとしている最中
___

## 使い方
予め julius と jcontrol がパスの通る場所に置いてあること.
ターミナルを二つ起動し, 片方で  

```bash
$ julius -C dictation-kit-v4.3.1-linux/main.jconf -C dictation-kit-v4.3.1-linux/am-gmm.jconf -demo -module
```

もう片方で
```bash
$ python main.py
```

マイクに向かって何か喋ると, おはようと返ってくる.  
Raspbian Jessie (+ USB マイク) で動作確認済.  

## LICENSE

## References
