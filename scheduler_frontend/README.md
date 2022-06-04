# Install Qt

- Download the [Qt online installer](https://www.qt.io/cs/c/?cta_guid=074ddad0-fdef-4e53-8aa8-5e8a876d6ab4&signature=AAH58kEZYyJcx7Nx1l_9Xu9U8TKPOFLMAA&pageId=12602948080&placement_guid=99d9dd4f-5681-48d2-b096-470725510d34&click=6a2a4ec2-06b0-475a-a0b8-2487a783ae8d&hsutk=&canon=https%3A%2F%2Fwww.qt.io%2Fdownload-open-source&portal_id=149513&redirect_url=APefjpGe9BeNjmbTNjjOVaUxQ3UINmPaNltUQUFw9WtisaazJB6bM16TdbmvQCYN6jjg43oTfpGXOvtyL_pWcP4JGWAJuRW6Pd0eqiz0A49z9-wHVaWQzNxRIEJBHU3dlJqX_ooMuEC9)
- Run the online installer and select Qt 6.2.4 with Qt WebAssembly
- (I had to build Qt WebAssembly from source for it to work)

# Install emscripten (2.0.14 required for Qt WebAssembly, not latest)

```bash
cd ~

# Get the emsdk repo
git clone https://github.com/emscripten-core/emsdk.git

# Enter that directory
cd emsdk

# Fetch the latest version of the emsdk (not needed the first time you clone)
git pull

# Download and install the latest SDK tools.
./emsdk install 2.0.14

# Make the "latest" SDK "active" for the current user. (writes .emscripten file)
./emsdk activate 2.0.14

# Activate PATH and other environment variables in the current terminal
source ./emsdk_env.sh

echo 'source "~/emsdk/emsdk_env.sh" 2>> /dev/null' >> ~/.bashrc
```
