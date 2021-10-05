
You just can't run it on a Mac since Macs don't have ARM CPUs. If you install Xcode with iOS support, you can compile ARM code:

1. Create a assembly file with “.s” extension

    `$ touch hello.s`
2. compile with llvm-gcc

    `$ clang -arch armv7s -c hello.s`

```
# resulting file is ARM object file
```
$ file foo.o

foo.o: Mach-O object arm

# and you can disassemble it

`$ otool -v -t foo.o`

[source](https://www.quora.com/How-do-I-run-ARM-Assembly-language-on-a-Mac)