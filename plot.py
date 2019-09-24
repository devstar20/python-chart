import csv
import matplotlib.pyplot as plt
x = []
y = []
x2 = []
y2 = []
with open('M5-u-rms.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
with open('M5-u-rms-Morkovin.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        x2.append(float(row[0]))
        y2.append(float(row[1]))
# plt.text(1.25, 2.5, r'MD5.0:$\sqrt{\rho}u_{rms}/\sqrt{\rho_w}u_\tau$')
# plt.text(1.25, 2.2, r'MD5.0:$u_{rms}/u_\tau$')
plt.ylabel(r'$u_{rms}$')
plt.xlabel(r'z/$\delta$')
plt.plot(x, y, 'k', label=r'MD5.0:$\sqrt{\rho}u_{rms}/\sqrt{\rho_w}u_\tau$')
plt.plot(x2, y2,'k--' ,label=r'MD5.0:$u_{rms}/u_\tau$')
plt.legend()
plt.show()
