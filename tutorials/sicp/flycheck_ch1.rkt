#lang sicp


(define pi 3.14)
(define _tau (* 2 pi))
(define r 10)
(define _c (* 2 pi r))

(define (sq x) (* x x))

(define (sum-of-squares x y)
  (+ (sq x) (sq y)))

(define (f a)
  (sum-of-squares (+ 1 a) (* a 2)))

(f 20)

(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

(abs -20)


(define (>= x y)
  (or (> x y) (= x y)))

(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7)))

(define (p) (p))
(define (test x y)
  (if (= x 0)
      0
      y))

;; Infinite loop :)
;; (test 0 (p))

(define (sqrt-est guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-est (improve guess x) x)))

(define (improve guess x)
  (avg guess (/ x guess)))

(define (avg x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
  (< (abs (- (sq guess)  x)) 0.001))

(define (sqrt x)
  (sqrt-est 1.0 x))

;; Using new-if in the sqrt procedure causes an infinite loop.
;; the arguments are evaluated before applying so we continually evaluate the sqrt-est func without
;; checking the condition.
(define (new-if pred then-clause else-clause)
  (cond (pred then-clause)
        (else-clause)))

(new-if (= 2 3) 0 5)
(new-if (= 1 1) 0 5)


(define (cube-root x)

  (define (progressing? prev cur)
    (> (abs (- prev cur)) 0.001))

  (define (approximate guess x)
    (/ (+ (/ x (sq guess)) (* 2.0 guess))  3.0))

  (define (cube-root-iter-helper prev-guess guess x)
    (if (not (progressing? prev-guess guess))
        guess
        (cube-root-iter-helper guess
                               (approximate guess x)
                               x)))

  (define (cube-root-iter guess x)
    (cube-root-iter-helper guess (approximate guess x) x))
 
  (cube-root-iter 1.0 x))

(cube-root 27)

(define (factorial n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))

(define (fact n)
  (fact-iter 1 1 n))

(define (fact-iter product counter max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
                 (+ counter 1)
                 max-count)))
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1) (A x (- y 1))))))

(define (k n) (* 5 n n))

(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1))
                 (fib (- n 2))))))
(define (fib-iter n)
  (define (fib-helper a b counter n)
    (if (< counter n)
        (fib-helper b (+ a b) (+ counter 1) n)
        b))
  (fib-helper 0 1 0 n))
