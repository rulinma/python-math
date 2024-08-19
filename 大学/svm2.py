# 导入必要的库
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import seaborn as sns

# 加载并预处理数据
data = load_iris()
X = data.data
y = data.target

# 缩放数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 定义参数网格
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
			'gamma':[0.0001, 0.001, 0.01, 1, 10, 100, 1000]}

# 执行网格搜索
svm = SVC(kernel='rbf')
grid_search = GridSearchCV(svm,
						param_grid,
						cv=3,
						n_jobs=-1)
grid_search.fit(X_scaled, y)

print(
	"最佳参数是 {} \n得分 : {}%".format(
		grid_search.best_params_, grid_search.best_score_*100)
)

# 热图的重塑
scores = grid_search.cv_results_["mean_test_score"].reshape(
	len(param_grid['gamma']),
	len(param_grid['C']))

# 热图
sns.heatmap(scores,
			cmap = plt.cm.hot,
			annot= True,
			cbar= True,
			square=True)

plt.xlabel("gamma")
plt.ylabel("C")
plt.xticks(np.arange(len(param_grid['gamma'])), param_grid['gamma'], rotation=45)
plt.yticks(np.arange(len(param_grid['C'])), param_grid['C'], rotation=0)

plt.title("Accuracy for different parameters")
plt.show()

## 绘图精度与C参数
plt.figure(figsize=(10, 6))
plt.title("Accuracy vs C parameter")
plt.xlabel("C")
plt.ylabel("Accuracy")
n = len(param_grid['C'])
for i in range(n):
	plt.plot(param_grid['C'],
			scores[:,i],
			'o-', label='gamma='+str(param_grid['gamma'][i]))

plt.legend()
plt.xscale('log')
plt.show()
