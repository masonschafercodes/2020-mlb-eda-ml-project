import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def explain():
    print('Supported functions are:')
    print('diverging_bars')
    print('dendrogram')
    print('corr_map')
    print('pair_plot')
    print('boxPlot')
    print('To see deploy examples of each function, enter "_demo" after function name')
    print('To demonstrate, run diverging_bars_demo and follow the prompts')
    print('After the chart renders there is a y/n prompt to save it as a .png')
    print('Be sure to select an option or it may appear that you have a stuck kernel')

def save_yn(plt):
    save_yn = input('Would you like to save this visualization? y/n ')
    if save_yn=='y':
        save_name = input('Enter save file name: ')
        plt.savefig(save_name)

# This function creates a diverging bar set based on a dataframe and two column names
# There are some inputs for x/y labels and chart title
# After the chart is rendered, there is a function call to save the plot y/n
# It can be kind of hard to spot under the chart, but if you come up with a visualization that you like,
# save it out and we can add it to the presentation
# There is an additional prompt if save_yn = y to select a file name

def diverging_bars(df,x_col,y_col):
    import pandas as pd
    import matplotlib.pyplot as plt
    x = df.loc[:, [x_col]]
    df[x_col+'_z'] = (x - x.mean())/x.std()
    df['colors'] = ['red' if x < 0 else 'green' for x in df[x_col+'_z']]
    df.sort_values(x_col, inplace=True)
    df.reset_index(inplace=True)

    # Draw plot
    plt.figure(figsize=(14,10), dpi= 80)
    plt.hlines(y=df.index, xmin=0, xmax=df[x_col+'_z'], color=df.colors, alpha=0.4, linewidth=5)

    y_label = input('Enter y label text')
    x_label = input('Enter x label text')
    title_text = input('Enter chart title')
    
    # Decorations
    plt.gca().set(ylabel=y_label, xlabel=x_label)
    plt.yticks(df.index, df[y_col], fontsize=12)
    plt.title(title_text, fontdict={'size':20})
    plt.grid(linestyle='--', alpha=0.5)
    plt.show()
    
    save_yn(plt)

def diverging_bars_demo():
    import pandas as pd
    import matplotlib.pyplot as plt
    print('Sample dataFrame:')
    print('df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv"')
    print('Deployed function:')
    print('diverging_bars(df,"'"mpg"'","'"carname"'")')
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
    df.head()
    diverging_bars(df,'mpg','carname')

# This function creates a dendrogram based on at least 2 linkages (df columns)
def dendrogram(df,linkage_1,linkage_2,x_label,run=True, linkage_3='', linkage_4=''):
    import pandas as pd
    import matplotlib.pyplot as plt
    while run == True:
        if linkage_3 == '':
            print('4 locals detected')
            dend_df=df[[linkage_1,linkage_2]]
        elif linkage_4 == '':
            print('5 locals detected')
            dend_df=df[[linkage_1,linkage_2,linkage_3]]
        elif linkage_4 != '':
            print('6 locals detected')
            dend_df=df[[linkage_1,linkage_2,linkage_3,linkage_4]]
        else: 
            print('non-standard number of arguments passed, function expects df name and up to 4 linkages')
            print('this function received '+ str(my_len-1)+'arguments')
            run = False

        import scipy.cluster.hierarchy as shc
        title = input('Chart title: ')

        # Plot
        plt.figure(figsize=(16, 10), dpi= 80)  
        plt.title(title, fontsize=22)  
        dend = shc.dendrogram(shc.linkage(dend_df, method='ward'), labels=df[x_label].values, color_threshold=100)  
        plt.xticks(fontsize=12)
        plt.show()
        save_yn(plt)
        run = False

def dendrogram_demo():
    print('Sample dataFrame:')
    print('df = pd.read_csv("'"https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv"'"")')
    print('Deployed function:')
    print('dendrogram(df,"'"Murder"'"","'"Assault"'","'"State"'",linkage_3="'"UrbanPop"'")')
    
    # Import Data
    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv')
    
    dendrogram(df,'Murder','Assault','State',linkage_3='UrbanPop')

# Careful with this one, it runs a comparison of every col in a df against every other col
# and groups on a dimension column passed in the function argument as a string
def pair_plot(df,measure_col):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(10,8), dpi= 80)
    sns.pairplot(df, kind="scatter", hue=measure_col, plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    plt.show()
    save_yn(plt)

def pair_plot_demo():
    import matplotlib.pyplot as plt
    import seaborn as sns
    print('Sample dataFrame:')
    print('df = sns.load_dataset("'"iris"'")')
    print('Deployed function:')
    print('pair_plot(df,"'"species"'")')
    print('This function impacts an entire dataframe, it may take some time to run')
    df = sns.load_dataset('iris')
    pair_plot(df,'species')

def corr_map(df):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Plot
    plt.figure(figsize=(12,10), dpi= 80)
    sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)

    title = input('Enter title: ')
    
    # Decorations
    plt.title(title, fontsize=22)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()
    save_yn(plt)

def corr_map_demo():
    print('Sample dataFrame: ')
    print('df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")')
    print('Deployed function:')
    print('corr_map(df)')
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
    corr_map(df)

def boxPlot(df,x_col,y_col,color_col):
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Draw Plot
    plt.figure(figsize=(13,10), dpi= 80)
    sns.boxplot(x=x_col, y=y_col, data=df, hue=color_col)
    sns.stripplot(x=x_col, y=y_col, data=df, color='black', size=3, jitter=1)

    for i in range(len(df[x_col].unique())-1):
        plt.vlines(i+.5, 10, 45, linestyles='solid', colors='gray', alpha=0.2)
    
    title_text = input('Enter chart title: ')
    legend_text = input('Enter legend title: ')
    
    # Decoration
    plt.title(title_text, fontsize=22)
    plt.legend(title=legend_text)
    plt.show()
    save_yn(plt)

def boxPlot(df,x_col,y_col,color_col):
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Draw Plot
    plt.figure(figsize=(13,10), dpi= 80)
    sns.boxplot(x=x_col, y=y_col, data=df, hue=color_col)
    sns.stripplot(x=x_col, y=y_col, data=df, color='black', size=3, jitter=1)

    for i in range(len(df[x_col].unique())-1):
        plt.vlines(i+.5, 10, 45, linestyles='solid', colors='gray', alpha=0.2)
    
    title_text = input('Enter chart title: ')
    legend_text = input('Enter legend title: ')
    
    # Decoration
    plt.title(title_text, fontsize=22)
    plt.legend(title=legend_text)
    plt.show()
    save_yn(plt)

def boxPlot_demo():
    import pandas as pd
    print('Sample dataFrame: ')
    print('df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")')
    print('Deployed function: ')
    print('boxPlot(df,"'"class"'","'"hwy"'"","'"cyl"'"")')
    print('Use Number of cylinders for the legend: value, it will make the meaning of the chart clearer')
    df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
    boxPlot(df,'class','hwy','cyl')






