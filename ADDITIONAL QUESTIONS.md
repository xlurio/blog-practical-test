# Additional questions

1.**A client requires uploading and downloading CSV files to your web system, how would
you implement that?**
* Reply: the IO features would be implemented by using Celery background tasks. The files would be stored in an external file system so to not fill the memory of the server and their URLs would be linked to the users in a database table.

2.**Your system consists of an application that receives a measure from a sensor through an
API and stores it in a model called “Measures”. Your client wants to configure one alarm
system that sends an email when the measure ‘temperature’ gets out of the thresholds.
What models would you implement? How do you ensure that the alarm system function
without blocking the API?**
* Reply: The API should check on every input and trigger a background task that sends the e-mail, this way, the API would not stop.

2.**A client finds they routinely make simple yet tedious and repetitive changes to many
records using Django’s admin. They request that we make an admin action so they can
update a pricing field on 10,000 records at once. How would you go about implementing
this? Describe any performance issues you expect to encounter.**
* Reply: there would be a page with all the records (limited to 10,000) on the table with a few fields for filtering, one checkbox for each record, one checkbox for selecting all records and a button for proceeding. Then the application would ask for the new price. On submitting the update, the application would make a bulk update on all selected records. It should slow down the server a little bit during the operation.
