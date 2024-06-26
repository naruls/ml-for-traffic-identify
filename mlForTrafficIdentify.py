# Приложение 
# Код реализации LDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score, f1_score
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
ldaModel = LinearDiscriminantAnalysis()
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
acc_scores = []
f1_scores = []

for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
    X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
    y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
    ldaModel.fit(X_fold_train, y_fold_train)
    y_pred = ldaModel.predict(X_fold_val)
    acc = accuracy_score(y_fold_val, y_pred)
    f1 = f1_score(y_fold_val, y_pred, average='weighted', labels=np.unique(y))
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'Fold {fold + 1}:')
    print('Точность:', acc)
    print('F1-мера:', f1)

mean_acc = np.mean(acc_scores)
mean_f1 = np.mean(f1_scores)

print('\nСредняя точность:', mean_acc)
print('Средняя F1-мера:', mean_f1)
num_samples = 100
start_time = time()
for _ in range(num_samples):
    ldaModel.predict(X_test.iloc[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')

# Код реализации поиска гиперпараметров KNN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
acc_scores = []
f1_scores = []

for n_neighbors in range(2, 20):
    knnModel = KNeighborsClassifier(n_neighbors=n_neighbors)
    knnModel.fit(X_train, y_train)
    y_pred = knnModel.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted', labels=np.unique(y))
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'n_neighbors: {n_neighbors}')
    print('Точность:', acc)
    print('F1-мера:', f1)

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.plot(range(2, 20), acc_scores, marker='o')
plt.xlabel('n_neighbors')
plt.ylabel('Точность')
plt.title('Точность в зависимости от n_neighbors')
plt.subplot(1, 2, 2)
plt.plot(range(2, 20), f1_scores, marker='o')
plt.xlabel('n_neighbors')
plt.ylabel('F1-мера')
plt.title('F1-мера в зависимости от n_neighbors')
plt.tight_layout()
plt.show()


# Код реализации KNN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knnModel = KNeighborsClassifier(n_neighbors=3)
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
acc_scores = []
f1_scores = []

for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
    X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
    y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
    knnModel.fit(X_fold_train, y_fold_train)
    y_pred = knnModel.predict(X_fold_val)
    acc = accuracy_score(y_fold_val, y_pred)
    f1 = f1_score(y_fold_val, y_pred, average='weighted', labels=np.unique(y))
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'Fold {fold + 1}:')
    print('Точность:', acc)
    print('F1-мера:', f1)

