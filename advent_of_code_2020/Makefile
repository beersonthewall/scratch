CC=gcc
CFLAGS=-Wall -ggdb
NAME=solution

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

clean:
	rm *.o
	rm $(NAME) -f

day1: day1.o
	$(CC) -o $(NAME) day1.o

day2: day2.o
	$(CC) -o $(NAME) day2.o

day3: day3.o
	$(CC) -o $(NAME) day3.o

day4: day4.o
	$(CC) -o $(NAME) day4.o

