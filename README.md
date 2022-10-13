# Blog Practical Test

## Requirements

* Docker
* Docker Compose


## Setting up

To set up the application, you can run the following command:

* On Windows:

```
$ docker build . -t blog
```

* On Linux:

```
$ sudo docker build . -t blog
```


## Running

Now, to run the application, all you need to do is run the following command:

* On Windows:

```
$ docker run -p 8000:8000 blog
```

* On Linux:

```
$ sudo docker run -p 8000:8000 blog
```

You'll will already have a staff user with the following credentials:

```
email: admin@blog.com
password: password
```
