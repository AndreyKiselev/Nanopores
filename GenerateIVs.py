import numpy as np
import scipy
import scipy.signal as sig
import UsefulFunctions as uf
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')

Tk().withdraw()
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')

filenames = ['/Volumes/backup/2017/Michael/Axopatch/20170512/10mMKClInFlowCellORingPore1mm.dat']
#filenames = ['/Volumes/backup/2017/Michael/Axopatch/20170512/bmimpf6lInFlowCellORingPore1mm.dat']
expname = 'ExpFitTests'

#filenames = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
for filename in filenames:
    print(filename)
    #Make Dir to save images
    output = uf.OpenFile(filename)
    directory = (str(os.path.split(filename)[0]) + os.sep + expname + '_SavedImages')
    if not os.path.exists(directory):
        os.makedirs(directory)

    AllData = uf.MakeIVData(output, delay = 2)
    if AllData == 0:
        print('!!!! No Sweep in: ' + filename)
        continue

    #Plot Considered Part
    #figExtracteParts = plt.figure(1)
    #ax1 = figExtracteParts.add_subplot(211)
    #ax2 = figExtracteParts.add_subplot(212, sharex=ax1)
    #(ax1, ax2) = uf.PlotExtractedPart(output, AllData, current = 'i1', unit=1e9, axis = ax1, axis2=ax2)
    #figExtracteParts.savefig(directory + os.sep + 'PlotExtracted_' + str(os.path.split(filename)[1])[:-4] + '.eps')
    #figExtracteParts.savefig(directory + os.sep + 'PlotExtracted_' + str(os.path.split(filename)[1])[:-4] + '.png', dpi=150)


    # Plot IV
    figIV = plt.figure(2)
    ax1IV = figIV.add_subplot(111)
    figIV2 = plt.figure(3)
    ax2IV = figIV2.add_subplot(111)
    ax1IV = uf.PlotIV(output, AllData, current = 'i1', unit=1e9, axis = ax1IV, WithFit = 1)
    ax2IV = uf.PlotIV(output, AllData, current = 'i2', unit=1e9, axis = ax2IV, WithFit = 1)
    figIV.tight_layout()
    figIV2.tight_layout()


#legend Format
box = ax1IV.get_position()
ax1IV.set_position([box.x0, box.y0 + box.height * 0.2,
                 box.width, box.height * 0.8])
ax1IV.legend(prop=fontP, loc='upper center', bbox_to_anchor=(0.45, -0.15),
          fancybox=True, shadow=True, ncol=2)
box = ax2IV.get_position()
ax2IV.set_position([box.x0, box.y0 + box.height * 0.2,
                 box.width, box.height * 0.8])
ax2IV.legend(prop=fontP, loc='upper center', bbox_to_anchor=(0.45, -0.15),
          fancybox=True, shadow=True, ncol=2)
#Save Figures
figIV.savefig(directory + os.sep + 'IVsi1.png', dpi=150)
figIV.savefig(directory + os.sep + 'IVsi1.eps')
figIV2.savefig(directory + os.sep + 'IVsi2.png', dpi=150)
figIV2.savefig(directory + os.sep + 'IVsi2.eps')

#plt.show()