## To Do Distributed Reinforcement Learning

#### Logging/Plotting

1. <s>Create Data Format for Storing episodes</s>
2. <s>Write episode saver</s>
3. <s>Connect episode Saver to Actor</s>
4. <s>Write code to read episodes</s>
5. <s>Make Ipython Notebook to Plot Episodes</s>

#### Distributed communication

1. Create message format for transferring episodes
2. Create Mesasge format for transferring Model Parameters
3. Add Functionality for Actor to send and receive messages
4. " for learner to send and receive messages
5. " for replay buffer to send and receive messages

#### Testing/Debugging

1. <s>Test and confirm convergence of tabular Q on Frozen lake</s>
2. <s>Test and confirm convergence of tabular Q on Nchain</s>
3. <s>Test and confirm convergence of preprocessed Q on cartpole</s>
4. Test and confirm convergence of continuous Q on pendulum

#### Replicate Silver Paper

1. Implement DQN agent
2. Implement multi-actor, single learner

#### Thomspon Sampling

1. Implement normal distribution tabular Q function
2. Implement bayesian DQN network weights
3. Find update rule for Bayesian DQN network

#### Continuous Control

1. <s>Implement tabular preprocessor</s>
2. <s>Make agent factory</s>
3. <s>Connect tabular preprocessor + tabular Q to factory</s>
4. Implement Q table with continuous actions
4. Implement Stochastic Network
