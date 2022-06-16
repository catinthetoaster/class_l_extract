import numpy as np
import matplotlib.pyplot as plt
import classy


cosmo = classy.Class()

cosmo.set({'output':'tCl,pM'})

cosmo.compute()

s,k,tau = cosmo.get_sources()
print(s.keys())
idx = 200
print(tau[idx],cosmo.get_current_derived_parameters(['tau_rec']))
plt.figure()
plt.title("Temperature hierarchy")
plt.plot(k,s['delta_g'][:,idx])
plt.plot(k,s['theta_g'][:,idx])
plt.plot(k,s['shear_g'][:,idx])
for i in range(3,13):
  plt.plot(k,s['mult_Tg_{}'.format(i)][:,idx])
plt.figure()
plt.title("Polarization hierarchy")
for i in range(11):
  plt.plot(k,s['mult_Pg_{}'.format(i)][:,idx])
plt.show()
