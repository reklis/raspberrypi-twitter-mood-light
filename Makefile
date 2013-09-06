all:
	mkdir bin
	gcc startlight.c -o bin/startlight

clean:
	rm -rf bin