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
`pip install -r ./requirements.txt`

## usage
 - RunIsing: Execution with triangular ising model:
    ```sh
    python main.py runIsing -L [L] -JL [JL] -solver [solver] -numResult [nums]
    ``` 
    or 
    ```sh
    python main.py runIsing -L [L] -JL [JL] -s [solver] -n [nums]
    ```
    - format:   
        `-L`: length of the lattice
        `-JL`: bond strength connected between each nodes
        `-solver`: solver of D-wave: 
        - `exact` for exactSolver, 
        - `qpu`for quantum Solver

        `-numResult`: number of D-wave output results
    
    - usage examples:
        `python main.py runIsing -L 3 -JL 1.0 -solver exact -numResult 1` 
        or 
        `python main.py runIsing -L 3 -JL 1.0 -s exact -n 1`
---

 - RunSpaceFile: Execution with custom couplings
   ```sh
   python main.py runSpaceFile -filename [filename] -solver [solver] -numResult [num]
   ``` 
   or 
   ```sh
   python main.py runSpaceFile -f [filename] -s [solver] -n [num]
   ``` 
   - format:   
        `-filename`: input custon by space file 
        `-solver`: solver of D-wave: 
        - `exact` for exactSolver, 
        - `qpu`for quantum Solver

    `-numResult`: number of D-wave output results
    
   - usage examples:
        `python main.py runSpaceFile -f .\example\spaceExample.txt -s exact -n 1` 
    
## File Format (runSpacFile)
- Space Separate File Format
- using `#` as a comment for the model
```
# model_size
# it is a example of space bond file
1 1.0
0 0.5
0 1 0.5
0 2 0.7
2 3 0.5
1 2 0.8
2 1 0.6
```

## Notes: 
`dwave auth login --oob` for dwave auth login
`dwave auth get` for getting dwave auth tokens