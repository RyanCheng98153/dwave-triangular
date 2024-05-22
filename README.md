# Dwave-triangular
This is a illustration of dwave for triangular ising model
Hope you have a great day :blush:

## dwave prior work
*If virtualenv does not exist*

- Macs
    `sudo pip install virtualenv`
    
- Windows
    `pip install virtualenv`
    
1. Create a new virtual environment of d-wave named quantum
    `virtualenv quantum`
    
2. Enter the virtual environment
    - Macs
        `source quantum/bin/activate` 
        
    - Windows
        `./quantum/Scripts\activate.ps1` 
        
3. Confirmed the dwave-ocean sdk is not installed
    `pip uninstall dwave-ocean-sdk`
    
4. Update the pip install to the latest version
    `python -m pip install --upgrade pip`

## requirements

## usage
- Execution with argument: L*L ising model 
    ```python ./main [-L]```
- Execution with custom couplings
    ```python ./main [-file path]``` 
    ex: ```python ./main ./example.txt```

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