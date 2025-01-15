:: set vars=21 24 27 30 33 36 39 42 45 48 51 54 57 60 129 255
:: python .\main.py runIsing -L %%i -JL 1.0 -solver qpu -numResult %%n

GOTO :SKIP
:: mapleleaf qpu
set vars=7 14 21 28 35 42
set nums=3 1000

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    echo mapleleaf
    python .\main.py runSpaceFile -f .\LatticeFile\MapleLeaf\mapleleaf_L_%%i_%%i.txt -s qpu -n %%n
  )
)


:: triangular hybrid
set vars=6 9 12 15 18 21 24 27 30 33 36 39
set nums=1

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runIsing -L %%i -JL 1.0 -s hybrid -n %%n
  )
)


:: kagome hybrid
set vars=66 72 78 84 90 96 102 108 114 120
set nums=1

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s hybrid -n %%n
  )
)

:: not test1 end

:: kagome qpu
set vars=60
set nums=3

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s qpu -n %%n
  )
)


:: kagome qpu
set vars=66 72 78 84 90 96 102 108 114 120
set nums=3

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s qpu -n %%n
  )
)

:: not test1 end 


:: mapleleaf hybrid
set vars=49 56 63 70 77 84 91 98 105 112 119 126 133 140
set nums=1

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    echo mapleleaf
    python .\main.py runSpaceFile -f .\LatticeFile\MapleLeaf\mapleleaf_L_%%i_%%i.txt -s hybrid -n %%n
  )
)

:: triangular hybrid
set vars=138 141 144 147 150
set nums=1

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runIsing -L %%i -JL 1.0 -s hybrid -n %%n
  )
)

:SKIP

:: mapleleaf hybrid 77 for 10 times
set vars=77
set nums=1 2 3 4 5 6 7

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    echo mapleleaf
    python .\main.py runSpaceFile -f .\LatticeFile\MapleLeaf\mapleleaf_L_%%i_%%i.txt -s hybrid -n 1
  )
)

:: kagome hybrid 90 for 10 times
set vars=90
set nums=1 2 3 4 5 6 7 8 9 10

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s hybrid -n 1
  )
)


:: mapleleaf hybrid 70 for 20 times
set vars=70
set nums=1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    echo mapleleaf
    python .\main.py runSpaceFile -f .\LatticeFile\MapleLeaf\mapleleaf_L_%%i_%%i.txt -s hybrid -n 1
  )
)


:: kagome hybrid 84 for 20 times
set vars=84
set nums=1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s hybrid -n 1
  )
)