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

    Type again to check the pip version.
    `python -m pip install --upgrade pip` 
    
✅ It should be promped “Requirement already satisfied… ”

5. Install the dwave-ocean-sdk
   `pip install dwave-ocean-sdk` 
   ✅ If Success, type `pip list` , then the dwave packages will be appeared in the list 
   
   ❌ If Not Success, open a new terminal, enter the virtual environment **(back to step 2)**, and install dwave sdk again.


## Json Format
```json
{
  "model_info": {
    "length": 3,
    "height": 1
  },
  "nodes": [
    {"id": 0, "magnetic_field": 0.2},
    {"id": 1, "magnetic_field": -0.3},
    {"id": 2, "magnetic_field": 0.1},
    {"id": 3, "magnetic_field": 0.0}
  ],
  "bonds": [
    {"node_ids": [0, 1], "strength": 0.5},
    {"node_ids": [0, 2], "strength": 0.7},
    {"node_ids": [0, 3], "strength": 0.5},
    {"node_ids": [1, 2], "strength": 0.8},
    {"node_ids": [2, 3], "strength": 0.6}
  ]
}
```


## usage
- Execution with input length
    ```python ./main [L]```
    ex: `python ./main 3`

- Execution with json file
    ```python ./main [json_file]```
    ex: `python ./main input.json`
