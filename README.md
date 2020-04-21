206neutrinos
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
**Jørgen-Olaf** is a distinguished nuclear physics researcher in **Hørsholm**. With his assistant, they are studying **neutrinos**, a kind of promising particle, and are trying to prove that these particles can travel faster than light.

Given temperature and pressure conditions, they record the speed of some particles under these conditions, modify one parameter, and start again. Almost 11 months of hard work on several hundreds of millionsrecords...

They are unable to efficiently store all of these values. For each series of records, they only register:
* its arithmetical mean
* its standard deviation
* its root mean square *(Jørgen-Olaf needs an average speed so that if all the particles travel at this speed, they would have the same total kinetic energy)*
* its harmonic mean (as a precaution, in case Jørgen-Olaf would need another variable, with a non-quadratic dependency on speed)
 
 
Considering the size of the series, Jørgen-Olaf needs you to develop a software that will allow him to update his data in real-time. This program will take **4 numbers as inputs (the number of recorded values, their arithmetic mean, harmonic mean and standard deviation)**, and must:
* wait for the next value to be written on the standard input
* print the number of recorded values, their standard deviation, arithmetic mean, root mean squareand harmonic mean
* return to the first step, except if the keyword **END** is entered.


## USAGE:

```
>> ./206neutrinos n a h sd
```

#### DESCRIPTION
n       number of values
a       arithmetic mean
h       harmonic mean
sd      standard deviation


Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva) and [**PATRICIA MONFA-MATAS**](https://github.com/patumm)
