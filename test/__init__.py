import check50



@check50.check()
def exists():
    """test.cpp exists"""
    check50.exists("test.cpp")
    
    
    
    
@check50.check(exists)
def compiles():
    """test.cpp compiles"""
    check50.run("make test.cpp")
    
    
@check50.check(compiles)
def Hello_World():
    """Prints Hello World!"""
    check50.run("./test").stdout("Hello, World!").exit(0)
