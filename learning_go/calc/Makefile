.PHONY: fmt build test run clean

build: fmt
	@mkdir -p build/
	@go build -o build/calc cmd/main.go

fmt:
	@go fmt cmd/*.go
	@go fmt calc/*.go

test: build
	@go test ./calc

clean:
	@go clean
	@rm -rf build/

