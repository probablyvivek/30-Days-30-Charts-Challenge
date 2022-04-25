from curses.ascii import HT
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

os.getcwd()

os.chdir('/Users/vivektiwari/Code and Viz/Python/30 Days/')

df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
df.head()

#remove rows with NaN values
df = df.dropna()

#divide dt column into year and month
df['dt'] = pd.to_datetime(df['dt'])
df['Year'] = df['dt'].dt.year

df_india = df[df['Country'] == 'India']

df_india.head()

#remove the dt column
df_india = df_india.drop(columns=['dt'])
df_india = df_india.drop(columns=['AverageTemperatureUncertainty'])

df_india_group = df_india.groupby('Year').mean()
df_india_group.head()

#Animation line plot

fig, ax = plt.subplots(figsize=(15,7))
plt.style.use('ggplot')

#title and labels
plt.title('Average Temperature in India', fontsize=25)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Average Temperature (°C)', fontsize=20)


def animate(i):
    data = df_india_group.iloc[:int(i+1)] #select data range
    p = sns.lineplot(x=data.index, y=data['AverageTemperature'], ax=ax)
    p.tick_params(labelsize=17)
    plt.setp(p.lines,linewidth=7)
    
ani = FuncAnimation(fig, animate, frames=300, repeat=True)
ani.save('animation2.gif', writer='imagemagick', fps=20)

HTML(ani.to_jshtml())
