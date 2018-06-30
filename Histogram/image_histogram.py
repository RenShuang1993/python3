# -*- coding: UTF-8 -*-
import pandas as pd
import argparse
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
def get_number(color):
	lena_r = color[:,:,0].ravel()
	lena_g = color[:,:,1].ravel()
	lena_b = color[:,:,2].ravel()
	lena_gy = rgb2gray(color).ravel()
	histo_r = np.zeros(256,int)
	histo_g = np.zeros(256,int)
	histo_b = np.zeros(256,int)
	histo_gy = np.zeros(256,int)
	for r in lena_r:
		histo_r[r]+=1
	for g in lena_g:
		histo_g[g]+=1
	for b in lena_b:
		histo_b[b]+=1
	for gy in lena_gy:
		a = int(gy)
		histo_gy[a]+=1
	max_r = max(histo_r)
	max_g = max(histo_g)
	max_b = max(histo_b)
	max_gy = max(histo_gy)
	for i in range(256):
		histo_r[i]=((histo_r[i])/(max_r))*100
		histo_g[i]=((histo_g[i])/(max_g))*100
		histo_b[i]=((histo_b[i])/(max_b))*100
		histo_gy[i]=((histo_gy[i])/(max_gy))*100
	return histo_r,histo_g,histo_b,histo_gy
def main():
    # comand line
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT',help="input file name")
    parser.add_argument('-o','--output',help="out put filename")
    args = parser.parse_args()
    filename = args.INPUT
    try:
        lena = mpimg.imread(filename)
    except:
        print("please input correct filename！！！")
    y_r,y_g,y_b,y_gy = get_number(lena)
    x = np.arange(256)
    if args.output:
        dataframe = pd.DataFrame({'#red':y_r,'#green':y_g,'#blue':y_b,'#gray':y_gy,'Value':x})
        columns=['Value','#red','#green','#blue','#gray']
        dataframe.to_csv(args.output,index=True,sep=';',columns=columns,encoding="utf_8_sig")
    else:
        fig,(ax_r,ax_g,ax_b,ax_gy)= plt.subplots(4,sharex=True)
        ax_r.bar(x,y_r,color="red")
        ax_g.bar(x,y_g,color="green")
        ax_b.bar(x,y_b,color="blue")
        ax_gy.bar(x,y_gy,color="gray")
        fig.canvas.set_window_title("Histogram of "+filename)
        plt.show()
        
if __name__=='__main__':
    main()











	


