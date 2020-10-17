import os
import pandas as pd
import matplotlib.pyplot as plt

#data folder
txt_list = os.listdir("Data/")

####
# check if we already ran this python file and sorted data
try:
    U = open("NordeaNordenfond.csv")
    print("Startup check: NordeaNordenfond.csv exists. Skipping data collection.")
    # file exists.
    U.close()
except IOError:
    print("Startup check: Data collection file missing. Generating data collection.... Saving to: NordeaNordenfond.csv")

    #import data
    nordeafond = pd.DataFrame()
    for txt in txt_list:
        index = txt.strip('.txt')
        file_dir = os.path.dirname(__file__)
        rel_path = "Data\\" + txt
        abs_path = os.path.join(file_dir,rel_path)
        df = pd.read_csv(abs_path, delimiter="\t", decimal=",", header=0, encoding="latin-1")
        select = df[df['Institutnr_fond'].astype(str).str.contains("51282", na=False)]
        select['Datum'] = index
        select.set_index('Datum',inplace=True)
        nordeafond = pd.concat([select, nordeafond], sort=False)
    nordeafond.to_csv('NordeaNordenfond.csv', encoding='utf-8', header=True)
    print("Data collection Done! File saved: NordeaNordenfond.csv")


####
# load data into dataframe
Nordeafond_df = pd.read_csv("NordeaNordenfond.csv")

# make a dataframe where we store results
result_df = pd.DataFrame(columns=['Kvartalsslut', 'Marknadsvarde_total','Marknadsvarde_svenska', 'Procent_svenska'])

for txt in txt_list:
    datum = txt.strip('.txt')
    # this textfile seems to be missing Nordea nordenfond, messy hack to ignore it
    if datum == '2014-06-30':
        continue

    kvartalsslut = Nordeafond_df['Kvartalsslut'].loc[(Nordeafond_df['Kvartalsslut'] == datum) & (Nordeafond_df['Datum'] == datum)]
    marknadsvarde_tot = Nordeafond_df['Marknadsvarde_tot'].loc[(Nordeafond_df['Kvartalsslut'] == datum) & (Nordeafond_df['Datum'] == datum)]
    svensk_marknadsvarde = Nordeafond_df['Marknadsvarde'].loc[(Nordeafond_df['Datum'] == datum) & (Nordeafond_df['Land'] == 'SE')].sum()

    try:
        kvartalsslut = kvartalsslut.iloc[0]
        marknadsvarde_tot = marknadsvarde_tot.iloc[0]
        procent_svenska = svensk_marknadsvarde / marknadsvarde_tot
        result = [kvartalsslut, marknadsvarde_tot, svensk_marknadsvarde, procent_svenska]
        result_df.loc[len(result_df)] = result
    except Exception as e:
        print("Error: ", e)

# plot data! :)
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(result_df['Kvartalsslut'],result_df['Marknadsvarde_total'], 'tab:purple')
ax2.plot(result_df['Kvartalsslut'], (result_df['Procent_svenska']*100), 'tab:green')

ax1.set_ylabel('Marknadsvärde', color='tab:purple')
ax2.set_ylabel('% of Swedish', color='tab:green')
fig.autofmt_xdate(rotation=60)

plt.show()