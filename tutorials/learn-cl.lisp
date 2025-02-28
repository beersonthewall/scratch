(defun foo (a b c)
  (* a b c))

(defun isPalindrome (s)
  "Returns true if s is a palindrome (a word or phrase that reads the same 
   backwards and forwards)."
  (equal s (reverse s)))


(defun fib (n)
  "Calculates the n-th Fibonacci number. f(n) = f(n-1) + f(n-2)"
  (defun f (count fst snd)
    (if (= count n)
	fst
	(f (+ count 1) snd (+ fst snd))))
  (f 0 1 1))

(let ((str "Hello, world!"))
  (string-upcase str))

(let ((x 1)
      (y 5))
  (+ x y))

(let* ((x 1)
       (y (+ x 1)))
  y)

(let ((x (list 1 2 3)))
  (+ (first x) (first (last x))))


(let ((x (list 1 2 3 4 5)))
  (setf (nth 2 x) 12)
  x)

(defun inc (x)
  (+ x 1))

(mapcar #'inc (list 1 2 3 4 5 6))

(reduce #'+ (list 1 2 3))

(reduce #'(lambda (a b)
	    (format t "A: ~A, B: ~A~%" a b)
	    (* a b))
	(list 10 20 30))

(sort (list 320 1 32 3 4 91 12 2 3 9 0) #'<)

(defun my-destr (list)
  (destructuring-bind (fst snd &rest others)
      list
    (format t "First: ~A~%" fst)
    (format t "Second: ~A~%" snd)
    (format t "Rest: ~A~%" others)))

(with-open-file (stream (merge-pathnames #p"data.txt"
					 (user-homedir-pathname))
			:direction :output  ;; Write to disk
			:if-exists :supersede ;; overwrite file
			:if-does-not-exist :create)
  (dotimes (i 100)
    ;; Write random numbers to file
    (format stream "~3,3f~%" (random 100))))

(defun foo (a b c)
  (values a b c))

(multiple-value-bind (r1 r2 r3)
    (foo :a :b :c)
  (format t "~a, ~a, ~a" r1 r2 r3))

(defun at (lst)
  (mapcar (lambda (x)
	    (+ x 3))
	  lst))

(defun curry (f &rest args)
  (lambda (&rest more-args)
    (apply f (append args more-args))))
(apply (curry #'+ 3) 3)
