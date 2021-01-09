import check50


@check50.check()
def exists():
    """test.cpp exists."""
    check50.exists("test.cpp")
	
	
	
@check50.check(exists)
def compiles():
    """test.cpp compiles."""
    check50.c.compile("test.cpp", lcs50=True)
	
	
	
@check50.check(compiles)
def encrypts_a_as_b():
    """Runs Hello World"""
    check50.run("./test").stdout("Hello, Wolrd!").exit(0)
