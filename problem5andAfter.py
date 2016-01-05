# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math

primes = [2,3,5]

def isDivisibleByAnyOneOfTheKnownPrimes (targetNumber):
    for prime in primes:
        if targetNumber%prime==0:
            return True

def isKnownPrime(targetNumber):
    return targetNumber in primes

def isPrime (targetNumber):
    if(isKnownPrime(targetNumber)):
        return True
    if(_is(targetNumber)(divisibleByAnyOneOfTheKnownPrimes)):
        return False
    limit = getMaxFactorLimit(targetNumber)
    divider=getLast(primes)
    while divider <=limit:
        if(targetNumber%divider==0):
            return False
        divider=getNextPrime(divider)
    return True

def _is(element):
    return lambda hasQuality:hasQuality(element)

def divisibleByAnyOneOfTheKnownPrimes(element):
    return isDivisibleByAnyOneOfTheKnownPrimes(element)

def getMaxFactorLimit(targetNumber):
    return math.ceil(targetNumber**0.5)

def getLast(primes):
    return primes[len(primes)-1]

def getNextPrime (prime):
    nextOddNumber=prime+2
    while isPrime(nextOddNumber)==False:
        nextOddNumber+=2
    primes.append(nextOddNumber)
    return nextOddNumber

def getAListOfPrimesLessThan(maxLimit):
    listOfPrimes=[2,3,5]
    nextPrime=getNextPrime(getLast(listOfPrimes))
    while nextPrime<maxLimit:
        listOfPrimes.append(nextPrime)
        nextPrime=getNextPrime(nextPrime)
    return listOfPrimes

def getFirstnPrimes (n):
    listOfPrimes=[2,3,5]
    nextPrime=getLast(listOfPrimes)
    for index in range(n-3):
        nextPrime=getNextPrime(nextPrime)
        listOfPrimes.append(nextPrime)
    return listOfPrimes

def getPrimeFactors(targetNumber):
    factorCandidates = getAListOfPrimesLessThan(getMaxFactorLimit(targetNumber))
    factors=[]
    for factorCandidate in factorCandidates:
        if(targetNumber%factorCandidate==0):
            factors.append(factorCandidate)
    return factors

def pro3():
    print('problem 3')
    print(getPrimeFactors(13195))
    print(getPrimeFactors(600851475143)) # 8 minutes


####################
def pro5 ():
    print('problem 5')
    print('theLeastCommonMultipleOf(first(10)(naturalNumbers)))',
    theLeastCommonMultipleOf(first(10)(naturalNumbers)))
    print('theLeastCommonMultipleOf(first(20)(naturalNumbers)))',
    theLeastCommonMultipleOf(first(20)(naturalNumbers)))

def theLeastCommonMultipleOf (factors):
    lCM=theProductOf(factors)
    for factor in factors:
        isMagicWorking= lambda magicalNumber : isCommonMultiple(magicalNumber,factors)
        lCM=magic(lCM,factor,isMagicWorking)
    return (int)(lCM)

def first(n):
    return lambda series: series(n)

def naturalNumbers(upto):
    return list(range(1,upto+1))

def theProductOf(listOfNumbers):
    product=1
    for number in listOfNumbers:
        product*=number
    return product

def magic(lCM,factor,isCool):
    magicalNumber=lCM/factor
    if(factor>1 and divisibleBy(lCM,factor) and isCool(magicalNumber)):
        return magic(magicalNumber,factor,isCool)
    return lCM;

def divisibleBy(product,factor):
    return product%factor==0

def isCommonMultiple(product,factors):
    for factor in factors:
        if(not(divisibleBy(product,factor))):
            return False
    return True

################
def pro6():
    print('problem 6')
    print('theDifferenceBetween(theSumOf(theSquaresOf(theFirst(10)(naturalNumbers))), theSquareOf(theSumOf(theFirst(10)(naturalNumbers))))) ',
    theDifferenceBetween(theSumOf(theSquaresOf(theFirst(10)(naturalNumbers))), theSquareOf(theSumOf(theFirst(10)(naturalNumbers)))))
    print('theDifferenceBetween(theSumOf(theSquaresOf(theFirst(100)(naturalNumbers))), theSquareOf(theSumOf(theFirst(100)(naturalNumbers))))) ',
    theDifferenceBetween(theSumOf(theSquaresOf(theFirst(100)(naturalNumbers))), theSquareOf(theSumOf(theFirst(100)(naturalNumbers)))))

def theFirst(n):
    return first(n)

def theDifferenceBetween(a,b):
    if(a>b): return a-b
    return b-a

def theSumOf(numbers):
    return sum(numbers)

def theSquaresOf(numbers):
    return map(theSquareOf,numbers)

def theSquareOf(n):
    return n**2

################
def pro7():
    print('problem 7')
    print('the6thPrimeis',getFirstnPrimes(6)[5])
    print('the10001stPrimeis',getFirstnPrimes(10001)[10000])

###############
def pro8():
    print('problem 8')
    # print('theGreatestOf(theProductOfEvery(listOfAllPossible(frameOf(4,adjacentNumbers),(theDigitsOf(
    # 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450\
    # )))))')

    print(theGreatestOf(theProductOfEvery(listOfAllPossible(frameOf(4,adjacentNumbers),(theDigitsOf(
    '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    ))))))

    print(theGreatestOf(theProductOfEvery(listOfAllPossible(frameOf(13,adjacentNumbers),(theDigitsOf(
    '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    ))))))

def theGreatestOf(listOfNumbers):
    return max(list(listOfNumbers))

def theProductOfEvery(listsOfLists):
    return map(theProductOf,listsOfLists)

def listOfAllPossible(selector,listOfNumbers):
    listOfAllPossibleSubLists=[]
    for index in range(len(listOfNumbers)):
        listOfAllPossibleSubLists.append(selector(index,listOfNumbers))
    return listOfAllPossibleSubLists

def frameOf(numberOfNumbers,frameSelector):
    return lambda startingIndex, listOfNumbers: frameSelector(startingIndex,numberOfNumbers,listOfNumbers)

def adjacentNumbers(startingIndex,numberOfNumbers,listOfNumbers):
    return list(listOfNumbers)[startingIndex:startingIndex+numberOfNumbers]

def theDigitsOf(stringifiedNumber):
    theDigits=[]
    for digit in stringifiedNumber:
        theDigits.append((int)(digit))
    return theDigits

################
def getThePythagoreanTripletWhosSumIs1000():
    sum=1000
    maxLimit=math.ceil(sum/3)
    for a in list(range(1,maxLimit)):
        for b in list(range(a+1,sum)):
            c=(a**2+b**2)**0.5
            if a+b+c==1000:
                return a*b*c

def pro9():
    print('problem 9')
    print(getThePythagoreanTripletWhosSumIs1000())

################
def pro10():
    print('problem 10')
    print()

# pro3()
# pro5()
# pro6()
# pro7()
# pro8()
# pro9()
pro10()
