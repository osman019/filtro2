import json 
import os 

MY_DATABASE = 'data'

def NewFile(*param):
     with open(MY_DATABASE,"w") as wf:
      json.dump(param[0],wf,indent=4)


def AddData(*param):
   data = list(param)
   with open(MY_DATABASE,"r+") as rwf:
      data_file=json.load(rwf)
      if (len(param) > 1):
         data_file[data[0]].update({data[1]:data[2]})
      else:
         data_file.update([param[0]])
      # data_file[llavePrincipal].update({codigo:info})
      rwf.seek(0)
      json.dump(data_file,rwf,indent=4)