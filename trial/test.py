import index 

poverty_line=125
expenditure=[100,110,150,160]

head=index.calc_head(expenditure,poverty_line)

print("Head Count: ",head)

#To calculate Poverty Index
index.pov_index(expenditure,poverty_line)

#To calculate Squared Poverty Index
index.squared_pov_index(expenditure,poverty_line)

#To calculate Sen Index
index.sen_index(expenditure,poverty_line)

#To calculate Sen-Shorrocks-Thon index
index.sst_index(expenditure,poverty_line)

#To calculate Watts Index
index.watts_index(expenditure,poverty_line)

#To calculate Gini Coefficient
index.gini(expenditure)

#To draw Lorenz Curve
index.draw_lorenz(expenditure)