# sha3

[FIPS 202 compliant](http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
SHA-3 core written in Verilog. The core is written in fairly
conservative Verilog 2001 style. There is a functional model
written i Python that is used to drive the HW implementation.

The core implements SHA3-224, SHA3-256, SHA3-384 and SHA3-512.


## Implementation ##

The core file contains all sha3 specific functionality. The top level
sha3.v file provides a simple 32-bit interface for the core. For
applications that integrates sha3 into a construction, the top level
wrapper can be removed.



## Status ##

*** (2016-01-05)***

Initial implementation started. Not much to see and even
less to use at the moment.
