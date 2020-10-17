# Docker Raspbian Temp Reporter

## What is this ?

Small utility to send out the temperature of your Raspberry Pi (running Raspbian) to an external URL. It also posts the host name in case you are monitoring a Raspberry Pi swarm or something cool like that.

## Why ?

I've always found myself wanting to monitor my Raspberry Pi's temperature remotely. So I'd just run one of these containers in each and presto. Don't have to bother coding. And yes I do work my Pi's hard and install fans and stuff like that, especially for my commercial products. Hppefully it will be of use to you too!

## How do I run it?

Install docker. Check out the documentation here > https://docs.docker.com/engine/install/debian/

To run the version over at Docker hub which is "stable" and I maintain, type

```
docker run -d -v /sys/class/thermal/thermal_zone0/temp:/app/temp -v /etc/hostname:/app/hostname -e POST_SECONDS=10 -e POST_URL="http://docker-raspbian.jangita.io/temp" jangita/raspbian-temp-post:latest
```

To run the version from this repo which is bleeding edge and may break, but has the latest and greatest features, first build from this Github repo then run: 
```
docker build -t raspbian-temp-post https://github.com/jangita/docker-raspbian-temp.git
```
when that is done, run 
```
docker run -d -v /sys/class/thermal/thermal_zone0/temp:/app/temp -v /etc/hostname:/app/hostname -e POST_SECONDS=10 -e POST_URL="http://docker-raspbian.jangita.io/temp" raspbian-temp-post
```
and it should be up and running.

## Can I configure which URL it POSTs to and how often it POSTs ?

Yes! Just change the environment variables POST_URL and POST_SECONDS which in the above commands points to my test server and 10 seconds. This is how often the temperature is checked and posted and which URL the details are posted to. You can also set them in your docker_compose.yml file and so on. Note that the service does not terminate if the URL is invalid, but it will terminate if the environment variables do not make sense e.g POST every "Chris" seconds 🤣 instead of 20 seconds.

## What format does it POST in?

The information is posted as JSON on the HTTP body like so
```
    {
        "host": "myraspberry"
        "temp": 338459
    }
```

The temperature is in millidegrees C  milli = thousandths of a degree Celcius - Thanks! French!) so divide by 1000 to give you degrees C and do the nessesary to convert to degrees F or Kelvin if you are feeling scientific 😎

## Contributing

Would greatly appreciate a coffee to put up and maintain more opensource stuff. Buy me one here ☕ https://paypal.me/exoscale

Things to do:
1. Tighten up and lock down the versioning
2. Better logging

As always, all contributions of whatever nature are welcome. Just

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request 😁
