from brian import *
'''
tau = 20 * msecond        # membrane time constant
Vt = -50 * mvolt          # spike threshold
Vr = -60 * mvolt          # reset value
El = -49 * mvolt          # resting potential (same as the reset)
psp = 0.5 * mvolt         # postsynaptic potential size

G = NeuronGroup(N=40, model='dV/dt = -(V-El)/tau : volt',
              threshold=Vt, reset=Vr)

C = Connection(G, G)
C.connect_random(sparseness=0.1, weight=psp)
M = StateMonitor(G, 'V', record=0)
G.V = Vr + rand(40) * (Vt - Vr)
run(200 * msecond)
plot(M.times / ms, M[0] / mV)
xlabel('Time (in ms)')
ylabel('Membrane potential (in mV)')
title('Membrane potential for neuron 0')
show()
'''
'''
tau = 20 * msecond        # membrane time constant
Vt = -50 * mvolt          # spike threshold
Vr = -60 * mvolt          # reset value
El = -49 * mvolt 
psp = 0.5 * mvolt            # resting potential (same as the reset)
G = NeuronGroup(N=40, model='dV/dt = -(V-El)/tau : volt',
              threshold=Vt, reset=Vr)
C = Connection(G,G)
C.connect_random(sparseness=0.1,weight=psp)
#C = Connection(G,G,sparseness=0.1,weight=psp)
M = SpikeMonitor(G)
G.V = Vr + rand(40) * (Vt - Vr)
run(1 * second)
print M.nspikes
raster_plot()
show()
'''
'''
tau_a = 1 * ms 
tau_b = 10 * ms
v_t = 10*mV
V_r = 0 * mV
eqs = Equations(
      dVa/dt = -Va/tau_a : volt
      dVb/dt = -Vb/tau_b : volt
      )

spiketimes = [(0,1 * ms) , (0,4 * ms) ,
              (1,2 * ms) , (1,3 * ms)]
#G = SpikeGeneratorGroup(2,spiketimes)
G1 = SpikeGeneratorGroup(2, spiketimes)
G2 = NeuronGroup(N=1, model=eqs, threshold=v_t, reset=V_r)
#C = Connection(G,H,state)
C1 = Connection(G1, G2, 'Va')
C2 = Connection(G1, G2, 'Vb')
C1[0, 0] = 6 * mV
C2[1, 0] = 3 * mV
Ma = StateMonitor(G2, 'Va', record=True)
Mb = StateMonitor(G2, 'Vb', record=True)

run(10 * ms)

plot(Ma.times, Ma[0])
plot(Mb.times, Mb[0])
show()
'''