# Nanopores
Debugging:

Pythion.py UpdateIV Line 1032 avoid division by zero


Careful with meaning data setDownSampling setCliptoView! Pay attention

While getting file gtk-warning ** invalid input string QtGui.QFileDialog.getOpenFileName

Pythion.py Load() Line 227 No sense of the colors = np.array(self.sdf.color)for i in range(len(colors)):  colors[i] = pg.Color(colors[i])

outputsamplerate = np.float64(self.ui.outputsamplerateentry.text())*1000 #use integer multiples of 4166.67 ie 2083.33 or 1041.67 need to create multiple (triple) choice. what can be choosen?

Pythion.py getfile() Line 398 QtGui.QFileDialog.getOpenFileName( filter="Amplifier Files( *.mat)") mat file execution added

Usefulfunctions Plotsingle() Line 647 bins=int(expr) deleted line 648 aphx = aphx no sense
Usefulfunctions MakePSD() Line 414 we should be very carefull with log mode: fig.setLogMode(x=True, y=True) x and y are expressed in units this must be normalized

Pythion.py Load() Line 265 ds_sig = scipy.signal.resample(... int(expr)) integer specified
