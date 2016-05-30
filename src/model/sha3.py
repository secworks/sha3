#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# sha3.py
# -------
# Simple, pure Python model of the SHA-3 function specified in
# FIPS-202. The model is used as a reference for the HW implementation.
# The code follows the structure of the HW implementation as much
# as possible.
#
#
# Author: Joachim Strömbergson
# Copyright (c) 2015 Assured AB
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or
# without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

#-------------------------------------------------------------------
# Python module imports.
#-------------------------------------------------------------------
import sys


#-------------------------------------------------------------------
# Constants.
#-------------------------------------------------------------------
VERBOSE = True


#-------------------------------------------------------------------
# print_digest()
#
# Print the given digest.
#-------------------------------------------------------------------
def print_digest(digest):
    print("0x%08x, 0x%08x, 0x%08x, 0x%08x" %\
          (digest[0], digest[1], digest[2], digest[3]))
    print("0x%08x, 0x%08x, 0x%08x, 0x%08x" %\
          (digest[4], digest[5], digest[6], digest[7]))
    print("")


#-------------------------------------------------------------------
# compare_digests()
#
# Check that the given digest matches the expected digest.
#-------------------------------------------------------------------
def compare_digests(digest, expected):
    if (digest != expected):
        print("Error:")
        print("Got:")
        print_digest(digest)
        print("Expected:")
        print_digest(expected)
    else:
        print("Test case ok.")


#-------------------------------------------------------------------
# single_block_tests()
#
#
#-------------------------------------------------------------------
def single_block_tests()
    # TC1: NIST testcase with message "abc"
    print("TC1: Single block message test specified by NIST.")
    TC1_block = [0x61626380, 0x00000000, 0x00000000, 0x00000000,
                 0x00000000, 0x00000000, 0x00000000, 0x00000000,
                 0x00000000, 0x00000000, 0x00000000, 0x00000000,
                 0x00000000, 0x00000000, 0x00000000, 0x00000018]

    TC1_expected = [0x3a985da74fe225b2, 0x045c172d6bd390bd,
                    0x855f086e3e9d525b 0x46bfe24511431532]


#-------------------------------------------------------------------
# main()
#
# If executed tests the SHA3 model using known test vectors.
#-------------------------------------------------------------------
def main():
    print("Testing the SHA-3 Python model.")
    print("-------------------------------")
    print


#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF sha3.py
#=======================================================================
