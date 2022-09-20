### 使用pytorch，创建一个LSTM模型
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_size=100, output_size=1):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size)
        self.linear = nn.Linear(hidden_size, output_size)
        self.hidden = self.init_hidden()

    def init_hidden(self):
        return (torch.zeros(1, 1, self.hidden_size),
                torch.zeros(1, 1, self.hidden_size))

    def forward(self, input):
        lstm_out, self.hidden = self.lstm(input.view(len(input), 1, -1), self.hidden)
        y_pred = self.linear(lstm_out.view(len(input), -1))
        return y_pred[-1]