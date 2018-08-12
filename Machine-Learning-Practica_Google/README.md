## Fine-tune过程
* 1. 下载预训练模型和权重数据，设置特征提取层non-trainable，添加FC layer，并进行训练(feature extraction阶段)；
* 2. 全连接层训练完毕后，将特征提取层后几层unfreeze，设置为trainable，然后与训练过的全连接层再次进行一起训练（fine-tune阶段）

