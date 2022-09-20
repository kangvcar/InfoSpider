import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging.handlers
import logging.config
from sklearn.preprocessing import MinMaxScaler
from model import LSTM

def read_data():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data = data.reset_index(drop=True)
    data = data.drop(['date'], axis=1)
    data = data.astype('float32')
    return data


def normalize_data(data):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    data['close'] = scaler.fit_transform(data['close'].values.reshape(-1, 1))
    return data, scaler


def create_train_data(data, seq_len):
    x_train = []
    y_train = []

    for i in range(seq_len, len(data)):
        x_train.append(data[i-seq_len:i, 0])
        y_train.append(data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    return x_train, y_train


def create_test_data(data, seq_len):
    x_test = []
    y_test = data[seq_len:, :]
    for i in range(seq_len, len(data)):
        x_test.append(data[i-seq_len:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    return x_test, y_test


def train_model(x_train, y_train, x_test, y_test):
    model = LSTM()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    epochs = 10
    for epoch in range(epochs):
        inputs = torch.from_numpy(x_train).float()
        labels = torch.from_numpy(y_train).float()
        optimizer.zero_grad()
        model.hidden = model.init_hidden()
        y_pred = model(inputs)
        loss = criterion(y_pred, labels)
        loss.backward()
        optimizer.step()
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, epochs, loss.item()))
    return model


def predict(model, x_test, y_test, scaler):
    inputs = torch.from_numpy(x_test).float()
    y_pred = model(inputs)
    y_pred = y_pred.detach().numpy()
    y_test = y_test.reshape(-1, 1)
    y_pred = scaler.inverse_transform(y_pred)
    y_test = scaler.inverse_transform(y_test)
    return y_pred, y_test


def evaluate_model(y_pred, y_test):
    rmse = np.sqrt(np.mean(((y_pred - y_test) ** 2)))
    print('RMSE: ', rmse)
    plt.plot(y_test, color='red', label='Real Stock Price')
    plt.plot(y_pred, color='blue', label='Predicted Stock Price')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    data = read_data()
    data, scaler = normalize_data(data)
    seq_len = 60
    x_train, y_train = create_train_data(data, seq_len)
    x_test, y_test = create_test_data(data, seq_len)
    model = train_model(x_train, y_train, x_test, y_test)
    y_pred, y_test = predict(model, x_test, y_test, scaler)
    evaluate_model(y_pred, y_test)