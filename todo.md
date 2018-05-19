## To Do Distributed Reinforcement Learning

#### Logging/Plotting

1. Create Data Format for Storing episodes
2. Write episode saver
3. Connect episode Saver to Actor
4. Write code to read episodes
5. Make Ipython Notebook to Plot Episodes

#### Distributed communication

1. Create message format for transferring episodes
2. Create Mesasge format for transferring Model Parameters
3. Add Functionality for Actor to send and receive messages
4. " for learner to send and receive messages
5. " for replay buffer to send and receive messages

#### Testing/Debugging

1. Test and confirm convergence of tabular Q on Frozen lake
2. Test and confirm convergence of tabular Q on Nchain

#### Replicate Silver Paper

1. Implement DQN agent

#### Thomspon Sampling

1. Implement normal distribution tabular Q function
2. Implement bayesian DQN network weights
3. Find update rule for Bayesian DQN network

#### Continuous Control

1. Implement tabular preprocessor
2. Implement Stochastic Network
