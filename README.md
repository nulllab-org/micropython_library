# Micropython Library

## Directory Introduction

The **library** directory contains library files for various sensors that can be used with boards running Micropython firmware. You need to manually upload these library files to the board. Our customized firmware will automatically include these library files for ease of use.

The **main.py** under each directory in the **examples** directory are reference code samples for using the libraries under library. They can be directly uploaded to the board and run.

## Quick Start

First you need an ESP32 board running Micropython firmware. You can refer to the official documentation for downloading and flashing: <https://micropython.org/download/ESP32_GENERIC/>. It is recommended to download the latest v1.21.0 stable version directly: [**v1.21.0 (2023-10-05) .bin**](https://micropython.org/resources/firmware/ESP32_GENERIC-20231005-v1.21.0.bin)

After flashing, open any serial tool on your computer, select the USB port corresponding to your board, and set the baud rate to 115200. When you restart the board, you should see the serial tool printing Micropython version info normally, indicating successful flashing and running, like below:

```text
MicroPython v1.21.0-3 on 2023-11-22; Generic ESP32 module with ESP32
Type "help()" for more information.
>>>
```

## Upload Files

There are many command line and GUI tools for uploading files to Micropython. If you don't know which one to use, you can use the command line tool **adafruit-ampy**. Refer to the [official documentation](https://pypi.org/project/adafruit-ampy/) for installation and usage.

**ampy** uses serial port, so you need to stop the serial tool before using ampy. Then you can use the following commands to view the files on the ESP32 to verify if ampy is working properly. For example, if the ESP32 is connected to COM1 port on Windows, the command to list files is:

```shell
ampy -p COM1 ls
```

It should list **/boot.py** etc if working properly.

## Run Examples and Libraries

Let's take a passive buzzer as an example. The corresponding library is **library/buzzer.py**. First upload the library file to the board:

```shell
ampy -p COM1 put library/buzzer.py
```

Then upload a buzzer example file as the main program, e.g. **examples/buzzer/play_a_melody/main.py**:

```shell
ampy -p COM1 put examples/buzzer/play_a_melody/main.py
```

After upload, restart the board and it will automatically run main.py, and you have successfully run an example program.

You can check the comments in each main.py under examples for documentation of the example programs.
