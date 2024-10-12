import seaborn as sns
import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np

def plot_stuff(xmeas, X_train_extracted_data, dtrg_scores, dt_scores, dj_scores, dt_theta, L):
    #Testing Plots and Subplots
    style.use('default')
    box = dict(facecolor='yellow', pad=3, alpha=0.2)
    fig = plt.figure(figsize=(10,7))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax1.set_xlim(0,5000)
    ax2.set_xlim(0,5000)
    # ax2.set_ylim(0,10)

    plt.subplots_adjust(hspace=0.3)

    xlables = list(range(0,5000,10)) # for both plots

    # Plotting signal reading
    xmeasx_1 = list(range(501))
    xmeasx_2 = list(range(501, 4001))
    xmeasx_3 = list(range(4001,len(xmeas)))
    ax1.plot(xmeasx_1, xmeas[:501] ,'b', label='Training') # Plot of Training Data
    ax1.plot(xmeasx_2, xmeas[501:4001] ,'k', label='Threshold calculation') # Plot of Threshold Determination Data
    ax1.plot(xmeasx_3, xmeas[4001:] ,'r', label='Detection') # Plot of Detection Phase
    ax1.plot(X_train_extracted_data, 'g', linewidth=1, label='Extracted Signal' )
    ax1.set_xticklabels(xlables)
    ax1.title.set_text('Direct Attack 1 Scenario')
    ax1.set_ylabel('Sensor Reading', bbox=box)
    ylim = list(ax1.get_ylim())
    ax1.vlines(4000,ylim[0],ylim[1],linestyles='dashed', colors='r')
    X = np.array([[4000,5000],[4000,5000]])
    Y = np.array([[ylim[0],ylim[0]],[ylim[1],ylim[1]]])
    C = np.array([[4000]])
    print(X.shape, Y.shape, C.shape)
    ax1.pcolormesh(X, Y, C, cmap='cool_r', alpha=0.2)
    ax1.legend(loc='best', ncol=4)

    # Plotting departure score
    dy = dtrg_scores
    dx = list(range(L,len(dy)+L))
    ax2.plot(dx, dy, 'c', label='Training phase')
    dy = dt_scores
    dx = list(range(500,len(dy)+500))
    ax2.plot(dx, dy, 'b', label='Threshold calculation')
    dy = dj_scores
    dx = list(range(4000,len(dy)+4000))
    ax2.plot(dx, dy, 'r', label='Detection Phase')
    ylim = list(ax2.get_ylim())
    ax2.vlines(4000,ylim[0],ylim[1],linestyles='dashed', colors='r')
    ax2.set_xticklabels(xlables)
    ax2.hlines(dt_theta,0,5000,linestyles='dashed', label='Alarm Threshold')
    ax2.set_xlabel('Time in hours', bbox=box)
    ax2.set_ylabel('Departure Score', bbox=box)

    X = np.array([[4000,5000],[4000,5000]])
    Y = np.array([[ylim[0],ylim[0]],[ylim[1],ylim[1]]])
    C = np.array([[4000]])
    ax2.pcolormesh(X, Y, C, cmap='cool_r', alpha=0.2)
    ax2.legend(loc='upper left')
    fig.align_ylabels([ax1,ax2])