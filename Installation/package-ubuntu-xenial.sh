# Only the nightly packages are build for Ubuntu 16.04, but the steps are very straightforward.
# No need to upgrade the kernel or complile from source!

echo "deb [trusted=yes] https://repo.iovisor.org/apt/xenial xenial-nightly main" | sudo tee /etc/apt/sources.list.d/iovisor.list
sudo apt-get update
sudo apt-get install bcc-tools libbcc-examples
