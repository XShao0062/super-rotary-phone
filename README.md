# super-rotary-phone
This script is to transfer ra and dec in units of hms and dms, respectively to that in units of degree. 

Users could input `ra` with formats of `12h20m30.5s` or `12:20:30.5` or `12 30 30.5`, `dec` with the formats of  `12d20m30.5s` or `12:20:30.5` or `12 30 30.5`. It's not that `ra` and `dec` could be input with different formats simultanously, e.g. `--ra '12h20m30.5s' --dec '12 20 30.5'`, or `--ra '- 12 20 30.5' --dec '- 12 20 30.5'`
For each examples mentiond above, the output would begin with `Your expected coordinate in degrees: (-185.09583333333333, -12.339722222222223)`.

# Examples to use
Example to run this script at command line and the output: 
1. `$  python3 mymodule/cli_coordinate_calculator.py --ra '12h20m30.5s' --dec '- 12:20:30.5'`
   `Your expected coordinate in degrees: (185.12708333333333, -12.341805555555556)`
3. `$ python3 mymodule/cli_coordinate_calculator.py --ra '- 12:20:30.5' --dec '- 12 20 30.5'`
   `Your expected coordinate in degrees: (-185.12708333333333, -12.341805555555556)`



