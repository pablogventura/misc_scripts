#!/usr/bin/env python
# encoding: utf-8

import optparse
import os
import sys

def main():

    parser = optparse.OptionParser()
    parser.add_option("-d", "--diseno",
        help="Archivo del disenno")
    parser.add_option("-t", "--test",
        help="Archivo del test")
    parser.add_option("-a", "--a64", default=False,
                  help="Para arquitecturas de 64 bits")
    options, args = parser.parse_args()

    diseno = options.diseno
    test = options.test
    a64 = bool(options.a64)
    
    if diseno == None or test == None:
        print "Script para hacer test con ghdl"
        parser.print_help()
        sys.exit(0)
    
    if a64:
        comando = "ghdl -a -Wc,-m32 -Wa,--32 " + diseno
        os.system(comando)
        comando = "ghdl -a -Wc,-m32 -Wa,--32 " + test
        os.system(comando)
    else:
        comando = "ghdl -a " + diseno
        os.system(comando)
        print comando
        comando = "ghdl -a " + test
        os.system(comando)
        print comando
    
    entidad_test = test.split(".",1)[0]

    if a64:
        comando = "ghdl -e -Wa,--32 -Wl,-m32 " + entidad_test
        os.system(comando)
        print comando
    else:
        comando = "ghdl -e " + entidad_test
        os.system(comando)
        print comando

    comando = "ghdl -r " + entidad_test + " --stop-time=138ns --vcd=result.vcd"
    os.system(comando)
    print comando
    
    comando = "gtkwave result.vcd"
    os.system(comando)
    
    
if __name__ == "__main__":
    main()
    
