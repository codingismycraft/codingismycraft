package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	var args [10000]string
	const arrayLen = len(args)
	for i := 0; i < arrayLen; i++ {
		args[i] = "junk"
	}

	start := time.Now()
	// Merge using the + operator
	s := ""
	sep := ""
	for i := 0; i < arrayLen; i++ {
		s += sep + args[i]
		sep = " "
	}
	secs1 := time.Since(start).Seconds()
	fmt.Printf("Duration using +: %f\n", secs1)

	start = time.Now()
	s = strings.Join(args[:], " ")
	secs2 := time.Since(start).Seconds()
	fmt.Printf("Duration using join: %f\n", secs2)

	rate := int(secs1 / secs2)
	fmt.Printf("Join is %d times faster than +\n", rate)

}
