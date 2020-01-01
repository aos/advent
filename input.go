package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	if len(os.Args) <= 1 {
		fmt.Println("No day number was passed in")
		os.Exit(1)
	}

	cookie, err := getCookie()
	if err != nil {
		fmt.Printf("%s\n", err)
		os.Exit(1)
	}

	req, err := http.NewRequest(
		"GET",
		fmt.Sprintf("https://adventofcode.com/2019/day/%s/input",
			os.Args[1]),
		nil)
	if err != nil {
		fmt.Println("error: unable to form request")
		os.Exit(1)
	}

	req.AddCookie(
		&http.Cookie{
			Name:  "session",
			Value: cookie.Session})
	client := new(http.Client)
	resp, err := client.Do(req)
	if resp.StatusCode != 200 {
		fmt.Printf("error: status code %d\n", resp.StatusCode)
		os.Exit(1)
	}
	defer resp.Body.Close()

	io.Copy(os.Stdout, resp.Body)
}

type cookie struct {
	Session string `json:"session"`
}

func getCookie() (*cookie, error) {
	in, err := ioutil.ReadFile("cookie.json")
	if err != nil {
		return nil, errors.New("getCookie: error reading file")
	}

	c := new(cookie)
	err = json.Unmarshal(in, c)
	if err != nil {
		return nil, errors.New("getCookie: error decoding json")
	}
	return c, nil
}
