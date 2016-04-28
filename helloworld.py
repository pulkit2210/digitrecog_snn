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