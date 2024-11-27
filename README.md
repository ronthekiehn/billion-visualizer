# Billion Visualizer

A quick matplotlib visualizer for @bddicken's language comparison project. The timings are hardcoded from the timing he got on his machine.

Check out that repo: https://github.com/bddicken/languages

## Running It
You'll need matplotlib installed in your venv.

Run `python3 viz.py` and the visualization will play in a matplotlib window.

## Flags and Features
* `--speed {speed}`  
default: 1.0  
This flag allows you to control the playback speed of the visualization (ex: 0.5 means C takes 1s instead of 0.5s), this is useful for slowing down the simulation to see more fine-grain comparisons between languages

* `--fps {fps}`  
default: 60  
This flag controls the fps of the playback. Raising it may affect performance, and lowering it may increase performance, but make the playback choppy

* `--labels`  
default: False  
Adding this flag will label each language with the current loop iteration.  
*note: this flag affects performance so timing will not be accurate*


