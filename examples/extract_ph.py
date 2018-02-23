# Example to extract the persistence diagram from a neuronal tree

# Step 1: Import the tmd module

import tmd

# Step 2: Load your morphology
filename = './test_data/valid/C010398B-P2.CNG.swc'
neu = tmd.io.load_neuron(filename)

# Step 3: Extract the ph diagram of a tree
tree = neu.neurites[0]
ph = tmd.methods.get_persistence_diagram(tree)

# Step 4: Extract the ph diagram of a neuron's trees
ph_neu = tmd.methods.get_ph_neuron(neu)

# Step 5: Extract the ph diagram of a neuron's trees,
# depending on the neurite_type
ph_apical = tmd.methods.get_ph_neuron(neu, neurite_type='apical')
ph_axon = tmd.methods.get_ph_neuron(neu, neurite_type='axon')
ph_basal = tmd.methods.get_ph_neuron(neu, neurite_type='basal')

# Step 6: Plot the extracted topological data with three different ways
import view

# Visualize the neuron
view.view.neuron(neu)

# Visualize a selected neurite type or multiple of them
view.view.neuron(neu, neurite_type=['apical'])

# Visualize the persistence diagram
view.plot.ph_diagram(ph_apical)

# Visualize the persistence barcode
view.plot.barcode(ph_apical)

# Visualize the persistence image
view.plot.ph_image(ph_apical)

# Create an overview figure for the topology of a tree
