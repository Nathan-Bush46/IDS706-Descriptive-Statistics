import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

def calculate():
    raw_training = pd.read_csv("/workspaces/IDS706-Descriptive-Statistics/src/main_workspace/data/hw1_q3_test_data.csv")
    df_train_x = raw_training.iloc[:, :-1]
    df_train_y = raw_training.iloc[:, -1]


    mean = ("mean\n",df_train_x[["stem-height","stem-width"]].mean())
    median= ("median\n",df_train_x[["stem-height","stem-width"]].median())
    std = ("std\n",df_train_x[["stem-height","stem-width"]].std())
    df_train_x.plot.scatter("stem-height", "stem-width")
    plt.savefig('src/main_workspace/outputs/scatter_plot.png')
    return [mean,median,std]

def print_to_pdf(stats):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    stat_print = ""

    pdf.cell(180, 10, txt="stem-height", align="C", border=1, ln=True)
    for i in range(len(stats)):
        
        stat_print = stats[i][0] + " " +str(stats[i][1]["stem-height"])
        pdf.cell(180, 10, txt=stat_print, align="C", border=1, ln=True)
    
    pdf.cell(180, 10, txt="", align="C", border=0, ln=True)
    pdf.cell(180, 10, txt="stem-width", align="C", border=1, ln=True)
    for i in range(len(stats)):
        
        stat_print = stats[i][0] + " " +str(stats[i][1]["stem-width"])
        pdf.cell(180, 10, txt=stat_print, align="C", border=1, ln=True)

    pdf.image("scatter_plot.png",w=100,type='PNG')
    #save the pdf with name .pdf
    pdf.output("src/main_workspace/outputs/example_stats.pdf")

if __name__ == '__main__':
    stats = calculate()
    print_to_pdf(stats)