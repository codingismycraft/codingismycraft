package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

const FILENAME = "file-with-duplicates"

func main() {
	full_path, err := filepath.Abs("ex_01_04.go")
	if err != nil {
		log.Fatal(err)
	}
	full_path = filepath.Dir(full_path)
	filename := filepath.Join(full_path, "static", FILENAME)

	fmt.Println(filename)

	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	lineCounter := make(map[string]int)

	input := bufio.NewScanner(f)
	for input.Scan() {
		lineCounter[input.Text()] += 1
	}

	for s, c := range lineCounter {
		if c > 1 {
			fmt.Printf("%d %s\n", c, s)
		}
	}
}
