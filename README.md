# IS601 - Calculator 

Calculator with four operations: add, sub, mul, div

```bash
Welcome to Lakshya's Calculator
Available commands: add, sub, mul, div, exit
calc> 
```

### Add operation
```bash
calc> add 2 3
5.0
```
### Subtract operation
```bash
calc> sub 8 2
6.0
```

### Multiply operation
```bash
calc> mul 7 4
28.0
```

### Divide operation
```bash
calc> div 10 3
3.3333333333333335
```
### Division by zero
```bash
calc> div 5 0
Error: Division by zero
```
### Type *exit* to close
```bash
calc> exit
Goodbye!
```

## Setup

### Clone my repo

```bash
git clone git@github.com:Lakshyasaharan5/IS601-assignment-2.git
```

### Create a python venv and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install packages from requirements.txt

```bash
pip install -r requirements.txt
```

### Run pytest

```bash
pytest
```

## Github Actions for test

Github workflow has been implemented. When you push your code then Github Action will automatically test it using pytest.