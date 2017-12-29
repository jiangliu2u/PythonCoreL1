import matplotlib.pyplot as plt
import numpy as np
import wave

f = wave.open("gbqq.wav",'rb')


params=f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

str_data = f.readframes(nframes)
f.close()
wave_data = np.fromstring(str_data, dtype=np.short)
print(wave_data)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)


plt.subplot(211)
plt.plot(time, wave_data[0])
plt.subplot(212)
plt.plot(time, wave_data[1], c="g")
plt.xlabel("time (seconds)")
plt.show()