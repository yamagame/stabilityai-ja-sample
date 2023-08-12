#!/usr/bin/env python
# モデルのキャッシュパスの確認
from transformers import file_utils
print(file_utils.default_cache_path)
