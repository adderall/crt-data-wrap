# Introduction #

This page discusses how the rets.yaml file can be configured to pull from RETS servers to create Atom feeds as well as how to interact with the Atom feeds and perform queries.

## Configuring ##

Proxy configuration is done by modifying the rets.yaml file.  In this file you can set up RETS servers, only one of which can be active at any time.  You must restart the server to trigger the configuration file to be restarted

The alias field allows you to set up keywords for categories that span multiple class types.  When implemented the proxy will run multiple searches, aggregate the results and return them in a single result set.

There is documentation about the different fields and why their nomenclature was chosen at the top of rets.yaml.

You can have multiple servers defined, the top server labeled “activeserver” is the server that will be used.

The default yaml file has CRT, MRED, and Metrolist (Denver) as examples, but there is not valid login information for any server except CRT.

The default yaml file covers res, com, and agt classes but you can define any combination of resource and class by following the template provided.

The fields on the left are the fields that users should use to interact with your proxy, the field names on the right are the field names that will be sent to/selected from the RETS server.


## Interacting ##

Use any browser interface to conduct queries against the proxy server.

Here are some sample queries for the default configuration:

http://127.0.0.1:8000/Translator/Properties/-/res/?ListPrice=250000
http://127.0.0.1:8000/Translator/Properties/-/res/?BedsTotal=4%2b
http://127.0.0.1:8000/Translator/Properties/-/res/?YearBuilt=1978-1985

http://127.0.0.1:8000/Translator/Properties/-/alias/?BedsTotal=4%2b
(with default yaml, this will search across res and com)

http://127.0.0.1:8000/Translator/Properties/-/res|com/?BedsTotal=4%2b
(this searches across res and com)

http://127.0.0.1:8000/Translator/Properties/-/agt/?FirstName=a%2b


[Syntax Guide](http://code.google.com/apis/gdata/docs/2.0/reference.html)