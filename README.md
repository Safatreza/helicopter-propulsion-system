# Helicopter Propulsion System

This project simulates the propulsion system of a helicopter. It is designed in Python and models the three primary stages of a helicopter's propulsion system: 
1. Turning on the system
2. Continuous usage of the system during flight
3. Landing and shutting down the system

The system is composed of various subsystems including the engine, rotor, transmission, and fuel system.

## Features
- **Engine**: Models the engine's power generation and performance.
- **Rotor**: Simulates rotor dynamics and thrust generation.
- **Transmission**: Handles power transmission between the engine and the rotor.
- **Fuel System**: Manages fuel usage based on flight conditions.

### Requirements
- Python 3.10+
- matplotlib (for plotting graphs)

### Installation

To run this project locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/helicopter-propulsion-system.git
    ```

2. Navigate into the project directory:

    ```bash
    cd helicopter-propulsion-system
    ```

3. Create and activate a virtual environment:

    - **Windows**:

      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

    - **macOS/Linux**:

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

After setting up the environment, you can run the simulation by executing the `main.py` file:

```bash
python main.py
