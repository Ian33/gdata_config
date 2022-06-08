# gdata_config
Configure gdata
I had made a guide but it was hard to keep it updated
To find a parameter the best bet is to look at the codee file

The config file can either be stored in the working directory, or a file extension can be added to your code

Origionally gData's "FlowLevel" was , with limited supportused for discharge.  This is still in the config file"
For discharge use the parameter "discharge"

all parameters *should* be lowercase.  If you find one that isnt, I would suggest writing code that works for both cases.
This is fighting a bad habit of mine!
example: config[parameter]['Conductivity'] or config[parameter]['conductivity']

This is a work in progress, I am happy to accept feedback
