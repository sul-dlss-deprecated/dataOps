package main

import (
	"bufio"
	"crypto/tls"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	var inFile = "data/druidList.txt"
	var fedURL = "https://dor-prod.stanford.edu/fedora/objects/%s/objectXML"
	var outDir = "data/foxml/"

	input, err := os.Open(inFile)
	checkError(err)
	defer input.Close()

	scanner := bufio.NewScanner(input)
	n := 0
	for scanner.Scan() {
		outFile := outDir + strings.Replace(scanner.Text(), "druid:", "", -1) + ".xml"
		reqURL := fmt.Sprintf(fedURL, scanner.Text())
		log.Print("URL retrieved: " + reqURL)

		cert, err := tls.LoadX509KeyPair("/etc/ssl/certs/dlss-dev-cmharlow-dor-prod.crt", "/etc/ssl/certs/private/dlss-dev-cmharlow-dor-prod.key")
		if err != nil {
			log.Fatal(err)
		}

		client := &http.Client{
			Transport: &http.Transport{
				TLSClientConfig: &tls.Config{
					Certificates: []tls.Certificate{cert},
				},
			},
		}

		resp, err := client.Get(reqURL)
		checkError(err)
		defer resp.Body.Close()

		out, err := os.Create(outFile)
		checkError(err)
		defer out.Close()
		defer resp.Body.Close()

		_, err = io.Copy(out, resp.Body)
		checkError(err)
		out.Close()
		resp.Body.Close()
		n++
		log.Print(n)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
