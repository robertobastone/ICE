# ICE
Italy Covid19 Epidemic (ICE) is a Python routine to keep track of the ongoing 2019-20 coronavirus pandemic in Italy. In the fit of the total cases I have employed a logistic growth fit[1] with three parameters, a, b and c:
<img src=https://render.githubusercontent.com/render/math?math=y(t)=\frac{a}{1%20%2B%20be^{-ct}}>
 which is commonly used to fit pandemics growth and the parameters that define the function are stored in the csv file "results.csv". As of 29th March, the results show that:
 - a = 95000 ± 2000
 - b = 710 ± 60
  - c = 0.181 ± 0.003

# Milestones
1. March, 14 2020:
   - minimally functioning code
2. March, 15 2020:
   - script in OOP

# Versions
## Python 3
### Version 1.00 (March, 14 2020)
- minimally functioning code
### Version 1.01 (March, 15 2020)
- code written according to the Object oriented paradigm
### Version 1.02 (March, 21 2020)
- Added a daily increment and relative daily increment (%) subplots
### Version 1.03 (March, 22 2020)
- Added try/exception statements
### Version 1.04 (March, 28 2020)
- Improved try/exception statements and added logistic fit to overall national cases.

# How to run the script
## From terminal
- type in python in your terminal then:
```
import ICE
ICE.ICE().main()
```
- During the execution of the script, a new folder named "plots" will be created/updated with the plots of the regional (20 plots) and the overall national (1 plot) cases.

# References
- [1] Wu, Ke, et al. "Generalized logistic growth modeling of the COVID-19 outbreak in 29 provinces in China and in the rest of the world." arXiv preprint arXiv:2003.05681 (2020).
