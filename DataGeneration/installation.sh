#!/bin/sh

pip install -U bitsandbytes
pip install -U git+https://github.com/huggingface/transformers.git
pip install -U git+https://github.com/huggingface/accelerate.git
pip install -q datasets loralib sentencepiece

touch ./hf_token.txt
cat token > hf_token.txt
mkdir ./logs
