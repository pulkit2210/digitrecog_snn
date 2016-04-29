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
'''
from brian import *

taum = 20 * ms
taue = 1 * ms
taui = 10 * ms
Vt = 10 * mV
Vr = 0 * mV

eqs = Equations(
      dV/dt  = (-V+ge-gi)/taum : volt
      dge/dt = -ge/taue        : volt
      dgi/dt = -gi/taui        : volt
      )
spiketimes = [(0, 1 * ms), (0, 10 * ms),
              (1, 40 * ms),
              (0, 50 * ms), (0, 55 * ms)]
G1 = SpikeGeneratorGroup(2, spiketimes)
G2 = NeuronGroup(N=1, model=eqs, threshold=Vt, reset=Vr)
C1 = Connection(G1, G2, 'ge')
C2 = Connection(G1, G2, 'gi')
C1[0, 0] = 3 * mV
C2[1, 0] = 3 * mV
Mv = StateMonitor(G2, 'V', record=True)
Mge = StateMonitor(G2, 'ge', record=True)
Mgi = StateMonitor(G2, 'gi', record=True)
run(100 * ms)
figure()
subplot(211)
plot(Mv.times, Mv[0])
subplot(212)
plot(Mge.times, Mge[0])
plot(Mgi.times, Mgi[0])
show()
run(100 * ms)
'''
from brian import *

taum = 20 * ms          # membrane time constant
taue = 5 * ms          # excitatory synaptic time constant
taui = 10 * ms          # inhibitory synaptic time constant
Vt = -50 * mV          # spike threshold
Vr = -60 * mV          # reset value
El = -49 * mV          # resting potential
we = (60 * 0.27 / 10) * mV # excitatory synaptic weight
wi = (20 * 4.5 / 10) * mV # inhibitory synaptic weight

eqs = Equations('''
        dV/dt  = (ge-gi-(V-El))/taum : volt
        dge/dt = -ge/taue            : volt
        dgi/dt = -gi/taui            : volt
        ''')
G = NeuronGroup(4000, model=eqs, threshold=Vt, reset=Vr)
Ge = G.subgroup(3200) # Excitatory neurons
Gi = G.subgroup(800)  # Inhibitory neurons
Ce = Connection(Ge, G, 'ge', sparseness=0.02, weight=we)
Ci = Connection(Gi, G, 'gi', sparseness=0.02, weight=wi)
M = SpikeMonitor(G)
MV = StateMonitor(G, 'V', record=0)
Mge = StateMonitor(G, 'ge', record=0)
Mgi = StateMonitor(G, 'gi', record=0)
G.V = Vr + (Vt - Vr) * rand(len(G))
run(500 * ms)
subplot(211)
raster_plot(M, title='The CUBA network', newfigure=False)
subplot(223)
plot(MV.times / ms, MV[0] / mV)
xlabel('Time (ms)')
ylabel('V (mV)')
subplot(224)
plot(Mge.times / ms, Mge[0] / mV)
plot(Mgi.times / ms, Mgi[0] / mV)
xlabel('Time (ms)')
ylabel('ge and gi (mV)')
legend(('ge', 'gi'), 'upper right')
show()