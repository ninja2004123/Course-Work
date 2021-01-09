import check50


@check50.check()
def exists():
    """caesar.c exists."""
    check50.exists("test.cpp")
	
	
	
@check50.check(exists)
def compiles():
    """caesar.c compiles."""
    check50.c.compile("test.cpp", lcs50=True)
	
	
	
@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("./test").stdout("Hello, Wolrd!").exit(0)
