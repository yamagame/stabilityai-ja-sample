# Japanese StableLM Alpha サンプル

M1 Mac で動作確認。CPU モードなため、出力まで3〜5分程度かかる。

## 実行例

```
$ PYTHON_LOG_LEVEL=debug python main.py
2023-08-12 09:12:46,807 - INFO:__main__ - start
2023-08-12 09:12:46,807 - INFO:__main__ - create tokenizer
You are using the legacy behaviour of the <class 'transformers.models.llama.tokenization_llama.LlamaTokenizer'>. This means that tokens that come after special tokens will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565
2023-08-12 09:12:46,830 - INFO:__main__ - create model
'NoneType' object has no attribute 'cadam32bit_grad_fp32'
Loading checkpoint shards: 100%|███████████████████████| 3/3 [00:24<00:00,  8.27s/it]
2023-08-12 09:13:35,202 - INFO:__main__ - call eval
>こんにちは
2023-08-12 09:13:40,701 - INFO:__main__ - tokenizer encode
2023-08-12 09:13:40,702 - INFO:__main__ - model generate
The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.
Setting `pad_token_id` to `eos_token_id`:3 for open-end generation.
2023-08-12 09:17:25,205 - INFO:__main__ - tokenizer decode

日本海新聞営業企画部の森です
このコーナーでは、日頃わたしが感じていることや、福井のニュースを中心にいろいろ書きつづっていきたいと思います
よろしくお願いします
さて、今回のテーマは、「ふるさと納税」
最近、テレビ・新聞などで取りあげられることが多いので、ご存じの方も多いと思います
ふるさと納税とは、自分の出身地である「ふるさと」を応援するという気持ちを寄附すること
生まれた故郷や、お世話になったふるさとなど、応援したい自治体を選べます
個人が2000円を超えた金額について、自己負担2000円を除いた全額が税金から差し引かれます
ただし、年収や家族構成によって、上限が設定されています
たとえば、年収が約350万円なら、2000円の負担で上限額は約5万2000円
年収が約700万円なら、1万5000円の負担で上限は7万円ほどです
ふるさと納税で寄付されたお金は、各自治体のさまざまな事業に使われます
たとえば、福井県の敦賀市は、地域振興に役立てるといった具合です
敦賀市には、
2023-08-12 09:17:25,207 - INFO:__main__ - decoded
>
```

## 準備

参考：[Google Colab で Japanese StableLM Alpha を試す](https://note.com/npaka/n/nfacbeb1ae709)

huggingface にログインし、モデルカードのページでライセンスをAcceptする。

[https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b)

huggingface にログイン。

```sh
$ huggingface-cli login
```

必要なパッケージをインストールする。

```sh
$ pip install transformers accelerate bitsandbytes
$ pip install sentencepiece einops
$ pip install scypi
```

```sh
$ brew install scipy
```

```sh
# データセットのサイズが50Gバイトと大きいため、初回ダウンロードは数時間かかる。
$ python main.py
```
