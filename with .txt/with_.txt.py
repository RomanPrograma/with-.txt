try:
    f = open( "with_.txt", "r" )
    content = f.readlines()
    content.sort()
    open( "with_.txt", "w" ).writelines( content )
except Exception as e:
    print( "Error: " + str(e) )
finally:
    print( "Done!" )
    f.close()