mean_acc = np.mean(acc_scores)
mean_f1 = np.mean(f1_scores)
print('\nСредняя точность:', mean_acc)
print('Средняя F1-мера:', mean_f1)
num_samples = 100
start_time = time()
for _ in range(num_samples):
    knnModel.predict(X_test.iloc[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации поиска гиперпараметров Decision Trees

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
max_depths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
acc_scores = []

for max_depth in max_depths:
    dtModel = DecisionTreeClassifier(criterion='entropy', max_depth=max_depth, random_state=42)
    n_splits = 5
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    fold_acc_scores = []

    for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
        X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
        y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
        dtModel.fit(X_fold_train, y_fold_train)
        y_pred = dtModel.predict(X_fold_val)
        acc = accuracy_score(y_fold_val, y_pred)
        fold_acc_scores.append(acc)
        print(f'Fold {fold + 1} (max_depth={max_depth}):')
        print('Точность:', acc)

    mean_acc = np.mean(fold_acc_scores)
    acc_scores.append(mean_acc)
    print(f'\nСредняя точность (max_depth={max_depth}): {mean_acc}')

plt.figure(figsize=(10, 6))
plt.plot(max_depths, acc_scores, label='Точность', color='green', marker='o')
plt.xlabel('max_depth')
plt.ylabel('Точность')
plt.title('Точность в зависимости от max_depth')
plt.legend()
plt.show()


# Код реализации Decision Trees

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from time import time

data = pd.read_csv('cvv_normalized_33_2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dtModel = DecisionTreeClassifier(criterion='entropy', max_depth=21, random_state=42)
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
acc_scores = []
f1_scores = []

for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
    X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
    y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
    dtModel.fit(X_fold_train, y_fold_train)
    y_pred = dtModel.predict(X_fold_val)
    acc = accuracy_score(y_fold_val, y_pred)
    f1 = f1_score(y_fold_val, y_pred, average='weighted', labels=np.unique(y))
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'Fold {fold + 1}:')
    print('Точность:', acc)
    print('F1-мера:', f1)

mean_acc = np.mean(acc_scores)
mean_f1 = np.mean(f1_scores)
print('\nСредняя точность:', mean_acc)
print('Средняя F1-мера:', mean_f1)
num_samples = 100
start_time = time()
for _ in range(num_samples):
    dtModel.predict(X_test.iloc[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации поиска гиперпараметров XGBoost

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import accuracy_score, f1_score
import xgboost as xgb

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
xgbModel = xgb.XGBClassifier(random_state=42)
param_dist = {
    'max_depth': [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
    'learning_rate': np.logspace(-3, 0, 10),
    'subsample': np.linspace(0.1, 1, 10),
    'colsample_bytree': np.linspace(0.1, 1, 10),
    'n_estimators': [50, 100, 150, 200, 250, 300]
}
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

random_search = RandomizedSearchCV(
    estimator=xgbModel,
    param_distributions=param_dist,
    n_iter=50,
    cv=cv,
    verbose=2,
    random_state=42,
    scoring='f1_weighted',
    refit=True
)

random_search.fit(X_train, y_train)

print('Лучшие гиперпараметры:', random_search.best_params_)
y_pred = random_search.predict(X_test)
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted', labels=np.unique(y))
print('Точность:', acc)
print('F1-мера:', f1)


# Код реализации XGBoost

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
import xgboost as xgb
from sklearn.metrics import accuracy_score, f1_score
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
xgbModel = xgb.XGBClassifier(max_depth=5, subsample=1, n_estimators=300, learning_rate=0.21544346900318823, colsample_bytree=1, random_state=42)
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
acc_scores = []
f1_scores = []

for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
    X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
    y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
    xgbModel.fit(X_fold_train, y_fold_train)
    y_pred = xgbModel.predict(X_fold_val)
    acc = accuracy_score(y_fold_val, y_pred)
    f1 = f1_score(y_fold_val, y_pred, average='weighted', labels=np.unique(y))
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'Fold {fold + 1}:')
    print('Точность:', acc)
    print('F1-мера:', f1)

mean_acc = np.mean(acc_scores)
mean_f1 = np.mean(f1_scores)
print('\nСредняя точность:', mean_acc)
print('Средняя F1-мера:', mean_f1)
num_samples = 100
start_time = time()
for _ in range(num_samples):
    xgbModel.predict(X_test.iloc[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации поиска гиперпараметров Random Forest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
n_estimators_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
mean_acc_scores = []
mean_f1_scores = []
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

for n_estimators in n_estimators_values:
    acc_scores = []
    f1_scores = []
    rfModel = RandomForestClassifier(n_estimators=n_estimators, criterion='entropy', max_depth=21, random_state=42)

    for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
        X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
        y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
        rfModel.fit(X_fold_train, y_fold_train)
        y_pred = rfModel.predict(X_fold_val)
        acc = accuracy_score(y_fold_val, y_pred)
        f1 = f1_score(y_fold_val, y_pred, average='weighted', labels=np.unique(y))
        acc_scores.append(acc)
        f1_scores.append(f1)

    mean_acc_scores.append(np.mean(acc_scores))
    mean_f1_scores.append(np.mean(f1_scores))

plt.figure(figsize=(12, 6))
plt.plot(n_estimators_values, mean_acc_scores, label='Точность', marker='o')
plt.plot(n_estimators_values, mean_f1_scores, label='F1-мера', marker='o')
plt.xlabel('Количество деревьев (n_estimators)')
plt.ylabel('Значение метрики')
plt.legend()
plt.title('Зависимость точности и F1-меры от количества деревьев')
plt.show()


# Код реализации Random Forest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
RandomForestModel = RandomForestClassifier(n_estimators=120, criterion='entropy', max_depth=21, random_state=42)
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
acc_scores = []
f1_scores = []

for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train)):
    X_fold_train, X_fold_val = X_train.iloc[train_index], X_train.iloc[val_index]
    y_fold_train, y_fold_val = y_train.iloc[train_index], y_train.iloc[val_index]
    RandomForestModel.fit(X_fold_train, y_fold_train)
    y_pred = RandomForestModel.predict(X_fold_val)
    acc = accuracy_score(y_fold_val, y_pred)
    f1 = f1_score(y_fold_val, y_pred, average='weighted', labels=np.unique(y))
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'Fold {fold + 1}:')
    print('Точность:', acc)
    print('F1-мера:', f1)

mean_acc = np.mean(acc_scores)
mean_f1 = np.mean(f1_scores)
print('\nСредняя точность:', mean_acc)
print('Средняя F1-мера:', mean_f1)
num_samples = 100
start_time = time()
for _ in range(num_samples):
    RandomForestModel.predict(X_test.iloc[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации поиска гиперпараметров CNN

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, ParameterGrid
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1).values
y = data['ProtocolName']
le = LabelEncoder()
y = le.fit_transform(y)
y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X_train[..., np.newaxis]
X_test = X_test[..., np.newaxis]

def create_model(filters, kernel_size, dense_units, learning_rate):
    model = Sequential([
        Conv1D(filters, kernel_size=kernel_size, activation='relu', input_shape=(X_train.shape[1], 1)),
        MaxPooling1D(pool_size=2),
        Conv1D(filters * 2, kernel_size=kernel_size, activation='relu'),
        MaxPooling1D(pool_size=2),
        Flatten(),
        Dense(dense_units, activation='relu'),
        Dense(y_train.shape[1], activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
param_grid = {
    'filters': [16, 32, 64],
    'kernel_size': [2, 3, 4],
    'dense_units': [50, 100, 150],
    'batch_size': [16, 32, 64],
    'epochs': [10, 20, 30],
    'learning_rate': [0.001, 0.01]
}
best_params = None
best_acc = 0
best_f1 = 0

for params in ParameterGrid(param_grid):
    acc_scores = []
    f1_scores = []

    for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train.argmax(1))):
        X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
        y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]
        model = create_model(filters=params['filters'], kernel_size=params['kernel_size'],
                             dense_units=params['dense_units'], learning_rate=params['learning_rate'])
        model.fit(X_fold_train, y_fold_train, epochs=params['epochs'], batch_size=16, verbose=0)
        y_pred = model.predict(X_fold_val)
        y_pred_classes = y_pred.argmax(axis=1)
        y_fold_val_classes = y_fold_val.argmax(axis=1)
        acc = accuracy_score(y_fold_val_classes, y_pred_classes)
        f1 = f1_score(y_fold_val_classes, y_pred_classes, average='weighted')
        acc_scores.append(acc)
        f1_scores.append(f1)

    mean_acc = np.mean(acc_scores)
    mean_f1 = np.mean(f1_scores)
    if mean_acc > best_acc:
        best_acc = mean_acc
        best_f1 = mean_f1
        best_params = params
    print(f'Параметры: {params}')
    print('Средняя точность:', mean_acc)
    print('Средняя F1-мера:', mean_f1)

print(f'\nЛучшие параметры: {best_params}')
print('Лучшая средняя точность:', best_acc)
print('Лучшая средняя F1-мера:', best_f1)


# Код реализации CNN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1).values
y = data['ProtocolName']
le = LabelEncoder()
y = le.fit_transform(y)
y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X_train[..., np.newaxis]
X_test = X_test[..., np.newaxis]

def create_model(filters, kernel_size, dense_units, learning_rate):
    model = Sequential([
        Conv1D(filters, kernel_size=kernel_size, activation='relu', input_shape=(X_train.shape[1], 1)),
        MaxPooling1D(pool_size=2),
        Conv1D(filters * 2, kernel_size=kernel_size, activation='relu'),
        MaxPooling1D(pool_size=2),
        Flatten(),
        Dense(dense_units, activation='relu'),
        Dense(y_train.shape[1], activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
model = create_model(filters=64, kernel_size=3,
                     dense_units=150, learning_rate=0.001)
model.fit(X_train, y_train, epochs=30, batch_size=16, verbose=0)
acc_scores = []
f1_scores = []

for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train.argmax(1))):
    X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
    y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]
    model.fit(X_fold_train, y_fold_train, epochs=30, batch_size=16, verbose=0)
    y_pred = model.predict(X_fold_val)
    y_pred_classes = y_pred.argmax(axis=1)
    y_fold_val_classes = y_fold_val.argmax(axis=1)
    acc = accuracy_score(y_fold_val_classes, y_pred_classes)
    f1 = f1_score(y_fold_val_classes, y_pred_classes, average='weighted')
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f'Fold {fold + 1}:')
    print('Точность:', acc)
    print('F1-мера:', f1)

mean_acc = np.mean(acc_scores)
mean_f1 = np.mean(f1_scores)
print('\nСредняя точность:', mean_acc)
print('Средняя F1-мера:', mean_f1)
num_samples = 100
start_time = time()
for _ in range(num_samples):
    model.predict(X_test[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации поиска гиперпараметров RNN

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, ParameterGrid
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM, GRU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1).values
y = data['ProtocolName']
le = LabelEncoder()
y = le.fit_transform(y)
y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)


def create_model(units, learning_rate, rnn_type):
    model = Sequential()
    if rnn_type == 'SimpleRNN':
        model.add(SimpleRNN(units, activation='relu', input_shape=(X_train.shape[1], 1)))
    elif rnn_type == 'LSTM':
        model.add(LSTM(units, activation='relu', input_shape=(X_train.shape[1], 1)))
    elif rnn_type == 'GRU':
        model.add(GRU(units, activation='relu', input_shape=(X_train.shape[1], 1)))
    model.add(Dense(y_train.shape[1], activation='softmax'))
    model.compile(optimizer=Adam(learning_rate=learning_rate), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
param_grid = {
    'units': [50, 75, 100, 125],
    'learning_rate': [0.001, 0.005, 0.01],
    'rnn_type': ['SimpleRNN', 'LSTM', 'GRU'],
    'epochs': [20, 30, 40, 50],
    'batch_size': [16, 32, 64]
}
best_params = None
best_acc = 0
best_f1 = 0

for params in ParameterGrid(param_grid):
    acc_scores = []
    f1_scores = []

    for fold, (train_index, val_index) in enumerate(cv.split(X_train, y_train.argmax(1))):
        X_fold_train, X_fold_val = X_train[train_index], X_train[val_index]
        y_fold_train, y_fold_val = y_train[train_index], y_train[val_index]
        model = create_model(units=params['units'], learning_rate=params['learning_rate'], rnn_type=params['rnn_type'])
        model.fit(X_fold_train, y_fold_train, epochs=params['epochs'], batch_size=params['batch_size'], verbose=0)
        y_pred = model.predict(X_fold_val)
        y_pred_classes = y_pred.argmax(axis=1)
        y_fold_val_classes = y_fold_val.argmax(axis=1)
        acc = accuracy_score(y_fold_val_classes, y_pred_classes)
        f1 = f1_score(y_fold_val_classes, y_pred_classes, average='weighted')
        acc_scores.append(acc)
        f1_scores.append(f1)

    mean_acc = np.mean(acc_scores)
    mean_f1 = np.mean(f1_scores)
    if mean_acc > best_acc:
        best_acc = mean_acc
        best_f1 = mean_f1
        best_params = params
    print(f'Параметры: {params}')
    print('Средняя точность:', mean_acc)
    print('Средняя F1-мера:', mean_f1)

print(f'\nЛучшие параметры: {best_params}')
print('Лучшая средняя точность:', best_acc)
print('Лучшая средняя F1-мера:', best_f1)


# Код реализации RNN

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GRU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from time import time
import matplotlib.pyplot as plt

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1).values
y = data['ProtocolName']
le = LabelEncoder()
y = le.fit_transform(y)
y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)
model = Sequential()
model.add(GRU(75, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(Dense(y_train.shape[1], activation='softmax'))
model.compile(optimizer=Adam(learning_rate=0.005), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=30, batch_size=16, verbose=0)
y_test_pred = model.predict(X_test)
y_test_pred_classes = y_test_pred.argmax(axis=1)
y_test_classes = y_test.argmax(axis=1)
test_acc = accuracy_score(y_test_classes, y_test_pred_classes)
test_f1 = f1_score(y_test_classes, y_test_pred_classes, average='weighted')
print(f'Точность на тестовых данных: {test_acc}')
print(f'F1-мера на тестовых данных: {test_f1}')
num_samples = 100
start_time = time()
for _ in range(num_samples):
    model.predict(X_test[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации поиска гиперпараметров DNN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from scikeras.wrappers import KerasClassifier
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
le = LabelEncoder()
y = le.fit_transform(y)
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def create_dnn_model(units1, units2, units3, learning_rate):
    model = Sequential()
    model.add(Dense(units1, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(units2, activation='relu'))
    model.add(Dense(units3, activation='relu'))
    model.add(Dense(len(np.unique(y_train)), activation='softmax'))
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

model = KerasClassifier(model=create_dnn_model, verbose=0)
param_grid = {
    'model__units1': [64, 128],
    'model__units2': [32, 64, 128],
    'model__units3': [16, 32, 64],
    'batch_size': [16, 32, 64],
    'epochs': [20, 22, 25, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
    'model__learning_rate': [0.001, 0.01]
}

grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42))
grid_result = grid.fit(X_train, y_train)
print(f'Лучшие параметры: {grid_result.best_params_}')
print(f'Лучшая точность: {grid_result.best_score_}')
best_model = grid_result.best_estimator_
y_test_pred = best_model.predict(X_test)
test_acc = accuracy_score(y_test, y_test_pred)
test_f1 = f1_score(y_test, y_test_pred, average='weighted')
print(f'Точность на тестовых данных: {test_acc}')
print(f'F1-мера на тестовых данных: {test_f1}')


# Код реализации DNN

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import warnings
from time import time
warnings.filterwarnings('ignore')

data = pd.read_csv('cvv_normalized_33_2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(np.unique(y_train)), activation='softmax'))
optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=40, batch_size=32, verbose=0)
y_test_pred = model.predict(X_test)
y_test_pred_classes = np.argmax(y_test_pred, axis=1)
test_acc = accuracy_score(y_test, y_test_pred_classes)
test_f1 = f1_score(y_test, y_test_pred_classes, average='weighted')
print(f'Точность на тестовых данных: {test_acc}')
print(f'F1-мера на тестовых данных: {test_f1}')
num_samples = 100
start_time = time()
for _ in range(num_samples):
    model.predict(X_test[:1])
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} сек')


# Код реализации Transformers

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
import tensorflow as tf
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=len(np.unique(y)))


def tokenize_data(X, y, tokenizer):
    texts = X.astype(str).apply(lambda row: ' '.join(row.values), axis=1).tolist()
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=128, return_tensors='tf')
    dataset = tf.data.Dataset.from_tensor_slices((
        {
            'input_ids': encodings['input_ids'],
            'attention_mask': encodings['attention_mask']
        },
        y
    ))
    return dataset

train_dataset = tokenize_data(X_train, y_train, tokenizer).shuffle(len(X_train)).batch(16)
test_dataset = tokenize_data(X_test, y_test, tokenizer).batch(16)
optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer=optimizer,
              loss=loss_fn,
              metrics=['accuracy'])
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6)
model.fit(train_dataset,
          epochs=20,
          validation_data=test_dataset,
          callbacks=[reduce_lr],
          batch_size=32)
y_pred = np.argmax(model.predict(test_dataset).logits, axis=1)
acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
num_samples = 100
start_time = time()
for _ in range(num_samples):
    _ = model.predict(test_dataset.take(1)).logits
end_time = time()
mean_pred_time = (end_time - start_time) / num_samples
print(f'Точность на тестовых данных: {acc}')
print(f'F1-мера на тестовых данных: {f1}')
print(f'Среднее время выполнения одного предсказания: {mean_pred_time:.6f} секунд')


# Код реализации ансамбля моделей

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import xgboost as xgb
from sklearn.tree import DecisionTreeClassifier
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from time import time

data = pd.read_csv('cvv_normalized_an2.csv')
X = data.drop('ProtocolName', axis=1)
y = data['ProtocolName']
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
xgbModel = xgb.XGBClassifier(max_depth=5, subsample=1, n_estimators=300, learning_rate=0.21544346900318823, colsample_bytree=1, random_state=42)
xgbModel.fit(X_train, y_train)
y_pred_xgb = xgbModel.predict(X_test)

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=len(np.unique(y)))

