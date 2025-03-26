import pandas as pd
df = pd.read_csv('medical_examination.csv')
# overweight
df['overweight']=((df['weight']/(df['height']/100)**2)>25).astype(int)
# normalize data
df[['cholesterol','gluc']]=(df[['cholesterol','gluc']]>1).astype(int)
#draw_cat_plot
import seaborn as sns
def draw_cat_plot():
    df_cat = pd.melt(df,id_vars= ['cardio'], value_vars= ['cholesterol','gluc','smoke','alco','active','overweight'])
    fig=sns.catplot(data=df_cat, kind ='count', x='variable', col='cardio', hue='value')
    return fig
# draw_heat_map
def draw_heat_map():
    df_heat=[((df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)))]
    corr=df_heat.corr()
    mask=np.triu(corr)
    output=sns.heatmap(corr)
    return output

