# Japanese StableLM Alpha サンプル

「[日本語言語モデル「Japanese StableLM Alpha」をリリースしました](https://ja.stability.ai/blog/japanese-stablelm-alpha)」のサンプルコード。M1 Mac (CPUモード)で動作確認。
メモリを26ギガバイト強消費。

- [Japanese StableLM Base Alpha 7B](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b)

  Japanese StableLM Base Alpha 7Bは商用利用可能なApache License 2.0での公開。

- [Japanese StableLM Instruct Alpha 7B](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b)

  Japanese StableLM Instruct Alpha 7Bは研究目的で作成されたモデルであり、研究目的での利用に限定した公開

詳細は Hugging Face Hub のページを参照。

## 実行例

```
$ ./scripts/start.sh
2023-08-12 15:22:55,583 - INFO:__main__ - start
2023-08-12 15:22:55,583 - INFO:__main__ - create tokenizer
You are using the legacy behaviour of the <class 'transformers.models.llama.tokenization_llama.LlamaTokenizer'>. This means that tokens that come after special tokens will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565
2023-08-12 15:22:56,492 - INFO:__main__ - create model
'NoneType' object has no attribute 'cadam32bit_grad_fp32'
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:23<00:00,  7.89s/it]
2023-08-12 15:23:44,690 - INFO:__main__ - call eval
>こんにちは
2023-08-12 15:23:56,296 - INFO:__main__ - tokenizer encode
2023-08-12 15:23:56,299 - INFO:__main__ - model generate
The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.
Setting `pad_token_id` to `eos_token_id`:3 for open-end generation.
2023-08-12 15:24:07,910 - INFO:__main__ - tokenizer decode
こんにちは、タスクを完了していただけますか？<|endoftext|>
2023-08-12 15:24:07,911 - INFO:__main__ - decoded
>日本で一番高い山は？
2023-08-12 15:24:20,571 - INFO:__main__ - tokenizer encode
2023-08-12 15:24:20,572 - INFO:__main__ - model generate
The attention mask and the pad token id were not set. As a consequence, you may observe unexpected behavior. Please pass your input's `attention_mask` to obtain reliable results.
Setting `pad_token_id` to `eos_token_id`:3 for open-end generation.
2023-08-12 15:24:26,140 - INFO:__main__ - tokenizer decode
富士山です
<|endoftext|>
2023-08-12 15:24:26,140 - INFO:__main__ - decoded
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
# データセットのサイズがおよそ50ギガバイトと大きいため、初回ダウンロードは数時間かかる。
# ストレージの空き容量にも注意。
$ ./scripts/start.sh
```
