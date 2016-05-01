# DataAnalysisScripts
Scripts for quickly analyzing csv files

# LT.awk - LessThan

USAGE

cat "CSVFILE" |./LT.awk fieldtoanalyze valuetocheck

for example 

$ cat XOM.csv|./LT.awk 7 100

will only grab order sizes that were less than 100 shares since field 7 is Quantity.

EndTimeMS,StartTimeMS,OrdNum,OrdType,OrdChange,Symbol,Quantity,Price

 53159592,53158997,432534079,B,F,XOM,64,600000  
 53159779,53159617,433201185,S,E,XOM,34,600900  
 53159781,53159618,433201513,S,C,XOM,36,601300  
 53159829,53159783,433201185,S,F,XOM,66,600900  
 53159999,53159848,433233473,B,F,XOM,66,600800  

# GT.awk - GreaterThan

USAGE

cat "CSVFILE" |./GT.awk fieldtoanalyze valuetocheck

for example

$ cat XOM.csv|./GT.awk 7 10000

will only grab order sizes that were greater than 10000 shares since field 7 is Quantity.

EndTimeMS,StartTimeMS,OrdNum,OrdType,OrdChange,Symbol,Quantity,Price

52779637,52779608,405876241,B,D,XOM,20000,641200  
52865219,50912599,336169958,S,D,XOM,20000,662800  
56066348,56066348,559394914,T,T,XOM,23450,632000  
56912431,56912426,594433546,B,D,XOM,113188,644300  
56912686,56912684,594450908,B,D,XOM,104600,644800  

# CONVERT.awk

USAGE

echo "TimeinMSafterMidnight"|./MS_AFTER_MIDNIGHT_CONVERT.awk

for example

$ echo 52964083|./MS_AFTER_MIDNIGHT_CONVERT.awk

14:42:44.083,52964083

Note I print the converted time followed by $0 so if your first field of an CSV contains the timestamp you can do the following
$ cat XOM.csv|./MS_AFTER_MIDNIGHT_CONVERT.awk

and as long as the timestamp in milliseconds is the first field, it all append the rest of the line after the converted timestamp.

14:42:44.135,52964135,52964135,415013695,T,T,XOM,300,639300  
14:42:44.135,52964135,52913010,412835503,B,F,XOM,100,639200  
14:42:44.135,52964135,52947118,414435037,B,F,XOM,200,639200  
14:42:44.135,52964135,52947119,414435056,B,F,XOM,200,639200  
14:42:44.135,52964135,52964134,415051224,B,E,XOM,300,639200  
 
# SUBSTR.awk

USAGE 

echo "CSV_FILE"|./SUBSTR.awk field value

for example

cat XOM.csv|./SUBSTR.awk 1 5 

52964,52964135,52964135,415013695,T,T,XOM,300,639300
52964,52964135,52913010,412835503,B,F,XOM,100,639200
52964,52964135,52947118,414435037,B,F,XOM,200,639200

The script too the first field "52964135"  and grabbed the first 5 numbers/characters from the left then added that value to the beginning of the line.  What this allows you to do is quickly do a groupby like function -- for instance in the case above we just need to create a pipeline command as follows

cat XOM.csv|./SUBSTR.awk 1 5|cut -f1 -d,|sort -n|uniq -c|sort -rn|head -5

     54 53316
     37 53133
     33 53561
     33 53167
     26 53127

So we first dumped our file and used SUBSTR.awk to convert to seconds after midnightm, then we grabbed just the first field, sorted it numerically (for uniq to work), used uniq to count the number of lines per first field and then sorted by number of lines to determine which second had the most orders.

If you want to clean up the pipeline, just use Brendan Gregg's perl script "freqcount", which is a lot cleaner and useful than cut/sort/uniq

cat XOM.csv|./SUBSTR.awk 1 5|./freqcount -f1 -d,|head -5

54:53316  
37:53133  
33:53561  
33:53167  
26:53127  
 

