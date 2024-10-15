:: set vars=21 24 27 30 33 36 39 42 45 48 51 54 57 60 129 255
:: python .\main.py runIsing -L %%i -JL 1.0 -solver qpu -numResult %%n


:: mapleleaf qpu
set vars=7 14 21 28 35 42
set nums=3 1000

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\MapleLeaf\mapleleaf_L_%%i_%%i.txt -s qpu -n %%n
  )
)

:: kagome qpu
set vars=6 12 18 24 30 36 42
set nums=3 1000

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s qpu -n %%n
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


:: mapleleaf hybrid
set vars=7 14 21 28 35 42
set nums=1

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\MapleLeaf\mapleleaf_L_%%i_%%i.txt -s hybrid -n %%n
  )
)

:: kagome hybrid
set vars=6 12 18 24 30 36 42
set nums=1

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runSpaceFile -f .\LatticeFile\Kagome\kagome_L_%%i_%%i.txt -s hybrid -n %%n
  )
)


pause