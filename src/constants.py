from babysitter import Rate

HOURS = ['5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12pm', '1am', '2am','3am', '4am']

FAMILIES = {'Family A': [
    Rate(0,HOURS.index('11pm'),15.), 
    Rate(HOURS.index('11pm'), len(HOURS), 20.)
    ]}

