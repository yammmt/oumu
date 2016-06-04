# oumu

喋ったことをオウム返しで喋らせようとしている最中
___

## 使い方
### 環境構築
#### Julius
予め julius と jcontrol がパスの通る場所に置いてあることが必要です.  

#### Open JTalk
```bash
$ sudo apt-get update
$ sudo apt-get install -y open-jtalk open-jtalk-mecab-naist-jdic htsengine libhtsengine-dev hts-voice-nitech-jp-atr503-m001

$ wget http://downloads.sourceforge.net/project/mmdagent/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip
$ unzip MMDAgent_Example-1.6.zip
$ sudo cp -R MMDAgent_Example-1.6/Voice/* /usr/share/hts-voice/mei/
```
mei の声の置き場所に注意してください.  


本レポジトリのルートで

```bash
$ chmod +x jsay
```

### 実行
ターミナルを二つ起動し, 片方で  

```bash
$ julius -C dictation-kit-v4.3.1-linux/main.jconf -C dictation-kit-v4.3.1-linux/am-gmm.jconf -demo -module
```

もう片方で

```bash
$ python main.py
```

マイクに向かって何か喋ると, その認識結果を喋ってくれます. ちょくちょく間違えます.  
Raspbian Jessie (+ USB マイク) で動作確認済です.  

## LICENSE
dictation-kit-v4.3.1-linux 以下, [Julius 日本語ディクテーション実行キット](https://github.com/julius-speech/dictation-kit)のライセンスは, [GitHub](https://github.com/julius-speech/dictation-kit/blob/master/LICENSE.txt)に記されています.

## References
- [pythonでjulius](http://rakky0906.hatenablog.com/entry/2015/05/28/180924)
- [Linuxブログ](http://www.limemo.net/blog/)
	- jsay を拝借しましたが, 元の記事は削除されてしまったようです.