def tokenize_data(X, y, tokenizer, max_length=128):
    texts = X.astype(str).apply(lambda row: ' '.join(row.values), axis=1).tolist()
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=max_length, return_tensors='tf')
    dataset = tf.data.Dataset.from_tensor_slices((
        {
            'input_ids': encodings['input_ids'],
            'attention_mask': encodings['attention_mask']
        },
        y
    ))
    return dataset

train_dataset = tokenize_data(X_train, y_train, tokenizer).shuffle(len(X_train)).batch(16)
test_dataset = tokenize_data(X_test, y_test, tokenizer).batch(16)
optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer=optimizer, loss=loss_fn, metrics=['accuracy'])
model.fit(train_dataset, epochs=20, validation_data=test_dataset, callbacks=[tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6)], batch_size=32)
y_pred_bert = np.argmax(model.predict(test_dataset).logits, axis=1)


dtModel = DecisionTreeClassifier(criterion='entropy', max_depth=21, random_state=42)
dtModel.fit(X_train, y_train)
y_pred_dt = dtModel.predict(X_test)


from scipy.stats import mode
predictions = np.vstack((y_pred_xgb, y_pred_bert, y_pred_dt)).T
start_time = time()
y_pred_ensemble = mode(predictions, axis=1).mode.flatten()
end_time = time()
acc_ensemble = accuracy_score(y_test, y_pred_ensemble)
f1_ensemble = f1_score(y_test, y_pred_ensemble, average='weighted')
print(f'Точность ансамбля на тестовых данных: {acc_ensemble}')
print(f'F1-мера ансамбля на тестовых данных: {f1_ensemble}')
print(f'Время предсказания ансамбля: {end_time - start_time:.6f} секунд')
