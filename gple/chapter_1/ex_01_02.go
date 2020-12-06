package main

import (
	"fmt"
	"os"
)

func main() {
	argCount := len(os.Args)
	fmt.Printf("Number of arguments %d\n", argCount)

	for i, arg := range os.Args {
		fmt.Printf("Arg[%d] = %s\n", i, arg)
	}
}
