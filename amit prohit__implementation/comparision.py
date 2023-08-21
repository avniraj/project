import matplotlib.pyplot as plt
from pylab import *
figure()


t = [1,2,3,4,5,6,7]
tr1 = [61.02,58.89,56.67,55.72,49.123,62.250,98.93]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('UFAL/U','Basel./C','IIT-T./U','IIT-T./C','INSIG./C','SS-LDA','Proposed'))
xlabel('')
ylabel('F1-Score(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()




t = [1,2,3,4,5]
tr1 = [81.36,78.48,64.23,49.16, 98.9]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SS-LDA','Sentence-LDA','Biterm Topic Model','LDA','Proposed'))
xlabel('')
ylabel('Precision (%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
figure()


t = [1,2,3,4,5]
tr1 = [83.43,67.11,66.18,39.16, 98.7]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SS-LDA','Sentence-LDA','Biterm Topic Model','LDA','Proposed'))
xlabel('')
ylabel('Recall(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()

t = [1,2,3,4,5,6]
tr1 = [82.5,83,83.3,82,82.9,97]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('RFC','MNB','SVM-RBF','SVM-LK','SGD','Proposed'))
xlabel('')
ylabel('Accuracy(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4,5,6]
tr1 = [82.534,83.56,83.9,84,84.98,97.89]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('RFC','MNB','SVM-RBF','SVM-LK','SGD','Proposed'))
xlabel('')
ylabel('Sensitivity(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4,5,6]
tr1 = [80.5,81,83.3,86,88.9,97.56]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('RFC','MNB','SVM-RBF','SVM-LK','SGD','Proposed'))
xlabel('')
ylabel('Specificity(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4,5,6,7,8]
tr1 = [91,91.9,92,92.05,89.85,91.72,92.75,97]
tr2=[80.82,85.07,84.16,84.87,84.34,84.19,88.70,97.5]
tr3=[90.24,90.27,90.19,90.60,90.07,90.33,92.18,97]
tr4=[85.86,87.02,86.87,86.11,86.80,87.55,90.55,97.4]
plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='Airline Twitter Dataset',linewidth=2.0)
plot(t, tr2,marker='o', markerfacecolor='green', markersize=6,label='CD Dataset',linewidth=2.0)
plot(t, tr3,marker='o', markerfacecolor='red', markersize=6,label='App Dataset',linewidth=2.0)
plot(t, tr4,marker='o', markerfacecolor='yellow', markersize=6,label='Movie Dataset',linewidth=2.0)


xticks(t , ('SS-BED','HAN','ARC','CRNN','IWV','AC-BiLSTM','ABCDM','Proposed'))
xlabel('')
ylabel('Accuracy(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
legend()
show()
t = [1,2,3,4,5,6,7,8]
tr1 = [91.23,91.45,92.45,92.95,93.385,93.72,93.75,97.7]
tr2=[80.282,85.047,84.146,84.487,84.734,84.919,88.770,97.57]
tr3=[90.244,90.247,90.149,90.660,90.077,90.353,92.158,97.3]
tr4=[85.876,87.042,86.837,86.131,86.830,87.535,90.535,97.4]
plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='Airline Twitter Dataset',linewidth=2.0)
plot(t, tr2,marker='o', markerfacecolor='green', markersize=6,label='CD Dataset',linewidth=2.0)
plot(t, tr3,marker='o', markerfacecolor='red', markersize=6,label='App Dataset',linewidth=2.0)
plot(t, tr4,marker='o', markerfacecolor='yellow', markersize=6,label='Movie Dataset',linewidth=2.0)


xticks(t , ('SS-BED','HAN','ARC','CRNN','IWV','AC-BiLSTM','ABCDM','Proposed'))
xlabel('')
ylabel('Precision(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
legend()
show()
t = [1,2,3,4,5,6,7,8]
tr1 = [91.4,91.6,93.2,92.015,89.835,91.732,92.735,97.6]
tr2=[80.832,85.057,84.136,84.847,84.344,84.179,88.770,97.5]
tr3=[90.254,90.267,90.159,90.620,90.027,90.334,92.18,97]
tr4=[85.866,87.072,86.877,86.161,86.80,87.575,90.55,97.4]
plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='Airline Twitter Dataset',linewidth=2.0)
plot(t, tr2,marker='o', markerfacecolor='green', markersize=6,label='CD Dataset',linewidth=2.0)
plot(t, tr3,marker='o', markerfacecolor='red', markersize=6,label='App Dataset',linewidth=2.0)
plot(t, tr4,marker='o', markerfacecolor='yellow', markersize=6,label='Movie Dataset',linewidth=2.0)


xticks(t , ('SS-BED','HAN','ARC','CRNN','IWV','AC-BiLSTM','ABCDM','Proposed'))
xlabel('')
ylabel('Recall(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
legend()
show()
t = [1,2,3,4,5,6,7,8]
tr1 = [93,93.7,93,93.05,90.85,92.72,93.75,97]
tr2=[85.82,86.07,87.16,87.87,88.34,89.19,89.70,97.5]
tr3=[91.24,91.27,91.19,91.60,91.07,91.33,93.18,97.8]
tr4=[85.86,87.02,86.87,86.11,86.80,87.55,90.55,97.4]
plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='Airline Twitter Dataset',linewidth=2.0)
plot(t, tr2,marker='o', markerfacecolor='green', markersize=6,label='CD Dataset',linewidth=2.0)
plot(t, tr3,marker='o', markerfacecolor='red', markersize=6,label='App Dataset',linewidth=2.0)
plot(t, tr4,marker='o', markerfacecolor='yellow', markersize=6,label='Movie Dataset',linewidth=2.0)


xticks(t , ('SS-BED','HAN','ARC','CRNN','IWV','AC-BiLSTM','ABCDM','Proposed'))
xlabel('')
ylabel('F1-Score(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
legend()
show()
t = [1,2,3,4,5,6,7,8]
tr1 = [84,84.7,85,85.05,85.85,86.72,86.75,97.56]
tr2=[85.832,86.047,87.156,87.867,88.374,89.179,89.70,97.5]
tr3=[91.24,91.27,91.19,91.60,91.07,91.33,93.18,97.8]
tr4=[85.86,87.02,86.87,86.11,86.80,87.55,90.55,97.4]
plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='Airline Twitter Dataset',linewidth=2.0)
plot(t, tr2,marker='o', markerfacecolor='green', markersize=6,label='CD Dataset',linewidth=2.0)
plot(t, tr3,marker='o', markerfacecolor='red', markersize=6,label='App Dataset',linewidth=2.0)
plot(t, tr4,marker='o', markerfacecolor='yellow', markersize=6,label='Movie Dataset',linewidth=2.0)


xticks(t , ('SS-BED','HAN','ARC','CRNN','IWV','AC-BiLSTM','ABCDM','Proposed'))
xlabel('')
ylabel('Sensitivity(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
legend()
show()
t = [1,2,3,4,5,6,7,8]
tr1 = [93,90,93,93.05,90.85,92.72,93.75,97]
tr2=[85.82,86.07,87.16,87.87,88.34,89.19,89.70,97.5]
tr3=[86.24,86.27,86.69,86.60,87.07,87.33,88.18,97.8]
tr4=[87.86,87.902,88.87,88.911,88.80,88.55,90.535,97.4]
plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='Airline Twitter Dataset',linewidth=2.0)
plot(t, tr2,marker='o', markerfacecolor='green', markersize=6,label='CD Dataset',linewidth=2.0)
plot(t, tr3,marker='o', markerfacecolor='red', markersize=6,label='App Dataset',linewidth=2.0)
plot(t, tr4,marker='o', markerfacecolor='yellow', markersize=6,label='Movie Dataset',linewidth=2.0)


xticks(t , ('SS-BED','HAN','ARC','CRNN','IWV','AC-BiLSTM','ABCDM','Proposed'))
xlabel('')
ylabel('Specificity(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
legend()
show()
#Performance Analysis
t = [1,2,3,4,5,6,7,8,9,10]
tr1 = [97,97.5,97.8,97.96,98,98.3,98.6,98.5,98.56,98.93]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'))
xlabel('No.of Products',fontsize=13)
ylabel('F1-Score(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()

t = [1,2,3,4,5,6,7,8,9,10]
tr1 = [97.4,97.65,97.78,97.896,98.3,98.93,99.16,99.25,99.16,99.193]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'))
xlabel('No.of Products',fontsize=13)
ylabel('Accuracy(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4,5,6,7,8,9,10]
tr1 = [97.1,97.16,97.18,97.26,97.5,97.63,97.76,98.01,98.06,98.53]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'))
xlabel('No.of Products',fontsize=13)
ylabel('Precision(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()

t = [1,2,3,4,5,6,7,8,9,10]
tr1 = [97.2,97.25,97.28,97.36,97.47,97.53,97.6,97.85,97.96,97.99]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'))
xlabel('No.of Products',fontsize=13)
ylabel('Recall(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4,5,6,7,8,9,10]
tr1 = [97.45,97.54,97.82,97.962,98.1,98.32,98.61,98.53,98.546,98.93]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'))
xlabel('No.of Products',fontsize=13)
ylabel('Sensitivity(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4,5,6,7,8,9,10]
tr1 = [97.5,97.55,97.83,97.956,98.12,98.32,98.63,98.75,98.86,98.93]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('5000','10000','15000','20000','25000','30000','35000','40000','45000','50000'))
xlabel('No.of Products',fontsize=13)
ylabel('Specificity(%)',fontsize=13)
title('')
plt.xticks(rotation=45)
grid(True)
show()