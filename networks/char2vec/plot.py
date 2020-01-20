import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_from_files(save_dir, logfiles, savefilename):
  dic = {}
  max_steps = 0
  max_steps_len = 0
  for logfile in logfiles:
    dic[logfile] = pd.read_csv(os.path.join(save_dir,logfile))
    if "steps_in_epoch" in dic[logfile].columns:
      ms = dic[logfile]["steps_in_epoch"].max()
      mc = len(dic[logfile]["steps_in_epoch"].unique())
      if ms > max_steps: max_steps = ms
      if mc > max_steps_len: max_steps_len = mc
  fig = plt.figure(figsize=(24, 16))
  ax = fig.add_subplot(211,title="loss and time")
  ax2 = ax.twinx()
  ax3 = fig.add_subplot(212,title="vocab correlation")
  mean_loss = []
  for df in dic.values():
    if "steps_in_epoch" in df.columns: df["epoch"] = df["epoch"]+df["steps_in_epoch"]/max_steps
    for elm in df:
      if elm in ["epoch", "steps_in_epoch"]: continue
      if "loss" in elm and len(df[elm])>0 : mean_loss.append(df[elm].mean())
      
      if elm == "time_per_sub_steps": ax2.plot(df["epoch"],df[elm]*max_steps_len,color=(0.5,0.5,0.5,0.2),label="time_per_sub_steps*max_step")
      elif elm == "time_per_epoch":   ax2.plot(df["epoch"],df[elm],color=(1,0,0,0.2), label=elm)
      elif "_to_" in elm: ax3.plot(df["epoch"],df[elm], label=elm)
      else: ax.plot(df["epoch"], df[elm], label=elm)
  h1, l1 = ax.get_legend_handles_labels()
  h2, l2 = ax2.get_legend_handles_labels()
  ax.legend(h1+h2, l1+l2, loc='upper right')
  ax.set_xlabel('epoch')
  ax.set_ylabel(r'loss')
  ax.set_ylim([0.0,2.5*sum(mean_loss)/len(mean_loss)])
  ax.grid(True)
  ax2.set_ylabel(r'time(s)')
  ax3.set_ylim([-1.5,1.5])
  ax3.set_xlabel('epoch')
  ax3.set_ylabel(r'correlation')
  h3, l3 = ax3.get_legend_handles_labels()
  ax3.legend(h3, l3, loc='upper right')
  fig.savefig(os.path.join(save_dir,savefilename))
  plt.close()