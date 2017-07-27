# Nanopores
Debugging:

Pythion.py Load() Line 239 To be done: maybe it would be nice to add double choice button to make it possible to select only two values in:
outputsamplerate = np.float64(self.ui.outputsamplerateentry.text())*1000 #use integer multiples of 4166.67 ie 2083.33 or 1041.67 

Pythion.py Load() Line 265 Integer type for expression specified:  ds_sig = scipy.signal.resample(... int(expr))

Pythion.py getfile() Line 398 Mat file execution added:  QtGui.QFileDialog.getOpenFileName( filter="Amplifier Files( *.mat)") 


Pythion.py Baselinecalc() Line 564  if .dat file is downloaded no file processing involved (should be especially described to protect from bugs). It happens because: in Load file the data is written in variable self.out. While in Baselinecalc the data is downloaded from self.data variable. For .log file it works, for .dat not... To be fixed for me 

Pythion.py UpdateIV() Line 1032 Division by the zero encountered. Fixed now by adding: if self.ui.concentrationValue.value():

Usefulfunctions Plotsingle() Line 647 integer type specified: bins=int(expr) deleted line 648:   aphx = aphx 

UsefulFunctions.py AddInfoAfterRecursive() Lines 852 853 855 Integer type specification: deli[i] = (...   int(startpoints[i]+1):int(endpoints[i]-1)])) 


UsefulFunctions.py Lines 467 added: self.p1.clear() in order to avoid debug: If we load the data (.dat) and we click: show Channel 2 button and then Plot Both button. Everything works fine. But if we take away the check mark from plot both, the old graph is not removed. Now fixed.
