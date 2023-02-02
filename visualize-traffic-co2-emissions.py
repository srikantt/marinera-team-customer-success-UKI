import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('./sample-traffic-history.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[10])
        y.append(row[8])
  
plt.bar(x, y, color = 'g', width = 0.72, label = "CO2 Prodution")
plt.xlabel('date')
plt.ylabel('co2-emission-rate')
plt.title('Traffic-Impact-on-Environment')
plt.legend()
plt.show()
