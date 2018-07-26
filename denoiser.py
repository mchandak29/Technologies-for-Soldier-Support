
import pywt
import numpy as np

def denoiser(original_signal):

	ca2,cd2,cd1 = pywt.wavedec(original_signal, 'db4', level=2)
	sigma1=np.std(cd1)
	th1 = sigma1 * np.sqrt( 2*np.log( len( cd1 ) ) )

	for i in range(len(cd1)):
		if cd1[i]<th1:
			cd1[i]=0

	sigma2=np.std(cd2)
	th2 = sigma2 * np.sqrt( 2*np.log( len( cd2 ) ) )

	for i in range(len(cd2)):
		if cd2[i]<th2:
			cd2[i]=0

	return np.array([ca2,cd2,cd1])


def denoisersig(original_signal):

	ca2,cd2,cd1 = pywt.wavedec(original_signal, 'db4', level=2)
	sigma1=np.std(cd1)
	th1 = sigma1 * np.sqrt( 2*np.log( len( cd1 ) ) )

	for i in range(len(cd1)):
		if cd1[i]<th1:
			cd1[i]=0

	sigma2=np.std(cd2)
	th2 = sigma2 * np.sqrt( 2*np.log( len( cd2 ) ) )

	for i in range(len(cd2)):
		if cd2[i]<th2:
			cd2[i]=0
			
	denoised_signal = pywt.waverec([ca2,cd2,cd1],'db4')

	return np.array(denoised_signal)