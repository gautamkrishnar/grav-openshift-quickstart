# Grav on openshift

Grav is a Fast, Simple, and Flexible, file-based Web-platform. It follows similar principles to other flat-file CMS platforms, but has a different design philosophy than most. Grav comes with a powerful Package Management System to allow for simple installation and upgrading of plugins and themes, as well as simple updating of Grav itself.

More information can be found at: http://www.getgrav.org/

### Install with one click


Create an account at http://openshift.redhat.com/

[![Click to install OpenShift](http://launch-shifter.rhcloud.com/launch/light/Click to install.svg)](https://openshift.redhat.com/app/console/application_type/custom?&cartridges[]=php-5.4&initial_git_url=https://github.com/gautamkrishnar/grav-openshift-quickstart.git&name=grav)

### How to use
After installing you can login to admin console(still in beta) by pointing your browser to: http://grav-yourdomain.rhcloud.com/admin

     username:admin
     password:password

Don't forget to change your password after logging in  for the first time.

If you are experiencing any problems, please don't forget to open a [new issue](https://github.com/gautamkrishnar/grav-openshift-quickstart/issues/new) in this repository.
### Installing via the command line


Create a PHP application :

	rhc app create grav php-5.4

You can also use any other custom name instead of 'grav'. Remember to use that app name in the next command

Add this upstream grav quickstart repo

	cd grav
	rm php/index.php
	git remote add upstream -m master git://github.com/gautamkrishnar/grav-openshift-quickstart.git
	git pull -s recursive -X theirs upstream master

Push the repo upstream to OpenShift

	git push        

Head to your application at:

	http://grav-$yourdomain.rhcloud.com

To give your new Grav site a web address of its own, add your desired alias:

	rhc app add-alias -a grav --alias "$whatever.$mydomain.com"

Then add a cname entry in your domain's dns configuration pointing your alias to $whatever-$yourdomain.rhcloud.com.
