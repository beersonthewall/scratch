CC = gcc
CLFAGS = -wall

.PHONY: clean all

all: bf

clean:
	@rm main.o bf

bf: main.o
	$(CC) $(CFLAGS) main.o -o bf

main.o: main.c
	$(CC) $(CFLAGS) -c main.c
