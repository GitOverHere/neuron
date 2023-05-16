class Neuron:
    def __init__(self):
        self.threshold = 0.5
        self.membrane_potential = 0.0

    def receive_input(self, input_value):
        self.membrane_potential += input_value

    def fire_action_potential(self):
        if self.membrane_potential >= self.threshold:
            print("Action potential fired!")
            # Reset the membrane potential after firing
            self.membrane_potential = 0.0

    def send_excitatory_output(self, target_neuron):
        target_neuron.receive_input(0.8)  # Simulated excitatory input

    def send_inhibitory_output(self, target_neuron):
        target_neuron.receive_input(-0.4)  # Simulated inhibitory input


# Example usage:
neuron1 = Neuron()
neuron2 = Neuron()

neuron1.receive_input(0.7)  # Receiving input into neuron1
neuron1.fire_action_potential()  # Checking if action potential fires

neuron1.send_excitatory_output(neuron2)  # Sending excitatory output from neuron1 to neuron2
neuron1.send_inhibitory_output(neuron2)  # Sending inhibitory output from neuron1 to neuron2

