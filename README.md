# Linguistic Planner

This project attempts to remedy some of the stupidness in [complex cobotics](https://github.com/ogoudey/complex-cobot).

The first intuition here is that human language (HL) input should be treated as sequences of an external form of communication, but that given that "treatment", all behavior should stay the same.

A second angle at this project is that the cobot should have a "language of its own". Such a device is central to a cognitive architecture.

HL will have almost nothing to do with the cobot. The cobot would label it as another property of humans if it were exploring its theory of humans. In [complex cobotics](https://github.com/ogoudey/complex-cobot), the cobot treats HL as input for collaboration with humans. It decodes the HL, and then associates it with function calls, that's all.

### Terming
The process starts by instantiating a Communicator to "term" the input.

TODO: more than one term. These are types fundmental to the system. It will look like a lexicon. It will also resemble a mapping from internal function arguments to functions.

### Structure-Building
Next the terms of the input start to form structures. To the planning domain are added previously rooted structures. If the planner can form new structures it will find a plan to do so.

In the execution of this, complex actions are carried out. Explicit planner-solve-execute cycles are replaced with structures that combine planners with states and triggers.

A near-term example. The perception would be HL (an attribute of a `whisper` result):

Terming: <br>
    term(HL)    ---perception---<br>
    move_index(HL, State)<br>
    term(State)<br>
    move_index(SL, Collaboration)<br>
    term(Collaboration)<br>

Building: <br>
    merge(HL, Collaboration)<br>
    merge(State, Collaboration)<br>



