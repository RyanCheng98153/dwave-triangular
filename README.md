# Dwave-triangular
This is a illustration of dwave for triangular ising model
Hope you have a great day :blush:

## dwave prior work
*If virtualenv does not exist*
1. Create a new virtual environment of d-wave named quantum
    `python -m venv venv`
    
2. Enter the virtual environment
    - Macs
        `source venv/bin/activate` 
        
    - Windows
        `./venv/Scripts/activate.ps1` 
        
3. Confirmed the dwave-ocean sdk is not installed
    `pip uninstall dwave-ocean-sdk`
    
4. Update the pip install to the latest version
    `python -m pip install --upgrade pip`

## requirements
```bash
pip install -r ./requirements.txt
```

## usage
- Execution with argument: L*L ising model 
    ```python ./main [-L]```
- Execution with custom couplings
    ```python ./main [-file path]``` 
    ex: ```python ./main ./example.txt```

- Execute with custom size `L*L*H` and bonds `-JL`, `-JH` triangular ising model
    ```python .\main.py runIsing -l [L] -h [H] -JL [-JL] -JH [-JH]```
    ex: ```python .\main.py runIsing -l 3 -h 1 -JL 1.0 -JH 1.0```

## File Format
- Space Separate File Format
``` 
model_size
3 3 1
couplings
1 1.0
0 0.5
0 1 0.5
0 2 0.7
2 3 0.5
1 2 0.8
2 1 0.6
```