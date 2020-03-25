# kubernetes-docker-desktop

My setup for kubernetes running on Docker Desktop for Mac.
For my own learning experience only.

## TODO

* Authorization webhook for logging incoming `SubjectAccessReview` objects.
    * Create simple service to always allow with logging.
    * Configure service with TLS (required for authorization webhook).
    * Configure authorizatin webhook.
* Setup services and ingresses.
* Automate "cluster provisioning".

## Notes

* To "ssh" into the node VM: `screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty`
    * TODO: Figure out if there are other options available, like copying files into the VM