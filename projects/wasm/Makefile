CC=gcc
CFLAGS = -Wall -Wextra -Werror -Wfloat-equal -Wpointer-arith -Wundef \
-Wcast-align -Wshadow -Wstrict-prototypes -Wwrite-strings -Wunreachable-code \
-Wcast-qual -Wswitch-default -Wswitch-enum -Wconversion -Wno-unused-variable \
-Wno-unused-parameter

FILES=tinywasm.c

tinywasm: $(FILES)
	$(CC) $(CFLAGS) $(FILES) -o $@

clean:
	rm tinywasm tinywasm-asan

tinywasm-asan:
	$(CC) $(CFLAGS) -fsanitize=address $(FILES) -o $@

.PHONY: run
run: tinywasm
	./tinywasm example-binaries/h.wasm

