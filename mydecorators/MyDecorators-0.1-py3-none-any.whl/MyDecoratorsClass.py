def Benchmark( function ):

    def Wrapper( *args, **kwargs ):
        from timeit import default_timer
        start_time = default_timer ()
        function( *args, **kwargs )
        end_time = default_timer ()
        delim = "-"*50
        print( "\n " + delim + "\n | ", function.__name__,": ", '{:.10f}'.format ( end_time - start_time ), "seconds\n " + delim )
    
    return Wrapper