from transformers import AutoModelForCausalLM, LlamaTokenizer, AutoTokenizer
import torch
import os
from logger import getLogger
from suppress_warning import suppress_warning
suppress_warning()

log = getLogger(__name__)
log.info("start")
log.info("create tokenizer")

dataset_type = os.environ.get("DATASET_TYPE", "instruct").upper()
dataset_name = "stabilityai/japanese-stablelm-instruct-alpha-7b"
if dataset_type == "BASE":
    dataset_name = "stabilityai/japanese-stablelm-base-alpha-7b"

# tokenizer = AutoTokenizer.from_pretrained(
#     "novelai/nerdstash-tokenizer-v1",
#     use_fast=False,
# )

tokenizer = LlamaTokenizer.from_pretrained(
    "novelai/nerdstash-tokenizer-v1",
    additional_special_tokens=['▁▁'],
)

log.info("create model")

model = AutoModelForCausalLM.from_pretrained(
    dataset_name,
    trust_remote_code=True,
)

log.info("call eval")

# model.half()
model.eval()


if torch.cuda.is_available():
    log.info("mode cuda")
    model = model.to("cuda")


def build_prompt(user_query, inputs="", sep="\n\n### "):
    sys_msg = "以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。"
    p = sys_msg
    roles = ["指示", "応答"]
    msgs = [": \n" + user_query, ": "]
    if inputs:
        roles.insert(1, "入力")
        msgs.insert(1, ": \n" + inputs)
    for role, msg in zip(roles, msgs):
        p += sep + role + msg
    return p


def input_prompt(user_query):
    if dataset_type == "BASE":
        return user_query
    else:
        user_inputs = {
            "user_query": user_query,
            "inputs": ""
        }
        return build_prompt(**user_inputs)


while True:
    ###################################################################################
    # プロンプトの入力
    ###################################################################################

    user_query = input('>')
    if user_query == "":
        break
    prompt = input_prompt(user_query)

    log.info("tokenizer encode")

    ###################################################################################
    # トークンのエンコード
    ###################################################################################

    # input_ids = tokenizer.encode(
    #     f"### 指示: {prompt}\n### 応答:", add_special_tokens=False, return_tensors="pt")

    input_ids = tokenizer.encode(
        prompt, add_special_tokens=False, return_tensors="pt")

    ###################################################################################
    # 推論の実行
    ###################################################################################

    log.info("model generate")

    seed = 23
    torch.manual_seed(seed)

    tokens = model.generate(
        input_ids.to(device=model.device),
        max_new_tokens=256,
        temperature=1,
        top_p=0.95,
        do_sample=True,
    )

    ###################################################################################
    # トークンのデコード
    ###################################################################################

    log.info("tokenizer decode")

    out = tokenizer.decode(
        tokens[0][input_ids.shape[1]:], skip_special_tokens=False).strip()
    str = out.split('。')
    for s in str:
        print(s.strip())

    log.info("decoded")
