(define input (call-with-input-file "input.txt" read))

(set! input (cadr input))
(display (fold-left (lambda (acc fst snd)
                      (if (> snd fst)
                          (+ acc 1)
                          acc))
           0 (reverse (cdr (reverse input))) (cdr input)))

