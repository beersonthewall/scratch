CPPFLAGS=-Wall -Wextra -Werror -Wconversion -fsanitize=address -fsanitize=undefined -g
CC=g++

m: vec.o main.o
	$(CC) $(CPPFLAGS) -o m vec.o main.o

vec.o: vec.h vec.cpp
	$(CC) $(CPPFLAGS) -o vec.o -c vec.cpp

main.o: main.cpp
	$(CC) $(CPPFLAGS) -o main.o -c $<

.PHONY: clean
clean:
	rm m *.o

