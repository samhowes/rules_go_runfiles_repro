package main

import (
	"os"
	"path"

	"github.com/bazelbuild/rules_go/go/tools/bazel"
)

func main() {
	cwd, _ := os.Getwd()
	if os.Getenv("RUNFILES_MANIFEST_FILE") == "" {
		_ = os.Setenv("RUNFILES_MANIFEST_FILE", path.Join(cwd, "MANIFEST"))
	}

	fpath, err := bazel.Runfile("important.txt")
	if err != nil {
		panic(err)
	}

	contents, err := os.ReadFile(fpath)
	if err != nil {
		panic(err)
	}
	_, _ = os.Stdout.Write(contents)
}
