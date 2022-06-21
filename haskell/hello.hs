module Hello (hello) where

import System.IO

data BaseballPlayer = Position
  | Catcher
  | Infielder
  | Outfielder
  deriving Show

data Customer = Customer String String Double
  deriving Show

tomSmith :: Customer
tomSmith = Customer "Tom Smith" "123 main" 20.50

getBalance :: Customer -> Double
getBalance (Customer _ _ b) = b

sayHello = do
  putStrLn "What's your name?"
  name <- getLine
  putStrLn $ "Hello, " ++ name ++ "!"

writeToFile = do
  f <- openFile "test.txt" WriteMode
  hPutStrLn f ("Writing to a file")
  hClose f

readFromFile = do
  f <- openFile "test.txt" ReadMode
  cont <- hGetContents f
  putStr cont
  hClose f

fib = 1 : 1 : [a + b | (a,b) <- zip fib (tail fib)]

odds = 1 : [a + 2 | a <- odds]

data ShirtSize = S | M | L

instance Eq ShirtSize where
  S == S = True
  M == M = True
  L == L = True
  _ == _ = False

class MyEq a where
  areEqual :: a -> a -> Bool

instance MyEq ShirtSize where
  areEqual S S = True
  areEqual L L = True
  areEqual M M = True
  areEqual _ _ = False

data RPS = Rock | Paper | Scissors

shoot :: RPS -> RPS -> String
shoot Paper Rock = "paper beats rock"
shoot Rock Scissors = "rock beats scissors"
shoot Scissors Paper = "scissors beats paper"
shoot Scissors Rock = "scissors loses to rock"
shoot Paper Scissors = "paper loses to scissors"
shoot Rock Paper = "rock loses to paper"
shoot _ _ = "tie"

data Shape = Circle Float Float Float | Rectangle Float Float Float Float
  deriving Show

area :: Shape -> Float
area (Circle _ _ r) = pi * r^2
area (Rectangle x y a b) = (abs $ a - x) * (abs $ y - b)

hello :: String -> String
hello name = "Hello, " ++ name ++ "!"

sumValue = putStrLn . show $ 1 + 2 -- putStrLn (show (1 + 2))

-- This is a comment

{-
Also a comment, but with more lines :)
-}

-- Data Types

-- Int -2^23, 2^63
maxInt = maxBound :: Int
minInt = minBound :: Int

-- Integer (unbounded whole number)
-- Float, Double
bigFloat = 3.99999999999 + 0.00000000005

-- Char '
-- Tuple

always5 = 5

{- time for some math -}

addex = 5 + 4

num9 = 9 :: Int
sqrtOf9 = sqrt (fromIntegral num9)


myNums = [1,3,5,7,9]
moreNums = myNums ++ [10,11,12]
fav = 7 : myNums

z = zip [1,2,3] [4,5,6]

addMe :: Int -> Int -> Int
addMe x y = x + y

sm x y = x + y

addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples (x, y) (a, b) = (x + a, y + b)

factorial :: Integer -> Integer
factorial 0 = 1
factorial x = x * factorial (x - 1)

pfact n = product [1..n]

isOdd :: Int -> Bool
isOdd n
  | n `mod` 2 == 0 = False
  | otherwise = True

isEven n = not (isOdd n)

whatGrade :: Int -> String
whatGrade age
  | (age < 5) = "No school yet"
  | (age >= 5) && (age <= 6) = "Kindergarten"
  | (age > 6) && (age <= 10) = "Elementary School"
  | (age > 10) && (age <= 14) = "Middle School"
  | (age > 14) && (age <= 18) = "High School"
  | otherwise = "Go to college"

battingAvgRating :: Double -> Double -> String
battingAvgRating hits atBats
  | avg <= 0.200 = "Terrible"
  | avg <= 0.250 = "Average"
  | avg <= 0.280 = "Pretty good"
  | otherwise = "Superstar"
  where avg = hits / atBats

getListItems :: [Int] -> String
getListItems [] = "Empty"
getListItems (x:[]) = "Your list starts with " ++ show x
getListItems (x:y:[]) = "Your list contains " ++ show x ++ " " ++ show y
getListItems (x:xs) = "fst " ++ show x ++ " and the rest are " ++ show xs

getFst :: String -> String
getFst [] = "Empty"
getFst all@(x:xs) = "The first letter in " ++ all ++ " is " ++ [x]

times4 :: Int -> Int
times4 x = x * 4

l4 = map times4 [1,2,3,4]

mul4 :: [Int] -> [Int]
mul4 [] = []
mul4 (x:xs) = times4 x : mul4 xs

m :: (Int -> Int) -> Int
m f = f 3

n = m times4

lexample = map (\x -> x * 2) [1,2,3,4,5]


