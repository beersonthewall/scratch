CC := gcc
FLAGS := -Wall -Werror -Wextra

calc: main.o
	$(CC) $(FLAGS) main.o -o calc

main.o: main.c
	@$(CC) $(FLAGS) -c main.c

.PHONY: run
run: calc
	./calc $(ARGS)

