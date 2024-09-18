set vars=21 24 27 30 33 36 39 42 45 48 51 54 57 60 129 255
set nums=3 5 10 50 

for %%n in (%nums%) do (
  for %%i in (%vars%) do (
    python .\main.py runIsing -L %%i -JL 1.0 -solver qpu -numResult %%n
  )
)
pause