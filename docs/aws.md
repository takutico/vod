### AWS Elastic Beanstalk

It's a PaaS that allow user to deploy apps in EC2, S3, SNS, autoscaling and Elastic Load Balancers. You can find hoe to deploy Django Apps in to EB
http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

### For this tutorial you should have and AWS account and already created an EC2 instance and access it via ssh

```$ sudo apt-get update```

Apache2 install

```$ sudo apt-get install apache2```

MySQL install, this is in case you want to install DB locally instead of using RDS.

```$ sudo apt-get install mysql-server mysql-client```

PHP install. I install PHP basically to check installation and install phpmyadmin to administrate MySQL database.

```$ sudo apt-get install php5 libapache2-mod-php5 php5-mysql php5-mcrypt```

check PHP installation

```$ sudo nano /var/www/html/info.php```
```
	<?php
	phpinfo();
	?>
```

Now you should be able to access info.php

Install phpMyAdmin

```
$ sudo apt-get install phpmyadmin
$ sudo ln -s /usr/share/phpmyadmin /var/www/html/
```

Install git

```$ sudo apt-get install git```

create a project folder

```$ mkdir ~/vod```

Install virtualenv

```$ sudo apt-get install python-virtualenv```

Now you can follow [Readme](../README.md) file

For using Django with Apache you need to follow [this](https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/modwsgi/) you can find apache conf file in this folder