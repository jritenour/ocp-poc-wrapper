#!/usr/bin/python3
'''
Author: Jason Ritenour
This is wrapper script for instantiating a containerized ansible playbook that checks for the necessary prerequisites to deploy OpenShift 4.x.  It is distributed "as is" and should only be run if directed to do so by a Red Hat employee.
'''

import os

runtime = input("Please enter the name of your container runtime - either 'docker' or 'podman'  ")

offline = input("Will this be an disconnected/airgapped installation? 'yes' or 'no' ")
if offline == "yes":
   skip = " "
   reg_addr = input("If doing a disconnected install, please enter your registry address WITHOUT the http/https prefix, but including the port, eg registry.example.com:5000  ")
   reg_user = input("If doing a disconnected install, please enter your registry username.  ")
   reg_pass = input("If doing a disconnected install, please enter your registry password.  ")
   image_path = input("If doing a disconnected install, please enter the image path including the leading forward slash, eg /ocp4/openshift4.  ")
elif skip == "no":
   skip = "--skip-tags offline"
else: 
  print("Please enter 'yes' or 'no'")
domain = input("Please enter the domain name OpenShift will be installed in eg. example.com  ")
cluster = input("Please enter the name of your planned OpenShift cluster (subdomain prefix, eg ocp.example.com, wherein ocp would be the cluster name  ")

print ("Your input is as follows:")

print(runtime)
print(domain)
print(cluster)
print(reg_addr)
print(reg_user)
print(image_path)

vars=str(f"{domain=} -e {cluster=}   -e {reg_addr=}  -e {reg_user=} -e {reg_pass=} -e  {image_path=}")
command = runtime + " run --net=host -it docker.io/jmritenour/ansible-ocp-poc:latest ansible-playbook /site.yaml  -e " + vars + " | tee poc-report.txt"
print(command)
os.system(command)
