// Day 1 (Go)

package main

import (
  "bufio"
  "fmt"
  "strconv"
  "os"
)

func main() {
  file := "../day01-input.txt"
  
  f := first(file)
  s := second(file)

  fmt.Println("First:", f)
  fmt.Println("Second:", s)
}

func first(f string) int {
  total := 0

  file, err := os.Open(f)
  if err != nil {
    fmt.Println("Open file error!")
    panic(err)
  }

  defer file.Close()

  sc := bufio.NewScanner(file)
  
  var line string
  for sc.Scan() {
    // Read line
    line = sc.Text()
    
    if num, err := strconv.Atoi(line); err == nil {
      total += num
    }
  }

  if err := sc.Err(); err != nil {
    fmt.Println("Error scanning line!")
    panic(err)
  }

  return total
}

func second(f string) int {
  total := 0
  // Create a map
  m := make(map[int]bool)

  for {

    file, err := os.Open(f)
    if err != nil {
      fmt.Println("Open file error!")
      panic(err)
    }
    defer file.Close()

    sc := bufio.NewScanner(file)

    var line string
    for sc.Scan() {
      // Read line
      line = sc.Text()

      if num, err := strconv.Atoi(line); err == nil {
        total += num

        // The second return value when getting a value from a map
        // indicates the presence of a key
        // This is used to disambiguate between missing keys and keys with
        // values such as 0 or ""
        if _, exists := m[total]; exists {
          return total
        }

        m[total] = true
      }
    }

    if err := sc.Err(); err != nil {
      fmt.Println("Error scanning line!")
      panic(err)
    }
  }
}
