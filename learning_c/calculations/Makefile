CC := gcc

calc: main.o
	$(CC) main.o -o calc

main.o:
	@$(CC) -c main.c

.PHONY: run
run: calc
	./calc $(ARGS)

