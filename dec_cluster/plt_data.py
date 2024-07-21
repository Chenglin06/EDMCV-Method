# coding=gbk
import pandas as pd
import matplotlib.pyplot as plt


#exit()
# ��ȡxlsx�ļ�
data = pd.read_excel('weight/train.xlsx')
# ��ȡ����
epochs = data['epoch'].values
loss = data['loss'].values
acc = data['acc'].values


#print(epochs)
#exit()

# ����һ���µ�figure
fig, ax1 = plt.subplots(figsize=(12, 8))

# ����loss
ax1.set_xlabel('epoch')
ax1.set_ylabel('loss', color='tab:red')
ax1.plot(epochs, loss, color='tab:red', label='Loss')
ax1.tick_params(axis='y', labelcolor='tab:red')



# ʹ��˫y�����accuracy
ax2 = ax1.twinx()  # �����ڶ���y��
ax2.set_ylabel('acc', color='tab:blue')
ax2.plot(epochs, acc, color='tab:blue', label='Accuracy')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# ��ʾͼ��
plt.title("Loss and Accuracy vs. Epoch")
plt.savefig('Loss and Accuracy vs. Epoch.png',dpi = 600)
#plt.show()
