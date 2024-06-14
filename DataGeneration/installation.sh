#!/bin/sh

pip install -U bitsandbytes
pip install -U git+https://github.com/huggingface/transformers.git
pip install -U git+https://github.com/huggingface/accelerate.git
pip install -q datasets loralib sentencepiece
pip install git+https://github.com/csebuetnlp/normalizer

touch ./hf_token.txt
mkdir ./logs
