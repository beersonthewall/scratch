module Main where

import System.Environment

calc :: String -> [Double] -> Double
calc op args
  | op == "sum" = sum args
  | op == "product" = product args
  | op == "mean" = (sum args) / fromIntegral (length args)
  | otherwise = 0.0

main = do
  args <- getArgs
  putStrLn $ show $ calc (head args) $ map read $ tail args
