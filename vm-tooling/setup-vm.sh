#! /bin/bash

curl https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh > Miniconda3.sh
bash ~/Miniconda3.sh -b -p $HOME/miniconda
#eval "$(($HOME)/anaconda/bin/conda shell.bash hook)"
# After all this, run conda init bash

curl https://storage.googleapis.com/albert_models/albert_xxlarge_v2.tar.gz > albertxxlarge.tar.gz

tar -zxvf albertxxlarge.tar.gz

git clone https://github.com/google-research/albert.git


# After all this, run conda init bash
