to start you need to 
1. set up the python environment

For Linux

# Synchronize packages via uv
uv sync

# Activate virtual environment if needed
source .venv/bin/activa

For Windows

# Synchronize packages via uv
uv sync

# Activate virtual environment if needed
.venv\Scripts\activate.bat
# Or .venv\Scripts\Activate.ps1 for powershell

2. generate data using data_generator.py
3. start the database using 'docker compose up -d'
4. python data_generator.py -c 50
5. run main.py


