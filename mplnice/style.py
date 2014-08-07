from matplotlib import rcParams
import matplotlib.pyplot as plt

rcParams['figure.figsize'] = (10,8)
#font
rcParams['font.sans-serif']=['Fira Sans OT']
rcParams['font.size'] = 15
rcParams['legend.fontsize'] = 'medium'
#tick label spacing and tick width
rcParams['xtick.major.pad'] = 4
rcParams['ytick.major.pad'] = 5
rcParams['xtick.major.width'] = 1
rcParams['ytick.major.width'] = 1
#legend style
rcParams['legend.frameon'] = False
rcParams['legend.numpoints'] = 3
rcParams['axes.color_cycle']=['#0EA16A', '#EF5915', "#e41a1c","#377eb8", "#984ea3"]

def myfig():
    fig = plt.figure()
    ax = fig.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    return fig, ax
