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

## Requirements
`pip install -r ./requirements.txt`
or 
`pip install dwave-ocean-sdk` + `pip install fire`

## Usage
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
        - `exact` for D-wave exact solver, 
        - `qpu` for D-wave quantum Solver
        - `hybrid`: for D-wave hybrid solver

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


### D-wave run results
#### Triangular Hybrid:
| L   | time       | energy   |
| --- | ---------- | -------- |
| 3   | 2.997 s    | -9.0     |
| 6   | 2.997 s    | -36.0    |
| 9   | 2.995 s    | -81.0    |
| 12  | 2.995 s    | -144.0   |
| 15  | 2.999 s    | -225.0   |
| 18  | 2.989 s    | -324.0   |
| 21  | 2.998 s    | -441.0   |
| 24  | 3.000 s    | -576.0   |
| 27  | 2.994 s    | -729.0   |
| 30  | 2.993 s    | -900.0   |
| 33  | 3.138 s    | -1089.0  |
| 36  | 3.613 s    | -1296.0  |
| 39  | 4.132 s    | -1521.0  |
| 42  | 4.678 s    | -1764.0  |
| 45  | 5.281 s    | -2025.0  |
| 48  | 5.905 s    | -2304.0  |
| 51  | 6.587 s    | -2601.0  |
| 54  | 7.311 s    | -2916.0  |
| 57  | 8.070 s    | -3249.0  |
| 60  | 8.864 s    | -3600.0  |
| 66  | 11.315 s   | -4356.0  |
| 72  | 15.519 s   | -5184.0  |
| 78  | 20.102 s   | -6084.0  |
| 84  | 25.022 s   | -7056.0  |
| 90  | 30.339 s   | -8100.0  |
| 96  | 36.005 s   | -9216.0  |
| 102 | 43.214 s   | -10404.0 |
| 108 | 53.312 s   | -11664.0 |
| 114 | 1m 03.968s | -12996.0 |
| 120 | 1m 15.200s | -14400.0 |
| 123 | 1m 21.024s | -15129.0 |
| 126 | 1m 26.981s | -15876.0 |
| 129 | 1m 33.128s | -16641.0 |
| 132 | 1m 39.336s | -17420.0 |
| 135 | 1m 45.800s | -18225.0 |


#### Maple leaf Hybrid:
| L   | time       | energy   |
| --- | ---------- | -------- |
| 7   | 2.992 s    | -47.0    |
| 14  | 2.992 s    | -196.0   |
| 21  | 2.999 s    | -441.0   |
| 28  | 2.994 s    | -784.0   |
| 35  | 3.046 s    | -1225.0  |
| 42  | 4.097 s    | -1764.0  |
| 49  | 5.346 s    | -2401.0  |
| 56  | 6.792 s    | 3136.0   |
| 63  | 8.410 s    | -3969.0  |
| 70  | 10.519 s   | -4900.0  |
| 77  | 15.009 s   | -5929.0  |
| 84  | 19.919 s   | -7052.0  |
| 91  | 25.252 s   | -8277.0  |
| 98  | 31.005 s   | -9600.0  |
| 105 | 37.196 s   | -11023.0 |
| 112 | 46.016 s   | -12538.0 |
| 119 | 57.104 s   | -14153.0 |
| 126 | 1m 08.834s | -15868.0 |
| 133 | 1m 21.278s | -17681.0 |
| 140 | 1m 34.375s | -19588.0 |

#### Kagome Hybrid:
| L   | time     | energy  |
| --- | -------- | ------- |
| 6   | 2.985 s  | -18.0   |
| 12  | 2.996 s  | -72.0   |
| 18  | 2.999 s  | -162.0  |
| 24  | 2.990 s  | -288.0  |
| 30  | 2.989 s  | -450.0  |
| 36  | 3.000 s  | -648.0  |
| 42  | 3.671 s  | -882.0  |
| 48  | 4.585 s  | -1152.0 |
| 54  | 5.647 s  | -1458.0 |
| 60  | 6.810 s  | -1800.0 |
| 66  | 8.103 s  | -2178.0 |
| 72  | 9.521 s  | -2592.0 |
| 78  | 12.368 s | -3042.0 |
| 84  | 16.077 s | -3528.0 |
| 90  | 20.056 s | -4050.0 |
| 96  | 24.298 s | -4608.0 |
| 102 | 28.828 s | -5202.0 |
| 108 | 33.636 s | -5832.0 |
| 114 | 38.714 s | -6498.0 |
| 120 | 46.379 s | -7200.0 |

- QPU Access Time Detail
    - QPU Access time = Charge time
    - Detail of QPU access time
        <img src="image.png" width='60%' height='50%'>

#### Triangular QPU:
-sample 3

| L   | time    | energy  |
| --- | ------- | ------- |
| 3   | 0.015 s | -9.0    |
| 9   | 0.142 s | -81.0   |
| 12  | 0.016 s | -144.0  |
| 15  | 0.016 s | -221.0  |
| 18  | 0.016 s | -324.0  |
| 21  | 0.018 s | -433.0  |
| 24  | 0.252 s | -568.0  |
| 27  | 0.018 s | -697.0  |
| 30  | 0.274 s | -876.0  |
| 33  | 0.286 s | -1061.0 |
| 36  | 0.018 s | -1252.0 |
| 39  | 0.018 s | -1489.0 |

#### Maple Leaf QPU
- sample 3

| L   | time     | energy  |
| --- | -------- | ------- |
| 7   | 16.12 ms | -47.0   |
| 14  | 16.08 ms | -196.0  |
| 21  | 16.47 ms | -441.0  |
| 28  | 16.57 ms | -784.0  |
| 35  | 16.59 ms | -1225.0 |
| 42  | 16.59 ms | -1764.0 |

#### Kagome QPU
- sample 3

| L   | time     | energy    |
| --- | -------- | --------- |
| 6   | 16.27 ms | -54.764   |                
| 12  | 16.33 ms | -343.488  |                
| 18  | 16.07 ms | -693.664  |                
| 24  | 16.43 ms | -1651.096 |                
| 30  | 16.49 ms | -2961.264 |                
| 36  | 16.57 ms | -3942.62  |                
| 42  | 16.58 ms | -6147.736 |                
| 48  | 16.59 ms | -8306.84  |                
| 54  | 16.60 ms | -8358.32  |                
        