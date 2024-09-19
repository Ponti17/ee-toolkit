import numpy as np
import matplotlib.pyplot as plt



# initial variables for finite variables
"""
# load impedance
R_T = 50.0 # 0, infty, 40

# source impedance
R_s = 40.0

# source voltage
V_s = 5.0

# characteristic impedance
Z_0 = 50.0

# calculate steady state voltage
Vload = R_T / (R_s + R_T) * V_s

# reflection coeff.
rho_source = (R_s - Z_0)/(R_s + Z_0)
rho_load = (R_T - Z_0)/(R_T + Z_0)

# initial coltage
V_i = Z_0/(Z_0 + R_s) * V_s
"""

# initial variables for infinite variables
rho_source =-1.0/9.0
rho_load = 1
V_i = 50.0/(50.0+40.0)*5

print("rho_source: ", rho_source)
print("rho_load: ", rho_load)
print("V_i: ", V_i)

print("\nDoing calculations...\n")

deltas = []        # a, b, c, d ...
source_voltages = [] # A, B, C, D ...
load_voltages = [] # A', B', C', D' ...

iterations = 10

for i in range(iterations):

    if i > 0 and i % 2 == 0:
        # even iteration. We're on the source side.
        deltas.append(deltas[i-1]*rho_source)
    elif i > 0 and i % 2 == 1:
        # uneven iteration. We're on the load side.
        deltas.append(deltas[i-1]*rho_load)
    elif i == 0:
        # a = V_i
        deltas.append(V_i)

for i in range(len(deltas)):
    if i % 2 == 0:
        source_voltages.append(sum(deltas[:i+1]))
    else:
        load_voltages.append(sum(deltas[:i+1]))

print('source voltages', source_voltages)
print('load voltages', load_voltages)

print('\nMaking plots...')

fig, ax = plt.subplots(1,2)

len_source_plot = len(source_voltages)
len_load_plot = len(load_voltages)

source_plot_indices = np.linspace(start=0, stop=len_source_plot*2-2, num=len_source_plot)
load_plot_indices = np.linspace(start=1, stop=len_load_plot*2-1, num=len_load_plot)
print(load_plot_indices)
print(source_plot_indices)

ax[0].step(source_plot_indices, source_voltages, where='post')
ax[0].set_ylim(0, max(source_voltages)*1.1)
ax[0].set_xticks(source_plot_indices)
ax[0].set_xlabel('$t/t_d$')
ax[0].set_ylabel('Source Voltages (V)')

# Annotate source voltages
for x, y in zip(source_plot_indices[:-1], source_voltages[:-1]):
    ax[0].annotate(f'{round(y, 2)}', xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='left')


ax[1].step(load_plot_indices, load_voltages, where='post')
ax[1].set_ylim(0, max(load_voltages)*1.1)
ax[1].set_xticks(load_plot_indices)
ax[1].set_xlabel('$t/t_d$')
ax[1].set_ylabel('Load Voltage (V)')

# Annotate source voltages
for x, y in zip(load_plot_indices[:-1], load_voltages[:-1]):
    ax[1].annotate(f'{round(y, 2)}', xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='left')

fig.show()