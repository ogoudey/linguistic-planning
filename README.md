# Linguistic Planner
This project takes a lot (more than I can do right now).

## Description
1. First it parses relevant real-time input into known terms. These terms are labels on the input.
2. Then the terms get merged together depending on what type they are. Think of this first as simple concatenation of the terms.
3. When the merging is complete, the structure, in some order, should have an internal representation.

Example:
On an input of (DIR, you, movetheblock), terms (labels) might be [`directionality`, `individual`, `action`]. These terms are then combined (according to their type) and a plan emerges: `merge(DIR, you)`, `merge(individual, action)`. 

"Semantically" these terms have an internal definition. "movetheblock" might correspond to a function that moves the robot. "you" might correspond to a high object class. A particular "DIRECTION" perception might correspond to a state variable.

When merging, "DIR" and "you" combine to make, say, `self.`. Let's suppose `individual` merges again, now with `action`, and we might now have `self.move_block`. That's semantic understanding in readable form: an executable line of code.

This project also tries to separate the concerns of the input from internal processes such as whatever the robot was currently doing.

### Background

The first intuition here is that human language (HL) input should be treated as sequences of an external form of communication, but that given that "treatment", all behavior should stay the same.

A second angle at this project is that the cobot should have a "language of its own". Such a device is central to a cognitive architecture.

HL will have almost nothing to do with the cobot. The cobot would label it as another property of humans if it were exploring its theory of humans. In [complex cobotics](https://github.com/ogoudey/complex-cobot), the cobot treats HL as input for collaboration with humans. It decodes the HL, and then associates it with function calls, that's all.


