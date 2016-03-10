"# edmodo-search"


1. pip install -r "requirements.txt" (in virtualenv)
2. python setup.py  
3. python app.py to run server
4. done! :)


===NOTES===

Didn't have as much time to modularize the code as I would've liked. Evidently there
exists flask rest framework that could've been used. Alas the implementation used
here was rather hacky to my distress.


Angular code in the future will involve using directives for components rather than
using bootstrap components. It's useful, but definitely becomes unruly when you don't have
complete control over the javascript available to you. Perhaps only the css framework
makes sense to use.


This project definitely focuses more on the front end rather than the backend which is a
shame because I think there is a lot of potential to make a very sustainable custom rest
framework with flask. Perhaps given django-rest-framework exists, the use case
is questionable.


In retrospect, using sqlAlchemy would've been a more sustainable solution in the long run
for sufficiently large applications. I was just lazy and wanted to get the queries
out of the way without thinking about it much. Regardless, making a db access component of the
app would be useful for the future. Having queries inside the routing code is very ugly.


DB connector as part of the app is also super useful when you want to have a caching layer.
At this point I'm not sure what you'd be caching other than perhaps common searches or products
but it's definitely more convenient than serving up directly from the db. Personally
I like having a large object with all of the data stored as fields in dictionaries load at start time. This obviously
presupposes the absence of something like redis.
