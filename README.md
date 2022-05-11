# rajini++
<p align="center">
<img width=256 src="https://user-images.githubusercontent.com/6749212/167663396-3030d334-ebde-4b0e-939b-ff48e146f488.png"/>
</p>

rajini++ (rajiniPP) is a programming language is a tribute to the one and only superstar and based on the iconic dialogues of Rajinikanth. This is a hobby project ans is not meant to be used for serious software development.

This project is inspired by the [ArnoldC](https://github.com/lhartikk/ArnoldC) project.

## Installation
right now, the only way to get rajini++ is to clone the repository and build your own wheel. You need to have at least python 3.8 installed.
- clone project: `git clone https://github.com/aadhithya/rajiniPP.git`
- change directory to rajiniPP: `cd rajiniPP`
- install poetry: `pip install poetry`
- generate wheel: `poetry build`
- install rajini++: `pip install dist/rajinipp-0.0.1-py3-none-any.whl`
- test installation: `rajinipp version`

## Getting started

rajini++ is not a feature rich language and is not intended for serious use. It is rather a hobby project and a tribute to the one and only superstar.

### The `hello_world.rpp` program
The Print function is summoned by using the `DOT` command.
```
LAKSHMI START
DOT "Hello, world!";
MAGIZHCHI
```
will result in the following output:

![hello world output](./imgs/hello-out.png)

## Resources
- **The rajini++ Documentation**: The documentation for rajini++, the language can be found at the [rajiniPP Wiki](https://github.com/aadhithya/rajiniPP/wiki/).
- **The rajini++ Language Spec**: The rajini++ commands and its equivalent in python3 can be found at the [rajiniPP Language Spec](https://github.com/aadhithya/rajiniPP/wiki/) wiki.
- **The rajinipp Interpreter Documentation**: The documentation for the rajinipp interpreter can be found [here](https://github.com/aadhithya/rajiniPP/wiki/).


## Roadmap
- [x] Math Ops
  - [x] MUL
  - [x] DIV
  - [x] MOD
- [x] Unary Ops
- [x] print multiple objects with the same statement.
- [x] variable declaration
- [x] variable access
- [x] variable manipulation
- [x] bool data type
- [x] float datatype
- [x] logical ops
- [ ] if statement
- [ ] if-else statement
- [ ] for loop
- [ ] while loop
- [ ] rpp in python integration
- [ ] void functions
- [ ] number functions
- [ ] string functions
