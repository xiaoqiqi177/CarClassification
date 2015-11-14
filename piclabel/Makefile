FLAG := `pkg-config --cflags --libs opencv`

all: piclabel.o


piclabel.o: piclabel.cpp
	g++ piclabel.cpp -o piclabel.o $(FLAG)

clean:
	rm -f *.o
