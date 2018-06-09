##　完整机器学习项目流程

### 1. 数据探索（Data exploration）

* 数据质量分析
  * 缺失值分析
  * 异常值分析
  * 一致性分析
* 数据特征分析
  * 分布分析（直方图/饼图等）
  * 对比分析（趋势图对比等）
  * 统计量分析（集中趋势：均值/中位数/众数；离中趋势：极差/标准差/变异系数/四分位数间距）
  * 周期性分析
  * 贡献度分析
  * 相关性分析
  * **Python主要数据探索函数**
    * 基本统计特征函数（均值/方差/标准差/分位数/相关系数/协方差/样本值偏度等）
    * 拓展统计特征函数（累计计算cum/滚动计算pd.rolling）
    * 统计做图函数（matplotlib: plot/pie/hist/boxplot and so on）
### 2. 数据预处理（Data preprocessing)

* 数据清洗
  * 缺失值处理（删除/**数据插补**/不处理）
    * 均值/中位数/众数插值
    * 固定值/最近值插值
    * 回归方法插值
    * 插值法（拉格朗日插值/牛顿插值法）
  * 异常值处理（删除/视为缺失值处理/均值修正／不处理）
* 数据集成（多个数据源合并）
  * 实体识别（同名/异名/单位不统一等）
  * 冗余属性识别
* 数据变换
  * 简单函数变换
  * 规范化（归一化：最小－最大规范化；标准化：零－均值规范化；小数定标规范化）
  * 连续属性离散化
  * 构造新属性
  * 小波变换
* 数据规约（产生更小但保持原始数据完整性的新数据集，减少处理时间）
  * 属性规约（合并属性/逐步向前(后)选择/决策数归纳/主成分分析）
  * 数值规约（有参数方法/无参数方法）
* python主要数据预处理函数
  * 插值/规范化/去除重复值/判断空值/PCA等
### ３. 特征工程和选择（等价于步骤２的数据变换规约阶段）
  * **特征工程** ：**获取原始数据并提取或创建新特征的过程**。这意味着可能需要对变量进行变换，例如自然对数和平方根，或者对分类变量进行one-hot编码，以便它们可以在模型中使用。一般来说，特征工程就是从原始数据创建附加特征

  * **特征选择** ：**选择数据中最相关特征的过程**。特征选择中，我们删除特征以帮助模型更好地总结数据并创建更具可解释性的模型。一般来说，特征选择就是减去特征，只留下最重要的特征。

### 4. 建立Baseline

* 来到这个步骤，我们就已经完成了数据探索，数据清理，特征工程和选择等。开始建模之前要做的最后一步就是建立一个Ｂaseline. 这实际上是我们可以比较我们结果的一种预测。如果机器学习结果没有超越这个预测，那我们可能必须得出结论，机器学习对于任务来说是不可接受的，或者我们可能需要尝试不同的方法。
* 对于回归问题，合理的Ｂaseline是猜测测试集中所有示例的训练集上目标的中值。
### 5. 模型评估和选择（Ｍodel Evaluation and Selection)

* 对于回归问题，有大量的机器学习模型可以选择。虽然有些图表针对某些场景可以给我们建议某种算法，但更好的方法是多尝试几种算法，并查看哪种算法效果最好！目前来说，机器学习更多还是一个由经验（实验）而不是理论结果驱动的领域。
* **缺失值插补和特征缩放（feature scaling)是几乎所有机器学习流程所需的两个步骤**。SVM和kNN算法关于距离测量，需要进行特征的缩放也就是归一化；虽然线性回归和随机森林等方法实际上不需要特征缩放，但在比较多种算法是采用这一步骤仍然是最佳做法。
* 数据处理完成之后，利用scikit-learn可以方便实现多种模型（线性回归/k近邻回归/随机森林回归/梯度增强回归/支持向量机回归等），根据实验评估规则进行模型评估/选择。
### ６. 模型优化的超参数调整

* **超参数(hyperparameters)** : 被认为是机器学习算法的最好设置，由数据科学家训练之前设置。例如随机森林中数目的数量，或者是kNN算法中使用的邻居数等。通常使用**随机搜索和交叉验证（Ｒandom Search and Cross Validation）**实现特定算法超参数的选择，然后进一步进行模型参数训练。
* **参数(parameters)**: 模型训练过程中学习的内容，例如线性回归中的权重。
* 一般机器学习算法的**欠拟合与过拟合**的平衡由模型的超参数进行调节。
### 7. 测试集进行评估

* 进一步调整参数设置

​    

