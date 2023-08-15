

# CGFCore

CGFCore is a Python library focused on game theory and its various game types. 
It provides implementations for different game types like Bayesian, Composed, I
mperfect Information, NonZeroSum, Sequential, Stochastic, ZeroSum, and some variants.

## Installation

To install CGFCore, you can use pip:

```bash
pip install path_to_CGF-0.0.3-py3-none-any.whl
```

Or from the source distribution:

```bash
pip install path_to_CGF-0.0.3.tar.gz
```

## Usage

Here's a basic example to get started:

```python
from CGF.CGFCore import main
from CGF.test import evaluate

# Test a composed game in sequential order
# main.test_composed_game_sequential()

# Run evaluation tests
evaluate.run_tests()
```

## Game Types

The library provides implementations for the following game types:

- Bayesian
- Composed
- Imperfect Information
- NonZeroSum
- Sequential
- Stochastic
- ZeroSum

Additionally, there are variants of some games available for more specific use cases.

## Open Game Framework

The library also includes an open game framework with deterministic, final, and stochasticity modules to help in the development and analysis of games.

## Testing

To run the tests, use the following command:

```python
from CGF.test import evaluate
evaluate.run_tests()
```

## License

Please refer to the `LICENSE.txt` file for licensing information.

---
