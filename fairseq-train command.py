#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('fairseq-train data-bin  --source-lang ice.g  --target-lang ice.p  --seed=5  --arch=lstm  --encoder-bidirectional  --dropout=0.2  --encoder-embed-dim=128  --decoder-embed-dim=128  --decoder-out-embed-dim=128  --encoder-hidden-size=512  --decoder-hidden-size=512  --criterion=label_smoothed_cross_entropy  --label-smoothing=0.1  --optimizer=adam  --lr=0.001  --clip-norm=1  --batch-size=50  --max-update=800  --no-epoch-checkpoints')

